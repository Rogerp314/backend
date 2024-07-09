import math

adja = float(input('Qual o valor em cm do Cateto Adjacente do triângulo? '))
opos = float(input('Qual o valor em cm do Cateto Oposto do triângulo? '))
hip = math.hypot(adja, opos)
print('O tamanho da hipotenusa é de {}cm.'.format(hip))