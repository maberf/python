valores = list() #cria lista vazia
for i in range(0, 5): #carregamento da lista
    valores.append(int(input(f'Valor{i}? ')))

for i, v in enumerate(valores): #saída
    print(f'Na posição {i} o valor é {v}.')
'''    
num = [2, 5, 9, 1]
num.append(7)
num.insert(2, 2)
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não encontrado o número 5!')
print(num)
'''
'''num = []
num.append(2)
num.append(5)
num.append(9)
num.append(1)
for i, v in enumerate(num):
    print(f'Na posição {i} o valor é {v}.')
'''
