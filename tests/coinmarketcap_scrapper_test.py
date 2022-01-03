#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/02 12:34:15.530170
#+ Editado:	2022/01/03 19:21:00.010410
# ------------------------------------------------------------------------------
import unittest

from src.coinmarketcap_scrapper.coinmarketcap_scrapper import CoinMarketCap
# ------------------------------------------------------------------------------
class TestCoinMarketCap_scrapper(unittest.TestCase):

    @staticmethod
    def get_url(pax=1, divisa='eur'):
        return f'https://coinmarketcap.com/?page={pax}&currency={divisa}'

    # Getters ------------------------------------------------------------------

    def test_get_pax(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        self.assertEqual(cmc.get_pax(), 1)

    def test_get_divisa(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()
        self.assertEqual(cmc.get_divisa(), 'eur')

    def test_get_url(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()
        self.assertEqual(cmc.get_url(), self.get_url())

    def test_get_url2(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()
        self.assertEqual(cmc.get_url(2), self.get_url(pax=2))

    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------

    def test_set_pax(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        self.assertEqual(cmc.get_pax(), 1)
        cmc.set_pax(5)
        self.assertEqual(cmc.get_pax(), 5)

    def test_set_divisa(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        self.assertEqual(cmc.get_divisa(), 'eur')
        cmc.set_divisa('usd')
        self.assertEqual(cmc.get_divisa(), 'usd')

    # --------------------------------------------------------------------------

    # get_top ------------------------------------------------------------------

    def test_get_top(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        print(cmc.get_top(100))

    # get_top # ----------------------------------------------------------------

# ------------------------------------------------------------------------------

