# Importing the libraries needed for the game
import pygame
import sys

# Importing the modules needed for the game
from settings import Settings
from ships import Ships

class AlienWars:
    """This is the main class for the alien war game"""
    def __init__(self):
        """A method to initalize the game and create the game resources"""
        # Initalizing pygame
        pygame.init()

        self.settings = Settings()

        # Setting the window size
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ships = Ships(self)

        # Setting the caption for the window
        pygame.display.set_caption("🛸 Alien Wars 🛸")

        # Setting the app icon for the game
        pygame.display.set_icon(self.settings.app_icon)

    def run_game(self):
        """Method for the main game loop"""
        while True:
            self._check_events()
            self.ships.update_ship()
            self._update_screen()

    def _check_events(self):
        """A method to respond to events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """"A method to respond to keydown events"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.type == pygame.K_LEFT:
            self.ship.moving_left = True

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # Making the border that divides both sides of the screen
        BORDER = pygame.Rect(1200//2 - 5, 0, 10, 750)
        pygame.draw.rect(self.screen, (255, 255, 255), BORDER)

        self.ships.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    aw = AlienWars()
    aw.run_game()