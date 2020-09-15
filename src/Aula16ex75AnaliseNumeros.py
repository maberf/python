#ANÁLISE DE DADOS
#Ler 4 valores e salvar numa tupla
#
# Este código também testa se os valores estão dentro do range
# Também gera mensagem de ausência de número par, se houver
#
while True:
    n1 = int(input('Valor1?[0-9] '))
    if 0 <= n1 <= 9:
        n2 = int(input('Valor2? [0-9]: '))
        if 0 <= n2 <= 9:
            n3 = int(input('Valor? [0-9]: '))
            if 0 <= n3 <= 9:
                n4 = int(input('Valor4? [0-9]: '))
                break
        print('Números fora do range. Tente novamente.')
num = (n1, n2, n3, n4)
print(f'Valores digitados: {num}')
print(f'Número 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'Número 3 na {num.index(3)}a posição.')
else:
    print(f'Número 3 não digitado.')
pares = 0
print(f'Números pares: ', end='')
for i in num:
    if i % 2 == 0:
        print(i, end=' ')
        pares +=1
if pares == 0:
    print('não há.')

