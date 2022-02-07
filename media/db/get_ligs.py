#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/03 21:05:26.106045
#+ Editado:	2022/02/07 19:21:32.575811
# ------------------------------------------------------------------------------

import requests as r
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet
from datetime import datetime
import sqlite3
from sqlite3 import Cursor
from secrets import token_urlsafe as tus
from typing import Optional

from uteis.imprimir import jprint

import info_db

# ------------------------------------------------------------------------------

def get_url(pax: int) -> str:
    return f'https://coinmarketcap.com/?page={pax}'

def get_url_novos() -> str:
    return 'https://coinmarketcap.com/new'

def get_url_gan_per() -> str:
    return 'https://coinmarketcap.com/gainers-losers'

def get_url_trending() -> str:
    return 'https://coinmarketcap.com/trending-cryptocurrencies'

def get_url_mais_visitados() -> str:
    return 'https://coinmarketcap.com/most-viewed-pages'

def print_info_db() -> dict:
    print()
    info = info_db.main()
    print(f'{info["cantidade"]} entradas totais na DB.')
    print()

    return info

def scrape(cur: Cursor, paxina_web: str, info_db_ini: dict, pax: Optional[int] = None) -> None:
    soup = bs(paxina_web.text, 'html.parser')
    taboa = soup.find('table').tbody.find_all('tr')

    for indice, fila in enumerate(taboa, 1):
        # simbolo
        try:
            simbolo = fila.find(class_='crypto-symbol').text
        except:
            try:
                simbolo = fila.find(class_='coin-item-symbol').text
            except Exception as e:
                if DEBUG: print(f'Erro en simbolo: {e}')
                simbolo = 'Erro'
        # simbolo #

        # nome
        try:
            nome = fila.find_all('td')[2].text
            if simbolo not in nome:
                nome = fila.find_all('td')[1].text
            if nome.endswith('Buy'):
                nome = nome[:-3]

            if nome.endswith(simbolo):
                nome = nome[:-len(simbolo)]

            # podería dar problema se fose algo tipo Moeda1 o nome pero bueno
            if not nome.isdigit():
                while nome[-1].isdigit():
                    nome = nome[:-1]
        except Exception as e:
            if DEBUG: print(f'Erro en nome: {e}')
            nome = 'Erro'
        # nome #

        # ligazon
        try:
            ligazon = fila.find(class_='cmc-link').get('href')
        except Exception as e:
            if DEBUG: print(f'Erro en ligazon: {e}')
            ligazon = 'Erro'
        # ligazon #

        try:
            cur.execute('insert into moeda("simbolo", "nome", "ligazon", "data")'\
                f' values("{simbolo}", "{nome}", "{ligazon}", "{datetime.now()}")')
        except sqlite3.IntegrityError:
            pass
        except Exception as e:
            raise e
        else:
            if DEBUG:
                num_engadidos += 1
                if pax:
                    print(f'Engadido novo elemento da páxina {pax}')
                else:
                    print(f'Engadido novo elemento da páxina de novidades')
                jprint({
                    'id': info_db_ini['cantidade']+num_engadidos,
                    'simbolo': simbolo,
                    'nome': nome,
                    'ligazon': ligazon
                    })
                print()


def scrape_auxiliar(cur: Cursor, info_db_ini: dict, auxiliar: str) -> None:

    auxiliares = {
            'gan_per': ['gañadores/perdedores', get_url_gan_per()],
            'trending': ['trending', get_url_trending()],
            '+visit': ['máis visitados', get_url_mais_visitados()],
            'novos': ['novidades', get_url_novos()]
            }

    try:
        if DEBUG: print(f'* Páxina de {auxiliares[auxiliar][0]}')
        paxina_web = r.get(auxiliares[auxiliar][1])
    except KeyError:
        raise Exception('Páxina inexistente.')
    except Exception as e:
        raise e


    if paxina_web.status_code != 404:
        scrape(cur, paxina_web, num_engadidos, info_db_ini)
        if DEBUG and num_engadidos == 0:
            print('Non se engadiu ningunha entrada da páxina.')
    else:
        if DEBUG: print('Páxina inaccesíbel.')

def scrape_inicio(cur: Cursor, info_db_ini: dict) -> None:
    pax = 1

    if DEBUG: print('* Páxina principal')
    while True:
        if DEBUG: print(f'Escrapeando a páxina {pax}', end='\r')

        paxina_web = r.get(get_url(pax))

        if paxina_web.status_code == 404:
            if DEBUG:
                print('Máximo de páxinas alcanzado.')
                print(f'Escrapeadas un total de {pax-1} páxinas.')
            break

        try:
            scrape(cur, paxina_web, info_db_ini, pax)

            #con.commit()
            pax+=1

        except Exception as e:
            if DEBUG: print(f'Erro: {e}'); print(f'Escrapeadas un total de {pax} páxinas')
            break

# ------------------------------------------------------------------------------

def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()

    # mostrar os datos iniciais
    if DEBUG:
        print(datetime.now())
        info_db_ini = print_info_db()

    scrape_auxiliar(cur, info_db_ini, 'gan_per')

    if DEBUG: print()

    scrape_auxiliar(cur, info_db_ini, 'trending')

    if DEBUG: print()

    scrape_auxiliar(cur, info_db_ini, '+visit')

    if DEBUG: print()

    scrape_auxiliar(cur, info_db_ini, 'novos')

    if DEBUG: print()

    scrape_inicio(cur, info_db_ini)

    if DEBUG: print()

    con.commit()
    con.close()

    if DEBUG:
        print(f'Engadidas un total de {num_engadidos} entradas.')
        print_info_db()
        print(datetime.now())

# ------------------------------------------------------------------------------

DEBUG = True
DB = 'ligazons.db'
num_engadidos = 0

if __name__ == '__main__':
    main()

# ------------------------------------------------------------------------------
