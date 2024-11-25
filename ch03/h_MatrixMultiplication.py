# coding: utf-8
import numpy as np

# X = np.array([1, 2])

# W = np.array([[1, 3, 5], [2, 4, 6]])
# print(X.shape)
# print(W.shape)

# Y = np.dot(X, W)
# print(Y)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([1.0, 0.5])

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])

# print(W1.shape)
# print(X.shape)
# print(B1.shape)

A1 = np.dot(X, W1) + b1

# print(A1)

Z1 = sigmoid(A1)

# print(Z1)

# --------------------------

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])

# print(Z1.shape)
# print(W2.shape)
# print(B2.shape)

A2 = np.dot(Z1, W2) + b2
Z2 = sigmoid(A2)

# --------------------------


def identity_function(x):
    return x


W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + b3

Y = identity_function(A3)

print(Y)
