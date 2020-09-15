'''pessoa = list()
pessoa.append('Uélinton')
pessoa.append(25)
turma = list()
turma.append(pessoa[:]) #cópia
pessoa[0] = 'Diónatan'
pessoa[1] = 30
turma.append(pessoa[:]) #cópia
print(turma)'''
#
#turma = [['Joao', 19], ['Ana', 33], ['Zé', 40], ['Maria', 25]]
#
turma = list()
pessoa = list()
#bloco de leitura de dados
for i in range(0, 3):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Idade: ')))
    turma.append(pessoa[:])  #cópia para turma
    pessoa.clear()           #limpa lista pessoa
#bloco de impressão dos dados
for pessoa in turma:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')