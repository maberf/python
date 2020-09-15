# MÓDULO
from datetime import date
from random import randint

# CLASSE PESSOA
class Pessoa:
    '''Esta classe estabelece as características de uma pessoa.'''

    #variável da classe
    ano_atual = int(date.today().year)

    #variáveis das instâncias
    #construtor
    def __init__(self, nome, nasc, comendo=False):
        self.nome = nome
        self.nasc = nasc
        self.comendo = comendo

    #métodos de instâncias

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def idade(self):
        return self.ano_atual - self.nasc

    #método de classe
    @classmethod
    def por_idade(cls, nome, idade):
        nasc = cls.ano_atual - idade
        return cls(nome, nasc)

    #método estático
    @staticmethod
    def gera_id():
        return randint(0, 100)
