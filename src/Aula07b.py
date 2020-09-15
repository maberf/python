n1 = int(input('Valor 1:'))
n2 = int(input('Valor 2:'))
som = n1 + n2
mul = n1 * n2
div = n1 / n2
dit = n1 // n2
print('Soma é {}, Produto é {}, \nDivisão é {:.3f}, Divisão Inteira é {}'.format(som, mul, div, dit))
# \n quebra a linha. {:..3f} fixa 3 casas decimais na divisão