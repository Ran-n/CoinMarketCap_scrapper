#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/02 12:34:15.530170
#+ Editado:	2022/01/15 15:03:40.240022
# ------------------------------------------------------------------------------
import unittest

from src.coinmarketcap_scrapper.coinmarketcap_scrapper import CoinMarketCap
# ------------------------------------------------------------------------------
class TestCoinMarketCap_scrapper(unittest.TestCase):

    @staticmethod
    def get_url(pax=1):
        return f'https://coinmarketcap.com/?page={pax}'

    # Getters ------------------------------------------------------------------

    def test_get_pax(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        self.assertEqual(cmc.get_pax(), 1)

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

    # --------------------------------------------------------------------------

    # get_top ------------------------------------------------------------------

    def test_get_top(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        cmc.get_top('./0.json', 0)
        #cmc.get_top('./10.json', 10)
        #cmc.get_top('./124.json', 124)
        #cmc.get_top('./200.json', 200)

    # get_top # ----------------------------------------------------------------

# ------------------------------------------------------------------------------

