import pygame
from constants import *

black = (0, 0, 0)

def main ():
    pygame.init
    print ("'Starting asteroids!'")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while screen:
        screen.fill(black)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



if __name__ == "__main__":
    main()