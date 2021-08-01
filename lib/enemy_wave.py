import pygame
from .config import *
from .enemy import Enemy

class EnemyWave:

    def __init__(self, main, image, array_enemies, speed):
        """
            Classe usada para criar as ondas inimigas do jogo.
        """
        self.main = main
        #############################################
        # array que armazena as posições que os inimigos
        # ficarão na tela
        self.array_enemies = array_enemies
        ########################################
        # array que armazena todos os inimigos
        #
        self.array_wave_enemy = []

        ###########################################
        # armazena a quantidade de inimigos definidos na lista
        space_ship_quantity = len(self.array_enemies)
        for i in range(space_ship_quantity):
            e = Enemy(self.main, image, self.array_enemies[i][0], self.array_enemies[i][1], self.array_enemies[i][2], self.array_enemies[i][3], speed, (200, 200, 0))
            self.array_wave_enemy.append(e) # adiciona os inimigos no array: self.array_wave_enemy


    def get_wave_enemies(self):
        """
            método usado para retornar o array que contêm todos os inimigos da onda inimiga.
        """
        return self.array_wave_enemy
