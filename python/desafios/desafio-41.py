mensal = float(input('Digite sua nota mensal: '))
bi = float(input('Digite sua nota bimentral: '))
média = (mensal + bi) / 2
if média < 5:
    print('REPROVADO')
elif 5 <= média <= 6.9:
    print('RECUPERAÇÂO')
else:
    print('APROVADO')