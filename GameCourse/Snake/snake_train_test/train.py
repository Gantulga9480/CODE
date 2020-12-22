import snake_game as sg
import new_snake_nn as sn
import numpy as np
import os
import random
# from tensorflow import keras
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Activation, Dense
# from tensorflow.keras.optimizers import Adam


def clear():
    os.system("cls")


REPLAY_BUFFER = list()
SAMPLES = list()


BUFFER_SIZE = 50000
MIN_BUFFER_SIZE = 100
BATCH_SIZE = 32
DISCOUNT_RATE = 0.99
LEARNING_RATE = 0.001
EPSILON = 1
MIN_EPSILON = 0.02
TARGET_NET_UPDATE_FREQUENCY = 500
EPSILON_DECAY = .999985


sg.init()
game = sg.Snake()
main_nn = sn.NN(lr=LEARNING_RATE)
target_nn = sn.NN(lr=LEARNING_RATE)
target_nn.load_in(main_nn.load_out())
frame = 1


def train():
    def loss():
        total_loss = 0
        for item in SAMPLES:
            total_loss += np.sum((main_nn.feed(item[0])[0] - item[4])**2)/4
        mean_loss = total_loss/BATCH_SIZE
        if mean_loss < 0.1 or a > 10000:
            return True, mean_loss
        else:
            return False, mean_loss

    converged = False
    a = 0
    i = 0
    while not converged:
        inpt = SAMPLES[i][0]
        target = y[i]
        h, d3, d2, d1 = main_nn.feed(inpt)
        main_nn.fit(h, d3, d2, d1, target, inpt)
        if a % 100 == 0:
            converged, ml = loss()
            print("in training", a, "with mean loss", ml)
        a += 1
        i += 1
        if i == BATCH_SIZE:
            i = 0


def calculate_target():
    print("in calculcate target")
    target_qs = []
    for i in range(len(SAMPLES)):
        a = main_nn.feed(SAMPLES[i][0])[0]
        if SAMPLES[i][4]:
            a[SAMPLES[i][1]] = SAMPLES[i][3]
            target_qs.append(a)
        else:
            a[SAMPLES[i][1]] = SAMPLES[i][3] +\
                DISCOUNT_RATE * max(target_nn.feed(SAMPLES[i][2])[0])
            target_qs.append(a)
    return target_qs.copy()


for episode in range(10000):
    state = game.reset()
    terminal = False
    while not terminal:
        frame += 1
        EPSILON = max(EPSILON*EPSILON_DECAY, MIN_EPSILON)
        if np.random.random() < EPSILON:
            action = np.random.randint(0, 3)
        else:
            action = np.argmax(main_nn.feed(state)[0])
        terminal, next_state, r = game.step(action=action, auto=False)

        if len(REPLAY_BUFFER) == BUFFER_SIZE:
            REPLAY_BUFFER.pop(0)
            REPLAY_BUFFER.append([state, action, next_state, r, terminal])
        else:
            REPLAY_BUFFER.append([state, action, next_state, r, terminal])

        if len(REPLAY_BUFFER) > MIN_BUFFER_SIZE:
            clear()
            print("Preparing nn in episode", episode)
            SAMPLES = random.sample(REPLAY_BUFFER, BATCH_SIZE)
            y = calculate_target()
            train()

        if frame % TARGET_NET_UPDATE_FREQUENCY == 0:
            print("TARGET NET UPDATED in episode", episode)
            target_nn.load_in(main_nn.load_out())


print("Training done congrat!!!")
np.save("snake_model/weight_1.npy", main_nn.weight_1)
np.save("snake_model/weight_2.npy", main_nn.weight_2)
np.save("snake_model/weight_3.npy", main_nn.weight_3)
np.save("snake_model/weight_4.npy", main_nn.weight_4)
np.save("snake_model/bias_1.npy", main_nn.bias_1)
np.save("snake_model/bias_2.npy", main_nn.bias_2)
np.save("snake_model/bias_3.npy", main_nn.bias_3)
np.save("snake_model/bias_4.npy", main_nn.bias_4)
