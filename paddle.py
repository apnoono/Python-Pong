"""Module defining Paddle class."""
import pygame
from window import Window


class Paddle(pygame.sprite.Sprite):
    """ Paddle class to store paddle state/behavior """
    PADDLE_WIDTH = 8
    PADDLE_HEIGHT = 80
    HALF_PADDLE_WIDTH = PADDLE_WIDTH // 2
    HALF_PADDLE_HEIGHT = PADDLE_HEIGHT // 2

    UP1 = False
    DOWN1 = False
    NEUTRAL1 = True

    UP2 = False
    DOWN2 = False
    NEUTRAL2 = True


    def __init__(self, player: int, window: Window):
        """ constructor to initialize paddle object
        :param player: An integer (1 or 2) denoting human player1 or player2
        :param window: The game window object; passed from the Pong class
        """
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.game_window = window
        self.player = player
        self.image = pygame.Surface([self.PADDLE_WIDTH, self.PADDLE_HEIGHT])
        self.image.fill(self.game_window.colors[2]) #green
        self.rect = self.image.get_rect()
        self.speed = 8

        # Set paddle location

        if self.player == 1:
            self.rect.centerx = self.game_window.game_surf_rect.left
            self.rect.centerx += 50
        elif self.player == 2:
            self.rect.centerx = self.game_window.game_surf_rect.right
            self.rect.centerx -= 50
        self.rect.centery = self.game_window.game_surf_rect.centery


    def move(self):
        """ method defining paddle movement """
        if self.player == 1:
            if (self.UP1 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (self.DOWN1 == True) and (self.rect.bottom < self.game_window.height -5):
                self.rect.y += self.speed
            elif (self.NEUTRAL1 == True):
                pass

        if self.player == 2:
            if (self.UP2 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (self.DOWN2 == True) and (self.rect.bottom < self.game_window.height -5):
                self.rect.y += self.speed
            elif (self.NEUTRAL2 == True):
                pass
