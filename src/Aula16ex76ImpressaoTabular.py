#NOMES DE PRODUTOS E PREÇOS EM TUPLA ÚNICA
#Imprimir de forma tabular
bebidas = ('Cerveja Long Neck', 4.75,
           'Cerveja 600 ml', 8,
           'Vodka', 10,
           'Caipirinha', 12.50)
print('-'*33)
#Alinhamento com uso de f string
print(f'{"BEBIDAS":^33}')
print('-'*33)
for i in range(0, len(bebidas)):
    if i % 2 == 0:
        #impressão com alinhamento
        #por default caractere alinha na esquerda (<)
        #mesmo assim inserido no comando .<25
        #25 espaços para a mensagem e preenchimento com pontos
        print(f'{bebidas[i]:.<25}', end='')
    else:
        #impressão com alinhamento
        #por default número alinha na direita (>)
        #mesmo assim inserido no comando >5.2f
        #5 espaços para o número com duas decimais restante espaço vazio
        print(f'R$ {bebidas[i]:>5.2f}')
print('-'*33)



