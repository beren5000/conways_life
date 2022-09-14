import sys
import time

import pygame

from life.game import Life
from life.boards import CellStatus


class Renderer:
    def __init__(self, game: Life, width: int = 600, height: int = 400, cycle_time: float = 0.1):
        pygame.init()
        self.game = game
        self.screen = pygame.display.set_mode((width, height))
        self.cell_width = self.screen.get_width() / game.get_board().width
        self.cell_height = self.screen.get_height() / game.get_board().height
        self.border_size = 2
        self.cycle_time = cycle_time

    def draw_life_cicle(self):
        for item in iter(self.game.get_board()):
            status = item["status"]
            x = item["index"][0]
            y = item["index"][1]
            if status == CellStatus.ALIVE:
                pygame.draw.rect(
                    self.screen,
                    (255, 0, 255),
                    (x * self.cell_width + self.border_size, y * self.cell_height + self.border_size, self.cell_width - self.border_size, self.cell_height - self.border_size)
                )

    def run(self):
        while True:
            if pygame.QUIT in [e.type for e in pygame.event.get()]:
                sys.exit(0)
            self.screen.fill((255, 255, 255))
            self.draw_life_cicle()
            self.game.cycle()
            pygame.display.flip()
            time.sleep(self.cycle_time)


