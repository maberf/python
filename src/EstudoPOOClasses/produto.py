class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        return

    #Getter
    @property
    def preco(self):
        return self._preco

    #Seter
    @preco.setter #nome da variável que se deseja conformar
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', '')) #conformador
        self._preco = valor
