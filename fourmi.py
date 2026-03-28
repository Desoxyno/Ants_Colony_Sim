from pygame import Vector2
from dataclasses import dataclass
from random import randint

@dataclass
class Fourmie():
    position: Vector2
    speed: float
    direction: Vector2 = Vector2(0, 0)
    destination: Vector2 = Vector2(randint(0, 1280), randint(0, 720))
    wait_time: float = 0.2
    def move_random(self):
        if Vector2.distance_to(self.position, self.destination) < 5:
            self.destination = Vector2(randint(0, 1280), randint(0, 720))
        else: 
            norm = (self.destination - self.position).normalize()
            self.direction = Vector2.lerp(self.direction, norm, 0.1) 
            self.position += self.direction * self.speed