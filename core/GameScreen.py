import pygame

from core.Const import screen_width, screen_height
from core.Target import Target


class GameScreen:
    def __init__(self, window, difficult):
        self.window = window
        self.difficult = difficult

        self.running = True
        self.targets = []
        self.score = 0

        self.clock = pygame.time.Clock()
        self.spawn_timer = pygame.time.get_ticks()

        # tempo do jogo
        self.start_time = pygame.time.get_ticks()
        self.game_duration = 60000  # 1 minuto

        #fundo
        self.background = pygame.image.load("assets/images/menu2.png").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))

        # configurações por dificuldade
        self.settings = {
            "Facil": 1500,
            "Medio": 1000,
            "Dificil": 600
        }

    def spawn_target(self):
        new_target = Target(pygame.image.load("assets/images/beagle.png").convert_alpha())

        # define tempo de vida baseado na dificuldade
        new_target.lifetime = self.settings[self.difficult]
        self.targets.append(new_target)

    def run(self):
        spawn_interval = self.settings[self.difficult]

        while self.running:
            now = pygame.time.get_ticks()

            # fim do jogo
            if now - self.start_time > self.game_duration:
                self.running = False
                return

            # eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for target in self.targets[:]:
                        if target.is_clicked(event.pos):
                            self.targets.remove(target)
                            self.score += 1

            # remover alvos expirados
            for target in self.targets[:]:
                if target.is_expired():
                    self.targets.remove(target)

            #  spawn (SOMENTE UMA VEZ, fora do loop de eventos)
            if now - self.spawn_timer > spawn_interval:
                self.spawn_target()
                self.spawn_timer = now

            #  desenho (ordem correta!)
            self.window.blit(self.background, (0, 0))  # fundo primeiro

            for target in self.targets:
                target.draw(self.window)

            #  UI
            font = pygame.font.SysFont(None, 36)

            score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))

            time_left = max(0, (self.game_duration - (now - self.start_time)) // 1000)
            time_text = font.render(f"Tempo: {time_left}", True, (255, 255, 255))
            self.window.blit(time_text, (650, 10))



            pygame.display.update()
            self.clock.tick(60)