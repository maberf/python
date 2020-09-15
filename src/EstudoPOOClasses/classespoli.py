class Pizza:
    pedacos = 8

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    def ingredientes():
        return 'Ingredientes'

class Muzzarela(Pizza):

    @staticmethod
    def ingredientes(): #sobrescreve
        return ['muzzarela', 'molho', 'orégano']

class Calabresa(Pizza): #herança simples

    @staticmethod
    def ingredientes(): #sobrescreve
        return ['calabreza', 'molho', 'pimenta']

    pass
