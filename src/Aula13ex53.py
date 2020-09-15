#DETECTOR DE PALÍNDROMOS
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA
#
# Letras das extremidades para o centro iguais
# Polídromo é sempre ímpar
texto = str(input('Digite o texto: ')).strip().lower() #limpa espaços e minúsculas
palavras = texto.split() #lista só com as palavras, tira espaços intermediários
letras = ''.join(palavras) #junta as palavras em sequência de letras
inverso = ''
for letra in range(len(letras)-1,-1,-1): #gera o inverso da sequência de letras
    inverso += letras[letra]
if letras == inverso:
    print('É polídromo!')
else:
    print('Não é polídromo!')
