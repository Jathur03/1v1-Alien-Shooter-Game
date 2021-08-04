import pygame

class Ships:
    """This is the class for the blue ship in alien wars"""
    def __init__(self, game):
        """Initialize the ships and its attributes"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings

        # Saving the ships' image to a variable and getting its rect
        self.blue_ship_image = pygame.image.load('img/blue.png')
        self.blue_ship_rect = self.blue_ship_image.get_rect()

        self.red_ship_image = pygame.image.load('img/red.png')
        self.red_ship_rect = self.red_ship_image.get_rect()

        # Making each ship to start in the left bottom part of the screen
        self.blue_ship_rect.bottomleft = self.screen_rect.bottomleft
        self.red_ship_rect.bottomright = self.screen_rect.bottomright

        # Moving flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update_ship(self):
        """Change the ships position"""
        

    def blitme(self):
        """Draw the blue ship at its current location"""
        self.screen.blit(self.blue_ship_image, self.blue_ship_rect)
        self.screen.blit(self.red_ship_image, self.red_ship_rect)