n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('Média: {:.1f}'.format(m))
print('APROVADO' if m >= 7 else 'REPROVADO')