import random

print('Um professor deseja sortear a ordem de apresentação de seus quatros alunos, sendo eles: Pedro, Gaby, Bruno e Marco.')
nomes = ['Pedro', 'Gaby', 'Bruno', 'Marco']
pre = random.choice(nomes)
nomes.remove(pre)
seg = random.choice(nomes)
nomes.remove(seg)
ter = random.choice(nomes)
nomes.remove(ter)
ul = random.choice(nomes)
print('O primeiro a apresentar é {}, o segundo é {}, o terceiro é {} e por último será {}.'.format(pre, seg, ter, ul))