'''def soma(*valores): #Desempacotamento
    sum = 0
    for num in valores:
        sum += num
    print(f'Somando {valores} temos {sum}')

soma(5, 2)
soma(15, 78, 116)'''


'''def dobra(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i += 1

valores = [6, 3, 9, 23]
dobra(valores)
print(valores)'''

'''def contador(* num): #parâmetros variáveis
    print(num) #imprime tuplas


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 8, 5)'''

'''def subtracao (a, b):
    print(f' {a} - {b} = {a-b}')


#Programa Principal
subtracao(6, 4) #sem explicitar parâmetro
subtracao(a=6, b=4) #parâmetros explícitos
subtracao(b=4, a=6) #parâmetros em outra ordem
subtracao(a=4, b=6) #parâmetros alterados'''

def mensagem(txt): #função com parâmetro
    tamtxt = len(txt)
    print('~' * tamtxt)  #linha do tamanho do texto
    print(f'{txt}') #imprime texto
    print('~' * tamtxt)

# Programa Principal
mensagem('   CURSO DE PYTHON   ')#mensagem altera com espaços
mensagem(' ESTUDO EM VIDEO ')
mensagem('MABER FERNANDES')

