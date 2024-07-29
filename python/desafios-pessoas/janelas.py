import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_teste['text'] = texto

janela = Tk()
janela.title('Janela de teste')
janela.geometry('500x500')

botao = Button(janela, text='Clique aqui para começar!', command=pegar_cotacoes)
botao.pack()

texto_teste = Label(janela, text='')
texto_teste.pack()


janela.mainloop()