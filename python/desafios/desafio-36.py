lado1 = float(input('Digite o comprimento de uma reta: '))
lado2 = float(input('Digite outro comprimento de uma reta: '))
lado3 = float(input('Digite outro valor de comprimento de uma reta: '))
if lado1 < lado2 + lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    print('As retas digitadas podem sim formar um triangulo!')
else:
    print('As retas nao podem formar um triangulo.')