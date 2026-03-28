import pygame
from pygame import Vector2
from fourmi import Fourmie
from random import randint
from config import *
from pheromones import Pheromones

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ph_sys = Pheromones()

colony = []
for i in range(50):
    fourmie = Fourmie(Vector2(randint(0, SCREEN_WIDTH), randint(0, 720)), 5)
    colony.append(fourmie)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((250, 249, 246))

    if pygame.mouse.get_pressed()[0]:
        m_pos = pygame.mouse.get_pos()
        ph_sys.deposer(m_pos[0], m_pos[1])

    for i in colony:
        i.move_random()
        pygame.draw.circle(screen, "black", i.position, 5)
        
    ph_sys.evaporer()
    ph_sys.afficher(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()