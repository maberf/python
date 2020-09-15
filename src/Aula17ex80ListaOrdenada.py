#5 VALORES ORDENADOS NA LISTA - SEM USAR SORT
valores = [] #cria lista vazia
maior = menor = 0
for i in range(0, 5):
    n = int(input(f'Valor? '))
    if i == 0 or n > valores[-1]: #insere valores maiores
        valores.append(n)
    else:
        j = 0
        while j < len(valores): #insere valores menores, testa o vetor
            if n <= valores[j]:
                valores.insert(j, n)
                break
            j += 1
print('-'*30)
print(f'Valores: {valores}')
print('-'*30)