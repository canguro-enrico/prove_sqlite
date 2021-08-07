import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect
def create_connection (db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except.Error as e:
        print(e)
return conn

def create_project (conn,project):
    sql = """INSERT INTO projects(name,begin_date,end_date) VALUES (?,?,?)"""
    cur =conn.cursor()
    cur.execute (sql, project)
    conn.commit()
return cur.lastrowid


def create_task (conn,task):
    sql ="""INSERT INTO TASKS 8name,priority,status_id,project_id,begin_date,end_daste) VALUES(?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()
return cur.lastrowid

def main():
    database =r "c:\    mettere path"
    conn =create_connection (database)
    with conn:
        project =('xxx','2015-01-02','2015-01-29');
        project_id =create_project(conn,project)
        task_1 =('yyy',project_id,'date_1','date_2')
        task_2 =('zzz',project_id,'date31','date_4')
        create_task(conn,task_1)
        create_task(conn,task_2)
        if __name__ = __main__
        main()






