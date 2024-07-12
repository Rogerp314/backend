from math import radians, sin, cos, tan

an = float(input('Digite o valor do ângulo em graus: '))
rad = radians(an)
print('O seno de {} vale aproximadamente {:.2f}, o cosseno vale aproximadamente {:.2f} e a tangente vale aproximadamente {:.2f}.'.format(an, sin(rad), cos(rad), tan(rad)))





#Obs: O Python só pode calcular seno, cosseno e tangente na unidade de radianos, por isto deve-se converter com a chamada do módulo 'math' .radians()
#Eu fiz o exercício com menos variáveis possíveis.