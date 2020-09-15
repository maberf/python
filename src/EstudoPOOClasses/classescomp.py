class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = [] #lista a ser carregada

    def insere_endereco(self, cidade, uf):
        self.enderecos.append(Endereco(cidade, uf))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.uf)

    def __del__(self): #chamada ao garbage collector
        print(f'{self.nome} APAGADO!')

class Endereco: #classe composta
    def __init__(self, cidade, uf):
        self.cidade = cidade
        self.uf = uf

    def __del__(self): #chamada ao garbage collector
        print(f'{self.cidade}/{self.uf} APAGADOS!')

