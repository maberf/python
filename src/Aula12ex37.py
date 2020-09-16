# Conversor de Números - Binário, Octal, Hexa
num = int(input('Número? '))
print('[1] binário   [2] octal    [3] hexa')
base = input('Qual base? ')
if base == '1':
    res = bin(num)
elif base == '2':
    res = oct(num)
elif base == '3':
    res = hex(num)
else:
    res = 'Opção Inválida!'
print('Resultado = {}'. format(res[2:]))  # fatiamento exclui 0x inicial (base)
