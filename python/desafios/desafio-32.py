viagem = float(input('Qual a distancia em km da sua viagem? '))
if viagem <= 200:
    preço = viagem * 0.5
    print('Sua viagem ira te custar R${:.2f}.'.format(preço))
else:
    preço = viagem * 0.45
    print('Sua viagem vai te custar R${:.2f}.'.format(preço))