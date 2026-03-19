import pygame
import random

class Target:
    def __init__(self, image, x=None, y=None):
        self.image = pygame.transform.scale(image, (100, 80))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # posição aleatória
        self.x = x if x is not None else random.randint(0, 800 - self.width)
        self.y = y if y is not None else random.randint(0, 600 - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # tempo de vida
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000  # valor padrão (vai ser sobrescrito)


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        mx, my = mouse_pos
        return (
                self.x <= mx <= self.x + self.width and
                self.y <= my <= self.y + self.height
        )

    def is_expired(self):
        now = pygame.time.get_ticks()
        return now - self.spawn_time >= self.lifetime