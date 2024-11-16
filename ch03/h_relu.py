# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return np.maximum(0, x)


print("Reru(1)", relu(1))
print("Reru(-1)", relu(-1))
