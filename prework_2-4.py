import numpy as np

X = np.array([[0, 1], [1, 0]])
Z = np.array([[1, 0], [0, -1]])
I = np.eye(2)

n = int(input("Enter the number of bits: "))
H = np.array([0])

for i in range(n):
    A = np.array([[1]])
    for j in range(i):
        A = np.kron(A, I)
    A = np.kron(A, Z)
    for j in range(n - i - 1):
        A = np.kron(A, I)
    H = H + A

for i in range(n - 1):
    B = np.array([[1]])
    for j in range(i):
        B = np.kron(B, I)
    B = np.kron(B, X)
    for j in range(n - i - 1):
        B = np.kron(B, I)
    C = np.array([[1]])
    for j in range(i + 1):
        C = np.kron(C, I)
    C = np.kron(C, X)
    for j in range(n - i - 2):
        C = np.kron(C, I)
    H = H + B @ C

print("H =\n", H.real)

v = np.zeros(2**n)
v[0] = 1

E = np.conj(v) @ H @ v
print("Expectation =", E.real)
