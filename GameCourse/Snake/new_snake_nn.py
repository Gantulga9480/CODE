import numpy as np
import random


class NN:

    def __init__(self):
        self.alpha = 0.1
        self.weight_1 = 2 * np.random.random((400, 512)) - 1
        self.weight_2 = 2 * np.random.random((512, 512)) - 1
        self.weight_3 = 2 * np.random.random((512, 512)) - 1
        self.weight_4 = 2 * np.random.random((512, 4)) - 1
        self.bias_1 = 2 * np.random.random((512)) - 1
        self.bias_2 = 2 * np.random.random((512)) - 1
        self.bias_3 = 2 * np.random.random((512)) - 1
        self.bias_4 = 2 * np.random.random((4)) - 1

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x))

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def d_sigmoid(self, x):
        return x * (1 - x)

    def relu(self, x):
        return np.array([0 if x[i] < 0 else x[i] for i in range(len(x))])

    def cost(self, target, prediction):
        return (prediction - target) ** 2

    def predict(self, x):
        d1 = self.sigmoid(np.dot(x, self.weight_1) + self.bias_1)
        d2 = self.sigmoid(np.dot(d1, self.weight_2) + self.bias_2)
        d3 = self.sigmoid(np.dot(d2, self.weight_3) + self.bias_3)
        h = self.sigmoid(np.dot(d3, self.weight_4) + self.bias_4)
        return h, d3, d2, d1

    def fit(self, h, d3, d2, d1, target, inpt):
        d_weight_4 = np.dot(d3[np.newaxis].T, np.array([2 * (h - target) * self.d_sigmoid(h)]))
        delta_3 = np.dot(2 * (h - target) * self.d_sigmoid(h), self.weight_4.T)
        d_weight_3 = np.dot(d2[np.newaxis].T, np.array([delta_3 * self.d_sigmoid(d3)]))
        delta_2 = np.dot(delta_3 * self.d_sigmoid(d3), self.weight_3.T)
        d_weight_2 = np.dot(d1[np.newaxis].T, np.array([delta_2 * self.d_sigmoid(d2)]))
        delta_1 = np.dot(delta_2 * self.d_sigmoid(d2), self.weight_2.T)
        d_weight_1 = np.dot(inpt[np.newaxis].T, np.array([delta_1 * self.d_sigmoid(d1)]))

        d_bias_4 = 2 * (h - target) * self.d_sigmoid(h)
        d_bias_3 = np.dot(d_bias_4, self.weight_4.T) * self.d_sigmoid(d3)
        d_bias_2 = np.dot(d_bias_3, self.weight_3.T) * self.d_sigmoid(d2)
        d_bias_1 = np.dot(d_bias_2, self.weight_2.T) * self.d_sigmoid(d1)

        self.weight_1 -= self.alpha * d_weight_1
        self.weight_2 -= self.alpha * d_weight_2
        self.weight_3 -= self.alpha * d_weight_3
        self.weight_4 -= self.alpha * d_weight_4
        self.bias_1 -= self.alpha * d_bias_1
        self.bias_2 -= self.alpha * d_bias_2
        self.bias_3 -= self.alpha * d_bias_3
        self.bias_4 -= self.alpha * d_bias_4
