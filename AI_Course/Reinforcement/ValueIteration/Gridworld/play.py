import numpy as np
import pygame
import Gridworld.game as game


class Play(game.GridWorld):

    def __init__(self, envi=None, table=None, size=None):
        super().__init__(envi=None, table=None, size=None)

    def play(self, visual):
        pygame.display.set_caption(f"GridWorld {self.env_len}x{self.env_len}")
        while self.run:
            state = self.reset()
            while not self.over:
                self.draw_border()
                if visual:
                    self.draw_game_visual()
                else:
                    self.draw_game_non_visual()
                action = self.get_action(state)
                state = self.move(action)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        self.over = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_f]:
                    self.run = False
                    self.over = False
        pygame.display.quit()

    def get_action(self, state):
        pass

    def show_env(self):
        pygame.display.set_caption(f"GridWorld {self.env_len}x{self.env_len}")
        while self.run:
            self.draw_border()
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                self.run = False
                outer_run = False
        pygame.display.quit()
