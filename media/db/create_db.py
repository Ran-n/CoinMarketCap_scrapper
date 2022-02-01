#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/29 13:23:47.607933
#+ Editado:	2022/01/30 12:44:17.596105
# ------------------------------------------------------------------------------
import sqlite3

from uteis.ficheiro import cargarFich
# ------------------------------------------------------------------------------
con = sqlite3.connect('ligazons.db')
cur = con.cursor()

cur.executescript(''.join(cargarFich('script_ligazons.sql')))

con.commit()
con.close()
# ------------------------------------------------------------------------------
