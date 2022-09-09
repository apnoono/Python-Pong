"""Module defining Window class."""
import pygame
import os

# define game icon
DEFAULT_ICON = os.path.relpath("images/DEFAULT_ICON.png")
icon_surf = pygame.image.load(DEFAULT_ICON)
pygame.display.set_icon(icon_surf)


class Window:
    """ Class to maintain consistent state of the game window"""
    _WHITE = (255, 255, 255) # 0
    _RED = (255, 0, 0) # 1
    _GREEN = (0, 255, 0) # 2
    _BLACK = (0, 0, 0) # 3
    _BLUE = (0, 0, 255) # 4
    _PINK = (255, 20, 147) # 5
    _SMOOTH_BLACK = (33, 33, 33) # 6
    _DARK_ORANGE = (255, 140, 0) # 7
    _INDIGO = (75, 0, 130) # 8
    _DARK_VIOLET = (148, 0, 211) # 9
    _PALETTE = [_WHITE, _RED, _GREEN, _BLACK, _BLUE, _PINK, _SMOOTH_BLACK, _DARK_ORANGE, _INDIGO, _DARK_VIOLET]

    def __init__(self):
        pygame.init()
        self.caption = 'Top Coder Pong'
        self.colors = self._PALETTE
        pygame.display.set_caption(self.caption)

        # game window dimensions
        self.width = 600
        self.height = 400

        # game window
        self.game_surf = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.game_surf_rect = self.game_surf.get_rect()

