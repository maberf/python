#Classificação de Triângulos
a = int(input('Reta a: '))
b = int(input('Reta b: '))
c = int(input('Reta c: '))
if a < b + c and b < a + c and c < a + b:
      if a == b == c:
          print('Equilátero')
      elif a != b != c != a:
          print('Escaleno')
      else:
          print('Isósceles')
else:
    print('Triângulo Inviável!')