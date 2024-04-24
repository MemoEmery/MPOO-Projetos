from servidor import Servidor

class Coordenador(Servidor):
    def __init__(self, nome, email, cpf, endereco, turno, cargo):
        super().__init__(nome, email, cpf, endereco, turno, cargo)