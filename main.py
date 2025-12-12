import sqlite3
from administrador import Admin

def cadastrar(admin):
    opcao = 0
    while opcao != 1:
        nome = input("\nDigite o nome da disciplina: ")
        cod = input("Digite o código da disciplina: ")
        id_prof = int(input("Digite o id do professor responsável pela disciplina: "))
        
        print(f"\n\n------ INFORMAÇÕES A SEREM CADASTRADAS -------\n")
        print(f"Nome da disciplina: {nome}\nCódigo da disciplina: {cod}\nID do professor: {id_prof}")
        opcao = int(input("Tem certeza?\n[1] Sim\n[0] Não\n\n"))  

    admin.cadastrarDisciplina(nome, cod, id_prof)
    admin.carregarDisciplinas()

def editar(admin):
    codigo = input("Digite o código da disciplina a ser alterada: ")
            
    opcao = 0
    while opcao != 1:
        print("* Digite apenas o que quiser editar, para pular digite [enter] *")
        nome = input("Digite o novo nome da disciplina: ")
        entrada_prof = input("Digite o id do novo professor: ")
        if entrada_prof.strip() == "":
            id_professor = None
        else:
            id_professor = int(entrada_prof)

        print(f"\n\n------ INFORMAÇÕES A SEREM ATUALIZADAS -------\nNome: {nome}\nID do professor: {id_professor}")
        opcao = int(input("Tem certeza?\n[1] Sim\n[0] Não\n\n"))  

    admin.editarDisciplina(nome=nome, codigo=codigo, id_professor=id_professor)
    admin.carregarDisciplinas()

# Função adicional para visualização do banco de dados
def printDisciplinas():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Disciplina")
    disciplinas = cursor.fetchall()

    if len(disciplinas) == 0:
        print("\n-> Nenhuma disciplina cadastrada")
    else:
        print("\n--- Disciplinas cadastradas ---")
        for d in disciplinas:
            print(f"->  {d[1]}")
            print(f"    ID: {d[0]}, código: {d[2]}, professor ID: {d[3]}, admin ID: {d[4]}")

    conn.close()

# Função adicional para visualização do banco de dados
def printUsers():
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, tipo FROM Usuario")
    usuarios = cursor.fetchall()

    if len(usuarios) == 0:
        print("\n-> Nenhum usuário encontrado")
    else:
        print("\n--- Usuários cadastrados ---")
        for u in usuarios:
            print(f"->  {u[1]}")
            print(f"    ID: {u[0]}, tipo: {u[2]}")

    conn.close()

def logarAdm(id_admin: int, senha: str) -> bool:
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM Usuario WHERE id = ? AND senha = ? AND tipo = 'Admin'",
        (id_admin, senha)
    )

    row = cursor.fetchone()
    conn.close()
    return row is not None

def login():
    id_admin = int(input("Digite o ID do administrador: "))
    admin = Admin.carregarAdminPorId(id_admin)

    if admin is None:
        print("\n[Erro] administrador não encontrado!")
        return None

    senha = input(f"\nAdministrador {admin.nome} digite sua senha: ")
    if logarAdm(admin.id, senha):
        print(f"-> Administrador {admin.nome} validado!")
    else:
        print(f"[Erro] senha inválida")
        return None

    return admin

def main():
    # Como as duas funcionalidades escolhidas para codificação só podem ser feitas
    # por um administrador, optamos por já logar como administrador
    admin = None
    while admin is None:
        admin = login()
    
    admin.carregarDisciplinas()

    while True:
        print("\n----- Gerenciamento de disciplinas -----")
        print("[1] - Cadastrar disciplina")
        print("[2] - Editar disciplina")
        print("[3] - Exibir disciplinas cadastradas") # Adicional não é uma das funcionalidades, mas é bom para visualizar
        print("[4] - Exibir usuários cadastrados") # Adicional não é uma das funcionalidades, mas é bom para visualizar
        print("[0] - Sair")
        op = input("\nSelecione uma das opções acima: ")
        match op:
            case "1":
                print("\n----- Cadastrar disciplinas -----")
                cadastrar(admin)
            case "2":
                print("\n----- Editar disciplinas -----")
                editar(admin) 
            case "3":
                printDisciplinas()
            case "4":
                printUsers()
            case "0":
                print("Saindo...")
                break
            case _:
                print("[Erro] opção inválida")

if __name__ == "__main__":
    main()
