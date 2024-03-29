

import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # 加载外新人图片
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 初始化外新人位置
        self.rect.x = self.rect.width
        self.rect.y = 0

        # 存储外星人位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_fleet_edges(self):
        """如果外星人位于屏幕的边缘,返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
