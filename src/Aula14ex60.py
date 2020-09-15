#FATORIAL
n = int(input('Numero? '))
fat = 1
i = n
while i > 0:
    print('{}'.format(i), end='')
    print(' * ' if i > 1 else ' = ', end='')
    fat *= i
    i -= 1
print('{}! = {}'.format(n, fat) if n >=1 else'0! = 1')