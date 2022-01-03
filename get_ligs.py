#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/03 21:05:26.106045
#+ Editado:	2022/01/03 21:49:03.329155
# ------------------------------------------------------------------------------
import requests as r
from bs4 import BeautifulSoup as bs

from uteis.ficheiro import gardarJson
# ------------------------------------------------------------------------------
def get_url(pax: int) -> str:
    return f'https://coinmarketcap.com/?page={pax}'

pax = 1
lista_moedas = []

while True:
    try:
        soup = bs(r.get(get_url(pax)).text, 'html.parser')

        for indice, fila in enumerate(soup.find('table').tbody.find_all('tr')):
            # simbolo
            try:
                simbolo = fila.find(class_='crypto-symbol').text
            except:
                simbolo = fila.find(class_='coin-item-symbol').text

            # nome
            nome = fila.find_all('td')[2].text
            if nome.endswith('Buy'):
                nome = nome[:-3]

            if nome.endswith(simbolo):
                nome = nome[:-len(simbolo)]

            while nome[-1].isdigit():
                nome = nome[:-1]

            # ligazon
            ligazon = fila.find(class_='cmc-link').get('href')

            lista_moedas.append({
                'posicion': pax*indice,
                'simbolo': simbolo,
                'nome': nome,
                'ligazon': ligazon
                })

        pax+=1
    except:
        gardarJson('./ligazons.json', lista_moedas)
        break

# ------------------------------------------------------------------------------
