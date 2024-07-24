sal = float(input('Digite seu salario:R$'))
if sal>1250:
    au = sal + (sal*10/100)
    print('Seu salario teve um aumento de 10%, e passou a valer {:.2f}'.format(au))
else:
    au = sal + (sal*15/100)
    print('Seu salario teve um aumento de 15% e passou a valer {:.2f}'.format(au))