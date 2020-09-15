#CADASTRO
#Cadastrar idade e sexo de várias pessoas
#Não há limite de pessoas, perguntar se usuário quer cadastra mais
#Mostrar quantidade de: (1) > 18 anos, (2) homens e (3) mulheres < 20 anos
mai18 = hom = mul20 = 0
while True:
    print('-'*20,'\n{:^20}'.format('CADASTRE UMA PESSOA'))
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F] ')).strip().upper()
    if idade > 18:
        mai18 += 1
    if sexo == 'M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mul20 += 1
    cad = str(input('Continuar[S/N]? ')).strip().upper()
    if cad == 'N':
        break
print(f'Maiores de 18 anos = {mai18}')
print(f'Homens = {hom}')
print(f'Mulheres menores de 20 anos = {mul20}')