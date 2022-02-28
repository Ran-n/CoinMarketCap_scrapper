#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/02 12:34:15.530170
#+ Editado:	2022/02/28 13:34:23.370058
# ------------------------------------------------------------------------------
import unittest

from src.coinmarketcap_scrapper.coinmarketcap_scrapper import CoinMarketCap
# ------------------------------------------------------------------------------
class TestCoinMarketCap_scrapper(unittest.TestCase):

    @staticmethod
    def get_url_pax(pax: int = 0):
        return f'https://coinmarketcap.com/?page={pax}'

    # Getters ------------------------------------------------------------------

    def test_get_pax(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        self.assertEqual(cmc.get_pax(), 1)

    def test_get_url_pax(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()
        self.assertEqual(cmc.get_url_pax(), self.get_url_pax())

    def test_get_url_pax2(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()
        self.assertEqual(cmc.get_url_pax(2), self.get_url_pax(pax=2))

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

    # get_info  ----------------------------------------------------------------

    def test_get_info(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        info = cmc.get_info()

        self.assertIsNotNone(info)

   # get_info # ---------------------------------------------------------------

    # get_top ------------------------------------------------------------------

    def test_get_top(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        #cmc.get_top(0)
        #cmc.get_top(200)
        top1 = cmc.get_top(10)
        top2 = cmc.get_top(124)

        self.assertIsNotNone(top1)
        self.assertIsNotNone(top2)

        self.assertEqual(len(top1), 10)
        self.assertEqual(len(top2), 124)

    # get_top # ----------------------------------------------------------------

    # get_moeda  ---------------------------------------------------------------

    def test_get_moeda(self):
        """
        Uso normal.
        """

        cmc = CoinMarketCap()

        shiba_inu = cmc.get_moeda('SHIB', 'simbolo')

        self.assertIsNotNone(shiba_inu)

        self.assertEqual(shiba_inu['nome'], 'Shiba Inu')
        self.assertIsNone(shiba_inu['max_supply'])

    # get_moeda # --------------------------------------------------------------

# ------------------------------------------------------------------------------
