from libr.interface import cabecalho


def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')  # lê existência de arquivo texto
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')  # cria arquivo texto se ele não existir
        arq.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')  # leitura de aquivo texto
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arq:  # rotina de formatação da tabela de saída
            dado = linha.split(';')  # registro linha dados separados lista
            dado[1] = dado[1].replace('\n', '')  # \n subst (linha47) "nada"
            print(f'{dado[0]:<33}{dado[1]:>3} anos')
# print(arq.read()) #leitura do conteudo do arquivo
    finally:
        arq.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        arq = open(arq, 'at')  # append
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            arq.write(f'{nome}; {idade}\n')  # escrita no arquivo
        except:
            print('Erro na escrita do dado!')
        else:
            print(f'Registro de {nome} adicionado.')
            arq.close()
