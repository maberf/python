#LISTA ORDENADA DECRESCENTE
num = list()
cont = ''
while True:
    num.append(int(input(f'Valor? ')))
    cont = str(input('Continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('-'*30)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True) #ordem decrescente
print(f'Você digitou os valores {num}.')
if 5 in num:
    print('Valor 5 adicionado na lista')
else:
    print('Valor 5 não adicionado lista')
