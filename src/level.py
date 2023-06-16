import pygame
from config import *
from sprites.tile import Tile
from sprites.player import Player


class Level:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.shift = 8
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

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        player.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def scrollx(self,):
        player = self.player.sprite
        playerx = player.rect.centerx
        directionx = player.direction.x
        print("playerx", playerx, "directionx", directionx)

        if playerx < (screen_width / 4) and directionx < 0:
            self.shift = 8
            player.speed = 0
        elif playerx > screen_width - screen_width / 4 and directionx > 0:
            self.shift = -8
            player.speed = 0
        else:
            self.shift = 0
            player.speed = 8

    def play(self):
        self.tiles.update(self.shift)
        self.tiles.draw(self.screen)
        self.player.draw(self.screen)
        self.player.update()
        self.scrollx()
        self.vertical_collision()
        self.horizontal_collision()
