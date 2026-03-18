from core import Menu
import pygame

from core.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (800, 600))
        pygame.display.set_caption("Click Rush")

        self.running = True
        self.difficult = None


    def run(self):
            menu = Menu(self.window)
            self.difficult = menu.run()

            print("Dificuldade escolhida", self.difficult)

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False




                self.window.fill((0, 0, 0))
                pygame.display.update()


            pygame.quit()