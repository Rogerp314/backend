print('O programa irá mostrar a tabuada que você escolher')
valor = int(input('Digite um número inteiro e saberemos sua tabuáda: '))
for x in range(0, 11):
    produto = x * valor
    print('{} x {} = {}'.format(valor, x, produto))