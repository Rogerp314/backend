import requests

#Pegar os dados de uma API com o módulo request, com o método .get()
cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL') #Esse link mostra a cotações das moedas nos últimos 30s.
#se der um print agora aparecera o número 200 que indica que foi pego os dados, mas não mostrara as cotações pois está em formato json, por isso devemos mudar o formato compatível com o Python.
#Abrindo o arquivo json para um dicionário em Python
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
#print(cotacoes)
print('Nesse momento a cotação do dólar para o real está R${} para cada $1'.format(dolar))