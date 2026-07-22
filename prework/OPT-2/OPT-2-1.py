import tensorcircuit as tc
import tensorflow as tf
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

a, b, c, d = map(int, input("Enter 4 parameters: ").split())


def f(x):
    return abs(a * x**3 + b * x**2 + c * x + d)


x = K.implicit_randn(shape=[1,])
history = []
opt = K.optimizer(tf.keras.optimizers.Adam(1e-2))

for _ in range(200):
    vgf = K.value_and_grad(f)
    v, g = vgf(x)
    x = opt.update(g, x)
    history.append(v)

print("Solution: ", x.numpy().item())
print("Loss: ", v.numpy().item())

plt.plot(range(200), history)
plt.ylabel("solution")
plt.xlabel("training step")
plt.show()

