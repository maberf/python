# JOKEMPÔ
from random import randint
jok = (0,'Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
jog = int(input('Qual sua jogada? '))
comp = randint(1, 3)
print('Você jogou {}'.format(jok[jog]))
print('Computador jogou {}'.format(jok[comp]))
print('='*5, 'RESULTADO', '='*5)
if jog == 1: #Jogador Pedra
    if comp == 1:
        print('EMPATE!')
    elif comp == 2:
        print('COMPUTADOR VENCEU!')
    elif comp == 3:
        print('VOCÊ VENCEU!')
elif jog == 2: #Jogador Papel
    if comp == 1:
        print('VOCÊ VENCEU!')
    elif comp == 2:
        print('EMPATE!')
    elif comp == 3:
        print('COMPUTADOR VENCEU!')
elif jog == 3: #Jogador Tesoura
    if comp == 1:
        print('COMPUTADOR VENCEU!')
    elif comp == 2:
        print('VOCÊ VENCEU!')
    elif comp == 3:
        print('EMPATE!')