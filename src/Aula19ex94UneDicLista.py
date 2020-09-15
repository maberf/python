#CADASTRO DE PESSOAS em dicionário - AULA 19 EXERCÍCIO 94
#dados das pessos: nome, sexo e idade
#todos os dicionários numa lista
#Informar quantos cadastrados, média de idade, lista de mulheres e nomes de pessoas de idade acima da média
#
pessoa = dict()
grupo = list()
somaidades = media = 0
while True:
    pessoa.clear() #limnpeza do dicionário senão dá erro nos laços
    pessoa["nome"] = str(input('Nome: ')).strip()
    pessoa["sexo"] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoa["idade"] = int(input('Idade: '))
    grupo.append(pessoa.copy()) #cópia do dicionário para lista
    cont = str(input('Continuar? [S/N] ')).strip().lower()
    somaidades += pessoa["idade"]
    if cont == 'n':
        break
media = somaidades/len(grupo)
print('-'*50)
print(f'A) Pessoas cadastradas: {len(grupo)}')
print(f'B) Média de idade: {media:.2f} anos')
print(f'C) Mulheres cadastradas: ', end='')
for i in range(len(grupo)):
    if grupo[i]["sexo"] == 'F':
        print(f'{grupo[i]["nome"]} ', end='')
print()
print(f'D) Acima da média: ', end='')
for i in range(len(grupo)):
    if grupo[i]["idade"] > media:
        print(f'{grupo[i]["nome"]} {grupo[i]["idade"]} anos   ', end='')
print()
print('-'*50)
