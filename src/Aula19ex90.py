aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
else:
    aluno['status'] = 'Reprovado'
print(f'Nome é {aluno["nome"]}.')
print(f'A média é {aluno["media"]}.')
print(f'O status é {aluno["status"]}.')