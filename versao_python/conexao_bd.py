import sqlite3
from administrador import Administrador

DB_PATH = "../db.sqlite"
conn = sqlite3.connect(DB_PATH)
def printar_usuarios():

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

def logar_adm(login:str, senha:str)->Administrador:

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario WHERE (nome,senha) = ('"+login+"','"+senha+"')")
    usuarios = cursor.fetchall()
    if(len(usuarios)==1):#acertou a senha e o login
        return
    
     

def fechar_con_db():
    conn.close()