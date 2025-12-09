from tipoTarefa import TipoTarefa
from disciplina import Disciplina

class Tarefa:
    def __init__(self, peso:float, tipo:TipoTarefa, disciplina:Disciplina):
        self.peso =peso
        self.tipo:TipoTarefa =tipo
        self.disciplina =disciplina