from pessoa import Pessoa
from disciplina import Disciplina

class Aluno(Pessoa,Disciplina):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula
        self.disciplina = []

    def matricularDisciplina(self,disciplina):
        self.disciplina.append(disciplina)

    def listarDisciplina(self):
        return f'{"Disciplina"+self.disciplina}'
    
    def removeDisciplina(self,disciplina):
        self.disciplina.remove(disciplina)
        