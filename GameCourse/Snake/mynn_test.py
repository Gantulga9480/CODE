import numpy as np


class NeuralNet:

    def __init__(self, net=list(), lr=0.1):
        # np.random.seed(1)
        self.net = net
        self.learning_rate = lr
        self.l_count = len(net)
        self.weights = list()
        self.biases = list()
        self.outputs = list()
        self.deltas = list()
        # initialize weights and biases
        for i in range(self.l_count - 1):
            self.weights.append(np.random.uniform(low=-1,
                                                  high=1,
                                                  size=(net[i][0],
                                                        net[i+1][0])))
            self.biases.append(np.random.random(low=-1,
                                                high=1,
                                                size=(net[i+1][0])))

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x))

    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def d_sigmoid(self, x):
        return (x * (1 - x))

    def relu(self, x):
        return np.array([0 if x[i] < 0 else x[i] for i in range(len(x))])

    def cost(self, target, prediction):
        return (target - prediction) ** 2

    def accuracy(self):
        pass

    def load_out(self):
        return self.weights.copy(), self.biases.copy()

    def load_in(self, weights, biases):
        self.weights = weights
        self.biases = biases

    def feed(self, x):
        self.outputs.clear()
        self.outputs.append(x)
        for i in range(self.l_count - 1):
            if self.net[i+1][1] == "sigmoid":
                self.outputs.append(self.sigmoid(np.dot(x, self.weights[i]) +
                                    self.biases[i]))
                # print(self.outputs[i+1].shape, i)
            elif self.net[i+1][1] == "relu":
                self.outputs.append(self.relu(np.dot(x, self.weights[i]) +
                                    self.biases[i]))
            elif self.net[i+1][1] == "softmax":
                self.outputs.append(self.softmax(np.dot(x, self.weights[i]) +
                                    self.biases[i]))
            x = self.outputs[i+1]
        return self.outputs[self.l_count-1]

    def fit(self, target):
        self.deltas.clear()
        delta = 2 * (target-self.outputs[self.l_count-1])
        d_bias = 0
        d_weight = 0
        for i in range(self.l_count - 1):
            d_weight = np.dot(self.outputs[self.l_count-2-i][np.newaxis].T,
                              np.array([delta * self.d_sigmoid(self.outputs[self.l_count-1-i])]))
            if i == 0:
                d_bias = delta * self.d_sigmoid(self.outputs[self.l_count-1])
            else:
                d_bias = np.dot(d_bias,
                                self.weights[self.l_count-1-i].T)*self.d_sigmoid(self.outputs[self.l_count-1-i])
            delta = np.dot(delta *
                           self.d_sigmoid(self.outputs[self.l_count-1-i]),
                           self.weights[self.l_count-2-i].T)
            self.deltas.append([d_weight, d_bias])

        for i, item in enumerate(self.deltas):
            if len(item[0].shape) == 1 and len(item[0]) != 1:
                self.weights[self.l_count-2-i] += \
                    self.learning_rate * item[0][np.newaxis].T
            else:
                self.weights[self.l_count-2-i] += self.learning_rate * item[0]
            self.biases[self.l_count-2-i] += self.learning_rate * item[1]
