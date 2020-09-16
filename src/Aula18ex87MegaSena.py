# MEGA SENA
# Sugere números de jogos
from random import randint
from time import sleep
aposta = list()
jogo = list()
print('-'*30)
print('      JOGA NA MEGA SENA     ')
print('-'*30)
qtd = int(input('Quantos jogos? '))
print('-'*3, f' Sorteando {qtd} jogos... ', '-'*3)
for i in range(qtd):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in aposta:
            aposta.append(num)
            cont += 1
        if cont >= 6:
            break
    aposta.sort()
    jogo.append(aposta[:])
    aposta.clear()
    print(f'Jogo {i+1}: {jogo[i]}')
    sleep(1)
print('         BOA SORTE!     ')
