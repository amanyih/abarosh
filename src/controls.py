import pygame
from state import State

class Controls:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up the screen
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))

        # Set up the font
        font = pygame.font.SysFont('nyala', 35)

        # Set up the text
        # It will be two columns one for the controls of the cop and one for the controls of the thief
        text = font.render("መቆጣጠሪያዎች", True, (255, 255, 255))

        # Set up the controls for the police on the left of the screen
        # The controls will be a list of strings
        police_controls = [
            "ወደ ላይ: W",
            "ወደ ቀኝ: D",
            "ወደ ግራ: A",
        ]

        # Set up the controls for the thief on the right of the screen
        thief_controls = [
            "ወደ ላይ: UP ARROW",
            "ወደ ቀኝ: RIGHT ARROW",
            "ወደ ግራ: LEFT ARROW",
        ]

        # Set up the title "controls"
        title = font.render("መቆጣጠሪያዎች", True, (255, 255, 255))
        screen.blit(title, (screen_width/2 - title.get_width()/2, 50))


        police_controls_title = "ለፖሊስ ቁጥጥር"

        text = font.render(police_controls_title, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width/4 - 20, screen_height/2 - 150))
        screen.blit(text, text_rect)


        for index, control in enumerate(police_controls):
            text = font.render(control, True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen_width/4 - 20, screen_height/2 - 100 + index * 50 + 20))
            screen.blit(text, text_rect)

        thief_controls_title = "ሌባውን ለመቆጣጠር"

        text = font.render(thief_controls_title, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width/4 * 3  - 20, screen_height/2 - 150))
        screen.blit(text, text_rect)

        for index, control in enumerate(thief_controls):
            text = font.render(control, True, (255, 255, 255))
            text_rect = text.get_rect(center=(screen_width/4 * 3  - 20, screen_height/2 - 100 + index * 50 + 20))
            screen.blit(text, text_rect)

        # Set up the back button
        button_width = 200
        button_height = 50
        back_button_rect = pygame.Rect(screen_width/2 - button_width/2, screen_height - 150, button_width, button_height)

        # Set up the back button text
        pygame.draw.rect(screen, (255, 0, 0), back_button_rect)
        back_button_text = font.render("< ተመለስ", True, (255, 255, 255))

        play_again_text_rect = back_button_text.get_rect(center=back_button_rect.center)
        screen.blit(back_button_text, play_again_text_rect)

        # Game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    State.current_page = 'QUIT'
                    running = False
                    break

                # Check if the user clicked on the back button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button_rect.collidepoint(event.pos):
                        State.current_page = 'MAINMENU'
                        running = False
                        break

            # Update the screen
            pygame.display.flip()

