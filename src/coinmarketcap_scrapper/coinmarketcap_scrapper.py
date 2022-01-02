#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/01 20:23:55.455964
#+ Editado:	2022/01/02 13:12:33.939101
# ------------------------------------------------------------------------------
from typing import Optional, List, Union
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

    def get_url(self) -> str:
        return self.__url
    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------
    def set_pax(self, nova_pax) -> None:
        self.__pax = nova_pax

    def set_divisa(self, nova_divisa) -> None:
        self.__divisa = nova_divisa
    # --------------------------------------------------------------------------

    def get_price(self, moeda: str, divisa: str) -> dict:
        """
        """
        pass

# ------------------------------------------------------------------------------

