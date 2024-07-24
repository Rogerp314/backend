ano = int(input('Em que ano estamos? '))
bi = ano % 4
if bi == 0:
    print('Este ano e bisesto? SIM!!!')
else:
    print('Este ano e bissesto? NAO!!!')