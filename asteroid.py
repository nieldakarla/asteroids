import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # Chama o construtor da classe CircleShape
    def draw(self, screen):
        # Desenha o asteroide
        pygame.draw.circle(screen, (250, 0, 0), self.position, self.radius, 2)
    def update(self, dt):
       # Atualiza a posição do asteroide
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20,50) #will be used for new ast directions

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)

        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast_1.velocity = pygame.math.Vector2.rotate(self.velocity, new_angle) * 1.2

        ast_2.velocity = pygame.math.Vector2.rotate(self.velocity, -new_angle) * 1.2










        

