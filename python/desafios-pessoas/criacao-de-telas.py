from requests import *
from tkinter import *
#O * serve para pegar todos ops códigos do módulo e não precisar mais ficar colocando o nome do módulo antes de qualquer comando.

#programa que vai ser executado na janela (Programa de exermplo)
def cu():
    teste = print('Olá, Mundo!')
    prog.config(text = teste)

#Criação da janela
janela = Tk()
janela.title('Teste de janela')
#colocando texto
texto = Label(janela, text = 'Texto de teste')
texto.grid(column=0, row=0)
#Criando um botão
botao = Button(janela, text='Clique aqui para começar!', command= cu)
botao.grid(column=0,row=1)
#Exibindo o programa
prog = Label(janela, text= '')
prog.grid(column=0, row=3)


janela.mainloop()