import pygame

pygame.init()
pygame.mixer.music.load('teste01.mpeg')
pygame.mixer.music.play()
input()
pygame.event.wait()