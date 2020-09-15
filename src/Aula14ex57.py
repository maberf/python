#VALIDAÇÃO DE DADOS
sexo =''
while sexo != 'M' and sexo != 'F': #uso de flags
    sexo = str(input('Sexo? ')).strip().upper()
print('O sexo é {}'.format(sexo))