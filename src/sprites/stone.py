import pygame
from config import *

stone_skin = pygame.transform.scale(pygame.image.load(
    "assets/stones/d4.png"), (stone_size, stone_size))


class Stone(pygame.sprite.Sprite):

    def __init__(self, size, position) -> None:
        super().__init__()
        self.image = stone_skin

        # self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=position)

    def update(self, x_shift):
        self.rect.x += x_shift
