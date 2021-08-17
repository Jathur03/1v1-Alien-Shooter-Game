import pygame
from pygame.sprite import Sprite

class BBullet(Sprite):
    """The class for the blue ship"""
    def __init__(self, game):
        """Create a blue bullet in the place the blue bullet is"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.blue_bullet_color

        # Creating the bullet's rectangle at 0, 0 then moving it to the ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
        self.rect.midtop = game.bships.rect.midtop

        # Storing the blue bullets x position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the other side of the window"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class RBullet(Sprite):
    """The class for the blue ship"""
    def __init__(self, game):
        """Create a blue bullet in the place the blue bullet is"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = game.settings.red_bullet_color

        # Creating the bullet's rectangle at 0, 0 then moving it to the ship
        self.rect = pygame.Rect(0, 0, self.settings.bullet_height, self.settings.bullet_width)
        self.rect.midtop = game.rships.rect.midtop

        # Storing the blue bullets x position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the other side of the window"""
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)