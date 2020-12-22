import snake_game as sg
import snake_brain as sb
import numpy as np
# from tensorflow import keras

sg.init()
game = sg.Snake()
# model = keras.models.load_model('target')

for episode in range(10000):
    state = game.reset()
    done = False
    while not done:
        # action = np.argmax(model.predict(np.expand_dims(state, axis=0)))
        done, state, _ = game.step(auto=True)
