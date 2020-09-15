# TABUADA
#Mostra a tabuada de vários números, um de cada vez
#O programa encerra quando o número digitado é negativo
while True:
    num = int(input('Número? '))
    print('=' * 10)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('='*10)
print('Fim')