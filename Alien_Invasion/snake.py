import pygame
class Snake:
    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/snake_right.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right:
            self.rect.x += 1
            self.image = pygame.image.load('images/snake_right.png')
        elif self.moving_left:
            self.rect.x -= 1
            self.image = pygame.image.load('images/snake_left.png')
        elif self.moving_up:
            self.rect.y -= 1
            self.image = pygame.image.load('images/snake_up.png')
        elif self.moving_down:
            self.rect.y += 1
            self.image = pygame.image.load('images/snake_down.png')

    def blitme(self):
        self.screen.blit(self.image,self.rect)