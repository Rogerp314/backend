def verificação(nome):
    if nome == 'Pedro':
        return 'Olá Pedro, prazer em ver você novamente!'
    else:
        return 'Você não é o dono desse computador, mas prazer em te conhecer {}.'.format(nome)

pergunta = input('Digite aqui seu nome: ').strip().capitalize()
print(verificação(nome = pergunta))