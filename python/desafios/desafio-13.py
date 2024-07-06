preco = float(input('Preço do produto: R$'))
print('Adicionando um desconto de 5%.',end=' ')
des = preco - (preco*(5/100))
print('O preço final do produto é de {:.2f}'.format(des))