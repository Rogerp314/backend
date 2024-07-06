dias = int(input('Quantos dias o automóvel foi alugado? '))
km = float(input('Quantos quilômetros rodados? '))
total = (dias * 60) + (km * 0.15)
print('O preço total a ser pago pelo aluguel é de R${:.2f}.'.format(total))