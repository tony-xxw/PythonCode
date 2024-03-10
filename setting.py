# _*_ coding: utf-8 _*_
class Settings():

    def __init__(self):
        '''初始化游戏设置'''
        self.title = "ALien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10
        self.alien_speed_factor = 1
        self.ship_limt = 3  # 玩家拥有的飞船数
        self.fleet_drop_speed = 10  # 撞到屏幕边缘后向下移动
        self.fleet_direction = 1  # 移动方向 1-向右 -1 向左

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 10

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
