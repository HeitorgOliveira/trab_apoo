from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from tarefa import Tarefa #isso resolver o import ciclico dentre tarefa e disciplina

class Disciplina:
    def __init__(self,nome:str, codigo:int):
        self.nome=nome
        self.codigo=codigo
        self.listaTarefas:list['Tarefa']=[] # Importa a classe e o Enum

    def incluir_atividade(self, tarefa: 'Tarefa') -> None:
        self.listaTarefas.append(tarefa)
        tarefa.disciplina = self 

