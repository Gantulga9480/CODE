import numpy as np
import random


class NN:

    def __init__(self):
        self.alpha = 0.1
        self.weight_1 = 2 * np.random.random((2, 4)) - 1
        self.weight_2 = 2 * np.random.random((4, 1)) - 1
        self.bias_1 = 2 * np.random.random((4)) - 1
        self.bias_2 = 2 * np.random.random((1)) - 1

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
        d = self.sigmoid(np.dot(x, self.weight_1) + self.bias_1)
        h = self.sigmoid(np.dot(d, self.weight_2) + self.bias_2)
        return h, d

    def fit(self, h, d):
        delta_D = np.dot(2 * (h - y[i]) * self.d_sigmoid(h), self.weight_2.T)
        d_weight_2 = np.dot(d[np.newaxis].T, np.array([2 * (h - y[i]) * self.d_sigmoid(h)]))
        d_weight_1 = np.dot(x[i][np.newaxis].T, np.array([delta_D * self.d_sigmoid(d)]))
        d_bias_2 = 2 * (h - y[i]) * self.d_sigmoid(h)
        d_bias_1 = np.dot(d_bias_2, self.weight_2.T) * self.d_sigmoid(d)
        self.weight_1 -= self.alpha * d_weight_1
        self.weight_2 -= self.alpha * d_weight_2
        self.bias_1 -= self.alpha * d_bias_1
        self.bias_2 -= self.alpha * d_bias_2



# np.random.seed()
x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])

nn = NN()

for itr in range(50000):
    i = random.randint(0, 3)
    h, d = nn.predict(x[i])
    nn.fit(h, d)

print(x[0], "-->", nn.predict(x[0])[0])
print(x[1], "-->", nn.predict(x[1])[0])
print(x[2], "-->", nn.predict(x[2])[0])
print(x[3], "-->", nn.predict(x[3])[0])
