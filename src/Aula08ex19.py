from random import shuffle #importação otimizada
n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))
lista = [n1, n2, n3, n4] #variável vetor
shuffle(lista) #embaralha a lista
print('Ordem de apresentação: ', lista)
#escolhido = random.choice(lista) #o random já opera direto no objeto
#print('O escolhido é {}.'.format(escolhido))


