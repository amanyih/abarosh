import pygame
from config import *
pygame.init()

left_tile = pygame.transform.scale(pygame.image.load(
    "assets/tiles/1.png"), (tile_size, tile_size))

top_middle_tile = pygame.transform.scale(pygame.image.load(
    "assets/tiles/2.png"), (tile_size, tile_size))
right_tile = pygame.transform.scale(pygame.image.load(
    "assets/tiles/3.png"), (tile_size, tile_size))
middle_tile = pygame.transform.scale(pygame.image.load(
    "assets/tiles/4.png"), (tile_size, tile_size))
single_tile = pygame.transform.scale(pygame.image.load(
    "assets/tiles/5.png"), (tile_size, tile_size))


class Tile(pygame.sprite.Sprite):
    """
    types:
    LT = left tile
    TM = top middle tile
    RT = right tile
    MT = middle tile
    ST = single tile

    """

    def __init__(self, size, position, type="LT") -> None:
        super().__init__()
        # resize all tiles to tile_size
        self.size = size
        self.position = position
        self.type = type

        if type == "LT":
            self.image = left_tile
        elif type == "TM":
            self.image = top_middle_tile
        elif type == "RT":
            self.image = right_tile
        elif type == "MT":
            self.image = middle_tile
        elif type == "ST":
            self.image = single_tile
        else:
            self.image = single_tile

        # self.image = pygame.Surface((size, size))

        # self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)

    def update(self, x_shift):
        self.rect.x += x_shift
