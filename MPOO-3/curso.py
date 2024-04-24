from disciplina import Disciplina

class Curso(Disciplina):
    def __init__(self,codCurso,turno):
        self._codCurso= codCurso 
        self.disciplina = []
        self.turno=turno

    def listarCurso(self):
        return f'{'Codigo do curso'+self._codCurso},{'Disciplina'+self.disciplina},{'Turno'+self.turno}'

        