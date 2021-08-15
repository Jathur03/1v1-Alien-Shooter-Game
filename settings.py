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

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.blue_bullet_color = ('#2980b9')
        self.red_bullet_color = ('#e74c3c')

        # Saving an image for the app icon
        self.app_icon = pygame.image.load('img/app-icon.png')

