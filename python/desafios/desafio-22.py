import pygame

pygame.init()
pygame.mixer.music.load('musica.mpeg')
pygame.mixer.music.play()
pygame.event.wait()





#Existem inúmeras bibliotecas no Python para tocar um MP3. Para isto vou ultilizar o módulo 'pygame' que cria jogos, e jogos tem músicas.
#Para instalar o módulo 'pygame' neste computador devemos abrir o terminal, necessariamente o nesta pasta para instalara somente nesta pasta.
#Para iniciar o uso da biblioteca pygame, devemos escrever 'pygame.init()' agora para carregar a música temos o comando 'pygame.mixer.music.load(nome do arquivo que queira carregar)'
#Para dar play na música tem que escrever o comando 'pygame.mixer.music.play()' e para o programa esperar o evento acabar temos o comando 'pygame.event.w