import sqlite3
from sqlite3 import Error




def conectar(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
        print(sqlite3.version)

    except Error as e:
        print(e)
    finally:
        if con is None:
            con.close()
            print('Conexão fechada!')


if __name__ == '__main__':
    conectar('D:\hospital.db')
