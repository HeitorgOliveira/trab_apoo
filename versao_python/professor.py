from usuario import Usuario 
class Professor(Usuario):
    def __init__(self,nome:str, id:int):
        super.__init__(nome,id)