#! /bin/sh
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/15 17:51:57.572545
#+ Editado:	2022/03/28 22:52:48.215583
# ------------------------------------------------------------------------------
cd media/db
./get_ligs.py $@

echo ''
read -p 'Copiar ' copiar

cp ligazons.db ../../src/coinmarketcap_scrapper/ligazons.db
# ------------------------------------------------------------------------------

