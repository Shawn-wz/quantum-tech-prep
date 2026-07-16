import tensorcircuit as tc
import numpy as np

K = tc.set_backend("tensorflow")

sx = np.array([[0, 1], [1, 0]], dtype=np.complex64)
sy = np.array([[0, -1j], [1j, 0]], dtype=np.complex64)
sz = np.array([[1, 0], [0, -1]], dtype=np.complex64)

theta = float(input("Enter theta (in rad): "))
exp_gate = tc.gates.exp_gate(sx, theta=-theta)
LHS = tc.gates.matrix_for_gate(exp_gate)
RHS = np.cos(theta) * np.eye(2, dtype=np.complex64) + 1j * np.sin(theta) * sx
print(f"LHS:\n{LHS}")
print(f"RHS:\n{RHS}")
print("LHS == RHS (all close)?:", np.allclose(LHS, RHS))