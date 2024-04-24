from aluno import*
from professor import*

class Cadastro:
    def __init__(self):
        self._nome = []

    def adicionarAluno (self,nome):
        self._nome.append(nome)

    def get_nome(self):
        return self._nome

    def set_aluno(self,nome):
        self._nome = nome
