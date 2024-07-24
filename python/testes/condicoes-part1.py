nome = input('Digite seu nome: ').strip().capitalize()
if nome == 'Pedro':
    print('Voce e o dono deste computador!')
    print('Seja Bem-vindo! Senhor {}.'.format(nome))
else:
    print('Voce n e o dono deste computador!\nTome vergonha na cara de invadir a privacidade dos outros.')
print('--FIM--')
print('Começando outro problema, com condiçao de mais de duas opçoes:')
mensal = float(input('Digite sua nota mensal: '))
bi = float(input('Digite sua nota bimestral: '))
media = (mensal + bi) / 2
if media < 5:
    print('Sua media e {}, e esta vermelha, esta de recuperaçao!'.format(media))
elif media == 5:
    print('Sua media e {}, e passou raspando!!!'.format(media))
else:
    print('Parabens voce passou de ano direto com uma media de {}!'.format(media))