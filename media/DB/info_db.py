#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/30 12:41:03.026263
#+ Editado:	2022/01/30 13:31:57.628448
# ------------------------------------------------------------------------------
import sqlite3

from uteis.imprimir import jprint
# ------------------------------------------------------------------------------
def main():
    con = sqlite3.connect('ligazons.db')
    cur = con.cursor()

    cantidade = cur.execute('select count(*) from moeda').fetchone()[0]

    con.commit()
    con.close()

    return {
            'cantidade': cantidade
            }

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    jprint(main())
# ------------------------------------------------------------------------------
