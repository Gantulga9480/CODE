import numpy as np
import random


class NN:

    def __init__(self, lr=0.1):
        self.alpha = lr
        self.weight_1 = np.random.uniform(low=-1, high=1, size=(400, 64))
        self.weight_2 = np.random.uniform(low=-1, high=1, size=(64, 64))
        self.weight_3 = np.random.uniform(low=-1, high=1, size=(64, 64))
        self.weight_4 = np.random.uniform(low=-1, high=1, size=(64, 4))
        self.bias_1 = np.random.uniform(low=-1, high=1, size=(64))
        self.bias_2 = np.random.uniform(low=-1, high=1, size=(64))
        self.bias_3 = np.random.uniform(low=-1, high=1, size=(64))
        self.bias_4 = np.random.uniform(low=-1, high=1, size=(4))
        self.weights = [self.weight_1, self.weight_2,
                        self.weight_3, self.weight_4]
        self.biases = [self.bias_1, self.bias_2,
                       self.bias_3, self.bias_4]

    def __sub__(self, other):
        diff = np.sum(self.weight_1 - other)
        return True if diff == 0 else False

    def load_out(self):
        return self.weights.copy(), self.biases.copy()

    def load_in(self, wb):
        self.weight_1 = wb[0][0]
        self.weight_2 = wb[0][1]
        self.weight_3 = wb[0][2]
        self.weight_4 = wb[0][3]
        self.bias_1 = wb[1][0]
        self.bias_2 = wb[1][1]
        self.bias_3 = wb[1][2]
        self.bias_4 = wb[1][3]

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x))

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def d_sigmoid(self, x):
        return x * (1 - x)

    def relu(self, x):
        return x * (x > 0)

    def d_relu(self, x):
        return 1 * (x > 0)

    def linear(self, x):
        return x

    def d_linear(self, x):
        return 1

    def cost(self, target, prediction):
        return (prediction - target) ** 2

    def feed(self, x):
        d1 = self.relu(np.dot(x, self.weight_1) + self.bias_1)
        d2 = self.relu(np.dot(d1, self.weight_2) + self.bias_2)
        d3 = self.relu(np.dot(d2, self.weight_3) + self.bias_3)
        h = self.linear(np.dot(d3, self.weight_4) + self.bias_4)
        return h, d3, d2, d1

    def fit(self, h, d3, d2, d1, target, inpt):
        d_weight_4 = np.dot(d3[np.newaxis].T,
                            np.array([2 * (h - target) * 1]))
        delta_3 = np.dot(2 * (h - target) * 1,
                         self.weight_4.T)
        d_weight_3 = np.dot(d2[np.newaxis].T,
                            np.array([delta_3 * self.d_relu(d3)]))
        delta_2 = np.dot(delta_3 * self.d_relu(d3),
                         self.weight_3.T)
        d_weight_2 = np.dot(d1[np.newaxis].T,
                            np.array([delta_2 * self.d_relu(d2)]))
        delta_1 = np.dot(delta_2 * self.d_relu(d2),
                         self.weight_2.T)
        d_weight_1 = np.dot(inpt[np.newaxis].T,
                            np.array([delta_1 * self.d_relu(d1)]))

        d_bias_4 = 2 * (h - target) * 1
        d_bias_3 = np.dot(d_bias_4, self.weight_4.T) * self.d_relu(d3)
        d_bias_2 = np.dot(d_bias_3, self.weight_3.T) * self.d_relu(d2)
        d_bias_1 = np.dot(d_bias_2, self.weight_2.T) * self.d_relu(d1)

        """
        d_weight_4 = np.dot(d3[np.newaxis].T,
                            np.array([2 * (h - target) * 1]))
        delta_3 = np.dot(2 * (h - target) * 1,
                         self.weight_4.T)
        d_weight_3 = np.dot(d2[np.newaxis].T,
                            np.array([delta_3 * 1]))
        delta_2 = np.dot(delta_3 * 1,
                         self.weight_3.T)
        d_weight_2 = np.dot(d1[np.newaxis].T,
                            np.array([delta_2 * 1]))
        delta_1 = np.dot(delta_2 * 1,
                         self.weight_2.T)
        d_weight_1 = np.dot(inpt[np.newaxis].T,
                            np.array([delta_1 * 1]))

        d_bias_4 = 2 * (h - target) * 1
        d_bias_3 = np.dot(d_bias_4, self.weight_4.T) * 1
        d_bias_2 = np.dot(d_bias_3, self.weight_3.T) * 1
        d_bias_1 = np.dot(d_bias_2, self.weight_2.T) * 1
        """
        self.weight_1 -= self.alpha * d_weight_1
        self.weight_2 -= self.alpha * d_weight_2
        self.weight_3 -= self.alpha * d_weight_3
        self.weight_4 -= self.alpha * d_weight_4
        self.bias_1 -= self.alpha * d_bias_1
        self.bias_2 -= self.alpha * d_bias_2
        self.bias_3 -= self.alpha * d_bias_3
        self.bias_4 -= self.alpha * d_bias_4
