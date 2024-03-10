
import sys
from time import sleep
import pygame
import json
from alien import Alien

from bullet import Bullet


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb):
    '''响应键盘鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_events(event, ai_settings, screen,
                             ship, bullets, True, stats)

        elif event.type == pygame.KEYUP:
            check_key_events(event, ai_settings, screen,
                             ship, bullets, False, stats)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                              ship, aliens, bullets, mouse_x, mouse_y, sb)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        ai_settings.initialize_dynamic_settings()

        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_key_events(event, ai_settings, screen, ship, bullets, is_right, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = is_right
    if event.key == pygame.K_LEFT:
        ship.moving_left = is_right

    if event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

    if event.key == pygame.K_q:
        save_game_score(stats)
        sys.exit()


def update_bullets(aliens, ai_settings, screen, ship, bullets, stats, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if (len(aliens) == 0):
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        sb.prep_level()


def update_screen(ai_settings, screen, stats, ship, alien, bulltes, play_button, sb):
    '''更新屏幕节目，更新屏幕图像，切换到新的屏幕'''
    screen.fill(ai_settings.bg_color)
    for bullte in bulltes.sprites():
        bullte.draw_bullet()
    ship.blitme()

    alien.draw(screen)

    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    # 绘制的屏幕可见
    pygame.display.flip()


def create_fleet(ai_settings, screen, ship, aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    # 获取一行可以创建多少个外星人
    number_alien_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    avliable_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(avliable_space_x/(2*alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                         (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width * alien_number
    alien.rect.x = alien.x

    # 设置飞船的y坐标
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number

    aliens.add(alien)

# 外星人移动 - 检查是否有外星人位于边缘


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """更新外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


# 检查,如果有外星人到达边缘是,改变移动方向,并向下移动外星人
def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时,采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_fleet_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移,并改变左右移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):

    if stats.ships_left > 0:
        stats.ships_left -= 1  # 玩家可用飞船个数-1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def save_game_score(stats):
    """保存游戏最高分"""
    data = {}
    data["high_score"] = stats.high_score
    with open("game_data.json", w) as fobj:
        json.dump(data, fobj)


def read_game_score(stats):
    """读取游戏最高得分记录"""
    file_name = "game_data.json"
    try:
        with open(file_name) as fobj:
            data = json.load(fobj)
            if data:
                high_score = data["high_score"]
                stats.high_score = high_score
                print(high_score)
    except FileNotFoundError:
        print("no high_score record")
