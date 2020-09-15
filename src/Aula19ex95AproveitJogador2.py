#APROVEITAMENTO DE JOGADORES
#Ler o nome e partidas e quantidade de gols do jogador em cada partida
#Guardar tudo em dicionário, inclusive total de gols
#Exemplo de lista dentro de dicionário e este dentro de outra lista
#
jogador = dict()
gols = list()
tabela = list()
while True:
    print('-' * 60)
    jogador.clear() #limpeza do dicionário jogador
    gols.clear() #limpeza da lista gols
    jogador["nome"] = str(input('Nome: ')).strip()
    jogador["part"] = int(input('Partidas: '))
    if jogador["part"] != 0:
        for i in range(jogador["part"]):
            gols.append(int(input(f'Gols na partida {i}: ')))
    else:
        gols[0] = 0
    jogador["gols"] = gols.copy() #coloca os gols no dicionário jogador
    jogador["totgols"] = sum(gols) #soma o total da lista gols e põe no dicionário
    tabela.append(jogador.copy()) #coloca os dados dos jogadores na tabela
    cont = str(input('Continuar? [S/N] ')).strip().lower()
    if cont == 'n':
        break
print('-' * 60)
#print da tabela, notar linhas 29, 32, 34, 41, 42 e 43
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i, v in enumerate(tabela): #varre a lista
    print(f'{i:>3}  ', end='')
    for d in v.values(): #varre o dicionário de cada jogador
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    busca = int(input('Dados de qual jogador? [99 para parar] '))
    if busca == 99:
        break
    if busca <= len(tabela):
        print(f' **** Dados de {tabela[busca]["nome"]} ****')
        for i, g in enumerate(tabela[busca]["gols"]):
            print(f'   No jogo {i} fez {g} gol(s).')
    else:
        print(f'Registro inexistente! Faça nova busca.')
print('-' * 60)