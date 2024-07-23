from random import choice

nome = input('Digite seu nome completo: ').strip().capitalize()
div = nome.split()
print('Seu primeiro nome e {} e seu ultimo e {}, e por fim um nome seu aleatorio: {}.'.format(div[0], div[len(div)-1], choice(div)))