import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Asteroids")
    print("Starting Asteroids!")

    updatable = pygame.sprite.Group() #cria grupos
    drawable = pygame.sprite.Group() #cria grupos
    asteroid = pygame.sprite.Group() #cria grupos

    # Definir os containers para o Player, Asteroid e AsteroidField

    Player.containers = (updatable, drawable) # grupos viram containers do player

    Asteroid.containers = (asteroid, updatable, drawable) #grupos viram containers do Asteroid.

    AsteroidField.containers = (updatable) #grupos viram containers do AsteroidField.

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Criando o jogador
    asteroidfield = AsteroidField() # Instanciando o campo de asteroides
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        screen.fill((0, 0, 0)) 
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
