idade = int(input('Diga sua idade: '))
if idade > 18:
    tempo = (18 - idade) * -1
    print('Você está atrasado em {} anos para o alistamento no tiro de guerra, {}CORRA!{}'.format(tempo, '\033[31m', '\033[m'))
elif idade < 18:
    tempo = 18 - idade
    print('Você ainda está jovem demais para o alistamento, falta {} anos.'.format(tempo))
else:
    print('Você tem 18 anos vá se alistar.')