#operazioni sul db
import os
import sqlite3
from sqlite3 import Error

db_nome = 'db_prova.sqlite3'
path ='C:/Users/Public/documents/provavisualstudio'
db_esiste = os.path.exists (db_nome)
def connetti_db(db_nome):
    
    return (conn)

def ins_dato_autori ():
    conn = sqlite3.connect(db_nome)
# campi nome, cognome
   
    c = conn.cursor()
    
    c.execute("INSERT INTO testi_autore (nome,cognome) VALUES ('Raymond','Carver')")
    c.execute("SELECT * FROM testi_autore")
    conn.commit()
    for riga in c:
        print(riga)
   


def ins_dato_testo():
    conn = sqlite3.connect(db_nome)
    c = conn.cursor()
    dati = ['4','ancora da scrivere','liberismo imperialista','4','1','2021-o8-06']
    c.execute("INSERT INTO testi_testo VALUES (?,?,?,?,?,?)", dati)
    c.execute("SELECT * FROM testi_testo")
    for riga in c:
        print(riga)
    conn.commit()
    conn.close()

#ins_dato_autori()
#ins_dato_testo()

def elenca_campi(tabella):
    con =sqlite3.connect(db_nome)
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute('SELECT * FROM '+tabella)
    r=cur.fetchone()
    print(r.keys())

#elenca_campi('testi_autore')
ins_dato_autori ()


