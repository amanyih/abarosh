import pygame


class MessageBoard(pygame.sprite.Sprite):

    def __init__(self, width, height, position, title) -> None:
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)
        self.leading = ""
        self.font = pygame.font.SysFont("nyala", 20)
        self.larger_font = pygame.font.SysFont("nyala", 60)
        self.title = ""
        self.subtitle = ""
        self.trailing = "trailing"
        self.globalTime = pygame.time.get_ticks()
        self.game_duration = 1000 * 120
        # self.game_duration = 2000

    def draw_text(self, text, position, font):
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=position)
        self.image.blit(text_surface, text_rect)

    def draw_message(self,):
        # leading_position = (self.rect.width // 2, self.rect.height // 4)
        leading_position = (self.rect.width//8, self.rect.height//2)
        self.draw_text(self.leading, leading_position, self.larger_font)

        title_position = (self.rect.width // 2, self.rect.height // 2)
        self.draw_text(self.title, title_position, self.larger_font)

        subtile_pos = (self.rect.width // 2, (3 * self.rect.height) // 4)
        self.draw_text(self.subtitle, subtile_pos, self.larger_font)

        time_pos = (self.rect.width - self.rect.width /
                    8, self.rect.height // 2)

        current_time = pygame.time.get_ticks()
        countdown_time_remaining = self.game_duration - \
            (current_time - self.globalTime)

        if countdown_time_remaining <= 0:
            quit()

        formatted_time = countdown_time_remaining // 1000

        time_sec = str(formatted_time % 60)
        time_min = str(formatted_time // 60)
        time_msg = time_min + ":" + time_sec

        self.draw_text(time_msg, time_pos, self.larger_font)

    def display(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def update(self, ):
        self.image.fill((255, 255, 255))
        self.draw_message()
