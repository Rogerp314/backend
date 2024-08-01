valor_casa = float(input('Qual o valor da casa:R$ '))
salario = float(input('Qual o seu salário:R$ '))
anos_parcela = int(input('Em quantos anos vai querer parcelar: '))

#Calculando o valor da prestação por mês, se exceder 30% do salário do comprador ele será impedido de comprar

prestação = valor_casa / (anos_parcela * 12)
taxa_limite = salario * 30/100
if prestação > taxa_limite:
    print('Me desculpe mas não podemos aceitar a oferta, pois o valor da prestação está comprometendo sua renda em mais de 30%.')
else:
    print('Meus parabéns! O valor da prestação será de R${:.2f} por mês.'.format(prestação))