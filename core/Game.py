import pygame
from core.Menu import Menu
from core.GameScreen import GameScreen
from core.ScoreScreen import ScoreScreen
from core.Const import screen_width, screen_height


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Click Rush")

    def run(self):
        difficult = None

        while True:
            # 1. Menu — só exibe se não houver dificuldade já escolhida
            if difficult is None:
                menu = Menu(self.window)
                difficult = menu.run()

                if difficult is None:
                    break  # jogador fechou a janela no menu

            # 2. Partida
            game_screen = GameScreen(self.window, difficult)
            score = game_screen.run()

            if score is None:
                break  # jogador fechou a janela durante a partida

            # 3. Tela de pontuação
            score_screen = ScoreScreen(self.window, score, difficult)
            result = score_screen.run()

            if result == "restart":
                pass           # mantém difficult e volta direto pra partida
            elif result == "menu":
                difficult = None  # limpa dificuldade para exibir o menu
            else:
                break          # jogador fechou a janela na tela de score

        pygame.quit()