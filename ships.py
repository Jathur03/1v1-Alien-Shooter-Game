import pygame
from pygame.sprite import Sprite

class BShips(Sprite):
    """This is the class for the ships"""
    def __init__(self, game):
        super().__init__()
        """Initialize the ships and its attributes"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.settings = game.settings

        # Saving the ships' image to a variable and getting its rect
        self.blue_ship_image = pygame.image.load('img/blue.png')
        self.blue_ship_rect = self.blue_ship_image.get_rect()

        self.red_ship_image = pygame.image.load('img/red.png')
        self.red_ship_rect = self.red_ship_image.get_rect()

        # Making each ship to start in the bottom part of the screen
        self.blue_ship_rect.bottomleft = self.screen_rect.bottomleft
        self.red_ship_rect.bottomright = self.screen_rect.bottomright

        self.y = float(self.blue_ship_rect.y)
        self.y = float(self.red_ship_rect.y)

        self.blue_moving_up = False
        self.red_moving_up = False
        self.blue_moving_down = False
        self.red_moving_down = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's y value, not the rect
        if self.blue_moving_down and self.blue_ship_rect.down < self.screen_rect.down:
            self.y += self.settings.ship_speed
        if self.blue_moving_up and self.blue_ship_rect.up < self.screen_rect.up:
            self.y -= self.settings.ship_speed

        # Update rect object from self.y.
        self.blue_ship_rect.y = self.y



    def blitme(self):
        """Draw the blue ship at its current location"""
        self.screen.blit(self.blue_ship_image, self.blue_ship_rect)
        self.screen.blit(self.red_ship_image, self.red_ship_rect)
    
    def spawn_ship(self):
        """Spawn ships on each side"""
