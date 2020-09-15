#APROVEITAMENTO DE JOGADOR
#Ler o nome e partidas
#Ler quantidade de gols do jogador em cada partida
#Guardar tudo em dicionário, inclusive total de gols
#Exemolo de lista dentro de dicionário
jogador = dict()
gols = list()
jogador["nome"] = str(input('Nome: ')).strip()
jogador["part"] = int(input('Partidas: '))
if jogador["part"] != 0:
    for i in range(jogador["part"]):
        gols.append(int(input(f'Gols na partida {i}: ')))
else:
    gols[0] = 0
jogador["gols"] = gols.copy()
jogador["totgols"] = sum(gols) #soma o total da lista gols
print('-'*55)
print(jogador)
print('-'*55)
print(f'O jogador {jogador["nome"]} jogou {jogador["part"]} partida(s) '
      f'e fez ao todo {jogador["totgols"]} gol(s).')
# for i, v in enumerate(gols): #referencia na lista diretamente
#    print(f'Na partida {i}, fez {v} gol(s).')
for i, v in enumerate(jogador['gols']): #referencia na lista dentro do dicionário
    print(f'Na partida {i}, fez {v} gol(s).')
print('-'*55)