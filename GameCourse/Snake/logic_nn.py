import numpy as np
import random


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def linear(x):
    return x


def d_sigmoid(x):
    return x * (1 - x)


def relu(x):
    return np.array([0 if x[i] < 0 else x[i] for i in range(len(x))])


def d_relu(x):
    return np.array([0 if x[i] <= 0 else 1 for i in range(len(x))],)


def cost(target, prediction):
    return (prediction - target) ** 2


def predict(wt, x, b):
    d = sigmoid(np.dot(x, wt[0]) + b[0])
    h = sigmoid(np.dot(d, wt[1]) + b[1])
    return [d, h]


def gradient(y):
    deltas = list()
    delta = 2 * (y - outputs[2])
    for j in range(2):
        d_weight = np.dot(outputs[1-j][np.newaxis].T,
                          np.array([delta * d_sigmoid(outputs[2-j])]))
        if j == 0:
            d_bias = delta * d_sigmoid(outputs[2])
        else:
            d_bias = np.dot(d_bias, weights[2-j].T) * d_sigmoid(outputs[2-j])
        delta = np.dot(delta * d_sigmoid(outputs[2-j]), weights[1-j].T)
        deltas.append([d_weight, d_bias])

    for i, item in enumerate(deltas):
        weights[1-j] += alpha * item[0]
        biases[1-j] += alpha * item[1]


# np.random.seed(1)
alpha = 0.1
x = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([0, 1, 1, 0])
weight_1 = 2 * np.random.random((2, 4)) - 1
weight_2 = 2 * np.random.random((4, 1)) - 1
bias_1 = 2 * np.random.random((4)) - 1
bias_2 = 2 * np.random.random((1)) - 1
biases = [bias_1, bias_2]
weights = [weight_1, weight_2]
# print(y)
for itr in range(10000):
    i = random.randint(0, 3)
    outputs = predict(weights, x[i], biases)
    outputs.insert(0, x[i])
    # print(outputs)
    gradient(y[i])

print(x[0], "-->", predict(weights, x[0], biases)[1])
print(x[1], "-->", predict(weights, x[1], biases)[1])
print(x[2], "-->", predict(weights, x[2], biases)[1])
print(x[3], "-->", predict(weights, x[3], biases)[1])
