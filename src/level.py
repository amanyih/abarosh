import random
import pygame
from config import *
from sprites.tile import Tile
from sprites.player import Player
from sprites.police import Police
from sprites.message_board import MessageBoard
from sprites.stone import Stone


class Level:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.shift = 0
        self.draw_levels(lst_tile)
        self.current_x = 0
        self.current_x_police = 0

        self.duration = 3000
        self.message_board = pygame.sprite.GroupSingle()
        self.message_board.add(MessageBoard(
            screen_width, 100, (0, 0),title=""),)
    
    def get_tile_type(self,x,y,levels):
        # LT = left tile
        # TM = top middle tile
        # RT = right tile
        # MT = middle tile
        # ST = single tile
        if x == 0 or y == 0 or x == len(levels[0]) - 1 or y == len(levels) - 1:
            return "MT"
        elif levels[y][x-1] == "-" and levels[y][x+1] == "-" and levels[y-1][x] == "-" and levels[y+1][x] == "-":
            return "ST"
        elif levels[y][x+1] == "-" and levels[y-1][x] == "-":
            return "RT"
        elif levels[y][x-1] == "-" and levels[y-1][x] == "-":
            return "LT"
        elif levels[y-1][x] != "-" and levels[y+1][x] != "-" and levels[y][x-1] == "-" and levels[y][x+1] == "-":
            return "TM"
        elif levels[y][x-1] != "-" and levels[y][x+1] != "-" and levels[y-1][x] != "-" and levels[y+1][x] != "-":
            return "MT"
        return "MT"

    def draw_levels(self, levels):
        # levels = levels * 100
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.police = pygame.sprite.GroupSingle()
        for y, row in enumerate(levels):
            for x, cell in enumerate(row):
                if cell == "X":
                    tile_type = self.get_tile_type(x,y,levels)
                    tile = Tile(tile_size, (x * tile_size, y * tile_size), tile_type)
                    self.tiles.add(tile)

                if cell == "P":
                    player = Player((x * tile_size, y * tile_size + 20),self.screen)
                    self.player.add(player)

                if cell == "G":
                    police = Police((x * tile_size, y * tile_size + 20),self.screen)
                    self.police.add(police)
                    pass
        self.draw_stones()
    # TODO: Add a method to draw stones

    def draw_stones(self):
        self.stones = pygame.sprite.Group()
        tiles_group = self.tiles.sprites()
        for i in range(200):
            tile = random.choice(tiles_group)

            stone_pos = tile.rect.center
            x, y = stone_pos
            print("stone pos", stone_pos, x, y)
            stone = Stone(stone_size, (x, y-60))
            self.stones.add(stone)
            tiles_group.remove(tile)

    def horizontal_collision(self):
        player = self.player.sprite
        police = self.police.sprite

        if player.rect.colliderect(police.rect) and police.freezed == False:
            print("gameover")
            # quit()
        

        player.rect.x += player.direction.x * player.speed
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

        #make sure the stones are not colliding with the tiles
        for stone in self.stones.sprites():
            for tile in self.tiles.sprites():
                if stone.rect.colliderect(tile.rect):
                    self.stones.remove(stone)
        
        #player collides with stones
        for stone in self.stones.sprites():
            if stone.rect.colliderect(player.rect):
                self.stones.sprites().remove(stone)
                self.stones.remove(stone)
                self.police.sprite.freezed = True
                print("የማርያም መንገድ")
                self.startTime = pygame.time.get_ticks()
                self.message_board.sprite.title = "የማርያም መንገድ"
                

        if self.police.sprite.freezed:
            current_time = pygame.time.get_ticks()
            countdown_time_remaining = self.duration - (current_time - self.startTime)
            self.message_board.sprite.leading = str(countdown_time_remaining //1000)

        
        if self.police.sprite.freezed and pygame.time.get_ticks() - self.startTime >= self.duration:
            print("የማርያም መንገድ ተከፍተዋል")
            self.message_board.sprite.subtitle = ""
            self.message_board.sprite.title = ""
            self.message_board.sprite.leading = ""
            self.police.sprite.freezed = False
                # quit()

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

    def scrollx(self):
        player = self.player.sprite
        playerx = player.rect.centerx
        directionx = player.direction.x
        # print("playerx", playerx, "directionx", directionx)
        police = self.police.sprite
        policex = police.rect.centerx
        directionPolicex = police.direction.x

        if playerx < (screen_width / 4) and directionx < 0:

            if policex > screen_width - screen_width / 4:
                self.shift = 0
                police.speed = 0
                player.speed = 0
            else:

                self.shift = 8
                police.direction.x = 1
                police.rect.x += police.direction.x * police.speed
                player.speed = 0
        elif playerx > screen_width - screen_width / 4 and directionx > 0:
            if policex < (screen_width / 4):
                self.shift = 0
                police.speed = 0
                player.speed = 0
            else:

                self.shift = -8
                police.direction.x = -1
                police.rect.x += police.direction.x * police.speed
                player.speed = 0
        else:
            self.shift = 0
            police.speed = 8
            player.speed = 8

        # police movement

        if policex > screen_width - screen_width / 4 and directionPolicex > 0:

            if playerx < (screen_width / 4):
                self.shift = 0
                police.speed = 0
                player.speed = 0
            else:

                self.shift = -8
                player.direction.x = -1
                player.rect.x += player.direction.x * player.speed
                police.speed = 0
        elif policex < (screen_width / 4) and directionPolicex < 0:
            if playerx > screen_width - screen_width / 4:
                self.shift = 0
                police.speed = 0
                player.speed = 0
            else:
                self.shift = 8
                player.direction.x = 1
                player.rect.x += player.direction.x * player.speed
                police.speed = 0

        # else:
        #     self.shift = 0
        #     police.speed = 8
        #     player.speed = 8

    def play(self):
        self.message_board.update()
        # self.message_board.draw(self.screen)
        self.screen.blit(self.message_board.sprite.image, self.message_board.sprite.rect)
        self.tiles.update(self.shift)
        self.stones.update(self.shift)
        self.tiles.draw(self.screen)
        self.stones.draw(self.screen)
        self.player.draw(self.screen)
        self.police.draw(self.screen)

        self.player.update()
        self.police.update()
        self.vertical_collision()
        self.horizontal_collision()
        self.scrollx()
