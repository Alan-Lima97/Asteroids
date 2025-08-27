import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if radius > 40:
            self.points = 20
        elif radius > 20:
            self.points = 40
        else:
            self.points = 80     
                        
    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, (255,255,255), center, int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = v1 * 1.2
        new_asteroid2.velocity = v2 * 1.2
