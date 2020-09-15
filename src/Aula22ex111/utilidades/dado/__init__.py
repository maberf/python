#MÓDULO DE VALIDAÇÃO DO DADO Ex.112
#
def leiaDinheiro(msg): #macetes para validação do dado de entrada
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip() #vírgula por ponto tira vazios
        if entrada.isalpha() or entrada == '': #se caractere ou sem espaços vazios
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
#
def leiaInt(msg): #opera igual a leia Dinheiro
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)