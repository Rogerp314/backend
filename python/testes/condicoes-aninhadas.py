nome = input('Digite seu nome: ').strip().title()
if 'Pedro' in nome:
    print('Seu sobrenome é bonito!')
elif 'Silva' in nome:
    print('Seu nome é bem comum.')
elif  nome in 'Maria' or 'Ana' in nome: #A ordem de antes e depois do in não importa, e pode colocar os nomes e strings em uma lista só
    print('Seu nome é bem popular.')
elif 'Gaby' in nome:
    print('Seu nome é o mais lindo que já ouvi!!!')
else:
    print('Seu nome é interresante.')
print('Tenha um bom dia {}!'.format(nome))