cu = 3*(5+4)**2
print(cu)
a = 2**100
print(a)
b = pow(3,2)
print(b)
raiz = 25**(1/2)
print(raiz)
print('CU' *10)

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma vale {}'.format(n1+n2))
print('A suntração vale {}'.format(n1-n2))
print('O produto vale {}'.format(n1*n2))
print('A divisão entre {} e {} vale {:.3f}'.format(n1, n2, n1/n2))
print('A divisão inteira entre {} e {} vale {}'.format(n1, n2, n1//n2))
print('O resto da divisão entre {} e {} vale {:.3f}'.format(n1, n2, n1%n2))
print('A potencia de {} elevado a {} é {}'.format(n1, n2, n1**n2))

print('{:=^40}'.format('Da para mostrar de outra forma!'))

nu1 = int(input('Digite um número: '))
nu2 = int(input('Digite outro número: '))
s =  nu1 + nu2
sub = nu1 - nu2
pro = nu1 * nu2
d = nu1 / nu2
di = nu1 // nu2
res = nu1%nu2
e = nu1**nu2
print('A soma é {}, a subtração é {}, o produto é {}, a divisão é {:.0f}.'.format(s, sub, pro, d), end='')
print(' A divisão inteira é {}, o resto é {} e a potencia é {}'.format(di, res, e))