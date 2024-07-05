print('Contação do dolar está a 5 reais')
reais = float(input('Quantos reais você possui? R$'))
dolar = reais / 5
euro = reais / 5.5
print('Você pode comprar {:.2f} dólares e {:.2f} euros.'.format(dolar, euro))