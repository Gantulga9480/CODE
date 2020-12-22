import pygame
import numpy as np
import math as mt
import snake_brain as sb

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
BLUE = (255, 0, 255)

WIDTH = 540
HEIGHT = 600
VELOCITY = 25
SHAPE = 24
BOARD_COUNT = int((WIDTH - 40) / VELOCITY)

HEAD = 22
TAIL = 11
FOOD = 99

FPS = 60

ACTION_SPACE = 4

FOOD_REWARD = 1000
OUT_REWARD = -1000
EMPTY_STEP_REWARD = -10


def init():
    pygame.init()
    pygame.display.set_caption("SNAKE")


class Snake:

    def __init__(self):
        self.font = pygame.font.SysFont("arial", 25)
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = np.zeros((BOARD_COUNT, BOARD_COUNT), dtype=int)
        self.snake = list()
        self.food_x = 0
        self.food_y = 0
        self.head = False
        self.out = False
        self.food_hit = False
        self.game_flip = True
        self.reward = 0
        self.ldir = ""
        self.brain = sb.Brain(vel=VELOCITY,
                              board_count=BOARD_COUNT,
                              shape=SHAPE)

    def step(self, auto=False, action=None):
        if self.game_flip:
            self.win.fill((0, 0, 0))
            self.draw_board()
        tmp = self.snake[0][2]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if not self.game_flip:
                    self.game_flip = True
                elif self.game_flip:
                    self.game_flip = False
        if auto:
            self.snake[0][2] = \
                self.brain.move(self.snake[0].copy(),
                                self.snake[len(self.snake) - 1].copy(),
                                self.board, [self.food_x,
                                self.food_y])
        else:
            if self.snake[0][2] == "↑":
                if action == 0:
                    self.snake[0][2] = "←"
                elif action == 1:
                    self.snake[0][2] = "↑"
                elif action == 2:
                    self.snake[0][2] = "→"
            elif self.snake[0][2] == "→":
                if action == 0:
                    self.snake[0][2] = "↑"
                elif action == 1:
                    self.snake[0][2] = "→"
                elif action == 2:
                    self.snake[0][2] ="↓"
            elif self.snake[0][2] == "↓":
                if action == 0:
                    self.snake[0][2] = "→"
                elif action == 1:
                    self.snake[0][2] = "↓"
                elif action == 2:
                    self.snake[0][2] = "←"
            elif self.snake[0][2] == "←":
                if action == 0:
                    self.snake[0][2] = "↓"
                elif action == 1:
                    self.snake[0][2] = "←"
                elif action == 2:
                    self.snake[0][2] = "↑"
        for index, block in enumerate(self.snake):
            if index == 0:
                self.head = True
            elif index > 0:
                self.head = False
                tmp = block[2]
                block[2] = self.ldir
            if self.snake[0][0] == self.food_x and \
                    self.snake[0][1] == self.food_y:
                lf_x = int((self.food_x - 21)/VELOCITY)
                lf_y = int((self.food_y - 21)/VELOCITY)
                self.board[lf_y][lf_x] = HEAD
                self.food_hit = True
                do = True
                while do:
                    rand_food_x = np.random.randint(0, BOARD_COUNT - 1)
                    rand_food_y = np.random.randint(0, BOARD_COUNT - 1)
                    if self.board[rand_food_y][rand_food_x] == TAIL:
                        pass
                    else:
                        do = False
                self.board[rand_food_y][rand_food_x] = FOOD
                self.food_x = rand_food_x * VELOCITY + 21
                self.food_y = rand_food_y * VELOCITY + 21
                tail = self.snake[len(self.snake) - 1].copy()
                if tail[2] == "↑":
                    tail[1] += VELOCITY
                elif tail[2] == "↓":
                    tail[1] -= VELOCITY
                elif tail[2] == "←":
                    tail[0] += VELOCITY
                elif tail[2] == "→":
                    tail[0] -= VELOCITY
                self.snake.append(tail)
            if self.game_flip:
                pygame.draw.rect(self.win, GREEN,
                                 (self.food_x, self.food_y, SHAPE, SHAPE))
            if self.out:
                pass
            else:
                self.snake[index] = self.draw_snake(block.copy())
            self.ldir = tmp
        if self.game_flip:
            score = self.font.render(f"Score: {len(self.snake) - 3} fps: {FPS}",
                                     1, WHITE)
            self.win.blit(score, (200, 540))
        if self.game_flip:
            pygame.display.flip()
            self.clock.tick(FPS)
        if self.out:
            self.reward = OUT_REWARD
            return True, self.get_state(), self.reward
        elif self.food_hit:
            self.food_hit = False
            self.reward = FOOD_REWARD
            return False, self.get_state(), self.reward
        else:
            self.reward = EMPTY_STEP_REWARD
            return False, self.get_state(), self.reward

    def get_state(self):
        state = []
        y = int((self.snake[0][0] - 21)/VELOCITY)
        x = int((self.snake[0][1] - 21)/VELOCITY)
        if self.snake[0][2] == "↑":
            if 0 <= y - 1:
                state.append(self.board[x][y-1])
            else:
                state.append(TAIL)
            if x - 1 >= 0:
                state.append(self.board[x-1][y])
            else:
                state.append(TAIL)
            if y + 1 < BOARD_COUNT:
                state.append(self.board[x][y+1])
            else:
                state.append(TAIL)
        elif self.snake[0][2] == "→":
            if x - 1 >= 0:
                state.append(self.board[x-1][y])
            else:
                state.append(TAIL)
            if y + 1 < BOARD_COUNT:
                state.append(self.board[x][y+1])
            else:
                state.append(TAIL)
            if x + 1 < BOARD_COUNT:
                state.append(self.board[x+1][y])
            else:
                state.append(TAIL)
        elif self.snake[0][2] == "↓":
            if y + 1 < BOARD_COUNT:
                state.append(self.board[x][y+1])
            else:
                state.append(TAIL)
            if x + 1 < BOARD_COUNT:
                state.append(self.board[x+1][y])
            else:
                state.append(TAIL)
            if 0 <= y - 1:
                state.append(self.board[x][y-1])
            else:
                state.append(TAIL)
        elif self.snake[0][2] == "←":
            if x + 1 < BOARD_COUNT:
                state.append(self.board[x+1][y])
            else:
                state.append(TAIL)
            if 0 <= y - 1:
                state.append(self.board[x][y-1])
            else:
                state.append(TAIL)
            if x - 1 >= 0:
                state.append(self.board[x-1][y])
            else:
                state.append(TAIL)
        return np.array(state)

    def reset(self):
        self.out = False
        self.food_hit = False
        self.reward = 0
        self.snake.clear()
        self.board = np.zeros((BOARD_COUNT, BOARD_COUNT), dtype=int)
        d = np.random.randint(1, 4)
        ldir = ""
        x, y = 0, 0
        rand_food_x, rand_food_y = 0, 0
        if d == 1:
            ldir = "↓"
            rand_x = np.random.randint(0, BOARD_COUNT - 1)
            x = rand_x * VELOCITY + 21
            x_1 = x
            x_2 = x
            rand_y = np.random.randint(2, BOARD_COUNT - 2)
            y = rand_y * VELOCITY + 21
            y_1 = y - VELOCITY
            y_2 = y_1 - VELOCITY
            self.board[rand_y][rand_x] = HEAD
            self.board[rand_y - 1][rand_x] = TAIL
            self.board[rand_y - 2][rand_x] = TAIL
        elif d == 2:
            ldir = "→"
            rand_y = np.random.randint(0, BOARD_COUNT - 1)
            y = rand_y * VELOCITY + 21
            y_1 = y
            y_2 = y
            rand_x = np.random.randint(2, BOARD_COUNT - 2)
            x = rand_x * VELOCITY + 21
            x_1 = x - VELOCITY
            x_2 = x_1 - VELOCITY
            self.board[rand_y][rand_x] = HEAD
            self.board[rand_y][rand_x - 1] = TAIL
            self.board[rand_y][rand_x - 2] = TAIL
        elif d == 3:
            ldir = "↑"
            rand_x = np.random.randint(0, BOARD_COUNT - 1)
            x = rand_x * VELOCITY + 21
            x_1 = x
            x_2 = x
            rand_y = np.random.randint(1, BOARD_COUNT - 3)
            y = rand_y * VELOCITY + 21
            y_1 = y + VELOCITY
            y_2 = y_1 + VELOCITY
            self.board[rand_y][rand_x] = HEAD
            self.board[rand_y + 1][rand_x] = TAIL
            self.board[rand_y + 2][rand_x] = TAIL
        elif d == 4:
            ldir = "←"
            rand_x = np.random.randint(1, BOARD_COUNT - 3)
            x = rand_x * VELOCITY + 21
            x_1 = x + VELOCITY
            x_2 = x_1 + VELOCITY
            rand_y = np.random.randint(0, BOARD_COUNT - 1)
            y = rand_y * VELOCITY + 21
            y_1 = y
            y_2 = y
            self.board[rand_y][rand_x] = HEAD
            self.board[rand_y][rand_x + 1] = TAIL
            self.board[rand_y][rand_x + 2] = TAIL
        do = True
        while do:
            rand_food_x = np.random.randint(0, BOARD_COUNT - 1)
            rand_food_y = np.random.randint(0, BOARD_COUNT - 1)
            if self.board[rand_food_y][rand_food_x] == TAIL:
                pass
            else:
                do = False
        self.snake.append([x, y, ldir])
        self.snake.append([x_1, y_1, ldir])
        self.snake.append([x_2, y_2, ldir])
        self.board[rand_food_y][rand_food_x] = FOOD
        self.food_x = rand_food_x * VELOCITY + 21
        self.food_y = rand_food_y * VELOCITY + 21
        return self.get_state()

    def draw_board(self):
        pygame.draw.line(self.win, WHITE,
                         (20 + 0 * VELOCITY, 20),
                         (20 + 0 * VELOCITY, 520))
        pygame.draw.line(self.win, WHITE,
                         (20 + 20 * VELOCITY, 20),
                         (20 + 20 * VELOCITY, 520))
        pygame.draw.line(self.win, WHITE,
                         (20, 20 + 0 * VELOCITY),
                         (520, 20 + 0 * VELOCITY))
        pygame.draw.line(self.win, WHITE,
                         (20, 20 + 20 * VELOCITY),
                         (520, 20 + 20 * VELOCITY))

    def draw_snake(self, block_s):
        x = int((block_s[0] - 21)/VELOCITY)
        y = int((block_s[1] - 21)/VELOCITY)
        try:
            if block_s[2] == "↑":
                if y == 0 or self.board[y-1][x] == TAIL:
                    self.out = True
                else:
                    if self.head:
                        self.board[y-1][x] = HEAD
                    else:
                        self.board[y-1][x] = TAIL
                    self.board[y][x] = 0
                    block_s[1] -= VELOCITY
                    if self.game_flip:
                        pygame.draw.rect(self.win, RED,
                                         (block_s[0], block_s[1], SHAPE, SHAPE))
            elif block_s[2] == "↓":
                if y == BOARD_COUNT - 1 or self.board[y+1][x] == TAIL:
                    self.out = True
                else:
                    if self.head:
                        self.board[y+1][x] = HEAD
                    else:
                        self.board[y+1][x] = TAIL
                    self.board[y][x] = 0
                    block_s[1] += VELOCITY
                    if self.game_flip:
                        pygame.draw.rect(self.win, RED,
                                         (block_s[0], block_s[1], SHAPE, SHAPE))
            elif block_s[2] == "←":
                if x == 0 or self.board[y][x-1] == TAIL:
                    self.out = True
                else:
                    if self.head:
                        self.board[y][x-1] = HEAD
                    else:
                        self.board[y][x-1] = TAIL
                    self.board[y][x] = 0
                    block_s[0] -= VELOCITY
                    if self.game_flip:
                        pygame.draw.rect(self.win, RED,
                                         (block_s[0], block_s[1], SHAPE, SHAPE))
            elif block_s[2] == "→":
                if x == BOARD_COUNT - 1 or self.board[y][x+1] == TAIL:
                    self.out = True
                else:
                    if self.head:
                        self.board[y][x+1] = HEAD
                    else:
                        self.board[y][x+1] = TAIL
                    self.board[y][x] = 0
                    block_s[0] += VELOCITY
                    if self.game_flip:
                        pygame.draw.rect(self.win, RED,
                                         (block_s[0], block_s[1], SHAPE, SHAPE))
            return block_s.copy()
        except IndexError:
            print(self.head)
            print(x, y, block_s[2])
            print(self.board)
            quit()
