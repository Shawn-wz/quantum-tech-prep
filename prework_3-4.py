import tensorcircuit as tc
import tensorflow as tf
import numpy as np
import scipy.optimize as optimize

K = tc.set_backend("tensorflow")

P = [tc.gates._x_matrix, tc.gates._y_matrix, tc.gates._z_matrix]
P_names = ["X", "Y", "Z"]


@K.jit
def f(theta):
    P1 = P[0]
    P2 = P[1]
    c = tc.Circuit(1)
    c.any(0, unitary=tc.gates.exp1_gate(P1, theta=-theta / 2))
    return K.real(c.expectation([P2, [0]]))


def derivative(f, x):
    delta = 0.001
    return (f(x + delta) - f(x)) / delta


learning_rate = 2e-2
opt = K.optimizer(tf.keras.optimizers.SGD(learning_rate))

f_val_grad = K.value_and_grad(f)


def grad_descent(x, i):
    val, grad = f_val_grad(x)
    x = opt.update(grad, x)
    if i % 10 == 0:
        print(f"i={i}, f={val}")
    return x


x = K.implicit_randn(1)
for i in range(200):
    x = grad_descent(x, i)
print(f"Best x={x.numpy().item()}")
