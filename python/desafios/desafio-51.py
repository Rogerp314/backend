soma = 0
for n in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num%2 == 0:
        soma += num
print('O soma dos números pares digitados é igual a {}'.format(soma))