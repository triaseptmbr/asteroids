import pygame
import random

from circleshape import CircleShape
from logger import log_event
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            angle = random.uniform(20, 50)
            one_angle = self.velocity.rotate(angle)
            two_angle = self.velocity.rotate(-angle)
            
            radius = self.radius - ASTEROID_MIN_RADIUS

            one = Asteroid(self.position.x, self.position.y, radius)
            two = Asteroid(self.position.x, self.position.y, radius)

            one.velocity = one_angle * 1.2
            two.velocity = two_angle * 1.2
