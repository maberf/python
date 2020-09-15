nome = input ('Qual o seu nome? ')
print('Olá,{:>15}!'.format(nome)) #espaçamento 15 caracteres alinhado à direita
print('Olá,{:<15}!'.format(nome)) #alinhado à esquerda
print('Olá,{:^15}!'.format(nome)) #centralizado
print('Olá,{:=^15}!'.format(nome), end=' ') #preenchido com = e emenda com print seguinte
print(f'Olá,{nome:=^15}!') #centralizado preenchido com instrução diferente