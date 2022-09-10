"""Module defining Pong class."""
import pygame
import sys
from window import Window
from ball import Ball
from paddle import Paddle
from avatar import Avatar
from random import randint


class Pong:
    clock = pygame.time.Clock()

    """ Pong class defining main game loop. """

    def __init__(self, mode: str, window: Window):
        """

        :param window:
        """
        # pygame.init()
        self.game_window = window
        self.ball = Ball(self.game_window.colors[0], self.game_window)
        self.player1 = Paddle(1, self.game_window)
        self.player2 = Avatar(self.ball, mode, self.game_window)
        self.player1_win = False
        self.player2_win = False
        self.all_sprites = pygame.sprite.RenderPlain(self.ball, self.player1, self.player2)

    def paddle_hit(self):
        """Method to detect ball collisions with paddle objects.
        With each successful hit, the ball speed increments by 1.
        """
        if pygame.sprite.collide_rect(self.ball, self.player2):
            if (self.ball.direction == 2):  # IF upper right...
                self.ball.direction = 0  # THEN change to upper left
            elif (self.ball.direction == 3):  # IF lower right...
                self.ball.direction = 1
            self.ball.speed += 1

        elif pygame.sprite.collide_rect(self.ball, self.player1):
            if (self.ball.direction == 0):
                self.ball.direction = 2
            elif (self.ball.direction == 1):
                self.ball.direction = 3
            self.ball.speed += 1

    def loop(self):
        """game looping construct """
        try:
            score_font = pygame.font.SysFont('Helvetica', 120)
        except Exception as e:
            score_font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 120)
            print("Something happened with the font")
            raise e
        # score, win status variables
        player1_score = 0
        player2_score = 0

        while True:
            self.clock.tick(60)

            # if the ball travels beyond a paddle, reset to the center
            if self.ball.rect.x > self.game_window.width:
                self.ball.rect.centerx = self.game_window.game_surf_rect.centerx
                self.ball.rect.centery = self.game_window.game_surf_rect.centery
                self.ball.direction = randint(0, 1)
                self.ball.speed = 4
            elif self.ball.rect.x < 0:
                self.ball.rect.centerx = self.game_window.game_surf_rect.centerx
                self.ball.rect.centery = self.game_window.game_surf_rect.centery
                self.ball.direction = randint(2, 3)
                self.ball.speed = 4

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # define game exit and movement keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == ord('w'):
                        self.player1.UP1 = True
                        self.player1.DOWN1 = False
                        self.player1.NEUTRAL1 = False
                    elif event.key == ord('s'):
                        self.player1.UP1 = False
                        self.player1.DOWN1 = True
                        self.player1.NEUTRAL1 = False

                elif event.type == pygame.KEYUP:
                    if event.key == ord('w') or event.key == ord('s'):
                        self.player1.NEUTRAL1 = True
                        self.player1.DOWN1 = False
                        self.player1.UP1 = False

            # Update the score board
            score_board = score_font.render(str(player1_score) + "           " + str(player2_score), True,
                                            self.game_window.colors[0], self.game_window.colors[3])
            score_board_rect = score_board.get_rect()
            score_board_rect.centerx = self.game_window.game_surf_rect.centerx
            score_board_rect.y = 10

            self.game_window.game_surf.fill(self.game_window.colors[3])
            self.game_window.game_surf.blit(score_board, score_board_rect)

            self.all_sprites.draw(self.game_window.game_surf)
            self.player1.move()
            self.player2.move()
            self.ball.move()
            self.ball.change_direction()

            self.paddle_hit()

            if self.ball.rect.x > self.game_window.width:
                player1_score += 1
            elif self.ball.rect.x < 0:
                player2_score += 1

            pygame.display.update()

            # check if there is a winner
            if player1_score == 10:
                self.player1_win = True
                return 1
            elif player2_score == 10:
                self.player2_win = True
                return 2

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.game_window.game_surf.fill(self.game_window.colors[3])

            pygame.display.update()
