#CADASTRO DE TRABALHADOR
#Dicionário com nome, nascimento, CTPS e
#se CPTS > 0 incluir ano de contratação e salário
#Calcular idade e quantos anos vai se aposentar com 35 anos de serviço
#
from datetime import datetime
dadotrab = dict()
dadotrab["nome"] = str(input('Nome: ')).strip()
dadotrab["anonasc"] = int(input('Ano de Nascimento: '))
dadotrab["idade"] = datetime.now().year - dadotrab["anonasc"]
dadotrab["ctps"] = int(input('CTPS: '))
if dadotrab["ctps"] != 0:
    dadotrab["anocontr"] = int(input('Ano de Contratação: '))
    dadotrab["salario"] = float(input('Salário: '))
    dadotrab["aposent"] = (dadotrab["anocontr"] + 35) - dadotrab["anonasc"]
else:
    dadotrab["ctps"] > 0
    dadotrab["anocontr"] = 0
    dadotrab["salario"] = 0
    dadotrab["aposent"] = 0
print('-'*50)
print(f'{dadotrab["nome"]} com idade de {dadotrab["idade"]} anos se aposentará aos {dadotrab["aposent"]} anos.')
#print(dadotrab)