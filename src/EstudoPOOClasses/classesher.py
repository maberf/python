class Pessoa: #superclasse ou classe mãe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

#subclasses ou classes filha

class Cliente (Pessoa): #herda da superclasse
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

class Aluno (Pessoa): #herda da superclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')