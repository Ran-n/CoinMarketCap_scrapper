#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2021/12/10 16:44:23.128361
#+ Editado:	2022/01/02 13:55:37.775660
# ------------------------------------------------------------------------------
import unittest

from src.coinmarketcap_scrapper.cmc_uteis import lazy_check_types
from src.coinmarketcap_scrapper.excepcions import ErroTipado
# ------------------------------------------------------------------------------
class TestCG_Uteis(unittest.TestCase):

    # lazy_check_types ---------------------------------------------------------
    def test_lazy_check_types_casos_base(self):
        # caso 1
        self.assertTrue(lazy_check_types('', str))
        # caso 2
        self.assertTrue(lazy_check_types(['', ''], str))
        # caso 3
        self.assertTrue(lazy_check_types(['', 0, ['', '']], [str, int, str]))

    def test_lazy_check_types_simples(self):
        # true
        self.assertTrue(lazy_check_types('a', str))         # str   ?   str
        self.assertTrue(lazy_check_types(1, int))           # int   ?   int
        self.assertTrue(lazy_check_types(False, bool))      # bool  ?   bool
        self.assertTrue(lazy_check_types([], list))         # list  ?   list
        #

        # false
        self.assertFalse(lazy_check_types('b', int))        # str   ?   int
        self.assertFalse(lazy_check_types('c', bool))       # str   ?   bool
        self.assertFalse(lazy_check_types('d', list))       # str   ?   list

        self.assertFalse(lazy_check_types(2, str))          # int   ?   str
        self.assertFalse(lazy_check_types(3, bool))         # int   ?   bool
        self.assertFalse(lazy_check_types(4, list))         # int   ?   list

        self.assertFalse(lazy_check_types(True, int))       # bool  ?   int
        self.assertFalse(lazy_check_types(False, str))      # bool  ?   str
        self.assertFalse(lazy_check_types(True, list))      # bool  ?   list
        #

    def test_lazy_check_types_simples_lista(self):
        # true
        self.assertTrue(lazy_check_types(['a'], str))           # str   ?   str
        self.assertTrue(lazy_check_types(['a'], [str]))         # str   ?   str
        self.assertTrue(lazy_check_types(['a', ''], str))       # str   ?   str

        self.assertTrue(lazy_check_types([0], int))             # int   ?   int
        self.assertTrue(lazy_check_types([1], [int]))           # int   ?   int
        self.assertTrue(lazy_check_types([2, 3], int))          # int   ?   int

        self.assertTrue(lazy_check_types([True], bool))         # bool  ?   bool
        self.assertTrue(lazy_check_types([False], [bool]))      # bool  ?   bool
        self.assertTrue(lazy_check_types([False, True], bool))  # bool  ?   bool

        self.assertTrue(lazy_check_types([], list))             # list  ?   list
        self.assertTrue(lazy_check_types([[], []], list))       # list  ?   list
        #

        # false
        self.assertFalse(lazy_check_types(['b'], int))          # str   ?   int
        self.assertFalse(lazy_check_types(['b', 'c'], int))     # str   ?   int
        self.assertFalse(lazy_check_types(['b'], [int]))        # str   ?   int
        self.assertFalse(lazy_check_types(['b'], bool))         # str   ?   bool
        self.assertFalse(lazy_check_types(['b', 'c'], bool))    # str   ?   bool
        self.assertFalse(lazy_check_types(['b'], [bool]))       # str   ?   bool
        self.assertFalse(lazy_check_types(['b'], list))         # str   ?   list
        self.assertFalse(lazy_check_types(['b', 'c'], list))    # str   ?   list
        self.assertFalse(lazy_check_types(['b'], [list]))       # str   ?   list

        self.assertFalse(lazy_check_types([4], str))            # int   ?   str
        self.assertFalse(lazy_check_types([7], [str]))          # int   ?   str
        self.assertFalse(lazy_check_types([5], bool))           # int   ?   bool
        self.assertFalse(lazy_check_types([8], [bool]))         # int   ?   bool
        self.assertFalse(lazy_check_types([6], list))           # int   ?   list
        self.assertFalse(lazy_check_types([9], [list]))         # int   ?   list

        self.assertFalse(lazy_check_types([], str))             # list  ?   str
        self.assertFalse(lazy_check_types([[], []], str))       # list  ?   str
        self.assertFalse(lazy_check_types([], int))             # list  ?   int
        self.assertFalse(lazy_check_types([[], []], int))       # list  ?   int
        self.assertFalse(lazy_check_types([], bool))            # list  ?   bool
        self.assertFalse(lazy_check_types([[], []], bool))      # list  ?   bool
        #

        # ErroTipado
        with self.assertRaises(ErroTipado):
            lazy_check_types(['a', ''], [str])      # str   ?   str
        with self.assertRaises(ErroTipado):
            lazy_check_types(['a', ''], [bool])     # str   ?   bool
        with self.assertRaises(ErroTipado):
            lazy_check_types([4, 5], [int])         # int   ?   int
        with self.assertRaises(ErroTipado):
            lazy_check_types([4, 5], [str])         # int   ?   str
        with self.assertRaises(ErroTipado):
            lazy_check_types([False, True], [bool]) # bool  ?   bool
        with self.assertRaises(ErroTipado):
            lazy_check_types([False, True], [int])  # bool  ?   int
        with self.assertRaises(ErroTipado):
            lazy_check_types([], [list])            # list  ?   list
        with self.assertRaises(ErroTipado):
            lazy_check_types([[], []], [list])      # list  ?   list

        with self.assertRaises(ErroTipado):
            lazy_check_types(['b', 'c'], [int])     # str   ?   int
        with self.assertRaises(ErroTipado):
            lazy_check_types(['b', 'c'], [bool])    # str   ?   bool
        with self.assertRaises(ErroTipado):
            lazy_check_types(['b', 'c'], [list])    # str   ?   list

        with self.assertRaises(ErroTipado):
            lazy_check_types([], [str])             # list  ?   str
        with self.assertRaises(ErroTipado):
            lazy_check_types([[], []], [str])       # list  ?   str
        with self.assertRaises(ErroTipado):
            lazy_check_types([], [int])             # list  ?   int
        with self.assertRaises(ErroTipado):
            lazy_check_types([[], []], [int])       # list  ?   int
        with self.assertRaises(ErroTipado):
            lazy_check_types([], [bool])            # list  ?   bool
        with self.assertRaises(ErroTipado):
            lazy_check_types([[], []], [bool])      # list  ?   bool
        #

    def test_lazy_check_types_complexas(self):
        # true
        self.assertTrue(lazy_check_types(['', 0, True], [str, int, bool]))
        self.assertTrue(lazy_check_types(['', 0, True, [0, 0, 0]], [str, int, bool, int]))
        self.assertTrue(lazy_check_types(['', 0, True, [0, 0, 0]], [str, int, bool, [int, int, int]]))
        self.assertTrue(lazy_check_types(['', 0, True, [0, 0, [0]]], [str, int, bool, [int, int, int]]))
        self.assertTrue(lazy_check_types(['', 0, True, [0, 0, [0]]], [str, int, bool, [int, int, [int]]]))
        #

        # false
        self.assertFalse(lazy_check_types(['', 0, True, [0, '', 0]], [str, int, bool, int]))
        self.assertFalse(lazy_check_types(['', 0, True, [0, 0, [0]]], [str, int, bool, int]))
        self.assertFalse(lazy_check_types(['', 0, True, [0, 0, [0]]], [str, int, bool, list]))
        #

        # ErroTipado
        with self.assertRaises(ErroTipado):
            lazy_check_types(['', 0, True, [0, 0, 0]], [str, int, bool, [int, int]])
        with self.assertRaises(ErroTipado):
            lazy_check_types(['', 0, True, [0, 0, [0]]], [str, int, bool, [int, [int]]])
        #

# ------------------------------------------------------------------------------

