#JOGO DE DADOS
#4 jogadores jogam dados. Imprimir em ordem.
#Usado discionário no jogo e duas listas.
#Alinhamento sorted funciona tanto com lambda quanto com itemgetter
#
from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
jogos = ranking = list()
for i in range(0, 4):
    jogo["jogador"] = i
    jogo["dado"] = randint(1, 6)
    jogos.append(jogo.copy())
print('-'*5, ' JOGOS  ', '-'*5)
for i in range(0, 4):
    print(f'Jogador {jogos[i]["jogador"]} tirou dado {jogos[i]["dado"]}.')
    sleep(1)
print('-'*5, ' RANKING ', '-'*5)
# ranking = sorted(jogos, key=lambda k: k['dado'], reverse=True) #em ordem decrescente
ranking = sorted(jogos, key=itemgetter('dado'), reverse=True)  #em ordem decrescente
#ranking = sorted(jogos.items(), key=intemgetter('dado'))#se jogos fosse dicionário
for i, v in enumerate(ranking):
    print(f'{i+1} lugar Jogador {v["jogador"]} com {v["dado"]}.')
    sleep(1)
print('-'*20)