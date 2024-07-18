cidade = input('Digite o nome da sua cidade: ').strip().capitalize()
divi = cidade.split()
print('Sua cidade começa com Santo? {}'.format('Santo' in divi[0]))