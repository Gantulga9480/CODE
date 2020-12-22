import pygame
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 255, 76)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

AGENT = 11
TARGET = 22
HOLE = 99
WIDTH_MAX = 600
DRAW_VEL = 4

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Create:

    def __init__(self, size):
        self.size = size
        self.env = np.zeros((size, size))
        self.vel = WIDTH_MAX // size
        self.shape = self.vel - 1
        self.width = self.vel * self.size + 1
        font_size = np.int(self.shape - np.sqrt(2*(self.shape/3)**2))
        self.height = self.width
        self.win = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", font_size)
        self.clock = pygame.time.Clock()
        self.choice = HOLE
        self.is_agent_placed = False
        self.is_treasure_placed = False
        self.hole_count = 0
        self.run = True
        self.fps = 60
        self.q_table = np.zeros((self.size, self.size))

    def draw_board(self):
        for i in range(self.size+1):
            pygame.draw.line(self.win, WHITE, (i*self.vel, 0),
                             (i*self.vel, self.vel*self.size))
            pygame.draw.line(self.win, WHITE, (0, i*self.vel),
                             (self.vel*self.size, i*self.vel))
        for i in range(self.size):
            for j in range(self.size):
                if self.env[i][j] == AGENT:
                    pygame.draw.rect(self.win, YELLOW,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.env[i][j] == HOLE:
                    pygame.draw.rect(self.win, RED,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.env[i][j] == TARGET:
                    pygame.draw.rect(self.win, GREEN,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))

    def draw_table(self, max_):
        for i in range(self.size):
            for j in range(self.size):
                score = self.q_table[i][j]
                if self.env[i][j] == TARGET:
                    pygame.draw.rect(self.win, GREEN,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.vel, self.vel))
                elif self.env[i][j] == HOLE:
                    pygame.draw.rect(self.win, RED,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.vel, self.vel))
                elif score == 0:
                    pygame.draw.rect(self.win, WHITE,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.vel, self.vel))
                else:
                    if score < 0:
                        if np.abs(score)/max_ >= 1:
                            pygame.draw.rect(self.win, BLUE,
                                             (self.vel*j+1, self.vel*i+1,
                                              self.vel, self.vel))
                        else:
                            color = 1 - np.abs(score)/max_
                            pygame.draw.rect(self.win, (255*color,
                                                        255*color,
                                                        255),
                                             (self.vel*j+1, self.vel*i+1,
                                             self.vel, self.vel))
                    else:
                        color = 1 - score/max_
                        pygame.draw.rect(self.win, (255*color, 255, 255*color),
                                         (self.vel*j+1, self.vel*i+1,
                                          self.vel, self.vel))

                if 0 < np.abs(score)-np.floor(np.abs(score)) < 1:
                    string1 = f"{np.round(score, 2)}"
                else:
                    string1 = f"{int(score)}"
                s = self.font1.render(string1, 1, BLACK)
                self.win.blit(s, (j*self.vel+5, i*self.vel+5))

        for i in range(self.size + 1):
            pygame.draw.line(self.win, BLACK, (i*self.vel, 0),
                             (i*self.vel, self.size*self.vel))
            pygame.draw.line(self.win, BLACK, (0, i*self.vel),
                             (self.size*self.vel, i*self.vel))

    def show_table(self, table, max_):
        pygame.display.set_caption("Q_Table")
        self.q_table = table
        max_val = max_
        try:
            self.env = np.load("env.npy")
        except FileNotFoundError:
            pass
        self.run = True
        outer_run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    outer_run = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:
                self.run = False
                outer_run = False
            self.win.fill(WHITE)
            self.draw_table(max_val)
            pygame.display.flip()
            self.clock.tick(self.fps)
        return outer_run
        # pygame.display.quit()

    def create_env(self):
        pygame.display.set_caption("Make Env")
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cursor_pos = event.pos
                    x = int(np.floor(cursor_pos[0] / self.vel))
                    y = int(np.floor(cursor_pos[1] / self.vel))
                    if self.choice == AGENT and not self.is_agent_placed:
                        if self.env[y][x] > 0:
                            pass
                        else:
                            self.env[y][x] = AGENT
                            self.is_agent_placed = True
                    elif self.choice == HOLE:
                        if self.env[y][x] > 0:
                            pass
                        else:
                            self.env[y][x] = HOLE
                            self.hole_count += 1
                    elif self.choice == TARGET:
                        if self.env[y][x] > 0:
                            pass
                        else:
                            self.env[y][x] = TARGET
                            self.is_treasure_placed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if not self.is_agent_placed:
                            self.choice = AGENT
                    elif event.key == pygame.K_f:
                        self.choice = HOLE
                    elif event.key == pygame.K_d:
                        if not self.is_treasure_placed:
                            self.choice = TARGET
                    elif event.key == pygame.K_r:
                        self.env = np.zeros((self.size, self.size))
                        self.hole_count = 0
                        self.is_agent_placed = False
                        self.is_treasure_placed = False
                    elif event.key == pygame.K_q:
                        poss = pygame.mouse.get_pos()
                        x = int(np.floor(poss[0] / self.vel))
                        y = int(np.floor(poss[1] / self.vel))
                        if self.env[y][x] == HOLE:
                            self.env[y][x] = 0
                            self.hole_count -= 1
                        elif self.env[y][x] == AGENT:
                            self.env[y][x] = 0
                            self.is_agent_placed = False
                        elif self.env[y][x] == TARGET:
                            self.env[y][x] = 0
                            self.is_treasure_placed = False
                    elif event.key == pygame.K_s:
                        if self.is_agent_placed and self.is_treasure_placed \
                                and self.hole_count >= 0:
                            np.save("env", self.env)
                            np.save("q_table", self.q_table)
                            self.run = False
                        else:
                            pass
            self.win.fill(BLACK)
            self.draw_board()
            if not self.run:
                pygame.image.save(self.win, "img\\env_img.jpg")
            count = self.font.render(f"{self.hole_count}", 1, BLUE)
            self.win.blit(count, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.display.quit()


class Image:

    def __init__(self, shape=None, width=None, height=None):
        self.car_dim = (shape, shape)
        self.floor_dim = (width, height)

    def process(self, img_path, dim=None, save=False):
        if dim is None:
            dim = self.car_dim
        try:
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            re_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
            if save:
                cv2.imwrite(img_path, re_img)
                img = pygame.image.load(img_path)
            else:
                cv2.imwrite("img\\temp.jpg", re_img)
                img = pygame.image.load("img\\temp.jpg")
                os.remove("img\\temp.jpg")
            return img
        except FileNotFoundError:
            pass

    def load_img(self):
        try:
            carImg_up = pygame.image.load("img\\down_up.png")
            carImg_right = pygame.image.load("img\\down_right.png")
            carImg_down = pygame.image.load("img\\down_down.png")
            carImg_left = pygame.image.load("img\\down_left.png")
            floor = pygame.image.load("img\\grass_down.jpg")
            wall = pygame.image.load("img\\wall_down.jpg")
            star = pygame.image.load("img\\star_down.jpg")
        except pygame.error:
            carImg_up = cv2.imread("img\\wheel_1_up.png", cv2.IMREAD_UNCHANGED)
            carImg_right = cv2.imread("img\\wheel_1_right.png",
                                      cv2.IMREAD_UNCHANGED)
            carImg_down = cv2.imread("img\\wheel_1_down.png",
                                     cv2.IMREAD_UNCHANGED)
            carImg_left = cv2.imread("img\\wheel_1_left.png",
                                     cv2.IMREAD_UNCHANGED)
            floor = cv2.imread("img\\grass.jpg", cv2.IMREAD_UNCHANGED)
            wall = cv2.imread("img\\wall.jpg", cv2.IMREAD_UNCHANGED)
            star = cv2.imread("img\\star.png", cv2.IMREAD_UNCHANGED)

            resized_up = cv2.resize(carImg_up, self.car_dim,
                                    interpolation=cv2.INTER_AREA)
            resized_right = cv2.resize(carImg_right, self.car_dim,
                                       interpolation=cv2.INTER_AREA)
            resized_down = cv2.resize(carImg_down, self.car_dim,
                                      interpolation=cv2.INTER_AREA)
            resized_left = cv2.resize(carImg_left, self.car_dim,
                                      interpolation=cv2.INTER_AREA)
            resized_floor = cv2.resize(floor, self.floor_dim,
                                       interpolation=cv2.INTER_AREA)
            resized_wall = cv2.resize(wall, self.car_dim,
                                      interpolation=cv2.INTER_AREA)
            resized_star = cv2.resize(star, self.car_dim,
                                      interpolation=cv2.INTER_AREA)

            cv2.imwrite("img\\down_up.png", resized_up)
            cv2.imwrite("img\\down_right.png", resized_right)
            cv2.imwrite("img\\down_down.png", resized_down)
            cv2.imwrite("img\\down_left.png", resized_left)
            cv2.imwrite("img\\grass_down.jpg", resized_floor)
            cv2.imwrite("img\\wall_down.jpg", resized_wall)
            cv2.imwrite("img\\star_down.png", resized_star)

            carImg_up = pygame.image.load("img\\down_up.png")
            carImg_right = pygame.image.load("img\\down_right.png")
            carImg_down = pygame.image.load("img\\down_down.png")
            carImg_left = pygame.image.load("img\\down_left.png")
            floor = pygame.image.load("img\\grass_down.jpg")
            wall = pygame.image.load("img\\wall_down.jpg")
            star = pygame.image.load("img\\star_down.png")
        return [carImg_up, carImg_down, carImg_left,
                carImg_right, floor, wall, star]


class GridWorld:

    def __init__(self, visual=False):
        # Game
        self.run = True
        self.game_flip = True
        self.fps = 60
        self.visual = visual
        self.clock = pygame.time.Clock()

        # Env
        try:
            self.envi = np.load("env.npy")
        except FileNotFoundError:
            self.envi = np.load("def\\env_default.npy")
        self.env_len = len(self.envi)
        ag_ta = self.get_ag_ta()
        self.agent = ag_ta[0]
        self.target = ag_ta[1]
        self.agent_start = self.agent
        self.env = self.get_env()
        self.vel = WIDTH_MAX // self.env_len
        self.shape = self.vel - 1
        self.width = self.vel * self.env_len + 1
        self.height = self.width
        if self.visual:
            img = Image(self.shape, self.width, self.height)
            self.images = img.load_img()
            self.carImg_up = self.images[0]
            self.carImg_down = self.images[1]
            self.carImg_left = self.images[2]
            self.carImg_right = self.images[3]
            self.floor = self.images[4]
            self.wall = self.images[5]
            self.star = self.images[6]
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(f"{self.env_len}x{self.env_len}")
        # Training
        try:
            self.q_table = np.load("q_table.npy")
        except FileNotFoundError:
            self.q_table = np.zeros((self.env_len, self.env_len))
        self.target_reward = 2
        self.hole_reward = -2
        self.empty_step_reward = self.hole_reward / ((self.env_len - 1) * 4)

    def play(self):
        pygame.display.set_caption("GridWorld")
        while self.run:
            over = False
            state = self.reset()
            while not over:
                action = np.argmax(self.q_table[state[0]][state[1]])
                state, _, over, _, _ = self.move(action)
        pygame.display.quit()

    def show_env(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.win.fill(BLACK)
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.display.quit()

    def move(self, action):
        converged = False
        over = False
        failed = False
        reward = 0
        if self.visual:
            self.draw_game_visual(action)
        else:
            self.draw_game_non_visual()
        if action == UP:
            self.agent[0] -= 1
        elif action == DOWN:
            self.agent[0] += 1
        elif action == RIGHT:
            self.agent[1] += 1
        elif action == LEFT:
            self.agent[1] -= 1
        if self.agent[0] < 0 or self.agent[1] < 0 or self.agent[0] >\
                self.env_len-1 or self.agent[1] > self.env_len-1:
            over = True
            reward = self.hole_reward
        elif self.agent[0] == self.target[0] and\
                self.agent[1] == self.target[1]:
            over = True
            reward = self.target_reward
        elif self.env[self.agent[0]][self.agent[1]] == 99:
            over = True
            reward = self.hole_reward
        else:
            reward = self.empty_step_reward
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                over = True
                converged = True
                failed = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if not self.game_flip:
                    self.game_flip = True
                elif self.game_flip:
                    self.game_flip = False
            elif keys[pygame.K_r]:
                over = True
            elif keys[pygame.K_q]:
                converged = True
                over = True
                failed = True
        return self.agent.copy(), reward, over, converged, failed

    def get_ag_ta(self):
        agent = []
        target = []
        for i in range(self.env_len):
            for j in range(self.env_len):
                if self.envi[i][j] == AGENT:
                    agent = [i, j]
                elif self.envi[i][j] == TARGET:
                    target = [i, j]
                else:
                    pass
        return agent.copy(), target.copy()

    def get_env(self):
        env = self.envi.copy()
        env[self.agent[0]][self.agent[1]] = 0
        # env[self.target[0]][self.target[1]] = 0
        return env

    def reset(self):
        self.agent = self.agent_start.copy()
        return self.agent.copy()

    def draw_game_non_visual(self):
        self.win.fill(BLACK)
        for i in range(self.env_len+1):
            pygame.draw.line(self.win, WHITE, (i*self.vel, 0),
                             (i*self.vel, self.env_len*self.vel))
            pygame.draw.line(self.win, WHITE, (0, i*self.vel),
                             (self.env_len*self.vel, i*self.vel))
        for i in range(self.env_len):
            for j in range(self.env_len):
                if self.env[i][j] == HOLE:
                    pygame.draw.rect(self.win, RED,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                else:
                    value = max(self.q_table[i][j])
                    if value > 0:
                        value *= 100
                        if value > 255:
                            value = 255
                        else:
                            pass
                        pygame.draw.rect(self.win, (0, 0, value),
                                         (self.vel*j+1, self.vel*i+1,
                                          self.shape, self.shape))
        pygame.draw.rect(self.win, GREEN,
                         (self.vel*self.target[1]+1,
                          self.vel*self.target[0]+1, self.shape, self.shape))
        pygame.draw.rect(self.win, YELLOW,
                         (self.vel*self.agent[1]+1,
                          self.vel*self.agent[0]+1, self.shape, self.shape))
        if self.game_flip:
            pygame.display.flip()
            self.clock.tick(self.fps)

    def draw_game_visual(self, dirr):
        start_pos = [self.agent[0]*self.vel+1, self.agent[1]*self.vel+1]
        for frame in range(int(self.vel/DRAW_VEL)):
            self.win.blit(self.floor, (0, 0))
            for i in range(self.env_len+1):
                pygame.draw.line(self.win, WHITE, (i*self.vel, 0),
                                 (i*self.vel, self.env_len*self.vel))
                pygame.draw.line(self.win, WHITE, (0, i*self.vel),
                                 (self.env_len*self.vel, i*self.vel))
            for i in range(self.env_len):
                for j in range(self.env_len):
                    if self.env[i][j] == 99:
                        self.win.blit(self.wall, (self.vel*j+1, self.vel*i+1))
            """
            pygame.draw.rect(self.win, YELLOW,
                             (start_pos[1],
                              start_pos[0], SHAPE, SHAPE))
            """
            self.win.blit(self.star, (self.vel*self.target[1]+1,
                                      self.vel*self.target[0]+1))
            if dirr == UP:
                self.win.blit(self.carImg_up,
                              (start_pos[1], start_pos[0]))
                start_pos[0] -= DRAW_VEL
            elif dirr == RIGHT:
                self.win.blit(self.carImg_right,
                              (start_pos[1], start_pos[0]))
                start_pos[1] += DRAW_VEL
            elif dirr == DOWN:
                self.win.blit(self.carImg_down,
                              (start_pos[1], start_pos[0]))
                start_pos[0] += DRAW_VEL
            elif dirr == LEFT:
                self.win.blit(self.carImg_left,
                              (start_pos[1], start_pos[0]))
                start_pos[1] -= DRAW_VEL
            if self.game_flip:
                pygame.display.flip()
                self.clock.tick(self.fps)

    def draw_board(self):
        for i in range(self.env_len+1):
            pygame.draw.line(self.win, WHITE, (i*self.vel, 0),
                             (i*self.vel, self.env_len*self.vel))
            pygame.draw.line(self.win, WHITE, (0, i*self.vel),
                             (self.env_len*self.vel, i*self.vel))
        for i in range(self.env_len):
            for j in range(self.env_len):
                if self.envi[i][j] == HOLE:
                    pygame.draw.rect(self.win, RED,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == TARGET:
                    pygame.draw.rect(self.win, GREEN,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == AGENT:
                    pygame.draw.rect(self.win, YELLOW,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))


class Training(GridWorld):

    def __init__(self, visual=False):
        super().__init__(visual=visual)
        # self.epsilon = 0
        # self.alpha = 0
        self.gamma = 1
        self.P = [1, 1, 1, 1]
        self.empty_step_reward = -1
        self.target_reward = 10
        self.hole_reward = -self.env_len*self.env_len
        self.game = Create(size=self.env_len)

    def get_state_val(self, state_):
        # all possible next states
        next_state = [[state_[0]-1, state_[1]], [state_[0], state_[1]+1],
                      [state_[0], state_[1]-1], [state_[0]+1, state_[1]]]
        vals = list()
        for i, item in enumerate(next_state):
            try:
                if item[0] >= 0 and item[1] >= 0:
                    vals.append(self.empty_step_reward + self.gamma *
                                self.q_table[item[0]][item[1]]*self.P[i])
                else:
                    pass
            except IndexError:
                pass
        return max(vals)

    def train(self):
        self.q_table = np.zeros((self.env_len, self.env_len))
        for i in range(self.env_len):
            for j in range(self.env_len):
                if self.env[i][j] == HOLE:
                    self.q_table[i][j] = self.hole_reward
                elif self.env[i][j] == TARGET:
                    self.q_table[i][j] = self.target_reward
        start_table = self.q_table.copy()
        temp_value = start_table.copy()
        run = True
        while run:
            run = self.game.show_table(self.q_table, self.target_reward)
            for i in range(self.env_len):
                for j in range(self.env_len):
                    if self.env[i][j] == TARGET:
                        pass
                    elif self.env[i][j] == HOLE:
                        pass
                    else:
                        temp_value[i][j] = self.get_state_val([i, j])
            self.q_table = temp_value.copy()
            temp_value = start_table.copy()
        self.game.show_table(self.q_table, self.target_reward)
        pygame.display.quit()


class Optimize(GridWorld):

    def __init__(self, visual=False):
        super().__init__(visual=visual)
        self.state_list = []
        self.action_list = []

    def play(self):
        over = False
        self.action_list.clear()
        self.state_list.clear()
        state = self.reset()
        self.state_list.append(state)
        while not over:
            action = np.argmax(self.q_table[state[0]][state[1]])
            self.action_list.append(action)
            state, _, over, _, _ = self.move(action)
            self.state_list.append(state)

    def fix(self):
        count = 0
        for ind in range(len(self.action_list)-2):
            first = self.action_list[ind]
            second = self.action_list[ind+1]
            third = self.action_list[ind+2]
            s1 = self.state_list[ind]
            s2 = self.state_list[ind+1]
            s3 = self.state_list[ind+2]
            first_to_second_failed = False
            second_to_third_failed = False
            if first != second and second != third:
                print("diff")
                if third == UP:
                    if self.env[s2[0]-1][s2[1]] == HOLE:
                        second_to_third_failed = True
                    else:
                        self.q_table[s2[0]][s2[1]][third] = \
                            self.target_reward
                        self.q_table[s2[0]][s2[1]][second] = 0
                elif third == DOWN:
                    if self.env[s2[0]+1][s2[1]] == HOLE:
                        second_to_third_failed = True
                    else:
                        self.q_table[s2[0]][s2[1]][third] = \
                            self.target_reward
                        self.q_table[s2[0]][s2[1]][second] = 0
                elif third == LEFT:
                    if self.env[s2[0]][s2[1]-1] == HOLE:
                        second_to_third_failed = True
                    else:
                        self.q_table[s2[0]][s2[1]][third] = \
                            self.target_reward
                        self.q_table[s2[0]][s2[1]][second] = 0
                elif third == RIGHT:
                    if self.env[s2[0]][s2[1]+1] == HOLE:
                        second_to_third_failed = True
                    else:
                        self.q_table[s2[0]][s2[1]][third] = \
                            self.target_reward
                        self.q_table[s2[0]][s2[1]][second] = 0
                if not second_to_third_failed:
                    print("2 to 3")
                    if third == UP:
                        self.q_table[s2[0]-1][s2[1]][second] = \
                            self.target_reward
                        self.q_table[s3[0]][s3[1]][third] = 0
                    elif third == DOWN:
                        self.q_table[s2[0]+1][s2[1]][second] = \
                            self.target_reward
                        self.q_table[s3[0]][s3[1]][third] = 0
                    elif third == RIGHT:
                        self.q_table[s2[0]][s2[1]+1][second] = \
                            self.target_reward
                        self.q_table[s3[0]][s3[1]][third] = 0
                    elif third == LEFT:
                        self.q_table[s2[0]][s2[1]-1][second] = \
                            self.target_reward
                        self.q_table[s3[0]][s3[1]][third] = 0
                    break
                else:
                    if second == UP:
                        if self.env[s1[0]-1][s1[1]] == HOLE:
                            first_to_second_failed = True
                        else:
                            self.q_table[s1[0]][s1[1]][second] = \
                                self.target_reward
                            self.q_table[s1[0]][s1[1]][first] = 0
                    elif second == DOWN:
                        if self.env[s1[0]+1][s1[1]] == HOLE:
                            first_to_second_failed = True
                        else:
                            self.q_table[s1[0]][s1[1]][second] = \
                                self.target_reward
                            self.q_table[s1[0]][s1[1]][first] = 0
                    elif second == LEFT:
                        if self.env[s1[0]][s1[1]-1] == HOLE:
                            first_to_second_failed = True
                        else:
                            self.q_table[s1[0]][s1[1]][second] = \
                                self.target_reward
                            self.q_table[s1[0]][s1[1]][first] = 0
                    elif second == RIGHT:
                        if self.env[s1[0]][s1[1]+1] == HOLE:
                            first_to_second_failed = True
                        else:
                            self.q_table[s1[0]][s1[1]][second] = \
                                self.target_reward
                            self.q_table[s1[0]][s1[1]][first] = 0
                    if not first_to_second_failed:
                        print("1 to 2")
                        if second == UP:
                            self.q_table[s1[0]-1][s1[1]][first] = \
                                self.target_reward
                            self.q_table[s2[0]][s2[1]][second] = 0
                        elif second == DOWN:
                            self.q_table[s1[0]+1][s1[1]][first] = \
                                self.target_reward
                            self.q_table[s2[0]][s2[1]][second] = 0
                        elif second == RIGHT:
                            self.q_table[s1[0]][s1[1]+1][first] = \
                                self.target_reward
                            self.q_table[s2[0]][s2[1]][second] = 0
                        elif second == LEFT:
                            self.q_table[s1[0]][s1[1]-1][first] = \
                                self.target_reward
                            self.q_table[s2[0]][s2[1]][second] = 0
                        break
                    else:
                        print("failed")
                        count += 1
            else:
                count += 1
            continue
        return count


class Path(Optimize):

    def __init__(self, visual=False):
        super().__init__(visual=visual)
        self.play()
        self.place()
        self.show_env()

    def place(self):
        for i in range(len(self.action_list)):
            self.envi[self.state_list[i][0]][self.state_list[i][1]] = \
                self.action_list[i]+1

    def draw_board(self):
        for i in range(self.env_len+1):
            pygame.draw.line(self.win, WHITE, (i*self.vel, 0),
                             (i*self.vel, self.env_len*self.vel))
            pygame.draw.line(self.win, WHITE, (0, i*self.vel),
                             (self.env_len*self.vel, i*self.vel))
        for i in range(self.env_len):
            for j in range(self.env_len):
                if self.envi[i][j] == HOLE:
                    pygame.draw.rect(self.win, RED,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == TARGET:
                    pygame.draw.rect(self.win, GREEN,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == AGENT:
                    pygame.draw.rect(self.win, YELLOW,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == UP+1:
                    pygame.draw.rect(self.win, WHITE,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == DOWN+1:
                    pygame.draw.rect(self.win, WHITE,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == LEFT+1:
                    pygame.draw.rect(self.win, WHITE,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
                elif self.envi[i][j] == RIGHT+1:
                    pygame.draw.rect(self.win, WHITE,
                                     (self.vel*j+1, self.vel*i+1,
                                      self.shape, self.shape))
