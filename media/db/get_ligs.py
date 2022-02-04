#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/03 21:05:26.106045
#+ Editado:	2022/02/02 14:06:28.217837
# ------------------------------------------------------------------------------
import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import datetime
import sqlite3
from secrets import token_urlsafe as tus

from uteis.imprimir import jprint

import info_db
# ------------------------------------------------------------------------------
def get_url(pax: int) -> str:
    return f'https://coinmarketcap.com/?page={pax}'

def print_info_db() -> dict:
    print()
    info = info_db.main()
    print(f'{info["cantidade"]} entradas totais na DB.')
    print()

    return info

# ------------------------------------------------------------------------------
DEBUG = True

con = sqlite3.connect('ligazons.db')
cur = con.cursor()

if DEBUG:
    print(datetime.now())
    num_engadidos = 0
    info_db_ini = print_info_db()

pax = 1
pasados = 0

while True:
    if DEBUG: print(f'Escrapeando a páxina {pax}', end='\r')

    try:
        paxina_web = r.get(get_url(pax))

        if paxina_web.status_code == 404:
            if DEBUG: print('Máximo de páxinas alcanzado.')
            if DEBUG: print(f'Escrapeadas un total de {pax-1} páxinas.')
            break

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
                    print(f'Engadido novo elemento da páxina {pax}')
                    jprint({
                        'id': info_db_ini['cantidade']+num_engadidos,
                        'simbolo': simbolo,
                        'nome': nome,
                        'ligazon': ligazon
                        })
                    print()

        con.commit()
        pasados += len(taboa)
        pax+=1

    except Exception as e:
        if DEBUG: print(f'Erro: {e}'); print(f'Escrapeadas un total de {pax} páxinas')
        break

con.close()

if DEBUG:
    print(f'Engadidas un total de {num_engadidos} entradas.')
    print_info_db()
    print(datetime.now())

# ------------------------------------------------------------------------------
