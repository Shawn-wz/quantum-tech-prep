import tensorcircuit as tc
import numpy as np
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

P = [tc.gates._x_matrix, tc.gates._y_matrix, tc.gates._z_matrix]
P_names = ["X", "Y", "Z"]


@K.jit
def f(theta, i, j):
    P1 = P[i]
    P2 = P[j]
    c = tc.Circuit(1)
    c.any(0, unitary=tc.gates.exp1_gate(P1, theta=-theta / 2))
    return K.real(c.expectation([P2, [0]]))


def derivative(f, x):
    delta = 0.001
    return (f(x + delta) - f(x)) / delta


theta_vals = np.linspace(-np.pi, np.pi, 200)

fig, axes = plt.subplots(3, 3, figsize=(12, 10))

for i in range(3):
    for j in range(3):
        ax = axes[i, j]
        f_vals = np.array([f(t, i, j).numpy().item() for t in theta_vals])
        fp_vals = np.array([derivative(lambda x: f(x, i, j), t).numpy().item() for t in theta_vals])

        ax.plot(theta_vals, f_vals, label=r"$f(\theta)$")
        ax.plot(theta_vals, fp_vals, label=r"$f'(\theta)$", linestyle="--")
        ax.set_title(f"$P_1={P_names[i]}, P_2={P_names[j]}$")
        ax.set_xlabel(r"$\theta$")
        ax.set_ylabel("Value")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

