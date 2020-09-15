#QUALIFICAÇÃO DE ELEITOR
#
# Funções Iniciais
#
def qualificacao(ano=2020):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        qualif = 'não permitido'
    elif 16 <= idade < 18 or idade > 65:
        qualif = 'opcional'
    else:
        qualif = 'obrigatório'
    return qualif


# Programa Principal
#
eleitor = int(input('Ano de nascimento do eleitor: '))
print(f' O voto do eleitor é: {qualificacao(eleitor)} ')