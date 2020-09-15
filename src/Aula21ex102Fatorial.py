#FATORIAL
#
# Funções Iniciais
#
def fatorial(num=1, show=True):
    '''
    Calcula o fatorial de um número num
    :param num: número
    :param show: mostra o cálculo com intervalo de 1 segundo para cada algarismo (default mostrar NÃO FUNCIONANDO como deveria. Investigar o erro)
    '''
    from time import sleep
    fat = 1
    for i in range(num, 0, -1):
        if show:
            sleep(1)
            print(f'{i}', end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        fat *= i
    return fat


# Programa Principal
num = int(input('Numero? '))
show = bool(input('Mostrar processo de cálculo? [True/False] '))
print(f'{num}! = {fatorial(num, show)}')
help(fatorial)