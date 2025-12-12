import sqlite3
from disciplina import Disciplina

class UsuarioGeral:
    def __init__(self, nome:str, id:int):
        self.nome = nome
        self.id = id
        self.disciplinas:list[Disciplina] = []
    
    def carregarDisciplinas(self):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome, codigo, id_professor, id_admin
            FROM Disciplina
            WHERE id_admin = ?
        """, (self.id,))

        linhas = cursor.fetchall()
        conn.close()

        self.disciplinas = []  # agora é LISTA

        for id_disc, nome, codigo, id_prof, id_adm in linhas:
            disciplina = Disciplina(nome, codigo, id_prof, id_adm)
            self.disciplinas.append(disciplina)  # adiciona no vetor


