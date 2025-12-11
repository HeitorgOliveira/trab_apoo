import sqlite3

DB_PATH = "db.sqlite"
conn = sqlite3.connect(DB_PATH)

# [Gabi] acho que não precisamos dessa fuunção eu já tinha feito um print_users no main.py
# def printar_usuarios():
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Usuario")
#     usuarios = cursor.fetchall()
#     for usuario in usuarios:
#         print(usuario)

def logar_adm(id_admin: int, senha: str) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM Usuario WHERE id = ? AND senha = ? AND tipo = 'Admin'",
        (id_admin, senha)
    )

    row = cursor.fetchone()
    return row is not None

def fechar_con_db():
    conn.close()