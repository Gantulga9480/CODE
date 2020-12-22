import tensorflow as tf
from tensorflow import keras


class MyCallback(tf.keras.callbacks.Callback):

    def on_epoch_end(self, epoch, logs={}):
        if logs.get('acc') > 0.8:
            print("\nReached 90% \accuracy so cancelling training!")
            self.model.stop_training = True


callbacks = MyCallback()
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images = train_images.reshape(60000, 28, 28, 1)
test_images = test_images.reshape(10000, 28, 28, 1)
training_images = train_images / 255.0
test_images = test_images / 255.0
model = keras.Sequential([
    keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, callbacks=[callbacks])

test_loss, test_acc = model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)

print(classifications[0])
