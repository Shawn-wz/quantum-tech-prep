import tensorcircuit as tc

K = tc.set_backend("tensorflow")


@K.jit
def ising(n):
    c = tc.Circuit(n)
    exp = 0
    for i in range(n):
        exp += K.real(c.expectation_ps(z=[i]))
    for i in range(n - 1):
        exp += K.real(c.expectation_ps(x=[i, i + 1]))
    return exp


n = int(input("Enter the number of bits: "))
print(f"Expectation: {ising(n).numpy().item()}")
