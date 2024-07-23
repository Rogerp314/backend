from random import choice

no1 = input('Digite um nome: ').strip().capitalize()
no2 = input('Digite um outro nome: ').strip().capitalize()
no3 = input('Digite um outro nome: ').strip().capitalize()
nomes = [no1, no2, no3]
print('Entre os nomes digitados eu escolho: {}'.format(choice(nomes)))