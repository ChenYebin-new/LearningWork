import sys
import pygame
from settings import Settings
from snake import Snake


class AlienInvasion:

    def __init__(self, ):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.snake = Snake(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.snake.moving_left = True
                elif event.key == pygame.K_UP:
                    self.snake.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.snake.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.snake.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.snake.moving_left = False
                if event.key == pygame.K_UP:
                    self.snake.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.snake.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.snake.blitme()
        pygame.display.flip()
    def run_game(self):
        while True:
            self._check_events()
            self.snake.update()
            self._update_screen()


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
