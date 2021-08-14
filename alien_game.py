# Importing the libraries needed for the game
import pygame
import sys

# Importing the modules needed for the game
from settings import Settings
from ships import BShips

class AlienWars:
    """This is the main class for the alien war game"""
    def __init__(self):
        """A method to initalize the game and create the game resources"""
        # Initalizing pygame
        pygame.init()

        self.settings = Settings()

        # Setting the window size
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.bships = BShips(self)

        # Setting the caption for the window
        pygame.display.set_caption("🛸 Alien Wars 🛸")

        # Setting the app icon for the game
        pygame.display.set_icon(self.settings.app_icon)

    def run_game(self):
        """Method for the main game loop"""
        while True:
            self._check_events()
            self.bships.update()
            self._update_screen()
            print(self.bships.y)
            

    def _check_events(self):
        """A method to respond to events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """"A method to respond to keydown events"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.type == pygame.K_w:
            self.ship.blue_moving_up = True
        elif event.type == pygame.K_s:
            self.ship.blue_moving_down = True
        elif event.type == pygame.K_UP:
            self.ship.red_moving_up = True
        elif event.type == pygame.K_DOWN:
            self.ship.red_moving_down = True
        # elif event.type == pygame.K_LSHIFT:
        #     self.blue_fire_bullet = True
        # elif event.type == pygame.K_RSHIFT:
        #     self.red_fire_bullet = True

    def _check_keyup_events(self, event):
        """"A method to respond to keydown events"""
        if event.type == pygame.K_w:
            self.ship.blue_moving_up = False
        elif event.type == pygame.K_s:
            self.ship.blue_moving_down = False
        elif event.type == pygame.K_UP:
            self.ship.red_moving_up = False
        elif event.type == pygame.K_DOWN:
            self.ship.red_moving_down = False



#             VEL = 5

# def yellow_handle_movement(keys_pressed, yellow):
#     if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
#         yellow.x -= VEL
#     if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
#         yellow.x += VEL
#     if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
#         yellow.y -= VEL
#     if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < settings.screen_height - 15:  # DOWN
#         yellow.y += VEL


# def red_handle_movement(keys_pressed, red):
#     if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
#         red.x -= VEL
#     if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < settings.screen_width:  # RIGHT
#         red.x += VEL
#     if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
#         red.y -= VEL
#     if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < settings.screen_height - 15:  # DOWN
#         red.y += VEL



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # Making the border that divides both sides of the screen
        BORDER = pygame.Rect(1200//2 - 5, 0, 10, 750)

        pygame.draw.rect(self.screen, (255, 255, 255), BORDER)

        self.bships.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    aw = AlienWars()
    aw.run_game()