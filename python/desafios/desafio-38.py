num = int(input('Digite um número qualquer inteiro: '))

cor = {'verde': '\033[32m',
        'vermelho': '\033[31m',
        'roxo': '\033[35m',
        'limpa': '\033[m',
        'amarelo': '\033[33m'}

opção = int(input('Escolha {}1{} para binário, {}2{} para octal e {}3{} para hexadecimal: '.format(cor['verde'], cor['limpa'], cor['vermelho'], cor['limpa'], cor['roxo'], cor['limpa'])))

if opção == 1:
    binario = bin(num)[2:] #Esse método converte um número decimal em binário e ele sempre começa com '0b' para tirar isto coloca-se o [2:]
    print('O número digitado em Binário é {}{}{}'.format(cor['amarelo'], binario, cor['limpa']))
elif opção == 2:
    octal = oct(num)[2:]
    print('O número digitado em octal é {}{}{}'.format(cor['amarelo'], octal, cor['limpa']))
elif opção == 3:
    hexa = hex(num)[2:]
    print('O número digitado em hexadecimal é {}{}{}'.format(cor['amarelo'], hexa, cor['limpa']))