import pygame
pygame.font.init()

class Settings:
    """This is the class where all the settings for the game will be"""
    def __init__(self):
        """A method to initialize the game settings"""
        pygame.font.init()

        self.ship_speed = 3

        # Screen size
        self.screen_width = 1200
        self.screen_height = 750

        # Screen background color
        self.bg_color = (4, 19, 28)

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.blue_bullet_color = (41, 128, 185)
        self.red_bullet_color = (231, 76, 60)

        self.blue_lives = 10
        self.red_lives = 10

        self.health_font = pygame.font.SysFont('comicsans', 40)
        self.winner_font = pygame.font.SysFont('comicsans', 100)

        # Saving an image for the app icon
        self.app_icon = pygame.image.load('img/app-icon.png')