import sqlite3
from typing import Container

con=sqlite3.connect(":memory:")
cur=con.cursor()
cur.execute("""create table tabella (data text,articolo text,codice text, qty real )""")
cur.execute("""insert into tabella values ("2021-10-12","lattina","ita956",1276 )""")
cur.execute("""insert into tabella values ("2021-10-24","vetro","vap",14 )""")
con.commit()

cur=con.cursor()
cur.execute("select sum(qty)from tabella")
r=cur.fetchone()
print("somma = ",r)
cur.execute("select * from tabella")
r=cur.fetchone()
# manca il richiamo a factory_row
#print(r.keys())
print(len(r))
print(r)
print(tuple(r))
#print(r["articolo"])
print(r[2])