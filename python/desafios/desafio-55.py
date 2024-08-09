from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - ano
    if idade < 21:
        menor += 1
    elif idade > 21:
        maior += 1
print('De 7 pessoas, {} são maiores de 21 anos e {} são menores de 21 anos.'.format(maior, menor))