import pygame
import numpy as np
import random
import math as mt
import snake_brain as sb

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 177, 76)
BLUE = (255, 0, 255)
GG = (0, 255, 255)


class Snake():
    pygame.init()

    def __init__(self, width, height, vel, fps):
        self.width = width
        self.height = height
        self.vel = vel
        self.shape = 24
        self.snake = list()
        self.board_count = int((self.width - 40) / self.vel)
        self.clock = pygame.time.Clock()
        self.win = pygame.display.set_mode((self.width, self.height))
        self.fps = fps
        self.board = np.zeros((self.board_count, self.board_count), dtype="int")
        self.food_hit = False
        self.out = False
        self.head = False
        self.food_y = 0
        self.food_x = 0
        self.discrete_os_size = [20] * 5
        self.discrete_os_win_size = np.array([20, 20, 20, 20, 707.1067811]) / self.discrete_os_size
        self.reward = 0
        self.learning_rate = 0.01
        self.discount = 0.99
        self.epsilon = 0.8
        self.step = 1
        self.step_reward = -5
        self.out_reward = -50
        self.food_reward = 0
        self.dist_temp = 0
        self.dist_change = 0
        self.game_flip = False
        self.discrete_state = (0, 0, 0, 0, 0)
        self.q_table = np.random.uniform(low=0, high=0, size=([20]*5 + [4]))
        # self.q_table = np.load("q_table.npy")
        for i in range(50000):
            self.food_x, self.food_y = self.start()
            wasd = self.check_board()
            dist = self.draw_line(self.snake[0].copy(), self.snake[len(self.snake) - 1], wasd)
            state = np.array(wasd + [self.dist_change])
            self.dist_temp = dist[0]
            self.discrete_state = self.get_discrete_state(state)
            print(i)
            self.game()
        np.save("q_table.npy", self.q_table)

    def get_discrete_state(self, state):
        discrete_state = state / self.discrete_os_win_size
        # print(tuple(discrete_state.astype(np.int)))
        return tuple(discrete_state.astype(np.int))

    def main(self):
        pygame.display.set_caption("Main")
        run = True
        while run:
            self.win.fill(RED)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                elif event.type == pygame.KEYUP:
                    if keys[pygame.K_SPACE]:
                        run = False
                    else:
                        pass
            pygame.display.flip()
            self.clock.tick(60)

    def pause(self):
        pygame.display.set_caption("Pause")
        run = True
        while run:
            self.win.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    run = False
            pygame.display.flip()
            self.clock.tick(60)

    def start(self):
        d = random.randint(1, 2)
        ldir = ""
        x, y = 0, 0
        rand_food_x, rand_food_y = 0, 0
        self.snake.clear()
        self.step = 1
        self.reward = 0
        self.dist_change = 0
        self.board = np.zeros((self.board_count, self.board_count), dtype=int)
        if d == 1:
            ldir = "↓"
            rand_x = random.randint(0, self.board_count - 1)
            x = rand_x * self.vel + 21
            y = 3 * self.vel + 21
            x_1 = x
            y_1 = y - self.vel
            x_2 = x
            y_2 = y_1 - self.vel
            self.board[3][rand_x] = 3
            self.board[2][rand_x] = 1
            do = True
            while do:
                rand_food_x = random.randint(0, self.board_count - 1)
                rand_food_y = random.randint(4, self.board_count - 1)
                if self.board[rand_food_y][rand_food_x] == 1:
                    pass
                else:
                    do = False
        elif d == 2:
            ldir = "→"
            x = 3 * self.vel + 21
            rand_y = random.randint(0, self.board_count - 1)
            y = rand_y * self.vel + 21
            x_1 = x - self.vel
            x_2 = x_1 - self.vel
            y_1 = y
            y_2 = y
            self.board[rand_y][3] = 3
            self.board[rand_y][2] = 1
            do = True
            while do:
                rand_food_x = random.randint(4, self.board_count - 1)
                rand_food_y = random.randint(0, self.board_count - 1)
                if self.board[rand_food_y][rand_food_x] == 1:
                    pass
                else:
                    do = False
        self.out = False
        self.snake.append([x, y, ldir])
        self.snake.append([x_1, y_1, ldir])
        self.snake.append([x_2, y_2, ldir])
        self.board[rand_food_y][rand_food_x] = 2
        food_x = rand_food_x * self.vel + 21
        food_y = rand_food_y * self.vel + 21
        return food_x, food_y

    def check_board(self):
            head_dir = self.snake[0][2]
            head_y = int((self.snake[0][0] - 21) / self.vel)
            head_x = int((self.snake[0][1] - 21) / self.vel)
            up_dis = 0
            down_dis = 0
            right_dis = 0
            left_dis = 0
            if head_dir == "↑":
                hitted = False
                i = head_x
                while not hitted:
                    i -= 1
                    if i == -1 or self.board[i][head_y] == 1:
                        hitted = True
                        up_dis = head_x - i - 1
                hitted = False
                i = head_y
                while not hitted:
                    i -= 1
                    if i == -1 or self.board[head_x][i] == 1:
                        hitted = True
                        right_dis = head_y - i - 1
                hitted = False
                i = head_y
                while not hitted:
                    i += 1
                    if i == self.board_count or self.board[head_x][i] == 1:
                        hitted = True
                        left_dis = i - head_y - 1
            elif head_dir == "↓":
                hitted = False
                i = head_x
                while not hitted:
                    i += 1
                    if i == self.board_count or self.board[i][head_y] == 1:
                        hitted = True
                        down_dis = i - head_x - 1
                hitted = False
                i = head_y
                while not hitted:
                    i -= 1
                    if i == -1 or self.board[head_x][i] == 1:
                        hitted = True
                        right_dis = head_y - i - 1
                hitted = False
                i = head_y
                while not hitted:
                    i += 1
                    if i == self.board_count or self.board[head_x][i] == 1:
                        hitted = True
                        left_dis = i - head_y - 1
            elif head_dir == "←":
                hitted = False
                i = head_x
                while not hitted:
                    i += 1
                    if i == self.board_count or self.board[i][head_y] == 1:
                        hitted = True
                        down_dis = i - head_x - 1
                hitted = False
                i = head_y
                while not hitted:
                    i -= 1
                    if i == -1 or self.board[head_x][i] == 1:
                        hitted = True
                        right_dis = head_y - i - 1
                hitted = False
                i = head_x
                while not hitted:
                    i -= 1
                    if i == -1 or self.board[i][head_y] == 1:
                        hitted = True
                        up_dis = head_x - 1 - i
            elif head_dir == "→":
                hitted = False
                i = head_x
                while not hitted:
                    i += 1
                    if i == self.board_count or self.board[i][head_y] == 1:
                        hitted = True
                        down_dis = i - head_x - 1
                hitted = False
                i = head_y
                while not hitted:
                    i += 1
                    if i == self.board_count or self.board[head_x][i] == 1:
                        hitted = True
                        left_dis = i - 1 - head_y
                hitted = False
                i = head_x
                while not hitted:
                    i -= 1
                    if i == -1 or self.board[i][head_y] == 1:
                        hitted = True
                        up_dis = head_x - 1 - i
            return [up_dis, down_dis, right_dis, left_dis]

    def draw_line(self, block_a, block_b, wasd):
        # up down right left (wasd)
        x = int((block_a[0] - 21)/self.vel)
        y = int((block_a[1] - 21)/self.vel)
        head = [block_a[0] + int(self.shape/2), block_a[1] + int(self.shape/2)].copy()
        food = [self.food_x + int(self.shape/2), self.food_y + int(self.shape/2)].copy()
        tail = [block_b[0] + int(self.shape/2), block_b[1] + int(self.shape/2)].copy()
        pygame.draw.line(self.win, BLUE, head, food, 2)
        pygame.draw.line(self.win, BLUE, head, [21 + (x - wasd[2]) * self.vel, head[1]], 2)
        pygame.draw.line(self.win, BLUE, head, [head[0], 21 + (y - wasd[0]) * self.vel], 2)
        pygame.draw.line(self.win, BLUE, head, [20 + (x + wasd[3] + 1) * self.vel, head[1]], 2)
        pygame.draw.line(self.win, BLUE, head, [head[0], 20 + (y + wasd[1] + 1) * self.vel], 2)
        pygame.draw.line(self.win, BLUE, head, tail, 2)
        head_food = mt.sqrt((head[0] - food[0]) ** 2 + (head[1] - food[1]) ** 2)
        head_tail = mt.sqrt((head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2)
        return [round(head_food), round(head_tail)]

    def game(self):
        def draw_board():
            pygame.draw.line(self.win, WHITE, (20 + 0 * self.vel, 20), (20 + 0 * self.vel, 520))
            pygame.draw.line(self.win, WHITE, (20 + 20 * self.vel, 20), (20 + 20 * self.vel, 520))
            pygame.draw.line(self.win, WHITE, (20, 20 + 0 * self.vel), (520, 20 + 0 * self.vel))
            pygame.draw.line(self.win, WHITE, (20, 20 + 20 * self.vel), (520, 20 + 20 * self.vel))
            #for i in range(self.board_count + 1):
            #   pygame.draw.line(self.win, WHITE, (20 + i * self.vel, 20), (20 + i * self.vel, 520))
            #   pygame.draw.line(self.win, WHITE, (20, 20 + i * self.vel), (520, 20 + i * self.vel))
        def draw_snake(block_s):
            x = int((block_s[0] - 21)/self.vel)
            y = int((block_s[1] - 21)/self.vel)
            # print(y, x)
            if block_s[2] == "↑":
                if y == 0 or self.board[y-1][x] == 1:
                    self.out = True
                else:
                    if self.head:
                        self.board[y-1][x] = 3
                        self.board[y][x] = 0
                    else:
                        self.board[y-1][x] = 1
                        self.board[y][x] = 0
                    block_s[1] -= self.vel
                    pygame.draw.rect(self.win, RED, (block_s[0], block_s[1], self.shape, self.shape))
            elif block_s[2] == "↓":
                if y == self.board_count - 1 or self.board[y+1][x] == 1:
                    self.out = True
                else:
                    if self.head:
                        self.board[y+1][x] = 3
                        self.board[y][x] = 0
                    else:
                        self.board[y+1][x] = 1
                        self.board[y][x] = 0
                    block_s[1] += self.vel
                    pygame.draw.rect(self.win, RED, (block_s[0], block_s[1], self.shape, self.shape))
            elif block_s[2] == "←":
                if x == 0 or self.board[y][x-1] == 1:
                    self.out = True
                else:
                    if self.head:
                        self.board[y][x-1] = 3
                        self.board[y][x] = 0
                    else:
                        self.board[y][x-1] = 1
                        self.board[y][x] = 0
                    block_s[0] -= self.vel
                    pygame.draw.rect(self.win, RED, (block_s[0], block_s[1], self.shape, self.shape))
            elif block_s[2] == "→":
                if x == self.board_count - 1 or self.board[y][x+1] == 1:
                    self.out = True
                else:
                    if self.head:
                        self.board[y][x+1] = 3
                        self.board[y][x] = 0
                    else:
                        self.board[y][x+1] = 1
                        self.board[y][x] = 0
                    block_s[0] += self.vel
                    pygame.draw.rect(self.win, RED, (block_s[0], block_s[1], self.shape, self.shape))
            return block_s.copy()

        # self.main()
        pygame.display.set_caption("SNAKE")
        last_avg_reward = 0
        tmp = ""
        ldir = ""
        is_pause = False
        playing = True
        font = pygame.font.SysFont("arial", 25)

        while playing:
            if self.game_flip:
                pygame.display.flip()
                self.clock.tick(self.fps)
            self.win.fill((0, 0, 0))
            draw_board()
            tmp = self.snake[0][2]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # np.save("q_table.npy", self.q_table)
                    quit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    """
                    if not is_pause:
                        is_pause = True
                        self.pause()
                        pygame.display.set_caption("SNAKE")
                        is_pause = False
                    else:
                        is_pause = False
                    """
                    if not self.game_flip:
                        self.game_flip = True
                    elif self.game_flip:
                        self.game_flip = False
                elif keys[pygame.K_r]:
                    playing = False
                    print("Reset")

            # action = np.argmax(self.q_table[self.discrete_state])
            if np.random.random() > self.epsilon:
                action = np.argmax(self.q_table[self.discrete_state])
            else:
                action = random.randint(0, 3)
            """
                cont = False
                while not cont:
                    action = np.random.randint(0,3)
                    if self.snake[0][2] == "←":
                        if action != 2:
                            cont = True
                    elif self.snake[0][2] == "↑":
                        if action != 3:
                            cont = True
                    elif self.snake[0][2] == "→":
                        if action != 0:
                            cont = True
                    elif self.snake[0][2] == "↓":
                        if action != 1:
                            cont = True
                """
            # print(action)
            if action == 0:
                self.snake[0][2] = "←"
            elif action == 1:
                self.snake[0][2] = "↑"
            elif action == 2:
                self.snake[0][2] = "→"
            elif action == 3:
                self.snake[0][2] = "↓"
            """
            if action == 0:
                if self.snake[0][2] == "↑":
                    self.snake[0][2] == "←"
                elif self.snake[0][2] == "←":
                    self.snake[0][2] = "↓"
                elif self.snake[0][2] == "↓":
                    self.snake[0][2] = "→"
                elif self.snake[0][2] == "→":
                    self.snake[0][2] = "↑"
            elif action == 1:
                pass
            elif action == 2:
                if self.snake[0][2] == "↑":
                    self.snake[0][2] == "→"
                elif self.snake[0][2] == "←":
                    self.snake[0][2] = "↑"
                elif self.snake[0][2] == "↓":
                    self.snake[0][2] = "←"
                elif self.snake[0][2] == "→":
                    self.snake[0][2] = "↓"
            """
            for index, block in enumerate(self.snake):
                if index == 0:
                    self.head = True
                elif index > 0:
                    self.head = False
                    tmp = block[2]
                    block[2] = ldir
                if self.snake[0][0] == self.food_x and self.snake[0][1] == self.food_y:
                    self.food_hit = True
                    lf_x = int((self.food_x - 21)/self.vel)
                    lf_y = int((self.food_y - 21)/self.vel)
                    self.board[lf_y][lf_x] = 3
                    do = True
                    while do:
                        rand_food_x = random.randint(0, self.board_count - 1)
                        rand_food_y = random.randint(0, self.board_count - 1)
                        if 1<= self.board[rand_food_y][rand_food_x] <= 3:
                            pass
                        else:
                            do = False
                    self.board[rand_food_y][rand_food_x] = 2
                    self.food_x = rand_food_x * self.vel + 21
                    self.food_y = rand_food_y * self.vel + 21
                    tail = self.snake[len(self.snake) - 1].copy()
                    if tail[2] == "↑":
                        tail[1] += self.vel
                    elif tail[2] == "↓":
                        tail[1] -= self.vel
                    elif tail[2] == "←":
                        tail[0] += self.vel
                    elif tail[2] == "→":
                        tail[0] -= self.vel
                    self.snake.append(tail)
                else:
                    self.snake[index] = draw_snake(block.copy())
                ldir = tmp
                pygame.draw.rect(self.win, GREEN, (self.food_x, self.food_y, self.shape, self.shape))

                # if index == 0:
            # up down right leht
            wasd = self.check_board()
            dist = self.draw_line(self.snake[0].copy(), self.snake[len(self.snake) - 1], wasd)
            self.dist_change = self.dist_temp - dist[0]
            state = np.array(wasd + [self.dist_change])
            # print(state)
            discrete_state_new = self.get_discrete_state(state)

            if self.food_hit:
                self.step = 1
                self.q_table[self.discrete_state + (action, )] = 50
                self.reward += 20
                self.food_hit = False
                print("Food!!!!")
                # pygame.time.delay(500)
            elif self.out:
                self.q_table[self.discrete_state + (action, )] = self.out_reward
                if last_avg_reward < self.reward / self.step:
                    print("Learning ↑", self.reward)
                else:
                    print("↓")
                last_avg_reward = self.reward / self.step
                if self.epsilon > 0:
                    self.epsilon -= 0.000002
                else:
                    self.epsion = -1
                playing = False
            else:
                self.step += 1
                if self.dist_change > 0:
                    self.reward += 5
                elif self.dist_change <= 0:
                    self.reward -= 5
                self.reward -= self.step / 10
                self.dist_temp = dist[0]
                """
                if self.step > 400:
                    # self.q_table[self.discrete_state + (action, )] = -20
                    if last_avg_reward < self.reward / self.step:
                        print("Learning ↑", self.reward)
                    else:
                        print("↓")
                    last_avg_reward = self.reward / self.step
                    # playing = False
                    print("Reset")
                    # self.game_flip = True
                """
                # print(f"Empty step: {self.empty_step}")
                max_future_q = np.max(self.q_table[discrete_state_new])
                current_q = self.q_table[self.discrete_state + (action, )]
                new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (self.reward + self.discount * max_future_q)
                self.q_table[self.discrete_state + (action, )] = new_q
                self.discrete_state = discrete_state_new

            score = font.render(f"Score: {len(self.snake) - 3} fps: {self.fps}", 1, WHITE)
            self.win.blit(score, (200, 540))


Snake(width=540, height=600, vel=25, fps=60)
