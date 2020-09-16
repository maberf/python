def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro de dado digitado. Tente novamente.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center((42)))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[m - \033[34m{item}\033[m')
        i += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao
