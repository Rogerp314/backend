valor = input('Digite algo: ')
print('O tipo primitivo de {} é {}'.format(valor, type(valor)))
print('Somente tem espaços? {}'.format(valor.isspace()))
print('É um número? ', valor.isnumeric())
print('É alfabético? {}'.format(valor.isalpha()))
print('É alfanumérico? {}'.format(valor.isalnum()))
print('Está em maiúsculo? {}'.format(valor.isupper()))
print('Está em minúscula? ', valor.islower())
print('Está capitalizada? ', valor.istitle())