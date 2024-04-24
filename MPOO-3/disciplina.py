from curso import Curso
class Disciplina ():
    def __init__(self,codigo,turno,disciplina,sala,curso):
        super .__init__(self,codigo,turno,curso)
        self.sala = sala
        self.disciplina=disciplina
        