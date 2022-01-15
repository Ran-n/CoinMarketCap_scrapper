#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/03 21:05:26.106045
#+ Editado:	2022/01/15 17:41:59.154724
# ------------------------------------------------------------------------------
import requests as r
from bs4 import BeautifulSoup as bs
import pandas as pd

from uteis.ficheiro import gardarJson, cargarJson
# ------------------------------------------------------------------------------
def get_url(pax: int) -> str:
    return f'https://coinmarketcap.com/?page={pax}'

def sair() -> None:
    gardarJson('./ligazons.json', lista_moedas)
# ------------------------------------------------------------------------------
DEBUG = True
BUXA = False

pax = 1
pasados = 0
lista_moedas = cargarJson('./ligazons.json')
# se non existe o ficheiro inicializase como diccionario
if lista_moedas == {}:
    BUXA = True
    lista_moedas = []

"""
Decidiuse pasar desta implementación por ser 1µs máis lento.
[True for ele in lista_moedas if simbolo in ele.values()][0]
"""
df_moedas = pd.DataFrame.from_dict(lista_moedas)

while True:
    if DEBUG: print(f'Escrapeando a páxina {pax}', end='\r')

    try:
        paxina_web = r.get(get_url(pax))

        if paxina_web.status_code == 404:
            if DEBUG: print('Máximo de paxs alcanzado.')
            if DEBUG: print(f'Escrapeadas un total de {pax-1} páxinas')
            sair()
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

            # meter só os novos valores
            if BUXA or (simbolo not in df_moedas.values):
                BUXA = False
                novo = {
                        'simbolo': simbolo,
                        'nome': nome,
                        'ligazon': ligazon
                        }
                if DEBUG: print(f'Engadido novo elemento: {novo}')
                lista_moedas.append(novo)
                df_moedas = df_moedas.append(novo, ignore_index=True)

        pasados += len(taboa)
        pax+=1

    except Exception as e:
        if DEBUG: print(f'Erro: {e}'); print(f'Escrapeadas un total de {pax} páxinas')
        sair()
        break

# ------------------------------------------------------------------------------
