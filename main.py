import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys


def main():
    pygame.init()
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720") #Figure out how to use the variables from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    on = True
    black = 000000
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_con = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_con, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroidfield = AsteroidField()

    while on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroids in asteroid_con:
            if asteroids.collision(player) == True:
                  print("Game over!")
                  sys.exit()
            else:
                 pass
            for bullets in shots:
                if asteroids.collision(bullets) == True:
                      asteroids.kill()
                      bullets.kill()
                else:
                    pass
        pygame.Surface.fill(screen, (0,0,0))
        for sprite in drawable:
             sprite.draw(screen)
        pygame.display.flip()

    

if __name__ == "__main__":
	main()
