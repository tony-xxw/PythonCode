class GameStats():
    '''跟踪游戏统计信息'''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limt  # 剩余可用数量
        self.score = 0
