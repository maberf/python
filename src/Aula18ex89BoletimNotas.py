#BOLETIM DE NOTAS
#Ler 2 notas de cada aluno e imprimir boletim com nome e média
aluno = list()
notas = list()
while True:
    #lê informações de cada aluno
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media) #calcula e insere a média
    notas.append(aluno[:]) #copia dados de alunos para lista notas
    aluno.clear() #limpa dados de aluno para a próxima leitura
    cont = (input('Continuar? [s/n] ')).strip().lower()
    if cont == 'n':
        break
#formatação do print com espaços e alinhamentos esquerda e direita
print('-'*30)
print(f'{"NOME":<20}{"MÉDIA":>10}')
for i in range(len(notas)):
    print(f'{notas[i][0]:<20}{notas[i][3]:>10.1f}')
print('-'*30)
#nota 1 e nota 2 não impressas, mas estão dentro da lista notas