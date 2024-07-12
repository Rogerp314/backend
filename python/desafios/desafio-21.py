from random import shuffle

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('DIgite o nome do quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
#pre = random.choice(nomes)
#nomes.remove(pre)
#seg = random.choice(nomes)
#nomes.remove(seg)
#ter = random.choice(nomes)
#nomes.remove(ter)
#ul = random.choice(nomes)
#print('O primeiro a apresentar é {}, o segundo é {}, o terceiro é {} e por último será {}.'.format(pre, seg, ter, ul))
#Obs: Eu posso fazer desta maneira mas prefeiro só embaralhar os nomes.
shuffle(nomes)
print('A ordem dos alunos agora em uma tabela\n {}.'.format(nomes))