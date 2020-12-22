import snake_game as sg
import numpy as np
import os
import random

GOAL = 10
BUFFER_SIZE = 100000
MIN_BUFFER_SIZE = 50000
BATCH_SIZE = 64
DISCOUNT_RATE = 0.99
LEARNING_RATE = 0.001
EPSILON = 1
MIN_EPSILON = 0.02
EPSILON_DECAY = .999985
TARGET_NET_UPDATE_FREQUENCY = 10000

REPLAY_BUFFER = deque(maxlen=BUFFER_SIZE)
SAMPLES = list()

TRAIN_COUNT = 1
FRAME = 1
EPISODE = 1




sg.init()
game = sg.Snake()
last_avg = 0
show_every = 1000
ep_reward = 0


while len(game.snake)-3 < GOAL:
    state = game.reset()
    terminal = False
    ep_reward = 0
    while not terminal:
        FRAME += 1
        if np.random.random() < EPSILON:
            action = np.random.randint(0, 2)
        else:
            action = np.argmax(main_nn.predict(np.expand_dims(state, axis=0)))
        terminal, next_state, r = game.step(action=action, auto=False)
        ep_reward += r

        REPLAY_BUFFER.append([state, action, next_state, r, terminal])

        if len(REPLAY_BUFFER) > MIN_BUFFER_SIZE:
            keras_train()
            TRAIN_COUNT += 1

        if FRAME % TARGET_NET_UPDATE_FREQUENCY == 0 and \
                len(REPLAY_BUFFER) > MIN_BUFFER_SIZE:
            target_nn.set_weights(main_nn.get_weights())
            print("target_net update!!!")
    avg_reward.append(ep_reward)
    if EPISODE % show_every == 0:
        avg = np.sum(avg_reward) / show_every
        if avg > last_avg:
            print("↑:", avg, "ep:", EPSILON, "frame:", FRAME)
        elif avg < last_avg:
            print("↓", avg, "ep:", EPSILON, "frame:", FRAME)
        last_avg = avg
    EPISODE += 1
    EPSILON = max(EPSILON * EPSILON_DECAY, MIN_EPSILON)

