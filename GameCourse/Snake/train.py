import snake_game as sg
import mynn as sn
import numpy as np
import os


REPLAY_BUFFER = list()
SAMPLES = list()
BUFFER_SIZE = 10000
BATCH_SIZE = 32
DISCOUNT_RATE = 0.99
LEARNING_RATE = 0.001
EPSILON = 1.0
MIN_EPSILON = 0.02
TARGET_NET_UPDATE_FREQUENCY = 1000
EPSILON_DECAY = .999985

sg.init()
game = sg.Snake()

main_nn = sn.NeuralNet([[400, "input"],
                        [512, "sigmoid"],
                        [512, "sigmoid"],
                        [512, "sigmoid"],
                        [4, "sigmoid"]], lr=LEARNING_RATE)
target_nn = sn.NeuralNet([[400, "input"],
                          [512, "sigmoid"],
                          [512, "sigmoid"],
                          [512, "sigmoid"],
                          [4, "sigmoid"]], lr=LEARNING_RATE)

frame_count = 0


def sample():
    SAMPLES.clear()
    while len(SAMPLES) < BATCH_SIZE:
        i = np.random.randint(len(REPLAY_BUFFER))
        if REPLAY_BUFFER[i][4] == "None":
            pass
        else:
            SAMPLES.append(REPLAY_BUFFER[i])
            REPLAY_BUFFER[i][4] = "None"


def calculate_target(samples):
    for i in range(len(samples)):
        a = [0, 0, 0, 0]
        if samples[i][4]:
            a[samples[i][1]] = samples[i][3]
            samples[i][4] = a
        else:
            a[samples[i][1]] = samples[i][3] + DISCOUNT_RATE * max(target_nn.feed(samples[i][2]))
            samples[i][4] = a
    return samples


for episode in range(10000):
    state = game.reset()
    done = False
    while not done:
        frame_count += 1
        EPSILON = max(EPSILON*EPSILON_DECAY, MIN_EPSILON)
        if np.random.random() < EPSILON:
            action = np.random.randint(4)
        else:
            action = np.argmax(target_nn.feed(state))
        done, next_state, r = game.step(action=action, auto=False)

        if episode % 50 == 0:
            SAMPLES = calculate_target(SAMPLES.copy)

        if frame_count % TARGET_NET_UPDATE_FREQUENCY == 0:
            main = main_nn.load_out()
            target_nn.load_in(main[0].copy(), main[1].copy())

        # replay memory for transitions
        if len(REPLAY_BUFFER) == BUFFER_SIZE:
            REPLAY_BUFFER.pop(0)
            REPLAY_BUFFER.append([state, action, next_state, r, done])
        else:
            REPLAY_BUFFER.append([state, action, next_state, r, done])
