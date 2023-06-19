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
        self.current_x = 0
        self.current_x_police = 0

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
                    player = Player((x * tile_size, y * tile_size + 20),self.screen)
                    self.player.add(player)

                if cell == "G":
                    police = Police((x * tile_size, y * tile_size + 20),self.screen)
                    self.police.add(police)
                    pass

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        police = self.police.sprite
        police.rect.x += police.direction.x * police.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left

                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
            if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
                player.on_left = False
            if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
                player.on_right = False

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(police.rect):
                if police.direction.x < 0:
                    police.rect.left = sprite.rect.right
                    police.on_left = True
                    self.current_x_police = police.rect.left
                elif police.direction.x > 0:
                    police.rect.right = sprite.rect.left
                    police.on_right = True
                    self.current_x_police = police.rect.right
            if police.on_left and (police.rect.left < self.current_x_police or police.direction.x >= 0):
                police.on_left = False
            if police.on_right and (police.rect.right > self.current_x_police or police.direction.x <= 0):
                police.on_right = False

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
                    player.on_ground = True
                    
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
        

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(police.rect):
                if police.direction.y > 0:
                    police.rect.bottom = sprite.rect.top
                    police.direction.y = 0
                    police.on_ground = True
                elif police.direction.y < 0:
                    police.rect.top = sprite.rect.bottom
                    police.direction.y = 0
                    police.on_ceiling = True
        if police.on_ground and police.direction.y < 0 or police.direction.y > 1:
            police.on_ground = False
        if police.on_ceiling and police.direction.y > 0:
            police.on_ceiling = False

    def scrollx(self,):
        player = self.player.sprite
        playerx = player.rect.centerx
        directionx = player.direction.x
        # print("playerx", playerx, "directionx", directionx)
        police = self.police.sprite
        policex = police.rect.centerx
        directionPolicex = police.direction.x

        if playerx < (screen_width / 4) and directionx < 0:
            self.shift = 8
            player.speed = 0
        elif playerx > screen_width - screen_width / 4 and directionx > 0:
            self.shift = -8
            player.speed = 0
        else:
            self.shift = 0
            player.speed = 8

        if policex < (screen_width / 4) and directionPolicex < 0:

            self.shift = 8
            police.speed = 0
        elif policex > screen_width - screen_width / 4 and directionPolicex > 0:
            self.shift = -8
            police.speed = 0
        else:
            self.shift = 0
            police.speed = 8

    def play(self):
        self.tiles.update(self.shift)
        self.tiles.draw(self.screen)
        self.player.draw(self.screen)
        self.police.draw(self.screen)
        self.player.update()
        self.police.update()
        self.scrollx()
        self.vertical_collision()
        self.horizontal_collision()
