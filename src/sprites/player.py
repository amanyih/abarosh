import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, position) -> None:

        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill((255, 0, 0))
        self.speed = 5

        self.rect = self.image.get_rect(topleft=position)

    def collectInputs(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_SPACE]:
            self.rect.y += self.speed

    def update(self):
        self.collectInputs()
