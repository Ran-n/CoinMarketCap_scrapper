#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/01 20:23:55.455964
#+ Editado:	2022/01/05 20:56:21.535003
# ------------------------------------------------------------------------------
import requests as r
#import pandas as pd
from bs4 import BeautifulSoup as bs
from math import ceil
from typing import Optional, List, Union

from uteis.ficheiro import gardarJson

from src.coinmarketcap_scrapper.excepcions import ErroTipado
from src.coinmarketcap_scrapper.cmc_uteis import lazy_check_types
# ------------------------------------------------------------------------------
class CoinMarketCap:
    # atributos de clase
    __pax: int = 1
    __url: str = 'https://coinmarketcap.com/?page='

    # Constructor --------------------------------------------------------------
    def __init__(self) -> None:
        # variables da instancia
        self.__pax = self.__pax
        self.__url = self.__url
    # --------------------------------------------------------------------------

    # Getters ------------------------------------------------------------------
    def get_pax(self) -> int:
        return self.__pax

    def get_url(self, nova_pax: Optional[int] = 0) -> str:
        if nova_pax:
            self.__pax = nova_pax

        return self.__url+str(self.__pax)

    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------

    def set_pax(self, nova_pax) -> None:
        self.__pax = nova_pax

    # --------------------------------------------------------------------------

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

        pax = 1
        lista_top = []

        #while pax<=ceil(topx/100):
        while True:
            try:
                #df = pd.read_html(r.get(self.get_url()).text)[0]
                soup = bs(r.get(self.get_url(pax)).text, 'html.parser')
                taboa = soup.find('table').tbody.find_all('tr')

                xpax = len(taboa)

                # pe: 123 serian 123-(100*(1-1))=123 e 123-(100*(2-1))=23
                pasados = xpax*(pax-1)
                if topx==0:
                    tope = xpax
                else:
                    tope = topx-pasados

                for indice, fila in enumerate(taboa[:tope], 1):
                    try:
                        simbolo = fila.find(class_='crypto-symbol').text    #símbolo
                    except:
                        simbolo = fila.find(class_='coin-item-symbol').text #símbolo

                    ligazon = fila.find(class_='cmc-link').get('href')  # ligazón
                    prezo = fila.find_all('td')[3].text                 # prezo
                    divisa = prezo[0]                                   # divisa
                    prezo = prezo[1:]                                   # prezo

                    # nome
                    nome = fila.find_all('td')[2].text
                    if nome.endswith('Buy'):
                        nome = nome[:-3]

                    if nome.endswith(simbolo):
                        nome = nome[:-len(simbolo)]

                    while nome[-1].isdigit():
                        nome = nome[:-1]

                    lista_top.append({
                        'posicion': indice+pasados,
                        'simbolo': simbolo,
                        'nome': nome,
                        'prezo': prezo,
                        'divisa': divisa,
                        'ligazon': ligazon
                        })

                pax+=1

                # aki en lugar de no while pq asi podo sacar o xpax sen
                # outro request idiota ou recursión
                if (pax>ceil(topx/xpax)) and (topx!=0):
                    break
            # se peta saese do bucle
            except:
                break

        gardarJson('./saida.json', lista_top)
        return lista_top

    # get_price
    def get_price(self) -> dict:
        # xFCRF devolve nunha soa divisa, molaría para o futuro implementar multiples
        """
        """
        pass


# ------------------------------------------------------------------------------

