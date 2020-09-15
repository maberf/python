#MATRIZ 3 X 3
num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #Matriz 3x3
somapar = somatercol = somaseglin = 0
for i in range(0, 3):
    for j in range(0, 3):
        num[i][j] = (int(input(f'Numero {[i,j]}? ')))
print('-'*25)
for i in range(0, 3):
    for j in range(0, 3):
        if num[i][j] %2 == 0:
            somapar += num[i][j]
        print(f'[{num[i][j]:^5}] ', end='')
    print()
    somatercol += num[i][2]
for j in range(0, 3):
    somaseglin += num[1][j]
print('-'*25)
print(f'Soma dos pares = {somapar}')
print(f'Soma 3a coluna = {somatercol}')
print(f'Soma 2a linha = {somaseglin}')