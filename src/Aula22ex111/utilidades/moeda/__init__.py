# MÓDULO MOEDAS - Exs. 107 a 112 (Ex. 111 pacote moeda)
def metade(n, formato=False):
    '''
    >> Calcula o aumento de deterinado preço,
    retornando o resultado com ou sem formatação.
    :param n: preço
    :param formato: True para saída tipo R$ X,XX.
    :return: valor calculado, com ou sem formatação
    '''
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n, p, formato=False):
    res = n * (1 + p/100)
    return res if formato is False else moeda(res)


def diminuir(n, p, formato=False):
    res = n * (1 - p/100)
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda ='R$ '):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(n, a, d): #instruções de chamada e impressão
    print('-' * 42)
    print(('RESUMO'.center(42)))
    print('-' * 42) #alinhamentos abaixo com uso de \t (tabs)
    print(f'Metade de {moeda(n):<20}\t{metade(n, True)}')
    print(f'Dobro de {moeda(n):<20}\t{dobro(n, True)}')
    print(f'{a:<2} % de aumento \t\t{aumentar(n, a, True)}')
    print(f'{d:<2} % de desconto \t\t{diminuir(n, d, True)}')
    print('-' * 42)