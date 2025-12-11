import sqlite3
from usuarioGeral import UsuarioGeral

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

        # Verifica se o professor existe
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
    
    def editarDisciplina():
        None

    def excluirDisciplina():
        None
