#ANALISE DE STRINGS NA EXPRESSÃO
#Analisar os parênteses da expressão
#
exp = str(input('Escreva expressão com parênteses: ')).strip().lower()
pilha = 0 #uso de uma variável acumuladora
for carac in exp:
    if carac == '(':
        pilha += 1
    elif carac == ')':
        pilha -= 1
if pilha == 0:
    print(f'Expressão OK.')
else:
    print(f'Expressão inválida.')