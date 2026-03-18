import pygame
import pygame.image
from core.Const import colorDifficultBtn, colorEasyBtn,colorMediumBtn

from core.Button import Button


class Menu:
    def __init__(self, window):
        self.window = window

        #carrega a imagem
        self.surf = pygame.image.load("./assets/images/menu2.png").convert_alpha()
        window_width = self.window.get_width()
        window_height = self.window.get_height()
        self.surf = pygame.transform.scale(self.surf, (window_width, window_height))
        self.rect = self.surf.get_rect(left = 0, top = 0)


    def run(self,):

        #botões para cada dificuldade
        easy_btn = Button("Facil", x = 100, y = 100, width = 150, height = 80, color = colorEasyBtn)
        medium_btn = Button("Medio", x = 100, y = 200, width= 150, height = 80, color = colorMediumBtn)
        hard_btn = Button("Dificil", x = 100, y = 300, width = 150, height = 80, color = colorDifficultBtn)


        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return None #jogador fechou a janela

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_btn.is_clicked(event.pos):
                        return "Facil"
                    if medium_btn.is_clicked(event.pos):
                        return "Medio"
                    if hard_btn.is_clicked(event.pos):
                        return "Dificil"



            self.window.fill((0, 0, 0))
            self.window.blit(self.surf, self.rect)
            easy_btn.draw(self.window)
            medium_btn.draw(self.window)
            hard_btn.draw(self.window)

            pygame.display.flip() #atualiza a tela


