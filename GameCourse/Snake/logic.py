import numpy as np
import random


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def d_sigmoid(x):
    return x * (1 - x)


def relu(x):
    return x * (x > 0)


def d_relu(x):
    return 1 * (x > 0)


def linear(x):
    return x * 1


def d_linear(x):
    return 1


def cost(target, prediction):
    return (prediction - target) ** 2


def predict(wt, x, biases):
    d = sigmoid(np.dot(x, wt[0]) + biases[0])
    h = linear(np.dot(d, wt[1]) + biases[1])
    return h, d


alpha = 0.1
# np.random.seed()
x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])
weight_1 = 2 * np.random.random((2, 5)) - 1
weight_2 = 2 * np.random.random((5, 1)) - 1
bias_1 = 2 * np.random.random((5)) - 1
bias_2 = 2 * np.random.random((1)) - 1
weights = [weight_1, weight_2]
biases = [bias_1, bias_2]
for itr in range(10000):
    i = random.randint(0, 3)
    h, d = predict(weights, x[i], biases)
    delta_D = np.dot(2 * (h - y[i]) * d_linear(h), weight_2.T)
    d_weight_2 = np.dot(d[np.newaxis].T,
                        np.array([2 * (h - y[i]) * d_linear(h)]))
    d_weight_1 = np.dot(x[i][np.newaxis].T, np.array([delta_D * d_sigmoid(d)]))
    d_bias_2 = 2 * (h - y[i]) * d_linear(h)
    d_bias_1 = np.dot(d_bias_2, weight_2.T) * d_sigmoid(d)
    weights[0] -= alpha * d_weight_1
    weights[1] -= alpha * d_weight_2
    biases[0] -= alpha * d_bias_1
    biases[1] -= alpha * d_bias_2

print(x[0], "-->", predict(weights, x[0], biases)[0])
print(x[1], "-->", predict(weights, x[1], biases)[0])
print(x[2], "-->", predict(weights, x[2], biases)[0])
print(x[3], "-->", predict(weights, x[3], biases)[0])
