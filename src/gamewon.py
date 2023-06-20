import pygame
import sys

from state import State


class Gamewon:

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen
        screen_width, screen_height = 800, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("YOU WON!!!")
        background = pygame.image.load("assets/background/introBackground.png")
        background = pygame.transform.scale(background, (screen_width, screen_height))

        # Set up fonts
        font = pygame.font.SysFont('nyala', 25) 
        fontH = pygame.font.SysFont('nyala', 80) 
        # Set up colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        # Set up scores
        current_score = 100  # Replace with your current score
        current_winner = "ሌባ"

        # Set up buttons
        button_width, button_height = 200, 50
        button_padding = 20

        # Calculate the horizontal center position for the buttons
        buttons_center_x = screen_width // 2 - (button_width + button_padding) // 2

        # Restart button
        restart_button_rect = pygame.Rect(
            buttons_center_x - 120,
            (screen_height - button_height) // 2,
            button_width,
            button_height,
        )
        restart_button_text = font.render("እንደገና ጀምር", True, WHITE)

        # Quit button
        quit_button_rect = pygame.Rect(
            buttons_center_x + button_width + button_padding - 40,
            (screen_height - button_height) // 2,
            button_width,
            button_height,
        )
        quit_button_text = font.render("ውጣ", True, WHITE)

        # Game over loop
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    if restart_button_rect.collidepoint(mouse_pos):
                        # Restart button clicked
                        print("Restarting the game...")
                        run = False
                        self.restart()
                        break
                        # Add your game logic to restart the game

                    elif quit_button_rect.collidepoint(mouse_pos):
                        # Quit button clicked
                        print("Quitting the game...")
                        pygame.quit()
                        sys.exit()

            # Draw the screen
            screen.blit(background, (0, 0))

            # Draw score
           
            current_winner_text = fontH.render(f"አሸናፊ: {current_winner}", True, BLACK)

            screen.blit(
                current_winner_text,
                ((screen_width - current_winner_text.get_width()) // 2, 150),
            )

            # Draw buttons
            pygame.draw.rect(screen, GREEN, restart_button_rect)
            pygame.draw.rect(screen, RED, quit_button_rect)
            screen.blit(
                restart_button_text,
                (
                    restart_button_rect.x + (button_width - restart_button_text.get_width()) // 2,
                    restart_button_rect.y + (button_height - restart_button_text.get_height()) // 2,
                ),
            )
            screen.blit(
                quit_button_text,
                (
                    quit_button_rect.x + (button_width - quit_button_text.get_width()) // 2,
                    quit_button_rect.y + (button_height - quit_button_text.get_height()) // 2,
                ),
            )

            # Update the screen
            pygame.display.flip()

    def restart(self):
        State.current_page = 'PLAY'

