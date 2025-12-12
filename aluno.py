from usuarioAcademico import UsuarioAcadem
from entrega import Entrega
from typing import List
import sqlite3

class Aluno (UsuarioAcadem):
    def __init__(self, nome:str, id:int):
        super().__init__(nome, id)
        self.entregas:List[Entrega] = []

    # Função adicional para exemplificar a forma como pensamos, onde 
    # o próprio aluno se inscreve na disciplina
    def inscreverEmDisciplina(self, codigo_disciplina:str):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        # Verifica se a disciplina existe
        cursor.execute("SELECT * FROM Disciplina WHERE codigo = ?", (codigo_disciplina))
        disciplina = cursor.fetchone()

        if not disciplina:
            print("\n[Erro] Disciplina não encontrada")
            conn.close()
            return

        try:
            cursor.execute("""
                INSERT INTO Inscricao (id_aluno, codigo_disciplina)
                VALUES (?, ?)
            """, (self.id, codigo_disciplina))

            conn.commit()
            print(f"\n-> Inscrição na disciplina '{codigo_disciplina}' realizada com sucesso!")

        except Exception as e:
            print("\n[Erro] ao inscrever na disciplina:", e)

        conn.close()