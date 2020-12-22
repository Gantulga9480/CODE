import numpy as np
import numpy as n
import os
import matplotlib.pyplot as plt
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
        self.target_reward = 1
        self.out_reward = -1
        self.step_reward = -0.05
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_flip = False
        self.fps = 60
        self.best = False

    def play(self, q_table=None, itr=1):
        self.game_flip = False
        self.fps = 20
        total_action = 0
        game_win = False
        for _ in range(itr):
            over = False
            state = self.reset()
            total_action = 0
            while not over:
                action = np.argmax(q_table[state[0]][state[1]])
                state, rew, over = self.move(action)
                total_action += 1
                if total_action > 28:
                    over = True
            if rew == self.target_reward:
                game_win = True
            else:
                game_win = False
            # if self.target[0] == self.agent[0] and self.target[1] == self.agent[1]:
                # print(act, "Won")
            # else:
                # print(act, "Over")
        return total_action, game_win

    def make_env(self):
        self.env = np.zeros((self.env_row, self.env_column), dtype=int)
        self.env[0][2] = 99
        self.env[1][2] = 99
        self.env[2][2] = 99
        self.env[0][3] = 99
        self.env[1][3] = 99
        self.env[2][3] = 99
        self.env[self.target[0]][self.target[1]] = 8

    def draw_game(self, q_table):
        for i in range(7):
            pygame.draw.line(self.win, WHITE, (i*VEL, 0), (i*VEL, 360))
            pygame.draw.line(self.win, WHITE, (0, i*VEL), (360, i*VEL))
        for i in range(self.env_row):
            for j in range(self.env_row):
                if self.env[i][j] == 99:
                    pygame.draw.rect(self.win, RED, (VEL*j+1, VEL*i+1, SHAPE, SHAPE))
                else:
                    value = max(q_table[i][j])
                    if value > 0:
                        value *= 100
                        if value > 255:
                            value = 255
                        else:
                            value *= 2
                        pygame.draw.rect(self.win, (0, 0, value), (VEL*j+1, VEL*i+1, SHAPE, SHAPE))
        pygame.draw.rect(self.win, YELLOW, (VEL*self.agent[1]+1, VEL*self.agent[0]+1, SHAPE, SHAPE))
        pygame.draw.rect(self.win, GREEN, (VEL*self.target[1]+1, VEL*self.target[0]+1, SHAPE, SHAPE))

    def get_path(self, q_table):
        path = np.zeros((self.env_row, self.env_column), dtype='<U11')
        for i in range(self.env_row):
            for j in range(self.env_column):
                action = np.argmax(q_table[i][j])
                if action == 0:
                    path[i][j] = "↑"
                elif action == 1:
                    path[i][j] = "↓"
                elif action == 2:
                    path[i][j] = "→"
                elif action == 3:
                    path[i][j] = "←"
        return path

    def reset(self):
        self.make_env()
        self.agent = [0, 0]
        return self.agent.copy()

    def move(self, action):
        self.win.fill(BLACK)
        self.draw_game(q_table)
        over = False
        if self.game_flip:
            pygame.display.flip()
            clock.tick(self.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.game_flip:
                        self.game_flip = True
                    elif self.game_flip:
                        self.game_flip = False
                elif event.key == pygame.K_r:
                    over = True
                elif event.key == pygame.K_q:
                    over = True
                    env.best = True
        if action == 0:
            self.agent[0] -= 1
        elif action == 1:
            self.agent[0] += 1
        elif action == 2:
            self.agent[1] += 1
        elif action == 3:
            self.agent[1] -= 1
        self.make_env()
        if self.agent[0] < 0 or self.agent[0] > len(self.env[0]) - 1 or self.agent[1] < 0 or self.agent[1] > len(self.env[0]) - 1:
            over = True
            reward = self.out_reward
        elif self.agent[0] == self.target[0] and self.agent[1] == self.target[1]:
            self.env[self.agent[0]][self.agent[1]] = 1
            over = True
            reward = self.target_reward
        elif self.env[self.agent[0]][self.agent[1]] == 99:
            over = True
            reward = self.out_reward
        else:
            self.env[self.agent[0]][self.agent[1]] = 1
            reward = self.step_reward
        return self.agent.copy(), reward, over

# 0 = up
# 1 = down
# 2 = left
# 3 = right


pygame.init()
pygame.display.set_caption("Simple GridWorld")
clock = pygame.time.Clock()
env = GridWorld()
np.random.seed(1)
max_iter = 2500
epsilon_min = 0

discount = 0.9
episode_reward = 0
avg_move_count = 100
best_q_table = None

act = 1
ep_reward = []
avg_move = []
num_actins = {'ep': [], 'lr': [], 'eps': [], 'act': []}
# num_actins = {'ep': [], 'avg': [], 'min': [], 'max': [], 'eps': []}
while not env.best:
    q_table = np.zeros((6, 6, 4))
    epsilon = n.random.randint(1, 99)/100
    starting_eps = epsilon
    learning_rate = n.random.randint(1, 99)/100
    epsilon_decay_val = (epsilon-epsilon_min) / (max_iter*0.9)
    for i in range(max_iter):
        over = False
        episode_reward = 0
        state = env.reset()
        actions = 0
        while not over:
            if np.random.random() > epsilon:
                action = np.argmax(q_table[state[0]][state[1]])
            else:
                action = np.random.randint(0, 3)
            new_state, reward, over = env.move(action)
            actions += 1
            episode_reward += reward
            if not over:
                max_future_q_value = np.max(q_table[new_state[0]][new_state[1]])
                current_q_value = q_table[state[0]][state[1]][action]
                new_q_value = current_q_value+learning_rate *\
                    (reward+discount*max_future_q_value-current_q_value)
                q_table[state[0]][state[1]][action] = new_q_value
                if actions > 28:
                    epsilon += 0.1
            elif over:
                avg_move.append(actions)
                if len(avg_move) >= avg_move_count:
                    if sum(avg_move[-avg_move_count:])/avg_move_count < 3:
                        epsilon += 0.1
                q_table[state[0]][state[1]][action] = reward
                if reward == env.target_reward:
                    if actions == 11:
                        print(f"{act} BEST episode with lr={learning_rate} eps={epsilon}")
                        actions, win = env.play(q_table=q_table)
                        if actions == 11:
                            epsilon = 0
                            best_q_table = q_table
                            np.save(f"best_q_table={actions}-lr={learning_rate}-eps={starting_eps}.npy", q_table)
            state = new_state
        epsilon = max(epsilon - epsilon_decay_val, epsilon_min)
    actions, win = env.play(q_table=q_table)
    if not win:
        print(f"{act} Training failed with lr={learning_rate} eps={starting_eps}")
    elif actions == 11:
        print(f"{act} Best training with lr={learning_rate} eps={starting_eps}")
        file_name = f"best_q_table={actions}-lr={learning_rate}-eps={starting_eps}.npy"
        np.save(file_name, q_table)
        best_q_table = q_table
        env.best = True
        num_actins['ep'].append(act)
        num_actins['lr'].append(learning_rate)
        num_actins['eps'].append(starting_eps)
        num_actins['act'].append(actions/10)
    else:
        file_name = f"q_table={actions}-lr={learning_rate}-eps={starting_eps}.npy"
        np.save(file_name, q_table)
        num_actins['ep'].append(act)
        num_actins['lr'].append(learning_rate)
        num_actins['eps'].append(starting_eps)
        num_actins['act'].append(actions/10)
    act += 1

plt.plot(num_actins['ep'], num_actins['lr'], label="lr")
plt.plot(num_actins['ep'], num_actins['eps'], label="eps")
plt.plot(num_actins['ep'], num_actins['act'], label="act")
plt.legend(loc=4)
plt.show()
env.game_flip = True
env.play(q_table=best_q_table, itr=1000)
pygame.quit()
