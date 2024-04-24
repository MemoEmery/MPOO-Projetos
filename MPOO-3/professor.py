from pessoa import Pessoa
from servidor import Servidor

class Professor(Pessoa,Servidor):
    def __init__(self,nome,email,cpf,endereco,cargo,formacao):
        super .__init__(nome,email,cpf,endereco,cargo)
        self._cargo=cargo
        self._formacao=formacao
        