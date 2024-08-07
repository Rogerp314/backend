from random import choice
from time import sleep

input('Vamos jogar jokenpo com o computador? Pressione a tecla ENTER para começar.')
lista = ['pedra', 'papel', 'tesoura']
jogador = input('Diga qual você escolheu: ').strip().lower()
pc = choice(lista)
print('{:=^40}')#Corrigir problemas mais tarde!!!, antes de assistir o vídeo.
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!!')
if pc == jogador:
    print('Vocês empataram.')
elif pc == lista[0] and jogador == lista[1]:
    print('VOCÊ GANHOU!!!')
elif pc == lista[1] and jogador == lista[2]:
    print('VOCÊ GANHOU!!!')
elif pc == lista[2] and jogador == lista[0]:
    print('VOCÊ GANHOU!!!')
elif jogador != lista[0] or jogador != lista[1] or jogador != lista[2]:
    print('\033[31m[ERROR]\033[m Escolha entre pedra, papel ou tesoura para jogar.')
else:
    print('O computador ganhou. Tente novamente.')
print('O computador escolheu {}'.format(pc.capitalize()))