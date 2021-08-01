import pygame
from .config import *

class Button:

    def __init__(self, screen, x, y, width, height, text, size_font, anti_aliasing, color=(0,200,200)):
        self.screen = screen
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y



    def pressed_button(self, mouse_pos):

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True


    def text_button(self, screen, text, size_font, anti_aliasing, color=(0, 0, 0)):
        default_font = pygame.font.get_default_font()
        font = pygame.font.Font(default_font, size_font)
        render = font.render(text, anti_aliasing, color)
        font_size = font.size(default_font)
        ########################
        # Só para testar a posição do texto do botão mesmo, depois vou inserir uma imagem no botão
        #
        self.screen.blit(render, (self.rect.centerx - font_size[0] / 5, self.rect.centery - font_size[1] / 5))
