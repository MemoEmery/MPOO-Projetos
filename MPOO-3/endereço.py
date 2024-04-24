class Endereco():
    def __init__(self,rua,numero,cidade,cep):
        self.rua=rua
        self.nuemro=numero
        self.cidade=cidade
        self.cep=cep

    def formatarEndereco(self):
        return f'{"Rua"+self.rua},{"nummero"+self.cidade}, {'Cidade'+self.cep}'