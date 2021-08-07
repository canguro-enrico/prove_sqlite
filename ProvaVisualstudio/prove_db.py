import os
import sqlite3
from sqlite3 import Error


def create_connection (db_file):
    conn = None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn







def righe (record):
    for riga in record.fetchall():
        print(riga)

db_nome = "db_prova.sqlite3"

db_exist =  os.path.exists(db_nome)
if db_exist:
    print ("esiste")
else:
    print ("non esiste")

with sqlite3.connect(db_nome) as conn:
    cursor =conn.cursor()
    record = cursor.execute("select * from testi_testo")
    righe (record)
    righe( cursor.execute('select * from testi_autore'))
    conn.close







    

    
