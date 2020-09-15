def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

final_price = calculate_price(100.0, discount=5.0)
#final_price = calculate_price(100.0, tax_percentage=7)
#final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
#
print(final_price)




'''def campeoescopa(pais, *args):
    print('Pais: ', pais)
    for titulo in args:
        print('ano: ', titulo)


campeoescopa('Brasil', '1958', '1962', '1970', '1994', '2002')
#poderiamos adicionar quantos paises quisessemos'''


'''def fatorial(num=1): #função com retorno
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    return fat


n1 = int(input('Numero 1? '))
n2 = int(input('Número 2? '))
print(f' {n1}! = {fatorial(n1)}.')
print(f' {n2}! = {fatorial(n2)}.')'''



'''def somar(a=0, b=0, c=0): #função com retorno
    """
    Soma valores
    :param a: valor 1
    :param b: valor 2
    :param c: valor 3
    :return: soma
    """
    soma = a + b + c
    return soma


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
print(f'Os resultados foram {r1} e {r2}.')'''



'''def funcao():
    n1 = 4
    print(f'n1 dentro da função = {n1}')


n1 = 2
funcao()
print(f'n1 fora da função = {n1}')'''

'''def teste():
    x = 8
    print(f'n na função teste = {n}')
    print(f'x na função teste = {x}')


#Programa Principal
n = 2
print(f'n no programa principal = {n}')
teste()
print(f'x no programa principal = {x}')'''

'''def somar(a=0, b=0, c=0): #a, b e c são opcionais, default zero
    ''''''
    Soma 3 valores e imorime o resultado
    :param a: primeiro algarismo
    :param b: segundo algarismo
    :param c: terceiro algarismo
    :return: sem retorno
    Função criada por Maber Fernandes no Estudo Python'''
'''
    soma = a + b + c
    print(f'Soma = {soma}')


somar(3, 2, 5)
somar(8, 4)'''


"""#Aula21 - DOCSTRINGS
def contador(i, f, p):"""

""" Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Maber Fernandes na Aula 21
    """
    
"""     c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)"""
