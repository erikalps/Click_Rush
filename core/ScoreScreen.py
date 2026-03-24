import pygame
from core.Const import screen_width, screen_height
from core.Button import Button


class ScoreScreen:
    def __init__(self, window, score, difficult):
        self.window = window
        self.score = score
        self.difficult = difficult
        self.result = None  # "menu" ou "restart"

        # Fundo
        self.background = pygame.image.load("assets/images/menu2.png").convert()
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

        # Fontes
        self.font_title = pygame.font.SysFont("Arial", 64, bold=True)
        self.font_score = pygame.font.SysFont("Arial", 48)
        self.font_msg   = pygame.font.SysFont("Arial", 28)

        # Botões
        cx = screen_width // 2
        self.btn_restart = Button("Jogar Novamente", cx - 120, 450, 220, 55, pygame.Color(34, 139, 34))
        self.btn_menu    = Button("Menu Principal",  cx + 120, 450, 220, 55, pygame.Color(178, 34, 34))

    def _get_message(self):
        """Retorna uma mensagem baseada na pontuação e dificuldade."""
        thresholds = {"Facil": (10, 20), "Medio": (7, 15), "Dificil": (5, 10)}
        low, high = thresholds.get(self.difficult, (5, 10))

        if self.score >= high:
            return "Incrivel! Voce e um mestre!"
        elif self.score >= low:
            return "Bom trabalho! Continue treinando!"
        else:
            return "Nao desista, tente de novo!"

    def _draw_text_centered(self, text, font, color, y, shadow=False):
        """Desenha texto centralizado horizontalmente, com sombra opcional."""
        cx = screen_width // 2
        surf = font.render(text, True, color)
        if shadow:
            shadow_surf = font.render(text, True, (80, 80, 80))
            self.window.blit(shadow_surf, (cx - surf.get_width() // 2 + 3, y + 3))
        self.window.blit(surf, (cx - surf.get_width() // 2, y))

    def render(self):
        self.window.blit(self.background, (0, 0))

        # Painel semi-transparente para destacar o conteúdo
        panel = pygame.Surface((500, 360), pygame.SRCALPHA)
        panel.fill((255, 255, 255, 180))
        self.window.blit(panel, (screen_width // 2 - 250, 130))

        # Título — mais abaixo (y=150 em vez de 100)
        self._draw_text_centered("Fim de Jogo!", self.font_title, (20, 20, 20), 150, shadow=True)

        # Score — preto
        self._draw_text_centered(f"Pontuacao: {self.score}", self.font_score, (10, 10, 10), 240)

        # Dificuldade — preto
        self._draw_text_centered(f"Dificuldade: {self.difficult}", self.font_msg, (10, 10, 10), 310)

        # Mensagem motivacional — preto
        self._draw_text_centered(self._get_message(), self.font_msg, (10, 10, 10), 355)

        # Botões
        self.btn_restart.draw(self.window)
        self.btn_menu.draw(self.window)

        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.btn_restart.is_clicked(event.pos):
                        return "restart"
                    if self.btn_menu.is_clicked(event.pos):
                        return "menu"

            self.render()
            clock.tick(60)