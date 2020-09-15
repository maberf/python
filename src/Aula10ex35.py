#condição de existência de um triângulo
a = int(input('Reta a: '))
b = int(input('Reta b: '))
c = int(input('Reta c: '))
if abs(b - c) < a < (b + c) and abs(a - c) < b < (c + c) and abs(a - b) < c < (a + b):
            print('Triângulo Viável!')
else:
    print('Triângulo Inviável!')