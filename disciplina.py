from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from tarefa import Tarefa # Isso resolve o import ciclico dentre tarefa e disciplina

class Disciplina:
    def __init__(self,nome:str, codigo:str, id_prof:int, id_adm:int):
        self.nome=nome
        self.codigo=codigo
        self.id_prof=id_prof
        id_adm=id_adm
        self.lista_tarefas:list['Tarefa']=[] # Importa a classe e o Enum

    def criarTarefa(self, tarefa: 'Tarefa') -> None:
        # Talvez remover (o que está comentado)???
        # self.lista_tarefas.append(tarefa)
        # tarefa.disciplina = self 
        None
    
    def calcularMediaTipoTarefa():
        None
    
    def calcularMediaFinal():
        None

    def editarTarefa():
        None
    
    def excluirTarefa():
        None


