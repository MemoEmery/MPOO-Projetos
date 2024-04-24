from disciplina import*
from aluno import*

class Sala(Disciplina, Aluno):
    def __init__(self, codigo, turno, disciplina, sala, curso):
        super().__init__(codigo, turno, disciplina, sala, curso)


    