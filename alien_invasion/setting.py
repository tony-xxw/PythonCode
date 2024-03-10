# _*_ coding: utf-8 _*_
class Settings():

    def __init__(self):
        '''初始化游戏设置'''
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

		# 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
		
		#限制子弹的数量
        self.bullets_allowed = 10 

		#设置外星人移动速度
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10 #撞到屏幕边缘后向下移动
        self.fleet_direction = 1 # 移动方向 1-向右 -1 向左


		# 玩家的飞船设置

        self.ship_speed_factor = 10 #玩家的飞船移动速度
        self.ship_limit = 3 #玩家拥有的飞船数

        # 设置游戏速度加快节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # 外星人分值提高的速度
        self.score_scale = 1.1

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 10

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
