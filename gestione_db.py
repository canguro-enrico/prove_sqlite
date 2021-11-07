import sqlite3
from sqlite3 import Error
import os
from sqlite3.dbapi2 import connect
db_path='C:/Users/Public/documents/provavisualstudio/'+'db_prova.sqlite3'


class Apri():
    def __init__(self,db_nome='db_prova.sqlite3', percorso='C:/Users/Public/documents/provavisualstudio/'):
        self.db_nome = db_nome
        self.percorso=percorso
    

        db_esiste= os.path.exists (self.percorso+self.db_nome)
        
    def __str__(self):
        return (self.percorso+self.db_nome)
                    
    def connetti(sef,db_path):
        conn =sqlite3.connect(db_path)
        curs=conn.cursor()
        return conn

    def nomi_campi(self,conn):  
        strsql ="select * from testi_testo "
        curs=conn.cursor()
        curs.execute(strsql)
        for col in curs.description:
            print (col)


    
        
            


    

db = Apri()
conn=db.connetti(db_path)
db.nomi_campi(conn)



  
