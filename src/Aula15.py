n = s = 0
while True: #loop infinito
    n = int(input('Número? '))
    if n == 99:
        break
    s += n #acumulador
#Teria-se que expurgar o 99 da soma se
#não utilizássemos o break (gambiarra)
#
#print('Soma é {}'.format(s))
#
#Uso de f string ao invé do print com format
# f string somente no Python 3.5 em diante!
print(f'Soma é {s}')