from core import Menu
import pygame

from core.Menu import Menu
from core.GameScreen import GameScreen

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (800, 600))
        pygame.display.set_caption("Click Rush")

        self.running = True
        self.difficult = None


    def run(self):
            menu = Menu(self.window)
            difficult = menu.run()

            print("Dificuldade escolhida", self.difficult)

            if difficult is None:
                pygame.quit()
                return
            print("Dificuldade:", difficult)

            game_screm = GameScreen(self.window, difficult)
            game_screm.run()

            pygame.quit()


