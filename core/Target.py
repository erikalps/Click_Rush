import pygame
import random

class Target:
    def __init__(self, image, x=None, y=None):
        self.image = pygame.transform.scale(image, (77, 34))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # posição aleatória se não passar
        self.x = x if x is not None else random.randint(0, 800 - self.width)
        self.y = y if y is not None else random.randint(0, 600 - self.height)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)