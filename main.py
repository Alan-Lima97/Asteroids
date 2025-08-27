import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid
from shot import Shot
from gameover import game_over_screen

def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    font = pygame.font.Font(None, 36)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#   groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

#   containers
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

#   create player
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#   create field
    asteroid_field = AsteroidField()


#   game loop
    while True:

#       events    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

#       update
        dt = clock.tick(60) / 1000

        updatables.update(dt)

#       colisions and gameover
        for asteroid in asteroids:
            if asteroid.collision(player1):
                action = game_over_screen(screen, score, SCREEN_WIDTH, SCREEN_HEIGHT, font)
                if action == "restart":
                    main()

#       shot collision
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    score += asteroid.points
                    asteroid.split()

#       draws
        screen.fill((0, 0, 0))
         
        for drawable in drawables:
            drawable.draw(screen)

        text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
                

if __name__ == "__main__":
    main()
