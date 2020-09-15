#NÚMERO PRIMO
num = int(input('Número? '))
t = 0
for i in range(1, num + 1):
    if num % i == 0:
        t += 1
        print('\033[31m{} '.format(i), end='')
    else:
        print('\033[33m{} '.format(i), end='')
print('\n\033[mDivisível {} vezes.'.format(t))
print('Primo' if t <= 2 else 'Não Primo')

