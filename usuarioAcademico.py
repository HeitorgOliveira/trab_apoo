from tarefa import Tarefa
from usuarioGeral import UsuarioGeral

class UsuarioAcadem(UsuarioGeral):
    def __init__(self):
        self.tarefas:list[Tarefa] = []