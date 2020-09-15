#CAIXA ELETRONICO
#Calcula o dispenser em cédulas de 1, 10, 20 e 50.
print('-'*20,'\n{:^20}'.format('BANCO XPTO SA'))
print('-'*20)
valor = int(input('Qual o valor desejado? '))
saldo = valor
ced = 50
totced = 0
while True:
    if saldo >= ced:
        saldo -= ced #Decrementa o saldo em múltiplos de cédula
        totced += 1
    else:
        print(f'{totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20 #Notar que a condição opera a primeira vez.
        elif ced == 20: #mesmo com atribuição igual na condição seguinte!
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saldo == 0:
            break
print('Obrigado por utilizar os serviços do Banco XPTO.')