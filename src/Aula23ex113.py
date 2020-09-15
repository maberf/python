#AULA 23 - Ex. 113
#Tratamento de Erro

# Funções Iniciais

def leiaInt(num):
    while True:
        try:
           n = int(input(num))
        except (ValueError, TypeError):
            print(f'\033[31mErro de dado digitado. Tente novamente.\033[m')
            continue  # joga para o laço de novo
        else:
            return n

def leiaFloat(num):
    while True:
        try:
           n = float(input(num))
        except (ValueError, TypeError):
            print(f'\033[31mErro de dado digitado. Tente novamente.\033[m')
            continue  # joga para o laço de novo
        else:
            return n

# Programa Principal
n1 = leiaInt('Valor inteiro? ')
n2 = leiaFloat(('Valor real? '))
print(f'Valores: inteiro = {n1} e real = {n2}.')