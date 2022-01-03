#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/01 20:23:55.455964
#+ Editado:	2022/01/03 19:16:21.652995
# ------------------------------------------------------------------------------
import requests as r
#import pandas as pd
from bs4 import BeautifulSoup as bs
from typing import Optional, List, Union

from uteis.ficheiro import gardarJson

from src.coinmarketcap_scrapper.excepcions import ErroTipado
from src.coinmarketcap_scrapper.cmc_uteis import lazy_check_types
# ------------------------------------------------------------------------------
class CoinMarketCap:
    # atributos de clase
    __pax: int = 1
    __divisa: str = 'eur'
    __url: str = f'https://coinmarketcap.com/?page={__pax}&currency={__divisa}'

    # Constructor --------------------------------------------------------------
    def __init__(self, divisa: Optional[str] = 'eur') -> None:
        # variables da instancia
        self.__pax = self.__pax
        self.__divisa = divisa
        self.__url = self.__url
    # --------------------------------------------------------------------------

    # Getters ------------------------------------------------------------------
    def get_pax(self) -> int:
        return self.__pax

    def get_divisa(self) -> str:
        return self.__divisa

    def get_url(self, nova_pax: Optional[int] = 0) -> str:
        if nova_pax:
            self.__pax = nova_pax
            self.__update_url()

        return self.__url

    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------

    def __update_url(self) -> None:
        self.__url = f'https://coinmarketcap.com/?page={self.__pax}&currency={self.__divisa}'

    def set_pax(self, nova_pax) -> None:
        self.__pax = nova_pax

    def set_divisa(self, nova_divisa) -> None:
        self.__divisa = nova_divisa

    # --------------------------------------------------------------------------

    '''
    # get_ligazons
    def __get_ligazons(self) -> None:
        """
        """

        soup = bs(r.get(self.get_url()).text, 'html.parser')

        for fila in soup.find('table').tbody.find_all('tr'):
            ele.find(class_='cmc-link').get('href')
    '''

    # get_top
    def get_top(self, topx: Optional[int] = 10) -> List[dict]:
        """
        Devolve o top de moedas en CoinMarketCap.

        @entradas:
            topx    -   Opcional    -   Enteiro
            └ Cantidade de moedas no top.

        @saídas:
            Lista de dicionarios  -   Sempre
            └ Cos datos pedidos.
        """

        if not lazy_check_types(topx, int):
            raise ErroTipado('O tipo da variable non entra dentro do esperado (int)')

        lista_top = []

        #df = pd.read_html(r.get(self.get_url()).text)[0]
        soup = bs(r.get(self.get_url()).text, 'html.parser')

        for indice, fila in enumerate(soup.find('table').tbody.find_all('tr')[:topx], 1):
            try:
                simbolo = fila.find(class_='crypto-symbol').text    #símbolo
            except:
                simbolo = fila.find(class_='coin-item-symbol').text    #símbolo

            ligazon = fila.find(class_='cmc-link').get('href')  #ligazón
            prezo = fila.find_all('td')[3].text                 #prezo
            divisa = prezo[0]
            prezo = prezo[1:]

            nome = fila.find_all('td')[2].text                  #nome
            if nome.endswith('Buy'):
                nome = nome[:-3]

            if nome.endswith(simbolo):
                nome = nome[:-len(simbolo)]

            while nome[-1].isdigit():
                nome = nome[:-1]

            lista_top.append({'posicion': indice,
                                'simbolo': simbolo,
                                'nome': nome,
                                'prezo': prezo,
                                'divisa': divisa,
                                'ligazon': ligazon})

            gardarJson('./saida.json', lista_top)

    # get_price
    def get_price(self, moeda: str) -> dict:
        # xFCRF devolve nunha soa divisa, molaría para o futuro implementar multiples
        """
        """
        pass


# ------------------------------------------------------------------------------

