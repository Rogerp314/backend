n1 = int(input('Digite um número para saber seu tipo primitivo: '))
print('O valor digitado tem o tipo {}'.format(type(n1)))
n2 = int(input('Agora outro valor para saber a classe do tipo: '))
print('O valor digitado tem o tipo', type(n2))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Testando tipos:

n = bool(input('Digite um valor: '))
print(n)