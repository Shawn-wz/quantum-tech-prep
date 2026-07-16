import tensorcircuit as tc
import numpy as np
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

@K.jit
def rotate_vector(theta):
    q = tc.Circuit(1)
    q.ry(0, theta=-2.0 * theta)
    return q.state()

theta_deg = float(input("Enter the rotation angle (in degrees): "))
theta = np.radians(theta_deg)

v = np.array([1, 0])
vprime = K.numpy(rotate_vector(theta)).real

plt.figure(figsize=(6, 6))
ax = plt.gca()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.6)
ax.axhline(0, color="gray", linewidth=0.5)
ax.axvline(0, color="gray", linewidth=0.5)
ax.arrow(
    0,
    0,
    v[0],
    v[1],
    head_width=0.08,
    head_length=0.1,
    fc="dodgerblue",
    ec="dodgerblue",
    linewidth=2.5,
    alpha=0.4,
    label=rf"$\vec{{v}}=[{v[0]},{v[1]}]$",
)
ax.arrow(
    0,
    0,
    vprime[0],
    vprime[1],
    head_width=0.08,
    head_length=0.1,
    fc="crimson",
    ec="crimson",
    linewidth=2.5,
    label=rf"$\vec{{v}}\,'=[{vprime[0]:.3f},{vprime[1]:.3f}]$",
)
ax.legend(fontsize=11)
plt.title(f"Vector Rotation by {np.degrees(theta):.1f}°")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.show()
