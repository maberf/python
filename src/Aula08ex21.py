import pygame
pygame.mixer.init()
pygame.mixer.music.load('Aula08ex21.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(5)
#pygame.event.wait()
x = input('digite algo para encerrar...')
