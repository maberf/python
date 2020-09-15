#print('\033[0;33;44mOlá Dummie!\033[m')
#print('\033[7;33;44mHello Dummie!\033[m') #inverte
#print('\033[1;30mOlá Kid!\033[m')
#print('\033[7;30mHello Kid!\033[m') #inverte
#
#nome = 'Creusa'
#print('Olá, {}{}{}!'.format('\033[1;31;43m', nome, '\033[m'))
#
nome = 'Creusa'
cor = {'limpa':'\033[m',
        'vermelha':'\033[31m',
        'azul':'\033[34m'}
print('Olá, {}{}{}!'.format(cor['limpa'], nome, '\033[m'))
print('Olá, {}{}{}!'.format(cor['vermelha'], nome, '\033[m'))
print('Olá, {}{}{}!'.format(cor['azul'], nome, '\033[m'))