from tkinter import *

#criando a função
def aumento():
    Label(tela , text='Digite seu salário atual: ', font='Georgia').pack(pady=20)
    caixa = Entry(tela, background='green', fg='white')
    caixa.pack(pady=5)
    Label(tela, text = 'Precione a tecla enter para confirmar', font='Georgia').pack(pady=5)
    #Sub-fanção que vai fazer as contas e mostrar
    def conta(event):
          valor = float(caixa.get())
          if valor >= 1500:
               au = valor + (valor * 10/100)
               Label(tela,text='Seu salário pasara a valer R${:.2f}'.format(au), font='Georgia').pack()
               Label(tela, text='-='*20).pack()
               Label(tela, text='FIM DO PRORAMA').pack()
          else:
               au = valor + (valor * 20/100)
               Label(tela, text = 'Seu salário agora aumentou para R${:.2f}'.format(au), font='georgia').pack()
               Label(tela, text='-='*20).pack()
               Label(tela, text='FIM DO PRORAMA').pack()
    #Comando .bind é para dar função a uma tecla
    caixa.bind('<Return>', conta)
   
#Criando a janela
tela = Tk()
tela.title('Janela de teste')
tela.geometry('1900x1080')
#criando um texto de exibição
label = Label(tela, text = 'Essa janela é um teste de aprendizado e logo a baixo temos um programa de teste', font='Georgia')
label.pack(pady=20)
#Criando um botão que chame a função
botao = Button(tela, text='Clique aqui para começar o programa', bg='black', fg='white', command=aumento)
botao.pack()

tela.mainloop()