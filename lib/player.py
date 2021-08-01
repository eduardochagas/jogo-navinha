import pygame
import time
from .config import *
from .bullet import Bullet
from .entity import Entity

class Player(Entity):

    def __init__(self, main, posX, posY, width, height, speed, color):
        Entity.__init__(self, posX, posY, width, height, speed, color)
        """
            Classe usada para criar o Player do jogo
        """

        self.main = main
        self.name = 'Player'
        self.life = 4
        self.score = 0
        self.last_time_shot = pygame.time.get_ticks()

    def update(self):
        """
            Método usado para fazer as atualizações das funcionalidades do Player
        """
        self.control()

        ##################################################
        # aplica as velocidades armazenadas em: self.vel_x e self.vel_y
        # quando apertamos as teclas: A, W, S, D.
        self.velocity = pygame.math.Vector2(self.vel_x, self.vel_y)

        #######################################
        # verifica se a velocidade foi aplicada em
        # um dos eixos (x, y) do vetor de velocidade...
        if self.velocity.x != 0 or self.velocity.y != 0:
            self.velocity = self.velocity.normalize()

        #####################################
        # multiplica os eixos normalizados (x,y)
        # no vetor de velocidade com a variável de velocidade...
        self.velocity.x *= self.speed
        self.velocity.y *= self.speed

        ######################################
        # criando o tempo de delta para aplicarmos o deltatime
        # no player
        now = time.time()
        delta = now - self.last_time
        self.last_time = now

        ###############################
        # aplicando o framerate Independente no player
        self.velocity.x *= delta * 60
        self.velocity.y *= delta * 60

        ########################################
        # insere os eixos do vetor normalizado no (x, y)
        # do rect do player
        self.rect.x += self.velocity.x

        self.check_colision('x')

        self.rect.y += self.velocity.y

        ##########################################
        # Verifiica as colisões
        # do lado esquerdo e lado direito da tela com o player
        #
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        #############################################
        # Verifica as colisões
        # do lado de cime e do lado de baixo da tela com o player
        if self.rect.top < HEIGHT_PANEL:
            self.rect.top = HEIGHT_PANEL
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        ###########################################
        # zera as variáveis que atribuimos no vetor de velocidade
        self.vel_x = 0
        self.vel_y = 0


    def check_colision(self, axis):
        """
            Método usado para checagem de colisão dos objetos do jogo com o player
        """

        if axis == 'x':
            hit = pygame.sprite.groupcollide(self.main.bullets_player_1, self.main.group_enemies1, True, True)
            if hit:
                self.score += 10

            hit = pygame.sprite.groupcollide(self.main.bullets_player_1, self.main.group_enemies2, True, True)
            if hit:
                self.score += 10


        if axis == 'y':
            pass



    def control(self):
        """
            Método usado para checagem dos comandos de direção do Player
        """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel_x = -1
        if keys[pygame.K_d]:
            self.vel_x = 1
        if keys[pygame.K_w]:
            self.vel_y = -1
        if keys[pygame.K_s]:
            self.vel_y = 1

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        """
            Método usado para acionar o tiro do player 
        """
        now = pygame.time.get_ticks()
        if now - self.last_time_shot > 400:
            self.last_time_shot = now
            b = Bullet(self, self.rect.midright, 5, 5)
            self.main.bullets_player_1.add(b)
            self.main.all_sprites.add(self.main.bullets_player_1)
