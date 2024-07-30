from datetime import date

ano = int(input('Coloque o ano que queira analizar? Coloque 0 para saber do ano atual. '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisesto? SIM!!!'.format(ano))
else:
    print('O ano {} é bisesto? NAO!!!'.format(ano))