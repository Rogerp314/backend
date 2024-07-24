vel = float(input('Qual a velocidade do seu carro em km/h? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Parado ai! Voce ultrapassou o limite da estrada de 80km/h, sera multado por R$7.00 a cada km acima do limite, assim sua multa e de R${:.2f}'.format(multa))
else:
    print('Pode seguir viagem, esta tudo certo.')