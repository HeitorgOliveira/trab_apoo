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
        if codigo == None:
            print("ERRO: Precisa informar o código da disciplina")
            return None
            
        if nome == None and id_professor == None:
            print("Informar pelo menos nome ou o id do professor a ser alterado")
            return None
        
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Disciplinas WHERE codigo = ?", (codigo))
        disciplina = cursor.fetchone()

        if not disciplina:
            print(f"[ERRO]: Disciplina com o código {codigo} não econtrada")
            conn.close()
            return
        
        print(disciplina)
        return 

        if nome != None:
            self.disciplinas[codigo].nome = nome

        if id_professor != None:
            self.disciplinas[codigo].id = id_professor

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
                UPDATE Disciplina SET nome = ? AND id_professor = ? WHERE id = ?
            """, (self.disciplinas[codigo].nome, self.disciplinas[codigo].id, codigo))

            conn.commit()
            print(f"Disciplina {codigo} editada com sucesso!")

        except Exception as e:
            print(f"Erro: {e}")

        None

    def excluirDisciplina():
        None
