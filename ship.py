import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.move_step = 10
        self.moving_left = False
        self.moving_right = False

        # 飞船放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.centerx -= self.move_step
            if self.rect.centerx < 0:
                self.rect.centerx = 0
        if self.moving_right:
            self.rect.centerx += self.move_step
            if self.rect.centerx > self.screen_rect.right:
                self.rect.centerx = self.screen_rect.right

    def center_ship(self):
        self.center = self.screen_rect.centerx
