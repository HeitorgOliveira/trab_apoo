import sqlite3
from conexao_bd import logar_adm
from administrador import Admin

def cadastrar():
    id_admin = int(input("Digite o ID do administrador: "))
    admin = Admin.carregarAdminPorId(id_admin)

    if admin is None:
        print("\n[Erro] administrador não encontrado!")
        return

    senha = input(f"\nAdministrador {admin.nome} digite sua senha: ")
    if logar_adm(admin.id, senha):
        print(f"-> Administrador {admin.nome} validado!")
    else:
        print(f"[Erro] senha inválida")
        return

    nome = input("\nDigite o nome da disciplina: ")
    cod = input("Digite o código da disciplina: ")
    id_prof = input("Digite o id do professor responsável pela disciplina: ")

    admin.cadastrarDisciplina(nome, cod, id_prof)

def editar():
    id_professor = int(input("Digite o id do administrador: "))
    admin = Admin.carregarAdminPorId(id_professor)
    if admin is None:
        print("\n[Erro]: Admin não encontrado ou o professor não é admin")
        return
    senha = input(f"\nAdministrador {admin.nome} digite sua senha: ")
    if logar_adm(admin.id, senha):
        print(f"-> Administrador {admin.nome} validado!")
    else:
        print(f"[Erro] senha inválida")
        return
    
    opcao = 0
    while opcao == 0:
        nome = input("Digite o nome do professor: ")
        codigo = input("Digite o código da disciplina: ")
        id_professor = int(input("Digite o id do professor: "))

        print(f"\n\n------ INFORMAÇÕES -------\nNome: {nome}\nCodigo: {codigo}\nID do professor: {id_professor}")
        opcao = int(input("Tem certeza?\n[1] Sim\n[0] Não\n\n"))  


    Admin.editarDisciplina(nome=nome, codigo=codigo, id_professor=id_professor)
    

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

def main():
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
                cadastrar()
            case "2":
                print("\n----- Editar disciplinas -----")

                editar() # Editar disciplina
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
