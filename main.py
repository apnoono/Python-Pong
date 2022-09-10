import pygame, sys
from pygame.locals import *
from window import Window
from ball import Ball
from random import randint
from pong import Pong
from pong2P import Pong2P

"""
Requirements

[+] One player version and two player version
[+] One player version will have two difficulties. Easy and Hard.
[-] Depending on which version the user picks the computer will be harder or easier to beat.
[+] Two player version will be using the same key board.
[+] Player one will be using key "w" to move the paddle up and "x" to move the paddle down
[|] Player two will be using key "p" to move the paddle up and ">" to move the paddle down
[+] The winner will be the first to 10 points.
[+] After there is a winner create a alert that states who won the game.
[+] Use the language of your choice and place it in the readme file
[+] You must include a README.md file with instructions on how to install/run your code.
[-] You must include a video (annotated or narrated) demo of your code
[+] Grading will not be based on UI/UX but a good presentation will be appreciated
[+] You must provide comments to what your methods/code are accomplishing

"""
pygame.init()


# global
clock = pygame.time.Clock()
solo = True
mode = "EASY"
game_window = Window()

def text_objects(text, font):
    text_surf = font.render(text, True, game_window._GREEN)
    return text_surf, text_surf.get_rect()


def game_intro(window):
    """Display a simple title screen with instructional text"""
    intro = True
    ball1 = Ball(window.colors[2], window)
    ball2 = Ball(window._DARK_VIOLET, window)
    ball3 = Ball(window._RED, window)
    ball4 = Ball(window._WHITE, window)
    balls = [ball1, ball2, ball3, ball4]
    ball_sprites = pygame.sprite.RenderPlain(ball1, ball2, ball3, ball4)

    while intro:

        # if the balls travel to screen edge, reset to center with random direction
        for ball in balls:
            if ball.rect.x > window.width:
                ball.rect.centerx = window.game_surf_rect.centerx
                ball.rect.centery = window.game_surf_rect.centery
                ball.direction = randint(0, 1)
            elif ball.rect.x < 0:
                ball.rect.centerx = window.game_surf_rect.centerx
                ball.rect.centery = window.game_surf_rect.centery
                ball.direction = randint(2, 3)
                ball.speed += 1

            if ball.speed == 5:
                ball.speed = 1

        # event listener loop for exit/start key press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        window.game_surf.fill(window.colors[6])
        title_font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 40)
        title_text_surf, title_text_rect = text_objects("TOP CODER PONG", title_font)
        title_text_rect.center = ((window.width // 2), (window.height // 2))

        small_font = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 12)
        sub_text_surf, sub_text_rect = text_objects("[w] UP [s] DOWN [SPACE] START [ESC] QUIT", small_font)
        sub_text_rect.center = ((window.width // 2), (window.game_surf_rect.bottom - 20))

        window.game_surf.blit(title_text_surf, title_text_rect)
        window.game_surf.blit(sub_text_surf, sub_text_rect)

        # Render ball objects on title screen
        ball_sprites.draw(window.game_surf)
        for ball in balls:
            ball.move()
            ball.change_direction()

        pygame.display.update()
        clock.tick(60)


def game_option(window):
    """ function to select difficulty"""
    # TODO: implement GUI for user to set game options instead of digging through API
    #       - ball speed
    #       - difficulty
    #       - 1 or 2 player game
    #       - color
    #       - controls
    pass


def game_end(player, window):
    """ function to display game winner

    :param player: the winning player retured from the Pong or Pong2P loop
    :param window: the game window on which to render text elements
    """

    end = True
    game_over_text = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 40)
    game_over_small_text = pygame.font.Font('fonts/PressStart2P-Regular.ttf', 20)

    while end:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    end = False
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        window.game_surf.fill(window._BLACK)

        game_over = game_over_text.render("GAME OVER", True, window._WHITE, window._BLACK)
        if player == 1:
            sub_message = game_over_small_text.render("Player 1 Wins", True, window._WHITE, window._BLACK)
        else:
            sub_message = game_over_small_text.render("Player 2 Wins", True, window._WHITE, window._BLACK)

        game_over_rect = game_over.get_rect()
        game_over_rect.centerx = window.game_surf_rect.centerx
        game_over_rect.centery = window.game_surf_rect.centery - 50
        game_over1_rect = sub_message.get_rect()
        game_over1_rect.centerx = game_over_rect.centerx
        game_over1_rect.centery = game_over_rect.centery + 75

        window.game_surf.blit(game_over, game_over_rect)
        window.game_surf.blit(sub_message, game_over1_rect)

        pygame.display.update()
        clock.tick(1)


def main(window):
    """ main program entry point

    Returns: None
    """
    while True:
        game_intro(game_window)
        # game_option(game_window)
        if solo:
            game = Pong(mode, game_window)
        else:
            game = Pong2P(game_window)
        winner = game.loop()
        game_end(winner, game_window)


if __name__ == "__main__":
    main(game_window)