import pygame

class Settings:
    """This is the class where all the settings for the game will be"""
    def __init__(self):
        """A method to initialize the game settings"""

        self.ship_speed = 1.5

        # Screen size
        self.screen_width = 1200
        self.screen_height = 750

        # Screen background color
        self.bg_color = (4, 19, 28)

        # Saving an image for the app icon
        self.app_icon = pygame.image.load('img/app-icon.png')

