import pygame
from core.Const import colorEasyBtn, colorMediumBtn, colorDifficultBtn, screen_width, screen_height
from core.Button import Button

class Menu:
    def __init__(self, window):
        self.window = window

        # fundo
        self.background = pygame.image.load("./assets/images/menu2.png").convert_alpha()
        window_width, window_height = self.window.get_size()
        self.background = pygame.transform.scale(self.background, (window_width, window_height))
        self.rect = self.background.get_rect(left=0, top=0)

        # fonte
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

        # botões centralizados
        center_x = window_width // 2
        self.easy_btn = Button("Facil", center_x, 250, 200, 60, colorEasyBtn)
        self.medium_btn = Button("Medio", center_x, 350, 200, 60, colorMediumBtn)
        self.hard_btn = Button("Dificil", center_x, 450, 200, 60, colorDifficultBtn)

    def render(self):
        """Desenha fundo, botões e textos"""
        self.window.fill((0, 0, 0))
        self.window.blit(self.background, self.rect)

        # desenha botões
        self.easy_btn.draw(self.window)
        self.medium_btn.draw(self.window)
        self.hard_btn.draw(self.window)

        # texto centralizado com sombra
        text = "Escolha uma Dificuldade"
        shadow_surface = self.font.render(text, True, (0, 0, 0))
        text_surface = self.font.render(text, True, (255, 255, 255))
        x = self.window.get_width() // 2
        y = 150
        self.window.blit(shadow_surface, (x - shadow_surface.get_width()//2 + 2, y + 2))
        self.window.blit(text_surface, (x - text_surface.get_width()//2, y))

        #aqui
        font_text = pygame.font.SysFont("Arial",  20, True)
        instru_text = font_text.render("Para capturar o Beagle, click nele com qualquer botão do Mouse", True, (70,130,180))
        text_rect = instru_text.get_rect()
        self.window.blit(instru_text, (0, screen_height - text_rect.height - 10))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_btn.is_clicked(event.pos):
                        return "Facil"
                    if self.medium_btn.is_clicked(event.pos):
                        return "Medio"
                    if self.hard_btn.is_clicked(event.pos):
                        return "Dificil"

            self.render()