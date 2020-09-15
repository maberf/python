'''filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
print(filme['titulo']) #acesso a elemento via chave
print(filme["titulo"]) #acesso via chave com declaração de referência entre aspas
print('-'*30)
for k, v in filme.items():
    print(f'O {k} é {v}.') #uso de laço no dicionário {k-chave} e {v-valor}
print('-'*30)
#No print formatado, declaração de referência TEM QUE SER COM ASPAS!
print(f'O filme {filme["titulo"]} foi feito em {filme["ano"]}.')
print('-'*30)
del filme['diretor'] #apaga diretor do vetor.
filme['ano'] = '1978' #alteração do ano
filme['genero'] = 'ação'#adição de elemento, NÃO USA APPEND
for k, v in filme.items():
    print(f'O {k} é {v}.')
print('-'*30)'''
#
#print(filme.values())
#print(filme.keys())
#print(filme.items())
#
#Dicionário dentro de lista
'''Brasil = [] #lista
estado1 = {'UF':'São Paulo', 'Sigla':'SP'} #dicionário
estado2 = {'UF':'Rio Grande do Sul', 'Sigla':'RS'} #dicionário
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(Brasil[1]['UF'])'''
#
#uso do copy()
estado = dict()
Brasil = list()
for i in range(0, 2):
    estado['UF'] = str(input('Nome do Estado: ')).strip()
    estado['Sigla'] = str(input('Sigla: ')).strip()
    Brasil.append(estado.copy())
print(Brasil)

