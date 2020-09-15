#CINCO NÚMEROS ALEATÓRIOS ENTRE 0 E 1000
#Colocar numa tupla e listar maior e menor
maior = 0
menor = 1001
from random import randint
num = (randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000))
print('Valores sorteados: ', end='')
for i in range(0, len(num)):
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]
    print(num[i], ' ', end='')
print(f'\nMaior = {maior}')
print(f'Menor = {menor}')