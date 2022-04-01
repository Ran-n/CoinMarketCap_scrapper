#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/03 21:05:26.106045
#+ Editado:	2022/03/28 22:53:30.099083
# ------------------------------------------------------------------------------

import sys
#import requests as r
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
from bs4.element import ResultSet
from datetime import datetime
import sqlite3
from sqlite3 import Cursor
from secrets import token_urlsafe as tus
from typing import List, Optional, Dict, Union
from tqdm import tqdm
from coinmarketcap_scrapi import CoinMarketCap
import logging

from uteis.imprimir import jprint
from conexions import Proxy

import info_db

# ------------------------------------------------------------------------------

def get_url_moeda(moeda: str) -> str:
    return 'https://coinmarketcap.com'+moeda

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

def print_info_db() -> Dict[str, str]:
    print()
    info = info_db.main()
    print(f'{info["cantidade"]} entradas totais na DB.')
    print()

    return info

# ------------------------------------------------------------------------------

def check_monero_db(cur: Cursor, info_db_ini: dict, r: Proxy, simbolo: str, nome: str, ligazon: str) -> int:
    global num_engadidos
    cant_engadidos = num_engadidos

    try:
        cur.execute('insert into moeda("simbolo", "nome", "ligazon", "creada")'\
            f' values("{simbolo}", "{nome}", "{ligazon}", "{datetime.now()}")')
        # para insertar o valor correcto de estado
        """
        manter_aux(
                moeda= (info_db_ini['cantidade']+num_engadidos, simbolo, nome, ligazon),
                cur= cur,
                r= r
                )
        """
    except sqlite3.IntegrityError:
        pass
    except Exception as e:
        logging.error(f'{e}')
        raise e
    else:
        if DEBUG:
            num_engadidos += 1
            monero = {
                'id': info_db_ini['cantidade']+num_engadidos,
                'simbolo': simbolo,
                'nome': nome,
                'ligazon': ligazon
                }
            logging.info(f'Engadido:\n{monero}\n')

    return num_engadidos-cant_engadidos

def scrape_auxiliar(cur: Cursor, soup: BeautifulSoup, info_db_ini: Dict[str, str], pax: Optional[Union[int, str]] = None, r: Proxy = None) -> None:
    global num_engadidos
    cant_engadidos = num_engadidos

    if soup.find(class_='sc-404__StyledError-ic5ef7-0'):
        raise Exception

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

        """
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
        """
        # nome
        try:
            #nome = fila.find_all('span')[3].text
            nome = fila.find(class_='circle').next_sibling.text
        except:
            try:
                nome = fila.find(class_='iworPT').text
            except Exception as e:
                if DEBUG: print(f'Erro en nome: {e}')
                simbolo = 'Erro'
        # nome #

        # ligazon
        try:
            ligazon = fila.find(class_='cmc-link').get('href').split('/')[-2]
        except Exception as e:
            if DEBUG: print(f'Erro en ligazon: {e}')
            ligazon = 'Erro'
        # ligazon #

        try:
            cur.execute('insert into moeda("simbolo", "nome", "ligazon", "creada")'\
                f' values("{simbolo}", "{nome}", "{ligazon}", "{datetime.now()}")')
            # para insertar o valor correcto de estado
            manter_aux(
                    moeda= (info_db_ini['cantidade']+num_engadidos, simbolo, nome, ligazon),
                    cur= cur,
                    r= r
                    )
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
                    print('Engadido novo elemento.')
                jprint({
                    'id': info_db_ini['cantidade']+num_engadidos,
                    'simbolo': simbolo,
                    'nome': nome,
                    'ligazon': ligazon
                    })

    return num_engadidos-cant_engadidos

def scrape(cur: Cursor, info_db_ini: Dict[str, str], auxiliar: str, r: Proxy) -> None:

    auxiliares = {
            'gan_per': ['gañadores/perdedores', get_url_gan_per()],
            'trending': ['trending', get_url_trending()],
            '+visit': ['máis visitados', get_url_mais_visitados()],
            'novos': ['novidades', get_url_novos()]
            }

    try:
        if DEBUG: print(f'\n{datetime.now()}\n* Páxina de {auxiliares[auxiliar][0]}.')
        logging.info(f'Scrape da páxina de {auxiliares[auxiliar][0]}.')
        paxina_web = r.get(auxiliares[auxiliar][1])
    except KeyError:
        logging.error('Páxina inexistente.\n')
        raise Exception('Páxina inexistente.')
    except Exception as e:
        logging.error(f'{e}')
        raise e

    if paxina_web.status_code != 404:
        cant_engadidos = scrape_auxiliar(cur, bs(paxina_web.text, 'html.parser'), info_db_ini, auxiliares[auxiliar][0], r)
        if DEBUG and cant_engadidos == 0:
            print(f'Non se engadiu ningunha entrada da páxina {auxiliares[auxiliar][0]}.')
            logging.info(f'Non se engadiu ningunha entrada da páxina {auxiliares[auxiliar][0]}.\n')
    else:
        if DEBUG: print('Páxina inaccesíbel.')
        logging.info('Páxina de {auxiliares[auxiliar][0]} inaccesíbel.\n')

def scrape_inicio(cur: Cursor, info_db_ini: dict, r: Proxy) -> None:
    r.set_verbose(False)

    paxina_web = r.get(get_url(1))
    soup = bs(paxina_web.text, 'html.parser')

    pax_totais = int(soup.find_all(class_="page")[-1].text)

    with tqdm(total= pax_totais, desc= 'Páxina Principal', unit=' paxina') as pbar:
        for pax in range(1, pax_totais+1):
            try:
                if pax != 1:
                    paxina_web = r.get(get_url(pax))
                    soup = bs(paxina_web.text, 'html.parser')
                pbar.update(1)
                scrape_auxiliar(cur, soup, info_db_ini, pax, r)
            except Exception as e:
                if DEBUG: print(f'Erro: {e}')

    r.set_verbose(True)

