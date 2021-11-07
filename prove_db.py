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
    d={}
    for riga in record.fetchall():
        d
        print(riga)

db_nome = "db_prova.sqlite3"

db_exist =  os.path.exists(db_nome)
if db_exist:
    print ("esiste")
else:
    print ("non esiste")
"""
with sqlite3.connect(db_nome) as conn:
    cursor =conn.cursor()
    record = cursor.execute("select * from testi_testo")
    righe (record)
    righe( cursor.execute('select * from testi_autore'))
    conn.close
"""
#boh?
"""
def dict_factory (cursor,row):
    d=dict()
    for idx,col in enumerate(cursor):
        d[col[0]]=row[idx]
        return d
"""
def apri_db():
    conn=sqlite3.connect(db_nome)
    return conn

def scaricaTesto(conn):
    c=conn.cursor()
    c.execute("select * from testi_testo")
    righe=c.fetchall()
    
    return(righe)


def scaricaEditore(conn):  #righe (record)\
    c=conn.cursor()
    righe=c.execute('select * from testi_editore')
    # id,editore = c.fetchone() interessante! assegna i dati scaricati alle variabili id, editore
    #print (id,editore)
    righe=c.fetchall()
    
    return righe

def aggiungeAutore(conn,nomeautore,cognomeautore):   
    c = conn.cursor()
    c.execute("INSERT INTO testi_autore (nome,cognome) VALUES (nomeautore.cognomeautore)")
    c.commit()
    #ricava l'ultimo id immesso
    id = "ultimo record"
    return(id)

    
def scaricaAutore(conn):
    c=conn.cursor()
    c.execute("select * from testi_autore")
    righe=c.fetchall()
    
    
    return righe

def modificaRecord(conn):
    c=conn.cursor()
    c.execute("""update testi_editore set editore = "panta rei" where id =2""")
    conn.commit()

def immettiRecord(conn,recAutore,recEditore):
    dictAutore ={}
    dictEditore ={}
    for r in recEditore:
        dictEditore[r[1]]=r[0]
    for r in recAutore:
        dictAutore[r[1]+" "+ r[2]]=r[10]

    testo=input("titolo: ")
    if len(testo)>30:
        print("il titolo verrà troncato a 30 chr")

    argomento =input("argomento: ")
    if len(argomento)>30:
        print("l'argomento verrà troncato a 30 chr")
    nomeautore= input ("nome autore: ")
    cognomeautore = input("cognome autore")
    #come trovare l'id dell'autore e vedere se è già contenuto nel dict
    autore = nomeautore + " " + cognomeautore
    #if autore = "cerca nelle keys": #verifica che autore sia nell'elenco
        #a=dict[autore]
    #else:
        #aggiungo autore
        #id = aggiungeAutore(con,nomeautore,cognomeautore)
       
    editore = input("editore: ")




    
# DA QUI INIZIA LO SPAZIO PER LE ISTRUZIONI

con= apri_db()
"""
recAutore =scaricaAutore(con)
recEditore =scaricaEditore(con)
recordTesto =scaricaTesto(con)
dictAutore ={}
dictEditore ={}
for r in recEditore:
        dictEditore[r[0]]=r[1]
for r in recAutore:
        dictAutore[r[0]]=r[1]+r[2]
for r in recordTesto:
    idTesto,titolo,arg,autore,editore=r
    print (f"{idTesto} titolo = {titolo} argomento = {arg} autore = {dictAutore[autore]} editore = {dictEditore[editore]}")




immettiRecord(con,recAutore,recEditore)
    

con.close()
    

    
"""
c=con.cursor()
c.execute ("""select testi_testo.id,titolo,argomento,testi_autore.nome,testi_autore.cognome
from testi_testo
inner join testi_autore on testi_autore.id =testi_testo.id""")
righe=c.fetchall()
for r in righe:
    print (r)
