h = float(input('Qual a altura da parede em metros? '))
w = float(input('Qual a largura da parede em metros? '))
print('Obs: A cada 1 litro de tinta usado pinta 2m².')
a = h*w
tinta = a/2
print('Para pintar uma parede de {:.2f}m² ultiliza-se {} litros de tinta.'.format(a, tinta))