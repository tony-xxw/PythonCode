
import pygame

import game_functions as gf

from button import Button

from game_stats import GameStats

from setting import Settings

from ship import Ship

from pygame.sprite import Group

from scoreboard import Scoreboard

from game_stats import GameStats


def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()

    ai_settings = Settings()
 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建飞船
    ship = Ship(ai_settings,screen)

    # 创建外星人数组
    aliens = Group()

    bullets = Group()

    stats = GameStats(ai_settings)

    play_button = Button(ai_settings, screen, "Play")
    # 函数导入
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 设置标题  
    pygame.display.set_caption(ai_settings.title)
    # 创建用于存储游戏状态统计的实例
    stats = GameStats(ai_settings)

    gf.read_game_score(stats)

    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats,play_button, ship, aliens, bullets,sb)
        
        if stats.game_active:

            ship.update()

            gf.update_bullets(aliens, ai_settings, screen, ship, bullets,stats,sb)

            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets,sb)

        gf.update_screen(ai_settings, screen, stats, ship,aliens, bullets, play_button,sb)


run_game()
