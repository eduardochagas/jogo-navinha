import pygame
from .config import *
from .entity import Entity
from .bullet import Bullet

class Enemy(Entity):

    def __init__(self, main, image, posX, posY, width, height, speed, color):
        Entity.__init__(self, posX, posY, width, height, speed, color)
        """
            Classe usada para criar os inimigos do jogo
        """
        self.name = 'Enemy'
        self.main = main
        self.last_time_shoot = pygame.time.get_ticks()

    def update(self):

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
            print('apagou o inimigo !!!')

        self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_time_shoot > 1500:
            self.last_time_shoot = now
            b = Bullet(self, self.rect.midleft, 5, 5, (255, 255, 0))
            self.main.group_bullets_enemy1.add(b)
            self.main.all_sprites.add(b)
