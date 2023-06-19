import pygame
from config import *
from sprites.tile import Tile
from sprites.player import Player
from sprites.police import Police


class Level:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.shift = 0
        self.draw_levels(lst_tile)

    def draw_levels(self, levels):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.police = pygame.sprite.GroupSingle()
        for y, row in enumerate(levels):
            for x, cell in enumerate(row):
                if cell == "X":
                    tile = Tile(tile_size, (x * tile_size, y * tile_size))
                    self.tiles.add(tile)

                if cell == "P":
                    player = Player((x * tile_size, y * tile_size + 20))
                    self.player.add(player)

                if cell == "G":
                    police = Police((x * tile_size, y * tile_size + 20))
                    self.police.add(police)
                    pass

    def horizontal_collision(self):
        player = self.player.sprite
        police = self.police.sprite

        if player.rect.colliderect(police.rect):
            print("gameover")
            # quit()

        player.rect.x += player.direction.x * player.speed
        police.rect.x += police.direction.x * police.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(police.rect):
                if police.direction.x < 0:
                    police.rect.left = sprite.rect.right
                elif police.direction.x > 0:
                    police.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        player.applyGravity()

        police = self.police.sprite
        police.applyGravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(police.rect):
                if police.direction.y > 0:
                    police.rect.bottom = sprite.rect.top
                    police.direction.y = 0
                elif police.direction.y < 0:
                    police.rect.top = sprite.rect.bottom
                    police.direction.y = 0

    def scrollx(self):
        player = self.player.sprite
        playerx = player.rect.centerx
        directionx = player.direction.x
        # print("playerx", playerx, "directionx", directionx)
        police = self.police.sprite
        policex = police.rect.centerx
        directionPolicex = police.direction.x

        # if abs(playerx - policex) >= screen_width/2:
        #     return

        if playerx < (screen_width / 4) and directionx < 0:
            self.shift = 8
            police.direction.x = 1
            police.rect.x += police.direction.x * police.speed
            player.speed = 0
        elif playerx > screen_width - screen_width / 4 and directionx > 0:
            self.shift = -8
            police.direction.x = -1
            police.rect.x += police.direction.x * police.speed
            player.speed = 0
        else:
            self.shift = 0
            police.speed = 8
            player.speed = 8

        if policex > screen_width - screen_width / 4 and directionPolicex > 0:
            self.shift = -8
            player.direction.x = -1
            player.rect.x += player.direction.x * player.speed
            police.speed = 0
        elif policex < (screen_width / 4) and directionPolicex < 0:
            self.shift = 8
            player.direction.x = 1
            player.rect.x += player.direction.x * player.speed
            police.speed = 0
        # else:
        #     self.shift = 0
        #     police.speed = 8
        #     player.speed = 8

    def play(self):
        self.tiles.update(self.shift)
        self.tiles.draw(self.screen)
        self.player.draw(self.screen)
        self.police.draw(self.screen)
        self.player.update()
        self.police.update()
        self.vertical_collision()
        self.horizontal_collision()
        self.scrollx()
