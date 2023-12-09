import pygame

white = (255,255,255)

pygame.init
pygame.display.init
background = pygame.display.set_mode((1280,720))




while True:
    pygame.draw.circle(background, white,(500,500) ,20)