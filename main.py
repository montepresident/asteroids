import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720") #Figure out how to use the variables from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    on = True
    black = 000000
    while on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
	main()
