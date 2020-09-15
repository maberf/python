from math import sqrt, floor #importação sós das instruções sqrt e floor
num = int(input('Número? '))
print('A raiz de {} é {:.2f}.'.format(num,floor(sqrt(num))))
#calcula a raiz arredondando em dias casas decimais para baixo (floor).