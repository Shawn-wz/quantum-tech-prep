import tensorcircuit as tc
import matplotlib.pyplot as plt

K = tc.set_backend("tensorflow")

c = tc.Circuit(2)
c.h([0, 1])
c.cx(0, 1)

exp = K.real(c.expectation_ps(z=[0, 1])).numpy().item()
print(f"Expectation = {exp}")

# c.draw(output="mpl")
# plt.show()


