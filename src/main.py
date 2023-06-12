import pygame


def main():
    pygame.init()
    pygame.display.set_caption("abarosh")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        screen.fill((0, 0, 0))

        pygame.display.flip()

        clock.tick(60)


main()
