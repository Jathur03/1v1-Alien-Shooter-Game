import pygame

class BlueShip:
    """This is the class for the blue ship in alien wars"""
    def __init__(self, game):
        """Initialize the blue ship and its attributes"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings

        # Saving the blue ship image to a variable and getting its rect
        self.blue_ship_image = pygame.image.load('img/app-icon.png')
        self.blue_ship_rect = self.blue_ship_image.get_rect()

        # Making each ship to start in the left bottom part of the screen
        self.blue_ship_rect = self.screen_rect.left_bottom