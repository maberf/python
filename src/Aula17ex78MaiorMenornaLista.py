#MAIOR E MENOR EM LISTA
valores = [] #cria lista vazia
maior = menor = 0
for i in range(0, 5): #carregamento da lista
    valores.append(int(input(f'Valor{i}? ')))
    if i == 0:
        menor = maior = valores[0]
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
print('-'*30)
print(f'Valores: {valores}')
#
#Não é caso de index porque pode ter mais de uma posiçãp
#print(f'Maior = {maior} na posição {valores.index(maior)}')
#print(f'Menor = {menor} na posição {valores.index(menor)}')
#
print(f'Maior valor {maior} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}..', end='')
print(f'\nMenor valor {menor} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}..', end='')
print('\n','-'*30)