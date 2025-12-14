from tipoMedia import TipoMedia
from disciplina import Disciplina

class Media():
    
    def __init__(self, disciplinaAssociada: Disciplina):
        self.disciplinaAssociada = disciplinaAssociada
        self.medias = {
            TipoMedia.MEDIA_FINAL : self.calcularMediaFinal,
            TipoMedia.MEDIA_ATIVIDADE : self.calcularMediaTipoTarefa,
            TipoMedia.MEDIA_TRABALHO : self.calcularMediaTipoTarefa,
            TipoMedia.MEDIA_PROVA : self.calcularMediaTipoTarefa
        }
        

    def calcularMediaFinal():
        None

    def calcularMediaTipoTarefa():
        None
