# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init # initialize all imported pygame modules
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Initialize a window or screen [Surface] for display

    while True: # Game loop
        
        # This will check if the user has closed the window and exit the game loop if they do. 
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # Fill screen with solid black RGB (0,0,0)
        pygame.display.flip() # Refresh the screen

if __name__ == "__main__":
    main()