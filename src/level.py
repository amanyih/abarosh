import pygame
from config import *
from sprites.tile import Tile
from sprites.player import Player


class Level:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.shift = 0
        self.draw_levels(lst_tile)

    def draw_levels(self, levels):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for y, row in enumerate(levels):
            for x, cell in enumerate(row):
                if cell == "X":
                    tile = Tile(tile_size, (x * tile_size, y * tile_size))
                    self.tiles.add(tile)

                if cell == "P":
                    player = Player((x * tile_size, y * tile_size + 20))
                    self.player.add(player)

    def play(self):
        self.tiles.update(self.shift)
        self.tiles.draw(self.screen)
        self.player.draw(self.screen)
        self.player.update()
