#LISTA DE PARES E IMPARES
#lista com 7 valores numéricos
#lista com duas sublistas, de pares e ímpares
#ímpares e pares impressos em ordem crescente
num = [[], []] #Estruturação lista com sublistas vazias
for i in range(0, 7):
    n = (int(input('Numero? ')))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('-'*30)
print(f'Os pares são {num[0]}.')
print(f'Os ímpares são {num[1]}.')
