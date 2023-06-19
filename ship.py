import pygame


class Ship:
    def __init__(self, ai_game) -> None:
        # inicializa la nave en la posicion correspondiente
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # carga la imagen y obtiene ssu rectangulo
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()

        # inicia cada nueva nave en la parte baja central de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # almacena un valor decimal para la posicion horizontal de la nave
        self.x = float(self.rect.x)

        # bandera de movimiento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # actualizar la posicion de la nave basada en el movimiento de la bandera
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # self.rect.x = self.x

    def blitme(self):
        # dibuja la nave en su ubicacion actual
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)