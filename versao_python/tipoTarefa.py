from enum import Enum

class TipoTarefa(Enum):
    ATIVIDADE = "atividade"
    TRABALHO = "trabalho"
    PROVA = "prova"

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor