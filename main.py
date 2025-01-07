import pygame
from constants import *
from player import *

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
    player = Player(x, y)


    while on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000
        player.update(dt)
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        pygame.display.flip()

    

if __name__ == "__main__":
	main()
