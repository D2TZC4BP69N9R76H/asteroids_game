# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init # initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Initialize a window or screen [Surface] for display
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group() # all the objects that can be updated
    drawable = pygame.sprite.Group() # all the objects that can be drawn
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable) # Future player instances will automatically be added to both the updatable and drawable groups because of the containers you set up
    
    main_player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while True: # Game loop

        # This will check if the user has closed the window and exit the game loop if they do. 
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill screen with solid black RGB (0,0,0)
        screen.fill((0, 0, 0)) 
        
        # Update the rotation
        updatable.update(dt)

        # Loop over all drawables and call their draw method individually
        for entity in drawable:
            entity.draw(screen)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collides_with(main_player):  # Replace 'player' with the actual variable name for your player object
                print("Game over!")
                
                # Exit the program
                sys.exit(0)
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()


        # Refresh the screen
        pygame.display.flip() 
        
        # Limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000 # It will compute how many milliseconds have passed since the previous call
            # It should be called  once per frame
            # converts the delta from miliseconds to seconds

if __name__ == "__main__":
    main()