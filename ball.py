"""Module defining Ball class."""
import pygame
from window import Window
from random import randint


class Ball(pygame.sprite.Sprite):
    """ Ball class to store ball state/behavior """

    UPLEFT = 0
    DOWNLEFT = 1
    UPRIGHT = 2
    DOWNRIGHT = 3

    def __init__(self, color: tuple, window: Window):
        """ constructor to initialize ball object
        :param color: A tuple representing an RGB color value; used to fill Ball object rectangle
        :param window: The game window object; passed from the Pong class
        """
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.ball_radius = 10
        self.game_window = window
        self.image = pygame.Surface([self.ball_radius, self.ball_radius])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game_window.game_surf_rect.centerx
        self.rect.centery = self.game_window.game_surf_rect.centery
        self.direction = randint(0, 3)
        self.speed = 4


    def move(self):
        if self.direction == self.UPLEFT:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.direction == self.UPRIGHT:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.direction == self.DOWNLEFT:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif self.direction == self.DOWNRIGHT:
            self.rect.x += self.speed
            self.rect.y += self.speed


    def change_direction(self):
        if self.rect.y < 0 and self.direction == self.UPLEFT:
            self.direction = self.DOWNLEFT
        if self.rect.y < 0 and self.direction == self.UPRIGHT:
            self.direction = self.DOWNRIGHT
        if self.rect.y > self.game_window.game_surf_rect.bottom \
                and self.direction == self.DOWNLEFT:
            self.direction = self.UPLEFT
        if self.rect.y > self.game_window.game_surf_rect.bottom \
                and self.direction == self.DOWNRIGHT:
            self.direction = self.UPRIGHT
