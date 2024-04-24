from aluno import *
from professor import *
from cadastro import *
from diretor import *
from coordenador import *


def cadastrarAluno():
    if Diretor or Coordenador:
       return Cadastro.adicionarAluno()