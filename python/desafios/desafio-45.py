preço = float(input('Digite o preço do produto:R$'))
forma_pagamento = int(input(' Dinheiro/Pix(1) 10 porcento de desconto \n Cartão de crédito a vísta(2) 5 porcento de desconto \n Cartão de crédito em 2x (3) \n Cartão de crédito em 3x ou mais. Sujeito a juros de 20 porcento (4) \n Qual será a forma de pagamento?: '))

vista = preço - (preço * 10/100)
cartão_parcelado2 = preço - (preço * 5/100)
cartão_pracelado3oumais = preço + (preço * 20/100)
if forma_pagamento == 1:
    print('O Preço a ser pago no protudo é de R${:.2f}'.format(vista))
elif forma_pagamento == 2:
    print('O preço a ser pago pelo produto é de R${:.2f}'.format(cartão_parcelado2))
elif forma_pagamento == 3:
    print('O preço a ser pago pelo produto é de R${:.2f}'.format(preço))
elif forma_pagamento == 4:
    print('O preço a ser pago pelo produto é de R${:.2f}'.format(cartão_pracelado3oumais))
else:
    print('[ERROR] A opção escolhida não existe. Tente novamente.')