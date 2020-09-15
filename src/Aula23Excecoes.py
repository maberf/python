try:
    n = int(input('Numerador: '))
    d = int(input('Denominador: '))
    r = n / d
except (ValueError, TypeError):
    print(f'Erro de dado digitado. ')
except KeyboardInterrupt:
    print(f'Usuário não informou o dado.')
except ZeroDivisionError:
    print(f'Divisão por zero.')
except Exception as erro:
    print(f'Erro encontrado foi {erro.__cause__}')
else:
    print(f'Resultado = {r:.1f}')
finally:
    print(f'Processado. Fim!')