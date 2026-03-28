import numpy as np
from dataclasses import dataclass
from config import *
import pygame

row = SCREEN_HEIGHT // CELL_SIZE
col = SCREEN_WIDTH // CELL_SIZE

@dataclass
class Pheromones():
    def __post_init__(self):
        self.grid = np.zeros([row, col])
    def deposer(self, x, y):
        hintx = x // CELL_SIZE
        hinty = y // CELL_SIZE
        self.grid[hinty][hintx] += 0.05
        cell_deposed = self.grid[hinty][hintx]
        np.clip(cell_deposed, 0, 1)
    def evaporer(self):
        self.grid *= (1 - TAUX_EVAPORATION)
    def afficher(self, screen):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell > 0.01:
                    pygame.draw.rect(screen, "red", (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE))