# FICHA JOGADOR
#
# Funções Iniciais
#
def ficha(jog='Desconhecido', gols=0):
    print(f' O jogador {jog} fez {gols} gols.')


# Programa Principal
jog = str(input('Nome: '))
gol = str(input('Gols: '))
if gol.isnumeric():
    gols = int(gol)
else:
    gols = 0
if jog.strip() == '':
    ficha(gols=gol)
else:
    ficha(jog, gols)