#O desafio é que quando colocado um número entre 1 a 26 mostre o alfabeto do A até a letra de número escolhido
alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = int(input('Digite um número entre 1 e 26: '))
cores = {'cor' : '\033[31m', 'limpa' : '\033[m'}
if num == 0:
    print('{} [ERROR] \nNão Existe letra no alfabeto que esteja na posição 0.{}'.format(cores['cor'], cores['limpa']))
elif num >= 27:
    print('{} [ERROR] {} O alfabeto só tem 26 letras.'.format(cores['cor'], cores['limpa']))
else:
    print(*alfa[:num])