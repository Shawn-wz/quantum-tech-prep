import numpy as np


def f(x):
    return np.array([1, x, x ** 2, x ** 3])


def derivative(f, x):
    delta = 0.001
    return (f(x + delta) - f(x)) / delta


x = 1

print(derivative(f, x))
