import tensorcircuit as tc
import numpy as np
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

sigma_names = ["sigma_x", "sigma_y", "sigma_z"]


@K.jit
def E(p, q, t):

    c = tc.Circuit(1)

    if p == 0:
        exp = tc.gates.exp1_gate(tc.gates._x_matrix, theta=-t / 2)
    elif p == 1:
        exp = tc.gates.exp1_gate(tc.gates._y_matrix, theta=-t / 2)
    else:
        exp = tc.gates.exp1_gate(tc.gates._z_matrix, theta=-t / 2)

    c.any(0, unitary=exp)

    if q == 0:
        Q = tc.gates.x()
    if q == 1:
        Q = tc.gates.y()
    if q == 2:
        Q = tc.gates.z()

    return c.expectation((Q, [0]))


fig, axes = plt.subplots(3, 3, figsize=(12, 10))
fig.suptitle(
    "Expectation ⟨psi(θ)|sigma_q|psi(θ)⟩, where |psi(θ)⟩ = exp(i θ/2 sigma_p)|0⟩",
    fontsize=14,
)

theta = np.linspace(0, 2 * np.pi, 100)

for p in range(3):
    for q in range(3):
        ax = axes[p, q]
        E_vals = [E(p, q, t).numpy().item() for t in theta]
        ax.plot(theta, E_vals)
        ax.set_title(f"sigma_p={sigma_names[p]}, sigma_q={sigma_names[q]}")
        ax.set_xlabel("θ")
        ax.set_ylabel("Expectation")
        ax.set_ylim(-1.1, 1.1)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color="k", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
