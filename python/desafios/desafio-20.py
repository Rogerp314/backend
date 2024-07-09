from random import choice

print('Um professor quer sortear um dos seus quatros alunos para apagar a lousa, sendo eles:\n Pedro, Gaby, Bruno e Marco.\n Então o professor escolhe um programa em Python para sortear:')
nomes = ['Pedro', 'Gaby', 'Bruno', 'Marco']
sorte = choice(nomes)
print('O aluno escolhido para apagar a louse é {}'.format(sorte))
