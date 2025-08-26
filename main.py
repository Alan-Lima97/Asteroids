import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid
from shot import Shot

def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:

#       events    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

#       update
        dt = clock.tick(60) / 1000

        updatables.update(dt)

#       colisions
        for asteroid in asteroids:
            if asteroid.collision(player1):
                print("Game Over")
                pygame.quit()
                sys.exit()

#       shot collision
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

#       draws
        screen.fill((0, 0, 0))
         
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
                

if __name__ == "__main__":
    main()
