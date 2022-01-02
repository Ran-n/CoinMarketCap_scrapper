#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/02 12:34:15.530170
#+ Editado:	2022/01/02 13:13:28.302899
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

# ------------------------------------------------------------------------------

