#ANALISE DE LISTAS COMPOSTAS
#Cadastrar pessoas e respectivo peso
#Perguntar novo cadastro. Se não (N) encerra.
#Imprimir a duas mais pesadas e as duas mais leves
#
grupo = list()
pessoa = list()
cont = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    cont = str(input('Continuar?[S/N] ')).strip().upper()
    if len(grupo) == 0:
        pmaior = pmenor = pessoa[1]
    elif pessoa[1] > pmaior:
        pmaior = pessoa[1]
    elif pessoa[1] < pmenor:
        pmenor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    if cont == 'N':
        break
grupo.sort(key=lambda x:x[1]) #chave do sort pelo peso
print('-'*30)
print(f'Cadastradas {len(grupo)} pessoas.')
print(f'Maior peso = {pmaior} Kg. Mais pesados {grupo[-2][0]} e {grupo[-1][0]}.')
print(f'Menor peso = {pmenor} Kg. Menos pesados {grupo[0][0]} e {grupo[1][0]}.')