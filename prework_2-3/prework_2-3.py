import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

s = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
v0 = np.array([1, 0])

sigma_names = ["sigma_x", "sigma_y", "sigma_z"]


def E(p, q, theta):
    v = expm(0.5j * theta * s[p, :, :]) @ v0
    return np.real(np.conj(v) @ s[q, :, :] @ v)


fig, axes = plt.subplots(3, 3, figsize=(12, 10))
fig.suptitle(
    "Expectation ⟨psi(θ)|sigma_q|psi(θ)⟩, where |psi(θ)⟩ = exp(i θ/2 sigma_p)|0⟩",
    fontsize=14,
)

theta = np.linspace(0, 2 * np.pi, 100)

for p in range(3):
    for q in range(3):
        ax = axes[p, q]
        E_vals = [E(p, q, t) for t in theta]
        ax.plot(theta, E_vals)
        ax.set_title(f"sigma_p={sigma_names[p]}, sigma_q={sigma_names[q]}")
        ax.set_xlabel("θ")
        ax.set_ylabel("Expectation")
        ax.set_ylim(-1.1, 1.1)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color="k", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
