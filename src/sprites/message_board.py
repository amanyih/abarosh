import pygame


class MessageBoard(pygame.sprite.Sprite):

    def __init__(self, width, height, position, title) -> None:
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)
        self.leading = "hahahaha"
        self.font = pygame.font.SysFont("Nunito", 20)
        self.title = ""
        self.subtitle = ""
        self.trailing = "trailing"

    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=position)
        self.image.blit(text_surface, text_rect)

    def draw_message(self,):
        # leading_position = (self.rect.width // 2, self.rect.height // 4)
        leading_position = (30, 30)
        self.draw_text(self.leading, leading_position)

        title_position = (self.rect.width // 2, self.rect.height // 2)
        self.draw_text(self.title, title_position)

        subtile_pos = (self.rect.width // 2, (3 * self.rect.height) // 4)
        self.draw_text(self.subtitle, subtile_pos)

    def display(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def update(self, ):
        self.image.fill((255, 255, 255))
        self.draw_message()
