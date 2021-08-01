import pygame
from lib.config import *
from lib.button import Button
from main import Main

class Menu:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        ###################################
        # Cria o fundo Verde da tela inicial...
        #
        self.background = pygame.Surface((WIDTH, HEIGHT))
        self.background.fill(GREEN)
        self.screen.blit(self.background, (0, 0))

        #############################################
        # Cria a instância do botão da tela...
        #
        self.button_start = Button(self.screen, WIDTH/2, HEIGHT/2, 100, 50, 'Start', 15, True)
        ########################################
        # Desenha o botao na tela inicial...
        #
        pygame.draw.rect(self.screen, (0, 150, 150), self.button_start.rect)
        self.button_start.text_button(self.screen, 'START', 15, True, (0, 0, 0))


        self.running = True
        self.loop()

    def loop(self):

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Main()


            #########################################
            # sempre atualizando e btendo a posição x,y do mouse...
            #
            self.mouse_pos = pygame.mouse.get_pos()



            ###################################################
            # Verifica se o botão foi pressionado com o mouse...
            #
            if self.button_start.pressed_button(self.mouse_pos):
                Main()


            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    Menu()
