#IMPRIME AS VOGAIS DA PALAVRAS DA TUPLA
palavras = ('estudar', 'trabalhar', 'praticar', 'treinar')
for palavra in palavras: #palavra em palavras
    print(f'\nEm {palavra} temos: ', end='')
    for letra in palavra: #letra em palavras
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
