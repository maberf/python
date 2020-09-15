#SÉRIE DE FIBONACCI
#Este código calcula também t0 e t1
# Diferente do exemplo do Guanabara!
#
n = int(input('Quantos termos de Fibonacci? '))
i = 1
fib = 0
fib1 = 0
fib2 = 0
while i <= n:
    fib = fib1 + fib2
    print(fib, ' ', end='')
    fib1 = fib2
    fib2 = fib
    if i == 1:
        fib2 = 1 #"arranca" a série
    i += 1
print('Fim')