def manter_aux(moeda: List[str], r: Proxy, cur: Cursor, num_mods: int = 0) -> int:
    paxina_web = r.get(get_url_moeda(moeda[3]))

    if paxina_web.status_code == 404:
        cur.execute(f'update moeda set estado=1, modificada="{datetime.now()}" where id="{moeda[0]}"')
        num_mods += 1
    else:
        mod = False
        sentenza = f'update moeda set [simbolo][nome][estado]modificada="{datetime.now()}" where id="{moeda[0]}"'
        soup = bs(paxina_web.text, 'html.parser')

        contidos = []
        for ele in soup.find(class_='h1').children:
            contidos.append(ele.text)

        # simbolo
        if contidos[1] != moeda[1]:
            sentenza = sentenza.replace('[simbolo]', 'simbolo="'+contidos[1]+'", ')
            mod = True
        else:
            sentenza = sentenza.replace('[simbolo]', '')

        # nome
        if contidos[0] != moeda[2]:
            sentenza = sentenza.replace('[nome]', 'nome="'+contidos[0]+'", ')
            mod = True
        else:
            sentenza = sentenza.replace('[nome]', '')

        # untracked
        if soup.find(class_='gPwpnS'):
            sentenza = sentenza.replace('[estado]', 'estado=2, ')
            mod = True
        else:
            sentenza = sentenza.replace('[estado]', 'estado=0, ')

        if mod:
            num_mods += 1
            cur.execute(sentenza)

    return num_mods

# ------------------------------------------------------------------------------

def scrapi_inicio(cur: Cursor, info_db_ini: dict, r: Proxy) -> None:

    cmc = CoinMarketCap(r= r)

    cmc.set_verbose(False)
    cmc.set_timeout(5)
    cmc.set_reintentos(1)

    crudo = cmc.crudo()

    #print(crudo)

    datos = crudo['data']

    cant_moneroj = datos['totalCount']
    moneroj = datos['cryptoCurrencyList']

    engadidos = 0
    for monero in tqdm(moneroj, desc='Páxina Principal', unit=' monero'):
        engadidos += check_monero_db(
                            cur= cur,
                            info_db_ini= info_db_ini,
                            r= r,
                            nome= monero['symbol'],
                            simbolo= monero['name'],
                            ligazon= monero['slug']
                        )
    mensaxe = f'Engadidas un total de {engadidos} entradas.'
    if DEBUG: print(mensaxe)
    logging.info(mensaxe+'\n')

# ------------------------------------------------------------------------------

def scraping() -> None:
    logging.basicConfig(
            filename= '.log',
            filemode='w',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
    )

    try:
        r = Proxy(verbose= DEBUG, verbosalo= False)
        con = sqlite3.connect(DB)
        cur = con.cursor()

        # mostrar os datos iniciais
        print(datetime.now())
        info_db_ini = print_info_db()
        logging.info(info_db_ini)

        #scrape_inicio(cur, info_db_ini, r)
        scrapi_inicio(cur, info_db_ini, r)

        """
        scrape(cur, info_db_ini, 'gan_per', r)
        scrape(cur, info_db_ini, 'trending', r)
        scrape(cur, info_db_ini, '+visit', r)
        scrape(cur, info_db_ini, 'novos', r)
        """

    except KeyboardInterrupt:
        print('\n\nPechando o programa')

    finally:
        con.commit()
        con.close()

        catex_info_engadidas = f'Engadidas un total de {num_engadidos} entradas.'
        print('\n'+catex_info_engadidas)
        logging.info(catex_info_engadidas)

        info_db_fin = print_info_db()
        logging.info(info_db_fin)
        print(datetime.now())

def manter(quitar_borrados:bool = False) -> None:
    try:
        r = Proxy(verbose= False, verbosalo= False)
        con = sqlite3.connect(DB)
        cur = con.cursor()

        # mostrar os datos iniciais
        print(datetime.now())
        info_db_ini = print_info_db()

        num_mods = 0
        #
        # operacións
        #
        try:
            sentenza = 'select * from moeda'#'where creada > date("now")'
            if quitar_borrados:
                sentenza += ' where estado!=1'

            for moeda in tqdm(cur.execute(sentenza).fetchall()):
                num_mods = manter_aux(
                                moeda= moeda,
                                r= r,
                                cur= cur,
                                num_mods= num_mods
                            )

        except Exception as e:
            print(f'\nErro: {e}')
            pass

    except KeyboardInterrupt:
        print('\n\nPechando o programa')

    finally:
        con.commit()
        con.close()

        print(f'\nModificadas un total de {num_mods} entradas.')
        print_info_db()
        print(datetime.now())

def axuda() -> None:
    print('axuda\t-> Esta mensaxe')
    print('scrape\t-> Escrapeo')
    print('manter\t-> Tarefas de mantemento da DB')

def main(opcion: str = 'scrape', modificadores: List[str] = None) -> None:
    dic_ops = {
            'axuda': axuda,
            'scrape': scraping,
            'manter': manter
            }

    if opcion in dic_ops.keys():
        dic_ops[opcion]()
    else:
        raise 'Opción inexistente'

# ------------------------------------------------------------------------------

DEBUG = True
DB = 'ligazons.db'
num_engadidos = 0

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[1:])
    except:
        main()

# ------------------------------------------------------------------------------
