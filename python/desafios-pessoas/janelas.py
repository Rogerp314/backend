from tkinter import *

def fun():
    nome = entrada.get().lower().strip()
    if 'silva' in nome:
        res = 'Seu nome tem Silva.'
    else:
        res = 'Seu nome não possui Silva.'


    texto_teste['text'] = res
janela = Tk()
janela.title('Janela de teste')
janela.geometry('500x500')

pergunta = Label(janela, text = 'Digite seu nome completo:')
pergunta.pack()

# Entrada de texto
entrada = Entry(janela)
entrada.pack()

botao = Button(janela, text = 'Clique aqui para começar', command = fun)
botao.pack()

texto_teste = Label(janela, text = '')
texto_teste.pack()

janela.mainloop()