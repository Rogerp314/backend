num = int(input('Digite um número inteiro: '))
if num == 2:
    print('O número 2 é primo.')
elif num%2 == 0 or num%3 == 0:
    print('O número {} não é primo'.format(num))
else:
    print('O número {} é primo'.format(num))