import pygame
from .config import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self, obj, pos, width, height, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        """
            Classe usada para criar as balas dos personagens do jogo
        """

        self.obj = obj
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 5

    def update(self):
        
        if self.obj.name == 'Player':
            self.rect.x += self.speed
            if self.rect.right > WIDTH:
                self.kill()
                print('apagou !!!')
        elif self.obj.name == 'Enemy':
            self.rect.x -= self.speed
            if self.rect.left < 0:
                self.kill()
