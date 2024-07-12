from random import choice

print('Um professor quer sortear quem será o primiero aluno que vai apresentar, sendo os alunos:')
nomes = []
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno : ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
nomes.append(al1)
nomes.append(al2)
nomes.append(al3)
nomes.append(al4)
sorteio = choice(nomes)
print('O aluno sorteado é {}.'.format(sorteio))

#Esse código não tá lá essas coisas mais funciona, da pra ser bem melhor que isso, mas é o que tem pra hoje. Eu só coloquei o comando 'append' para treino em relação ao mecanismo de funcionamento das listas.