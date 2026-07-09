import numpy as np
from scipy.linalg import expm

sx = np.array([[0, 1], [1, 0]])
sy = np.array([[0, -1j], [1j, 0]])
sz = np.array([[1, 0], [0, -1]])
print(expm(1j * sx))
print(expm(1j * sy))
print(expm(1j * sz))

theta = float(input("Enter theta (in rad): "))
LHS = expm(1j * theta * sx)
RHS = np.cos(theta) * np.eye(2) + 1j * np.sin(theta) * sx
print("LHS = expm(1j * theta * sx):")
print(LHS)
print("RHS = cos(theta)*I + i*sin(theta)*sx:")
print(RHS)
print("LHS == RHS (all close)?:", np.allclose(LHS, RHS))
