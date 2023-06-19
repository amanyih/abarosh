import pygame


class Stone(pygame.sprite.Sprite):

    def __init__(self, size, position) -> None:
        super().__init__()
        self.image = pygame.Surface((size, size))

        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=position)

    def update(self, x_shift):
        self.rect.x += x_shift
