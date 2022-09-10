"""Module defining Avatar class."""
import pygame
from window import Window
from ball import Ball
from paddle import Paddle


class Avatar(Paddle):
    """ Avatar class to store avatar state/behavior """

    def __init__(self, ball: Ball, mode: str, window: Window):
        """ constructor to initialize avatar object

        :param ball: A ball object which is passed from the Pong class
        :param mode: A string denoting difficulty ('EASY' or 'HARD')
        :param window: The game window object; passed from the Pong class
        """
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.game_window = window
        self.mode = mode
        self.player_number = 2
        self.ball = ball

        if mode == "EASY":
            self.image = pygame.Surface([self.PADDLE_WIDTH, self.PADDLE_HEIGHT])
            self.image.fill(self.game_window.colors[4])  # blue
            self.speed = 5

        else:
            self.image = pygame.Surface([self.PADDLE_WIDTH, self.PADDLE_HEIGHT + 25])
            self.image.fill(self.game_window.colors[5])  # deep pink
            self.speed = 6

        self.rect = self.image.get_rect()

        # Set paddle location
        self.rect.centerx = self.game_window.game_surf_rect.right
        self.rect.centerx -= 50
        self.rect.centery = self.game_window.game_surf_rect.centery


    def move(self):
        """ overide of Paddle class move method; tracks ball y-coordinate"""

        # track ball moving toward upper right
        if self.ball.direction == 2:
            if self.rect.y > 5:
                # self.rect.y = self.ball.rect.y
                self.rect.y -= self.speed

        # track ball moving toward lower right
        elif self.ball.direction == 3:
            if self.rect.bottom < self.game_window.height - 5:
                self.rect.y += self.speed + 2
                self.rect.y = self.ball.rect.y