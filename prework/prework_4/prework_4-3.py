import tensorcircuit as tc
import numpy as np
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

c = tc.Circuit(2)
c.h([0, 1])
c.cx(0, 1)

theory = K.real(c.expectation_ps(z=[0, 1])).numpy().item()


def measure(n):
    counts = c.sample(allow_state=True, batch=n, format="count_dict_bin")
    return (
        counts.get("00", 0)
        + counts.get("11", 0)
        - counts.get("01", 0)
        - counts.get("10", 0)
    ) / n


N = np.arange(1, 10000, 100)
Exp = np.array([measure(n) for n in N])
The = np.ones((len(N),)) * theory
plt.plot(N, Exp)
plt.plot(N, The)
plt.xlabel("n")
plt.ylabel("Expectation")
plt.show()
