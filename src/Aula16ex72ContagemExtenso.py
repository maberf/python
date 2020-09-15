#CONTAGEM POR EXTENSO DE 0 A 10
#Tupla totalmente preenchida com contagem por extenso
#Ler um número e imprimir o extenso
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Numero?[0-10] '))
    if 0 <= num <= 10:
        break
    else:
        print('Número fora do range. Tente novamente.')
print(f'O número em extenso é {ext[num]}')