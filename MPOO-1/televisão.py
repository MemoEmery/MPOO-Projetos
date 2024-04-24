class Televisao:
    def __init__(self, volume_inicial=10, canal_inicial=1):
        self.volume = volume_inicial
        self.canal = canal_inicial
        self.modo_mudo = False

    def aumentar_volume(self):
        if not self.modo_mudo:
            self.volume += 1
            print("Volume aumentado para", self.volume)
        else:
            print("Modo mudo ativado. Volume não pode ser alterado.")

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print("Canal alterado para", self.canal)

    def ativar_modo_mudo(self):
        self.modo_mudo = True
        print("Modo mudo ativado.")

    def desativar_modo_mudo(self):
        self.modo_mudo = False
        print("Modo mudo desativado.")

tv = Televisao()

tv.aumentar_volume()  # Aumentar o volume
tv.mudar_canal(5)     # Muda para o canal 5
tv.ativar_modo_mudo() # Ativar o modo mudo
tv.aumentar_volume()  # Tentativa de aumentar o volume no modo mudo
tv.desativar_modo_mudo() # Desativa o modo mudo
tv.aumentar_volume()  # Aumentar o volume após desativar o modo mudo
