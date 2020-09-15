#CAIXA ELETRONICO
#Calcula o dispenser em cédulas de 1, 10, 20 e 50.
c01 = c10 = c20 = c50 = 0
print('-'*20,'\n{:^20}'.format('BANCO XPTO SA'))
print('-'*20)
while True:
    valor = int(input('Qual o valor desejado? '))
    saldo = valor
    if saldo >= 50:
        c50 = saldo // 50
        saldo = saldo % 50
    if saldo >= 20:
        c20 = saldo // 20
        saldo = saldo % 20
    if saldo >= 10:
        c10 = saldo // 10
        saldo = saldo % 10
    if saldo >= 1:
        c01 = saldo
    print(f'Suas notas: {c50} x R$50, {c20} x R$20, {c10} x R$10 e {c01} x R$1')
    fim = str(input('Deseja sacar outro valor? [S/N] ')).strip().upper()
    if fim != 'S':
        break
print('Obrigado por utilizar os serviços do Banco XPTO.')