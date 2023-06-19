class Settings:
    def __init__(self) -> None:
        # settings de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (26, 155, 232)

        # settings de la nave
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullets settings
        self.bullets_speed = 1.5
        self.bullets_width = 3
        self.bullets_height = 15
        self.bullets_color = (60, 60, 60)
        self.bullets_allowed = 3

        # aliens settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet direction
        self.fleet_direction = 1
        