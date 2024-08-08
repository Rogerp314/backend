print('O programa a seguir somará os ímpares múltiplos de 3 entre 1 à 500')
soma = 0
for i in range(0, 501, 3):
    multi = i%3
    if multi == 0:
        soma += i
print('O soma de todos os ímpares múltiplos de 3 entre 1 e 500 é de {}'.format(soma))
print('FIM')