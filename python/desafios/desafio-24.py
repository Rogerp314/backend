num = int(input('Digite um número de 0 à 9999: '))

#achar a unidade
uni = num % 10
print('Unidade: {}'.format(uni))

#Dezena
num = (num - uni) // 10
dez = num % 10
print('Dezena: {}'.format(dez))

#centena
num = (num - dez) // 10
cen = num % 10
print('Centena: {}'.format(cen))

#Milhar
num = (num - cen) // 10
milhar = num % 10
print('Milhar: {}'.format(milhar))