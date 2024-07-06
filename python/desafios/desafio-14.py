sal = float(input('Digite seu salário atual: '))
print('Você receberá um aumento de 15% no salário.')
foda = sal + (sal*15/100)
print('Seu salário passou a valer R${:.2f}'.format(foda))