#MENU DE OPÇÕES
n1 = int(input('Número 1? '))
n2 = int(input('Número 2? '))
menu = 0
while menu != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair''')
    menu = int(input('Opção? '))
    if menu == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif menu == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Maior entre {} e {} é {}'.format(n1, n2, maior))
    elif menu == 4:
        n1 = int(input('Número 1? '))
        n2 = int(input('Número 2? '))
        print('Novos valores {} e {}.' .format(n1, n2))
    elif menu == 5:
        print('Sem mais cálculos.')
    else:
        print('Opção Inválida!')
    print('=' * 20)
print('Fim do programa!')