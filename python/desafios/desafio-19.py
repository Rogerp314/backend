import math

anglo = float(input('Digite qualquer ângulo que queira: '))
sen = math.sin(math.radians(anglo))
cos = math.cos(math.radians(anglo))
tg = math.tan(math.radians(anglo))
print('O seno de {}° vale aproximadamente {}.'.format(anglo, sen))
print('O cosseno de {}° vale aproximadamente {}.'.format(anglo, cos))
print('A tangente de {}° vale aproximadamente {}.'.format(anglo, tg))