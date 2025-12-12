import sqlite3
from usuarioGeral import UsuarioGeral
from disciplina import Disciplina

class Admin(UsuarioGeral):
    def __init__(self, nome: str, id: int):
        super().__init__(nome, id)
    
    # Para validar o administrador antes de cadastrar disciplina
    @classmethod
    def carregarAdminPorId(cls, id_admin: int):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, nome
            FROM Usuario
            WHERE id = ? AND tipo = 'Admin'
        """, (id_admin,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], nome=row[1])
        else:
            return None

    def cadastrarDisciplina(self, nome: str, codigo: str, id_professor: int):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        # Verifica se o professor existe de novo
        cursor.execute("SELECT * FROM Usuario WHERE id = ? AND tipo = 'Prof'", (id_professor,))
        prof = cursor.fetchone()

        if not prof:
            print("\n[Erro] professor não encontrado")
            conn.close()
            return

        try:
            cursor.execute("""
                INSERT INTO Disciplina (nome, codigo, id_professor, id_admin)
                VALUES (?, ?, ?, ?)
            """, (nome, codigo, id_professor, self.id))

            conn.commit()
            print(f"\n-> Disciplina '{nome}' cadastrada com sucesso!")

        except Exception as e:
            print("\n[Erro] ao cadastrar disciplina:", e)

        conn.close()
    
    def editarDisciplina(self, nome=None, codigo=None, id_professor=None):
        # Busca a disciplina no vetor de disciplinas da classe mãe Usuario Geral
        disciplina = None
        for d in self.disciplinas:
            print(d.codigo, codigo)
            if d.codigo == codigo:
                disciplina = d
                break

        if disciplina is None:
            print(f"[ERRO] Disciplina com código '{codigo}' não encontrada")
            return

        # Alterações na disciplina
        if nome.strip() != "":
            disciplina.nome = nome

        if id_professor is not None:
            disciplina.id_prof = id_professor

        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        if id_professor is not None:
            cursor.execute("SELECT id FROM Usuario WHERE id = ? AND tipo = 'Prof'", (id_professor,))
            if cursor.fetchone() is None:
                print("[ERRO] Professor não encontrado")
                conn.close()
                return

        # Atualiza o BD
        try:
            cursor.execute(
                """
                UPDATE Disciplina
                SET nome = ?, id_professor = ?
                WHERE codigo = ? AND id_admin = ?
                """,
                (disciplina.nome, disciplina.id_prof, codigo, self.id)
            )

            conn.commit()
            print(f"Disciplina '{codigo}' editada com sucesso!")

        except Exception as e:
            print("Erro ao atualizar disciplina:", e)
        
        finally:
            conn.close()

    def excluirDisciplina():
        None
