from usuarioAcademico import UsuarioAcadem
from entrega import Entrega
from typing import List

class Aluno (UsuarioAcadem):
    def __init__(self, nome:str, id:int):
        super().__init__(nome, id)
        self.entregas:List[Entrega] = []
