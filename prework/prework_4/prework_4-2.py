import tensorcircuit as tc
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

c = tc.Circuit(2)
c.h([0, 1])
c.cx(0, 1)

theory = K.real(c.expectation_ps(z=[0,1])).numpy().item()

@K.jit
def measure(n):
    counts = c.sample(allow_state=True, batch=n, format="count_dict_bin")
    return (counts['00'] + counts['11'] - counts['01']- counts['10']) / n 



