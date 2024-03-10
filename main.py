import pygame
from button import Button
from game_stats import GameStats

from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    aliens = Group()

    bullets = Group()

    stats = GameStats(ai_settings)

    play_button = Button(ai_settings, screen, "Play")

    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.display.set_caption(ai_settings.title)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,aliens, bullets)
        # 让最近绘制的屏幕可见
        # 设置背景色 灰色
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, ai_settings, screen, ship, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship,
                         aliens, bullets, play_button)


run_game()
