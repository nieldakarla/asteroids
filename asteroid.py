import pygame
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius) # Chama o construtor da classe CircleShape
    def draw(self, screen):
        # Desenha o asteroide
        pygame.draw.circle(screen, (250, 0, 0), self.position, self.radius, 2)
    def update(self, dt):
       # Atualiza a posição do asteroide
        self.position += self.velocity * dt