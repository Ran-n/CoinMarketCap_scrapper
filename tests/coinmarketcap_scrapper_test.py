#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/02 12:34:15.530170
#+ Editado:	2022/02/27 14:39:02.543341
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
        NON TEN SENTIDO PQ NON TEÑO FORMA DE COMPROBAR
        """

        cmc = CoinMarketCap()

        cmc.get_info()

   # get_info # ---------------------------------------------------------------

    # get_top ------------------------------------------------------------------

    def test_get_top(self):
        """
        Uso normal.
        NON TEN SENTIDO PQ NON TEÑO FORMA DE COMPROBAR
        """

        cmc = CoinMarketCap()

        #cmc.get_top(0)
        #cmc.get_top(200)
        top1 = cmc.get_top(10)
        top2 = cmc.get_top(124)

        self.assertEqual(len(top1), 10)
        self.assertEqual(len(top2), 124)

    # get_top # ----------------------------------------------------------------

    # get_moeda  ---------------------------------------------------------------

    def test_get_moeda(self):
        """
        Uso normal.
        NON TEN SENTIDO PQ NON TEÑO FORMA DE COMPROBAR
        """

        cmc = CoinMarketCap()

        shiba_inu = cmc.get_moeda('SHIB', 'simbolo')

        self.assertEqual(shiba_inu['nome'], 'Shiba Inu')

    # get_moeda # --------------------------------------------------------------

# ------------------------------------------------------------------------------
