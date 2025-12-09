from usuario import Usuario
from entrega import Entrega
from typing import List

class Aluno (Usuario):
    def __init__(self, nome:str, id:int):
        super().__init__(nome, id)
        self.entregas:List[Entrega] = []
