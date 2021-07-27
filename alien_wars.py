# Importing the libraries needed for the game
import pygame
import sys

# Importing the modules needed for the game
from settings import Settings

class AlienWars:
    """This is the main class for the alien war game"""
    def __init__(self):
        """A method to initalize the game and create the game resources"""
        # Initalizing pygame
        pygame.init()

        # Storing the settings from settings.py in a variable
        self.settings = Settings()

        # Setting the window size
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Setting the caption for the window
        pygame.display.set_caption("🛸 Alien Wars 🛸")

    def run_game(self):
        """Method for the main game loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """A method to respond the check for events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
    aw = AlienWars()
    aw.run_game()