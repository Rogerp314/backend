a1 = float(input('Digite o primeiro valor de uma PA: '))
razão = float(input('Digite o valor da razão dessa PA: '))
print('Os 10 primeiros termos dessa PA são: ')
for n in range(1, 11):
    an = a1 + (n - 1)*razão
    print(an)