import pygame

from shot import Shot
from circleshape import *
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED, 
    PLAYER_SHOOT_SPEED, 
    PLAYER_SHOOT_COOLDOWN
)
    
class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # Rotation to the left "a"
            self.rotate(dt * -1)
        if keys[pygame.K_d]: # Rotation to the right with "d"
            self.rotate(dt)
        if keys[pygame.K_s]: # Move backwards with "s"
            self.move(dt * -1)
        if keys[pygame.K_w]: # Move forwards with "w"
            self.move(dt)
        if keys[pygame.K_SPACE]: # Shot with "space"
            if self.shot_timer <= 0:
                self.shoot()
        
        self.shot_timer -= dt