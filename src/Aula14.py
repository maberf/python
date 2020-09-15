print('--for----------------------')
for i in range(1, 10): #limite fixo
    print(i, ' ' ,end='')
#
print('\n--while--------------------')
i = 1
while i < 10: #limite fixo
    print(i, ' ' ,end='')
    i += 1
#
print('\n--for----------------------')
for i in range(1,4): #limite fixo
    n = int(input('Valor? '))
print('Fim')
#
print('\n--while com teste lógico---')
while n != 0: #teste lógico, para quando digitar zero
    n = int(input('Valor? '))
print('Fim')
