import numpy as np
import random


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def relu(x):
    return np.array([0 if x[i] < 0 else x[i] for i in range(len(x))])


def cost(target, prediction):
    return (prediction - target) ** 2


def predict(wt, x, b):
    d = sigmoid(np.dot(x, wt[0]) + b[0])
    h = sigmoid(np.dot(d, wt[1]) + b[1])
    return h, d


alpha = 0.1
np.random.seed(1)
x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])
weight_1 = 2 * np.random.random((2, 4)) - 1
weight_2 = 2 * np.random.random((4)) - 1
bias_1 = 2 * np.random.random((4)) - 1
bias_2 = 2 * np.random.random((1)) - 1
biases = [bias_1, bias_2]
weights = [weight_1, weight_2]
print(y)
for itr in range(1):
    i = random.randint(0, 3)
    h, d = predict(weights, x[i], biases)
    print(d)
    print(h)
    # cost of hidden layer
    delta_D = 2 * (h - y[i]) * h * (1 - h) * weight_2
    # delta value for weight 2
    d_weight_2 = 2 * (h - y[i]) * h * (1 - h) * d
    # delta value for weight 1
    d_weight_1 = np.dot(np.array([x[i]]).T, (np.array([delta_D]) * d * (1 - d)))
    d_bias_1 = 2 * (h - y[i]) * h * (1 - h)
    d_bias_0 = d_bias_1 * weight_2 * d * (1 - d)
    weight_1 -= alpha * d_weight_1
    weight_2 -= alpha * d_weight_2
    biases[0] -= alpha * d_bias_0
    biases[1] -= alpha * d_bias_1
    # print(loss)
print(x[0], "-->", predict([weight_1, weight_2], x[0], biases)[0])
print(x[1], "-->", predict([weight_1, weight_2], x[1], biases)[0])
print(x[2], "-->", predict([weight_1, weight_2], x[2], biases)[0])
print(x[3], "-->", predict([weight_1, weight_2], x[3], biases)[0])
