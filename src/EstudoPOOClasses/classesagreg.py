class CarrinhodeCompras:
    def __init__(self):
        self.produtos = [] #agregação na lista

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

