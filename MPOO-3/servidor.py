from pessoa import Pessoa

class Servidor(Pessoa):
    def __init__(self, nome, email, cpf, endereco,turno,cargo):
        super().__init__(nome, email, cpf, endereco)
        self._turno=turno
        self._cargo=cargo
        