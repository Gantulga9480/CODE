import numpy as np
import os
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
BLUE = (255, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 361
HEIGHT = 361
VEL = 60
SHAPE = 59


def clear():
    os.system("cls")


class GridWorld:

    def __init__(self):
        self.env_column = 6
        self.env_row = 6
        self.env = np.zeros((self.env_row, self.env_column), dtype=int)
        self.agent = [0, 0]
        self.target = [0, 5]
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.q_table = np.load("q_table.npy")

    def play(self):
        while True:
            over = False
            state = self.reset()
            while not over:
                action = np.argmax(self.q_table[state[0]][state[1]])
                state, over = self.move(action)
            if self.target[0] == self.agent[0] and\
                    self.target[1] == self.agent[1]:
                print("Won")
            else:
                print("Over")

    def make_env(self):
        self.env = np.zeros((self.env_row, self.env_column), dtype=int)
        self.env[0][2] = 99
        self.env[1][2] = 99
        self.env[2][2] = 99
        self.env[0][3] = 99
        self.env[1][3] = 99
        self.env[2][3] = 99
        self.env[self.target[0]][self.target[1]] = 8

    def draw_game(self):
        for i in range(7):
            pygame.draw.line(self.win, WHITE, (i*VEL, 0), (i*VEL, 360))
            pygame.draw.line(self.win, WHITE, (0, i*VEL), (360, i*VEL))
        for i in range(self.env_row):
            for j in range(self.env_row):
                if self.env[i][j] == 99:
                    pygame.draw.rect(self.win, RED,
                                     (VEL*j+1, VEL*i+1, SHAPE, SHAPE))
        pygame.draw.rect(self.win, YELLOW,
                         (VEL*self.agent[1]+1,
                          VEL*self.agent[0]+1, SHAPE, SHAPE))
        pygame.draw.rect(self.win, GREEN,
                         (VEL*self.target[1]+1,
                          VEL*self.target[0]+1, SHAPE, SHAPE))

    def reset(self):
        self.make_env()
        self.agent = [0, 0]
        return self.agent.copy()

    def move(self, action):
        over = False
        self.win.fill(BLACK)
        self.draw_game()
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if action == 0:
            self.agent[0] -= 1
        elif action == 1:
            self.agent[0] += 1
        elif action == 2:
            self.agent[1] += 1
        elif action == 3:
            self.agent[1] -= 1
        self.make_env()
        if self.agent[0] < 0 or self.agent[1] < 0 or self.agent[0] >\
                self.env_row-1 or self.agent[1] > self.env_row-1:
            over = True
        elif self.agent[0] == self.target[0] and\
                self.agent[1] == self.target[1]:
            self.env[self.agent[0]][self.agent[1]] = 1
            over = True
        elif self.env[self.agent[0]][self.agent[1]] == 99:
            over = True
        else:
            self.env[self.agent[0]][self.agent[1]] = 1
        return self.agent.copy(), over


pygame.init()
pygame.display.set_caption("Simple GridWorld")
clock = pygame.time.Clock()
env = GridWorld()
env.play()
