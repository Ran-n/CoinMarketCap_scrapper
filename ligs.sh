#! /bin/sh
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/15 17:51:57.572545
#+ Editado:	2022/03/28 23:01:39.542544
# ------------------------------------------------------------------------------
cd media/db
./get_ligs.py $@

#echo ''
#read -p 'Copiar ' copiar

#if [ -n "$copiar" ] && [ "$copiar" = 's' ]; then
#    cp -v ligazons.db ../../src/coinmarketcap_scrapper/ligazons.db
#fi
cp ligazons.db ../../src/coinmarketcap_scrapper/ligazons.db
# ------------------------------------------------------------------------------

