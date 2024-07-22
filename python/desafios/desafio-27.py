frase = input('Digite uma frase: ').strip().lower()
print('A letra A aparece {} vezes na frase;'.format(frase.count('a')))
print('A letra A apareceu primeiro na posiçao {}.'.format(frase.find('a')+1))
print('A ultima letra a aparece na posiçao {}.'.format(frase.rfind('a')+1))