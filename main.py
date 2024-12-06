import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!\nScreen width: 1280\nScreen height: 720") #Figure out how to use the variables from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    on = True
    black = 000000
    clock = pygame.time.Clock()
    dt = 0

    while on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()



# Base class for game objects #####
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

if __name__ == "__main__":
	main()
