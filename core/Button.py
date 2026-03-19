import pygame

class Button:
    def __init__(self, text, x, y, width, height, color):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.text = text
        self.base_color = color
        self.color_hover = (50,205,50)
        self.color_click = (0,100,0)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 36)
        self.hovered = None
        self.clicked = None
        self.border_radius = 10

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        # seleciona a cor
        if self.clicked:
            color_to_draw = self.color_click
        elif self.hovered:
            color_to_draw = self.color_hover
        else:
            color_to_draw = self.base_color

        # desenha o botão com bordas arredondadas
        pygame.draw.rect(window, color_to_draw, self.rect, border_radius=self.border_radius)

        # desenha o texto centralizado
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        window.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)