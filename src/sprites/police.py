from config import *
from support import import_folder
import pygame
import os
import sys
path = os.path.abspath('abarosh/src/support.py')
sys.path.append(path)


class Police(pygame.sprite.Sprite):

    def __init__(self, position, surface) -> None:
        print("police, police, police")

        super().__init__()
        self.import_character_states()
        self.frame_index = 0
        self.animation_speed = 0.15
        print(self.animations['idle'])
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=position)

        # dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.15
        self.display_surface = surface
        # self.create_jump_particles = create_jump_particles

        # movement
        self.speed = 8
        self.gravity = 0.6
        self.jump_speed = -16
        self.image = pygame.Surface((20, 40))
        # self.image.fill((0, 0, 255))
        self.speed = 10
        self.gravity = 0.8
        self.jump_speed = -16
        self.freezed = False
        self.direction = pygame.math.Vector2(0, 0)

        # status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_right = False
        self.on_left = False

    def import_character_states(self):
        character_path = 'graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            path = character_path + animation
            print(path)
            # print("about to be in import folder")
            # print(path)
            self.animations[animation] = import_folder(path)
            print(self.animations[animation])

    def collectInputs(self):

        # print("collecting inputs")

        keys = pygame.key.get_pressed()

        # TODO: Add a way to move left and right with a and d
        # TODO: Add a way to move up and down with w and s

        if keys[pygame.K_a]:
            if self.freezed:
                return
            self.direction.x = -1
            self.facing_right = False
            print("left")
            # self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            if self.freezed:
                return
            print("right")
            self.facing_right = True
            self.direction.x = 1
        else:
            self.direction.x = 0
            # self.rect.x += self.speed

        if keys[pygame.K_w] and self.on_ground:
            # print("jump")
            self.jump()

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        pygame.mixer.music.load('src/jump.wav')
        pygame.mixer.music.play()
        self.direction.y = self.jump_speed

    def colorPolice(self):
        if self.freezed:
            self.image.fill((150, 150, 150))
        else:
            self.image.fill((0, 0, 255))
        # self.applyGravity()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder(
            '../graphics/character/dust_particles/run')

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:

            self.image = pygame.transform.flip(image, True, False)

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def update(self, ):
        # self.colorPolice()
        self.applyGravity()
        self.get_status()
        self.animate()
        self.collectInputs()
