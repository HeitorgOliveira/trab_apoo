from disciplina import Disciplina

class UsuarioGeral:
    def __init__(self, nome:str, id:int):
        self.nome = nome
        self.id = id
        self.disciplinas:list[Disciplina] = []
