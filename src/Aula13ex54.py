from datetime import date
atual = date.today().year
nasc = [0,0,0,0,0,0,0,0]
idade = [0,0,0,0,0,0,0,0]
maior = 0
menor = 0
for p in range(1,8):
    nasc[p-1] = int(input('Data Nascimento {}a. pessoa? '.format(p)))
    idade[p-1] = atual - nasc[p-1]
    if idade[p-1] >= 18:
        maior += 1 #no python tem que por o valor 1 no incremento
    else:
        menor += 1
for p in range(1,8):
    print('A {} pessoa tem {} anos.'.format(p, idade[p-1]))
print('Total de Maiores = {}'.format(maior))
print('Total de Menores = {}'.format(menor))