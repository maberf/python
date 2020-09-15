class Pizza:
    pedacos = 8

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

class Muzzarela(Pizza): #herança simples
    pass

class Calabresa(Pizza): #herança simples
    pass

class MeioAMeio(Muzzarela, Calabresa): #herança múltipla
    pass
