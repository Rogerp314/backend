import math

adja = float(input('Qual o valor em cm do Cateto Adjacente do triângulo? '))
opos = float(input('Qual o valor em cm do Cateto Oposto do triângulo? '))
hip = math.hypot(adja, opos)
print('O tamanho da hipotenusa é de {}cm.'.format(hip))


#Outra maneira de se fazer o desafio é com o próprio conceito matemático.

ad = float(input('Qual o comprimento do cateto adjacente? '))
op = float(input('Qual o comprimento do cateto oposto? '))
h = ((ad**2) + (op**2))**0.5
print('A hipotenusa vale {}.'.format(h))