import pygame
from lib.config import *
from lib.player import Player
from lib.panel import Panel
from lib.bullet import Bullet
from lib.enemy import Enemy
from lib.enemy_wave import EnemyWave
from lib.button import Button


class Main:

    def __init__(self):
        """
            Classe Principal do jogo
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.wave = 1
        self.change_wave = False



        ##################################
        # Cria o grupo que armazena todas as sprites do jogo
        #
        self.all_sprites = pygame.sprite.Group()
        ###################################
        # Cria o grupo que armazena todos os player do jogo
        #
        self.group_all_players = pygame.sprite.Group()
        ####################################
        # criando o playeyr1 e adicionando
        # o player1 no grupo: self.group_all_players
        #
        self.player1 = Player(self, 30, 200, 30, 30, 5, GREEN)
        self.group_all_players.add(self.player1)
        ####################################
        # adicionando o grupo: self.group_all_players
        # no grupo: self.all_sprites
        #
        self.all_sprites.add(self.group_all_players)

        self.bullets_player_1 = pygame.sprite.Group()


        ############################################
        # Criando o grupo que armazena os inimigos 1
        #
        self.group_enemies1 = pygame.sprite.Group()
        ####################################
        # criando a primeira onda inimiga (testando !!!)
        #
        s = pygame.Surface((30, 30))
        self.wave1 = EnemyWave(self, s, enemies1, 2)
        self.group_enemies1.add(self.wave1.get_wave_enemies())
        self.all_sprites.add(self.group_enemies1)

        self.group_bullets_enemy1 = pygame.sprite.Group()

        ############################################
        # Criando o grupo que armazena os inimigos 2
        #
        self.group_enemies2 = pygame.sprite.Group()
        ####################################
        # criando a primeira onda inimiga (testando !!!)
        #
        # s = pygame.Surface((30, 30))
        # self.wave2 = EnemyWave(s, enemies2, 3)
        # self.group_enemies2.add(self.wave2.get_wave_enemies())
        # self.all_sprites.add(self.group_enemies2)


        ################################
        # Cria o objeto painel do jogo
        #
        self.panel = Panel(0, 0, WIDTH_PANEL, HEIGHT_PANEL)




        ################################
        #
        self.running = True
        #############################
        # chama o loop do jogo
        #
        self.loop()

    def loop(self):
        """
            Método que faz o loop dos objetos do jogo
        """

        while self.running:

            self.screen.fill(RED)

            #########################################
            # Desenha o painel do jogo na parte superior da tela
            #
            self.panel.draw(self.screen)

            ###########################################
            # Desenha as informações do Player no painel (vida, sangue, etc...)
            # no painel superior da tela do jogo.
            #
            self.panel.info_player(self.screen, 5, 5, self.player1.blood, 5, 45, self.player1.life, self.player1.name, self.player1.score)
            self.draw_text(self.screen, 'WAVE: '+str(self.wave), 18, True, WHITE)

            ##########################################
            # Se não houver inimigos no Grupo: self.group_enemies1...
            # e self.wave (número da onda) for igual a 1...
            # Cria a onda 2
            #
            if len(self.group_enemies1) == 0 and self.wave == 1:
                self.wave = 2
                s = pygame.Surface((30, 30))
                self.wave2 = EnemyWave(self, s, enemies2, 2)
                self.group_enemies2.add(self.wave2.get_wave_enemies())
                self.all_sprites.add(self.group_enemies2)




            #################################
            # evento para fechar a janela do jogo
            #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                    pygame.quit()



            ################################
            # Desenha os objetos do jogo na tela do Pygame
            #
            self.draw()

            ################################
            # atualiza os objetos do jogo na tela do Pygame
            #
            self.update()


            pygame.display.update()
            self.clock.tick(FPS)

    def draw(self):
        """
            Método que desenha os objetos do jogo
        """
        ################################
        # Desenha todos os objetos do jogo na tela do Pygame
        #
        self.all_sprites.draw(self.screen)


    def update(self):
        """
            Método que atualiza os objetos do jogo
        """
        ################################
        # atualiza os objetos do jogo na tela do Pygame
        #
        self.all_sprites.update()

    def draw_text(self, screen, text, size, anti_aliasing, color):
        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, size)
        render = font.render(text, anti_aliasing, color)
        font_size = font.size(default_font)
        x = (WIDTH / 2) - font_size[0] / 4
        screen.blit(render, (x, 50))

# if __name__ == '__main__':
#     Main()
