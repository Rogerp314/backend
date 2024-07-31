lado1 = float(input('Digite o comprimento de uma reta: '))
lado2 = float(input('Digite outro comprimento de uma reta: '))
lado3 = float(input('Digite outro valor de comprimento de uma reta: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('As retas digitadas podem \033[4;32msim\033[m formar um triangulo!')
else:
    print('As retas \033[4;31mnão\033[m podem formar um triangulo.')