import pygame 
from level import Level
from config import *
from state import State

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("abarosh")
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        level = Level(screen)
        running = True

        while running and State.current_page == "PLAY":

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()

            screen.fill((0, 0, 0))
            level.play()

            pygame.display.flip()

            clock.tick(60)