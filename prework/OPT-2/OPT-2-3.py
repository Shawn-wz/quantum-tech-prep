import tensorcircuit as tc
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

rng = np.random.default_rng(123456)
P_np = rng.random((20, 2))
P = tc.array_to_tensor(P_np, dtype="float32")


def loss(params):
    h = P[:, 1] - params[0] * P[:, 0] - params[1]
    d = abs(h) / K.sqrt(params[0] ** 2 + 1)
    return K.sum(d)


params = K.implicit_randn((2,), dtype="float32")
opt = K.optimizer(tf.keras.optimizers.Adam(1e-2))

for _ in range(200):
    vgf = K.value_and_grad(loss)
    v, g = vgf(params)
    params = opt.update(g, params)

k = float(params[0])
b = float(params[1])
print(f"Best line: y = {k} x + {b}")
print("Loss:", v)

X = np.linspace(0, 1, 200)
Y = k * X + b
plt.scatter(P_np[:, 0], P_np[:, 1], color="b")
plt.plot(X, Y, color="r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
