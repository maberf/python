# Alistamento Militar
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento? '))
idade = atual - nasc
if idade < 18:
    print('Não alistável. Sua idade é {} anos, faltam {} anos.'.format(idade, 18-idade))
elif idade == 18:
    print('Alistar imediatamente!')
else: print('Sua idade é {} anos, deveria ter se alistado em {}.'.format(idade, nasc+18))