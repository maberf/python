#AULA 17 EX 79 - LÊ LISTA ATÉ USUÁRIO DEFINIR (BREAK)
num = list()
cont = ''
while True:
    n = int(input(f'Valor? '))
    if n not in num:#aqui é o "pulo do gato", variável not in lista
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não adicionado!')
    cont = str(input('Continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('-'*30)
num.sort()#tem que ser separado, não opera dentro do place holder
print(f'Você digitou os valores {num}.')
