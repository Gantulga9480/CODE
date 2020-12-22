import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential, save_model, load_model
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam


class MyCallback(keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs=None):
        if logs.get('accuracy') > 0.99:
            print("\nReached 90% accuracy so cancelling training!")
            self.model.stop_training = True


x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])
callbacks = MyCallback()
model = Sequential()
model.add(Dense(4, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss="mse", optimizer=Adam(lr=0.1), metrics=["accuracy"])

model.fit(x, y, epochs=500, batch_size=4, shuffle=True, callbacks=[callbacks])

a = model.predict(np.expand_dims(x[1], axis=0))
print(a, "\n")
b = model.predict(x)
print(b)
