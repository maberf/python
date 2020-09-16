# PROGRAMA PRINCIPAL DE SISTEMA
#
from libr.interface import cabecalho, menu, leiaInt
from libr.arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrar
from time import sleep

arq = 'arqsistema.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Cadastrados', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema')
        break
    else:
        print('\033[31mERRO: Escolha opção novamente!\033[m')
    sleep(2)
