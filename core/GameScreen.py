import pygame
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

        # configurações por dificuldade
        self.settings = {
            "Facil": 1500,
            "Medio": 1000,
            "Dificil": 600
        }

    def spawn_target(self):
        new_target = Target(pygame.image.load("assets/images/beagle.png").convert_alpha())
        self.targets.append(new_target)

    def run(self):
        spawn_interval = self.settings[self.difficult]

        while self.running:
            now = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for target in self.targets[:]:
                        if target.is_clicked(event.pos):
                            self.targets.remove(target)
                            self.score += 1

            # spawn de targets
            if now - self.spawn_timer > spawn_interval:
                self.spawn_target()
                self.spawn_timer = now

            # desenho
            self.window.fill((0, 0, 0))

            for target in self.targets:
                target.draw(self.window)

            # score
            font = pygame.font.SysFont(None, 36)
            score_text = font.render(f"Score: {self.score}", True, (255,255,255))
            self.window.blit(score_text, (10, 10))

            pygame.display.update()
            self.clock.tick(60)