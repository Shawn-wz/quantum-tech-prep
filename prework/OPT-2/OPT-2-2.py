import tensorcircuit as tc
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

K = tc.set_backend("tensorflow")

rng = np.random.default_rng(123456)
P_np = rng.random((20, 2))
P = tc.array_to_tensor(P_np, dtype=float)


def loss(params):
    dx = P[:, 0] - params[0]
    dy = P[:, 1] - params[1]
    distances = K.sqrt(dx**2 + dy**2)
    return K.sum(distances)

params = K.implicit_randn(shape=(2,))
opt = K.optimizer(tf.keras.optimizers.Adam(1e-2))

for _ in range(200):
    vgf = K.value_and_grad(loss)
    v, g = vgf(params)
    params = opt.update(g, params)

x = float(params[0])
y = float(params[1])
print(f"Best point: ({x}, {y})")
print("Loss :", v)

plt.scatter(P[:, 0], P[:, 1], color="b")
plt.scatter(np.array([x]), np.array([y]), color="r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
