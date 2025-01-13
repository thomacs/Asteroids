# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups for easy game logic and rendering
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField_1 = AsteroidField()


    while True:
        screen.fill(color="black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update sprites
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player_1):
                print("Game over!w")
                exit()
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()


        # Draw sprites
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()