lado1 = float(input('Digite um número: '))
lado2 = float(input('Digite mais um número: '))
lado3 = float(input('Digite somente mais um número: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Esse número podem formar um triângulo de lados {}, {} e {}.'.format(lado1, lado2, lado3))
    if lado1 == lado2 == lado3:
        print('Por tanto esse triângulo é equilátero.')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('Por tanto esse triângulo é escaleno.')
    else:
        print('Por tanto esse triângulo é isósceles.')#cucucucucucucucu
else:
    print('Não é possível fazer um triângulo com os números dados. Desculpe')