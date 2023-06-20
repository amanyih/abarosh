import pygame
from config import *
from level import Level


def main():
    pygame.init()
    pygame.display.set_caption("abarosh")
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    level = Level(screen)
    running = True
    bg = pygame.transform.scale(pygame.image.load(
        "assets/background/bg.jpg"), (screen_width, screen_height))

    while running:
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        # screen.fill((0, 0, 0))
        level.play()

        pygame.display.flip()

        clock.tick(60)


main()
