import snake_game as sg
import new_snake_nn as sn
import numpy as np
import os
import random
from collections import deque
from tensorflow import keras
from tensorflow.keras.models import Sequential, save_model, load_model
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam

GOAL = 20
BUFFER_SIZE = 100000
MIN_BUFFER_SIZE = 20000
BATCH_SIZE = 16
DISCOUNT_RATE = 0.999
LEARNING_RATE = 0.0001
EPSILON = 1
MIN_EPSILON = 0.01
EPSILON_DECAY = 0.001
TARGET_NET_UPDATE_FREQUENCY = 5000

REPLAY_BUFFER = deque(maxlen=BUFFER_SIZE)
SAMPLES = list()

TRAIN_COUNT = 1
FRAME = 1
EPISODE = 1


class MyCallback(keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs=None):
        if logs.get('accuracy') > 0.9:
            self.model.stop_training = True


def get_model():
    model = Sequential()
    model.add(Dense(512, input_dim=400, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(64, activation="relu"))
    # model.add(Dense(32, activation="relu"))
    # model.add(Dense(16, activation="relu"))
    # model.add(Dense(8, activation="relu"))
    model.add(Dense(3, activation="linear"))
    model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE),
                  metrics=["accuracy"])
    return model


sg.init()
game = sg.Snake()
main_nn = get_model()
target_nn = get_model()
target_nn.set_weights(main_nn.get_weights())
callbacks = MyCallback()
avg_reward = deque(maxlen=1000)
last_avg = 0
show_every = 50
ep_reward = 0


def keras_train():
    SAMPLES = random.sample(REPLAY_BUFFER, BATCH_SIZE)
    current_states = np.array([item[0] for item in SAMPLES])
    new_current_state = np.array([item[2] for item in SAMPLES])
    current_qs_list = []
    future_qs_list = []
    current_qs_list = main_nn.predict(current_states)
    future_qs_list = target_nn.predict(new_current_state)

    X = []
    Y = []
    for index, (state, action, n_state, reward, done) in enumerate(SAMPLES):
        if not done:
            new_q = reward + DISCOUNT_RATE * np.max(future_qs_list[index])
        else:
            new_q = reward

        current_qs = current_qs_list[index]
        current_qs[action] = new_q

        X.append(state)
        Y.append(current_qs)
    main_nn.fit(np.array(X), np.array(Y), epochs=20,
                batch_size=BATCH_SIZE, shuffle=False,
                verbose=0, callbacks=[callbacks])


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
    EPSILON = max(EPSILON - EPSILON_DECAY, MIN_EPSILON)

print("Training done congrat!!!")
main_nn.save("main")
target_nn.save("target")
