from pygame import Vector2
from dataclasses import dataclass, field
from random import randint
from config import *

@dataclass
class Fourmie():
    position: Vector2
    speed: float
    etat: str = "cherche"
    direction: Vector2 = field(default_factory=lambda: Vector2(0, 0))
    destination: Vector2 = field(default_factory=lambda: Vector2(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)))
    def move(self):
        if self.etat == "cherche":
            if Vector2.distance_to(self.position, NOURRITURE) < CELL_SIZE:
                self.etat = "rentre"
            else: 
                if Vector2.distance_to(self.position, self.destination) < 5:
                    self.destination = Vector2(randint(0, 1280), randint(0, 720))
                else:
                    norm = (self.destination - self.position).normalize()
                    self.direction = Vector2.lerp(self.direction, norm, 0.1) 
                    self.position += self.direction * self.speed

        if self.etat == "rentre":
            if Vector2.distance_to(self.position, NID) < CELL_SIZE:
                self.etat = "cherche"
            else:
                self.destination = NID
                norm = (self.destination - self.position).normalize()
                self.direction = Vector2.lerp(self.direction, norm, 0.1) 
                self.position += self.direction * self.speed
        