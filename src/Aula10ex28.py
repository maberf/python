from random import randint
num = int(input('Número? '))
nal = randint(0, 5)  # randômico inteiro entre 0 e 5
print('Seu número: {}'.format(num))
print('Número sorteado: {}'.format(nal))
# if num == nal:
#    print('ACERTOU!')
# else:
#    print('ERROU!')
print('ACERTOU!' if num == nal else 'ERROU!')
