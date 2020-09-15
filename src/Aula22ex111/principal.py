# PROGRAMA PRINCIPAL - Exs. 107 a 112
#
#importação dos pacotes
from utilidades import moeda, dado

n = dado.leiaDinheiro('Preço R$? ')
a = dado.leiaInt('Aumento %? ')
d = dado.leiaInt('Desconto %? ')
moeda.resumo(n, a, d)






