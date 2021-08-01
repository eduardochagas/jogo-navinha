import pygame
import time

class Entity(pygame.sprite.Sprite):

    def __init__(self, posX, posY, width, height, speed, color):
        pygame.sprite.Sprite.__init__(self)
        """
            Classe ABSTRATA que reune todas as caracteristicas em comum
            de um personagem do jogo
        """

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(posX, posY)
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.velocity = pygame.math.Vector2(0, 0)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = speed
        self.last_time = time.time()
        self.blood = 100


    def update(self):
        pass
