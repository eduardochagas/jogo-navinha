import pygame


class Panel:

    def __init__(self, x, y, width, height, color=(75, 54, 33)):
        """
            Classe que cria o Painel do jogo !!!
        """
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        """
            método que desenha o fundo do painel na tela do Pygame
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))#, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])

    def info_player(self, screen, posX, posYdrawlife, blood_player, \
                    posXblood, posYblood, playerlifes, namePlayer, scorePlayer):
        """
            método que desenha no painel do jogo todas as informações do Player
        """

        #################################
        # Desenha as vidas do Player
        #
        self._draw_lifes(screen, playerlifes, posX, posYdrawlife)
        ###############################
        # retorna a área retângular do sangue do player
        #
        rect = self._draw_bar_blood(screen, blood_player, posX, posYblood)
        #####################################
        # Desenha o nome do Player no Painel do jogo
        #
        y = self._draw_text_player(rect, posX, namePlayer, screen)

        self._text_score_player(y, posX, screen, scorePlayer)



        # ################################################
        # # pega a posição inicial no eixo y onde está
        # # o sangue do player
        # #
        # size_height_blood_bar = (rect.y + rect.height)
        # ###############################
        # # valor da distância entre o sangue do player e
        # # o nome do player
        # distance = 10
        # #########################
        # # variável y que armazena o tamanho da altura do sangue
        # # do player, mais a distância (o vão) entre o sangue do player e
        # # o nome do player
        # #
        # y = size_height_blood_bar + distance
        #
        # default_font = pygame.font.get_default_font()
        # font = pygame.font.Font(default_font, 20)
        # render = font.render('Player1', False, (200, 200, 0))
        # screen.blit(render, (rect.x, y))

    def _draw_lifes(self, screen, player_lifes, posXdrawlife, posYdrawlife):
        """
            Método que desenha as vidas do Player
        """
        surf = pygame.Surface((30, 30))
        surf.fill((220, 200, 0))
        rect = surf.get_rect()
        rect.x = posXdrawlife
        rect.y = posYdrawlife
        for life in range(player_lifes):
            screen.blit(surf, (rect.x + (rect.width + 5) * life, rect.y))

    def _draw_bar_blood(self, screen, blood_player, posXdrawblod, posYdrawblod):
        """
            Método que desenha a barra de sangue do Player no painel do jogo
        """
        ##########################
        # Define o tamanho da barra de sangue do player
        #
        BAR = 100
        #################################
        # Define a porcentagem de sangue do player
        #
        BLOOD_BAR = BAR * blood_player / 100
        #############################################
        # Cria a barra de sangue do player
        #
        rect = pygame.Rect(posXdrawblod, posYdrawblod, BLOOD_BAR, 15)
        ###############################################
        # Desenha a barra de sangue do player
        #
        pygame.draw.rect(screen, (0, 200, 0), rect)
        ###############################################
        # Desenha o contorno da barra de sangue do player
        #
        pygame.draw.rect(screen, (200, 200, 0), pygame.Rect(posXdrawblod, posYdrawblod, BAR, 15), 2)
        # retorna a área retângular do sangue do player
        #
        return rect



    def _draw_text_player(self, rect, posX, namePlayer, screen):
        """
            Método que desenha o texto do Player no painel do jogo
        """

        ###############################
        # armazena o gap (o vão na posição x) definido
        # para cada objeto criado no painel (vidas, sangue do player, etc...)
        x = posX

        ################################################
        # pega a posição inicial no eixo y onde está
        # o sangue do player
        #
        size_height_blood_bar = (rect.y + rect.height)
        print(size_height_blood_bar)
        ###############################
        # valor da distância entre o sangue do player e
        # o nome do player
        distance = 10
        #########################
        # variável y que armazena o tamanho da altura da área retângular
        # do sangue do player, mais a distância (o vão) entre
        # o sangue do player e o nome do player
        #
        y = size_height_blood_bar + distance

        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, 18)
        render = font.render('Player1', False, (200, 200, 0))
        rect = render.get_rect()
        ###############################
        # adicionamos o valor do vão (gap) definido
        # para cada um dos objetos (vida do player,
        # sangue do player, etc...), no x do texto
        #
        rect.x += x
        screen.blit(render, (rect.x, y))

        ######################################
        # Pega o tamanho da fonte...
        #
        size_font = font.size(default_font)
        #######################################
        # armazena o tamanho da fonte mais
        height_font = size_font[1] + y
        ####################################
        # Retorna o tamanho da fonte junto com o tamanho do vao no eixo y
        return height_font

    def _text_score_player(self, height_size_text_player, posX, screen, score):
        """
            Método que desenha os pontos do Player no painel do jogo.
        """

        ###############################
        # armazena o gap (o vão na posição x) definido
        # para cada objeto criado no painel (vidas,
        # sangue do player, texto nome do player, etc...)
        x = posX

        ################################################
        # pega a posição inicial no eixo y onde está
        # o sangue do player
        #
        # size_height_score_player = (y_draw_text_player + rect.height)
        # print(size_height_text_player)
        ###############################
        # valor da distância entre o sangue do player e
        # o nome do player
        distance = 10
        #########################
        # variável y que armazena o tamanho da altura do sangue
        # do player, mais a distância (o vão) entre o sangue do player e
        # o nome do player
        #
        height = height_size_text_player + distance


        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, 16)
        render = font.render('Score: '+str(score), False, (200, 200, 0))
        rect = render.get_rect()
        ###############################
        # adicionamos o valor do vão (gap) definido
        # para cada um dos objetos (vida do player,
        # sangue do player, etc...), no x do texto score
        #
        rect.x += x
        #############################
        # adicionamos o valor do tamanho da altura
        # do nome do player, no y do retângulo do texto score.
        #
        y = rect.y + height
        screen.blit(render, (rect.x, y))


    def draw_text(self, screen, text, size, anti_aliasing, color):
        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, size)
        render = font.render(text, anti_aliasing, color)
        screen.blit(render, (100, 50))
