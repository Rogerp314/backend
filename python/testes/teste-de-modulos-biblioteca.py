import math
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raiz quadrada de {} vale {}'.format(n, math.ceil(raiz)))
print('Esse foi um exemplo importando tudo da biblioteca, agora vamos importar somente a função sqrt')
from math import sqrt
num = int(input('Escreva outro número: '))
root = sqrt(num)
print('A raiz de {} é igual a {}, ultilizando o método de importação específico.'.format(num, root))
print('Agora irei importar uma biblioteca diferente, sendo ela a ramdom para testes. Essa biblioteca me da números aleatórios.')
import random
num1 = random.random()
print('O número que o computador escolheu foi {}'.format(num1))
al = random.randint(1,10)
print('Agora um número inteiro aleatório: {}'.format(al))
