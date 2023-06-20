import pygame
from state import State

class MainMenu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

#Load audio file
        pygame.mixer.music.load('assets/sounds/song.mp3')

        print("music started playing....")

        #Set preferred volume
        pygame.mixer.music.set_volume(0.2)

        #Play the music
        pygame.mixer.music.play(loops=-1)

        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("ሌባ እና ፖሊስ")
        background = pygame.image.load("assets/background/introBackground.png")
        background = pygame.transform.scale(background, (screen_width, screen_height))

        # Set up the font
        font = pygame.font.SysFont('nyala', 25)
        larger_font = pygame.font.SysFont('nyala', 80)


        # Set up the text አባሮሽ with larger font size
        text = larger_font.render("ሌባ እና ፖሊስ", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width/2, screen_height/2 - 100))

        # Set up the buttons
        button_width = 200
        button_height = 50
        play_again_button = pygame.Rect(screen_width/2 - button_width/2, screen_height/2 - 50, button_width, button_height)
        controls_button = pygame.Rect(screen_width/2 - button_width/2, screen_height/2 + 20, button_width, button_height)
        quit_button = pygame.Rect(screen_width/2 - button_width/2, screen_height/2 + 90, button_width, button_height)

        # Set up the loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_again_button.collidepoint(mouse_pos):
                        State.current_page = 'PLAY'
                        pygame.mixer.music.stop()
                        running = False
                        break
                    elif quit_button.collidepoint(mouse_pos):
                        # Quit the game
                        State.current_page = "QUIT"
                        running = False
                        break
                    elif controls_button.collidepoint(mouse_pos):
                        State.current_page = "CONTROLS"
                        running = False
                        break

            # Draw the screen
            screen.blit(background, (0, 0))

            pygame.draw.rect(screen, (255, 0, 0), play_again_button)
            pygame.draw.rect(screen, (255, 0, 0), controls_button)
            pygame.draw.rect(screen, (255, 0, 0), quit_button)
            screen.blit(text, text_rect)
            play_again_text = font.render("ተጫወት", True, (255, 255, 255))
            play_again_text_rect = play_again_text.get_rect(center=play_again_button.center)
            screen.blit(play_again_text, play_again_text_rect)

            controls_text = font.render("መቆጣጠሪያዎች", True, (255, 255, 255))
            controls_text_rect = controls_text.get_rect(center=controls_button.center)
            screen.blit(controls_text, controls_text_rect)

            quit_text = font.render("ውጣ", True, (255, 255, 255))
            quit_text_rect = quit_text.get_rect(center=quit_button.center)
            screen.blit(quit_text, quit_text_rect)
            pygame.display.flip()