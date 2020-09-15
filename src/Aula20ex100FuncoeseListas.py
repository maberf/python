from time import sleep

def sorteio(lista):
    print(f'Os números são: ', end='')
    from random import randint
    i = 0
    while i <= 5:
        lista.append(randint(0, 100))
        sleep(1)
        print(f'{lista[i]} ', end='')# flush=True)
        i += 1

def somaPar(lista):
    par = 0
    for num in lista:
        if num % 2 == 0:
            par += num
    print()
    print(f'Soma dos pares: {par}')


#Programa Principal
numeros = []
sorteio(numeros)
somaPar(numeros)
