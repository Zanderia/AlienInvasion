class Settings:
    """Store all the game settings"""

    def __init__(self):
        """"Initialize fixed game settings"""
        # Screen params
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_caption = "Alien Invasion"

        # Ship params
        self.ship_limit = 3

        # Bullet params
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # At any moment on the screen can be a maximum of three bullets
        self.bullet_allowed = 3

        # Alien params
        self.fleet_drop_speed = 10

        # Speed up params
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic game settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # 1 means left direction and -1 means right direction
        self.fleet_direction = 1

        # Score count
        self.alien_point = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_point = int(self.alien_point * self.score_scale)
