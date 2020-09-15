nome = input('Nome? ').strip()#strip tira espaços antes e depois do nome todo
print('O nome em maiúsculas é {}.'.format(nome.upper()))
print('O nome em minúsculas é {}.'.format(nome.lower()))
comp = len(nome)-nome.count(' ')#conta os caracteres do nome, subtrai espaços
print('O nome tem {} caracteres'.format(comp))
nomes = nome.split() #lista com os nomes
nomepri = nomes[0] #primeiro nome
print('O nome {}'.format(nomepri), 'possui comprimento de', len(nomepri), 'caracteres.')