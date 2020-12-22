import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# tensorflow version
# print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

plt.imshow(train_images[1])
# print(train_labels[0])
# print(train_images[0])

