from random import randint
from time import sleep

#lista = [0,1,2,3,4,5]
pc = randint(0,5)
print('O computador vai escolher um numero entre 0 a 5, voce deve adivinhar qual foi o numero escolhido!')
usuario = int(input('Escreva o numero que voce acha que o computador escolheu: '))
print('PROCESSANDO...')
sleep(1)
print('O numero que o computador escolheu foi o {}!'.format(pc))
if usuario == pc:
    print('Voce acertou! Parabens')
else:
    print('Voce errou! Tente novamente.')
print('---FIM DO PROGRAMA---')

#Esse foi facil pra caralho, tive a ideia de quando errar colocar um print falando para precionar tal tecla para tentar dnv mas isso e estrutura de repetiçao. Ainda n sei no Python.
#Existe o parametro randint() que sorteia aleatóriamente um número entre o intervalo que foi colocado no parenteses.