import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 175)
circle(screen, (255, 0, 0), (120, 150), 50)
circle(screen, (0, 0, 0), (120, 150), 20)
circle(screen, (255, 0, 0), (280, 150), 40)
circle(screen, (0, 0, 0), (280, 150), 20)

rect(screen, (0, 0, 0), (100, 250, 200, 50))

polygon(screen, (0, 0, 0), [(180,100), (160,120),
                               (60,80), (80,60)])
polygon(screen, (0, 0, 0), [(220,120), (240,140),
                               (320,100), (300,80)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
