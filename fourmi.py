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
    def move(self, ph_sys):
        if self.etat == "cherche":
            if Vector2.distance_to(self.position, NOURRITURE) < CELL_SIZE:
                self.etat = "rentre"
            else: 
                if Vector2.distance_to(self.position, self.destination) < 5:
                    left_a = self.get_angle(-30)
                    front_a = self.get_angle(30)
                    right_a = self.get_angle(0)
                    pheromones = {}
                    pos_la = self.read_pheromones(left_a, ph_sys)
                    pos_fa = self.read_pheromones(front_a, ph_sys)
                    pos_ra = self.read_pheromones(right_a, ph_sys)
                    pheromones = {pos_la: left_a, pos_fa: front_a, pos_ra: right_a}
                    better_way = max(pheromones)
                    if max(pheromones) == 0:
                        self.destination = Vector2(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))
                    else:
                        self.destination = pheromones[max(pheromones)]
                else:
                    norm = (self.destination - self.position).normalize()
                    self.direction = Vector2.lerp(self.direction, norm, 0.1) 
                    self.position += self.direction * self.speed

        if self.etat == "rentre":
            if Vector2.distance_to(self.position, NID) < CELL_SIZE * 7:
                self.etat = "cherche"
            else:
                self.destination = NID
                norm = (self.destination - self.position).normalize()
                self.direction = Vector2.lerp(self.direction, norm, 0.1) 
                self.position += self.direction * self.speed
                ph_sys.deposer(int(self.position[0]), int(self.position[1]))
    def get_angle(self, angle):
        angle_t = self.position + Vector2.rotate(self.direction, angle) * (CELL_SIZE * 3)
        return angle_t
    def read_pheromones(self, pos, ph_sys):
        x = max(0, min(int(pos[0] // CELL_SIZE), col - 1))
        y = max(0, min(int(pos[1] // CELL_SIZE), row - 1))
        value = ph_sys.grid[y][x]
        return value    