
'''
public, _protected, __private
'''

class BasedeDados:
    def __init__(self):
        self.__dados = {} #dicionário como "pseuda" base de dados
                         #atributo dados é o "coração" do sistema

    @property #getter - faz um método parecer uma propriedade da classe
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados: #cria dicionário
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome}) #atualiza dicionário

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]