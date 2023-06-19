import pygame
from config import *


class Player(pygame.sprite.Sprite):

    def __init__(self, position) -> None:

        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill((255, 0, 0))
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16

        self.direction = pygame.math.Vector2(0, 0)

        self.rect = self.image.get_rect(topleft=position)

    def collectInputs(self, ):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            # self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            # self.rect.x += self.speed

        if keys[pygame.K_UP]:
            print("jump")
            self.jump()

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        # self.applyGravity()

    def update(self, ):
        self.collectInputs()
        self.applyGravity()
