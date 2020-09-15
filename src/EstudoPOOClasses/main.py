# PROGRAMA PRINCIPAL
from classespoli import *

print(Pizza.ingredientes())
#sobrescreve os ingredientes da pizza
print(Muzzarela.ingredientes())
print(Calabresa.ingredientes())

'''from classeshermult import *
print(MeioAMeio.pedacos)
MeioAMeio.mudar_tamanho(10)
print(MeioAMeio.pedacos)'''

'''from classesher import *

cliente1 = Cliente('Suélen', 25)
print(cliente1.nome)
cliente1.falar()
cliente1.comprar()

aluno1 = Aluno('Dienefer', 21)
print(aluno1.nome)
aluno1.falar()
aluno1.estudar()'''

'''from classescomp import Cliente

cliente1 = Cliente('Ariovardo', 56)
cliente1.insere_endereco('Herval', 'RS')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1 #apaga o cliente e o endereço composto
print('-' * 10)

cliente2 = Cliente('Ariosto', 30)
cliente2.insere_endereco('Cacimbinhas', 'BA')
cliente2.insere_endereco('João Pessoa', 'PB')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2 #apaga o cliente e o endereço composto
print('-' * 10)

print('################################')'''


'''from classesagreg import CarrinhodeCompras, Produto

carrinho = CarrinhodeCompras()

prod1 = Produto('Camisa', 120)
prod2 = Produto('Bola', 150)
prod3 = Produto('Chuteira', 250)

carrinho.inserir_produtos(prod1)
carrinho.inserir_produtos(prod2)
carrinho.inserir_produtos(prod3)

carrinho.lista_produto()
print(carrinho.soma_total())'''


'''from classesassoc import Escrito
from classesassoc import Caneta
from classesassoc import Computador

#No primeiro momento, as classes são independentes
#uma da outra
escritor = Escritor('Joao das Couves')
caneta = Caneta('Bic')
computador = Computador('Asus')

#ASSOCIAÇÃO
#Na associação leva-se o objeto inteiro para outro
escritor.ferramenta = computador #associação
#Atributo ferramenta recebeu inteira a classe computador
escritor.ferramenta.escrever() #chama método da classe associada
#Atributo ferramenta recebeu inteira a classe caneta
escritor.ferramenta = caneta #associação
escritor.ferramenta.escrever() #chama método da classe associada'''


'''from basededados import BasedeDados

bd = BasedeDados()
bd.inserir_cliente(1, 'Artamir')
bd.inserir_cliente(2, 'Emerenciana')
bd.inserir_cliente(3, 'Everardo')
print('-' * 60)
#print(bd.__dados)
bd.lista_clientes()
print('-' * 60)
bd.apaga_cliente(1)
bd.lista_clientes()
print('-' * 20, 'até aqui funcionando', '-' * 20)
#bd.__dados = 'Uma coisa qualquer' #erro que buga todos os demais comandos!
bd.inserir_cliente(4, 'Doisberto')
bd.lista_clientes()
#print(bd.__dados)
#print(bd._BasedeDados__dados)
print(bd.dados)'''

'''from produto import Produto

p1 = Produto('camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('bicicleta', 'R$600') #dado errado, string
p2.desconto(15)
print(p2.preco)'''


'''from pessoa import Pessoa

p1 = Pessoa('Joao', 1990)
p2 = Pessoa('Maria', 1980)

print(p1.nome)
print(p2.nome)
p1.comer('maçã')
p1.comer('laranja')
p1.parar_comer()
p1.parar_comer()
p1.comer('laranja')
print(Pessoa.ano_atual)
print(f'{p1.nome} tem {p1.idade()} anos.')

p3 = Pessoa.por_idade('Ze', 32)
print(p3.nome, p3.nasc)

print(Pessoa.gera_id())
print(p1.gera_id())'''