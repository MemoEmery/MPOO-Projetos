from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.matricula = matricula

    

   