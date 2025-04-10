import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    def draw(self, screen):
        # Draw the triangle
        pygame.draw.polygon(screen,(255, 255, 255), self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) # Rotaciona para a esquerda
        if keys[pygame.K_d]:
            self.rotate(dt) # Rotaciona para a direita
        if keys[pygame.K_w]:
            self.move(dt) # move o player pra frente
        if keys[pygame.K_s]:
            self.move(-dt) # move o player pra trás
    
    def move(self, dt): #move player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt): #rotate player
        self.rotation += PLAYER_TURN_SPEED * dt
class Shot (CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, SHOT_RADIUS) # Chama o construtor da classe CircleShape
    def draw(self, screen):
        # Desenha o asteroide
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 5)
    def update(self, dt):
       # Atualiza a posição do asteroide
        self.position += self.velocity * dt