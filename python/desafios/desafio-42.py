from datetime import date
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 0 or idade > 100:
    print('[ERROR] Ano de nascimento inválido.')
elif idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 20:
    print('SENIOR')

else:
    print('MASTER')