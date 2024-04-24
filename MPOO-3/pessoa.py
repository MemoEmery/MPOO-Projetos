from endereço import Endereco

class Pessoa(Endereco):
    def __init__(self, nome, email,cpf,rua,cidade,cep,numero):
        super .__init__(self,rua,cidade,cep,numero)
        self._nome = nome 
        self._email = email
        self._cpf = cpf
    
    def get_nome(self):
        return self._nome
    
    def set_nome(self,nome):
        self._nome =nome
    





