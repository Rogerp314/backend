nome = input('Qual o seu nome? ')
#Ultilizando dicionário
cores = {'vermelho': '\033[4;31m',
         'limparcor':'\033[m'}
print('Olá {}{}{}, prazer em te conhecer!!!'.format(cores['vermelho'], nome, cores['limparcor']))