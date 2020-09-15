# Categoria de Atletas
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento? '))
idade = atual - nasc
if idade <= 9:
    print('{} anos - Mirim'.format(idade))
elif idade <= 14:
    print('{} anos - Infantil'.format(idade))
elif idade <= 19:
    print('{} anos - Junior'.format(idade))
elif idade <= 25:
    print('{} anos - Senior'.format(idade))
elif idade > 25:
    print('{} anos - Master'.format(idade))