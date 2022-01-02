#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/01 20:23:55.455964
#+ Editado:	2022/01/02 12:48:37.224221
# ------------------------------------------------------------------------------
from typing import Optional, List, Union
# ------------------------------------------------------------------------------
class CoinMarketCap:
    # atributos de clase
    __pax: int = 1
    __moeda: str = 'eur'
    __url: str = f'https://coinmarketcap.com/?page={__pax}&currency={__moeda}'

    # Constructor --------------------------------------------------------------
    def __init__(self, moeda: Optional[str] = 'eur') -> None:
        # variables da instancia
        self.__pax = self.__pax
        self.__moeda = moeda
        self.__url = self.__url
    # --------------------------------------------------------------------------

    # Getters ------------------------------------------------------------------
    def get_pax(self) -> int:
        return self.__pax

    def get_moeda(self) -> str:
        return self.__moeda

    def get_url(self) -> str:
        return self.__url
    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------
    def set_pax(self, nova_pax) -> None:
        self.__pax = nova_pax

    def set_moeda(self, nova_moeda) -> None:
        self.__moeda = nova_moeda
    # --------------------------------------------------------------------------

# ------------------------------------------------------------------------------

