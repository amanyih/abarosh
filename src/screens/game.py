import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("አባሮሽ")

# Set up the font
font = pygame.font.SysFont('nyala', 25)
larger_font = pygame.font.SysFont('nyala', 50)

def play_again_screen():
    # Set up the text አባሮሽ with larger font size
    text = larger_font.render("አባሮሽ", True, (255, 255, 255))
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
                    # Start the game again
                    return True
                elif quit_button.collidepoint(mouse_pos):
                    # Quit the game
                    running = False
                    return False

        # Draw the screen
        screen.fill((0, 0, 0))
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

# Set up the game loop
playing = True
play_again_screen()

# Quit Pygame
pygame.quit()