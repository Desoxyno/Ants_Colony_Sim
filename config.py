import pygame
from pygame import Vector2
from fourmi import Fourmie
from random import randint

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

colony = []
for i in range(50):
    fourmie = Fourmie(Vector2(randint(0, SCREEN_WIDTH), randint(0, 720)), 5)
    colony.append(fourmie)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((250, 249, 246))

    for i in colony:
        i.move_random()
        pygame.draw.circle(screen, "black", i.position, 5)
        

    pygame.display.flip()

    clock.tick(60)

pygame.quit()