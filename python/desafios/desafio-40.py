from datetime import date
sexo = input('Seu sexo é masculino ou feminino? ').strip().title()
if sexo == 'Feminino':
    print('Você não precisa se alistar no exército brasileiro.')
else:
    ano_nascimento = int(input('Qual seu ano de nascimento? '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    ano_faltantes = 18 - idade
    ano_alistamento = ano_atual + ano_faltantes
    if idade < 18:
        print('Você tem {} anos em {}, ainda falta {} ano(s) para seu alistamento que será em {}.'.format(idade, ano_atual, ano_faltantes, ano_alistamento))
    elif idade == 18:
        print('Você tem 18 anos em {}. Esse é seu ano de alistamento. \033[31mCORRA!!!\033[m'.format(ano_atual))
    else:
        ano_faltantes = ano_faltantes * -1
        print('Você tem {} anos e está atrasado para o alistamento em {} ano(s) em que ocorreu em {}. CORRA!'.format(idade, ano_faltantes, ano_alistamento))