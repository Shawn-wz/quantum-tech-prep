import tensorcircuit as tc

K = tc.set_backend("tensorflow")

c = tc.Circuit(2)
c.h([0, 1])
c.cx(0, 1)

counts = c.sample(allow_state=True, batch=1024, format="count_dict_bin")
print("Measurement counts:", counts)
measure = (counts["00"] + counts["11"] - counts["01"] - counts["10"]) / 1024
theory = K.real(c.expectation_ps(z=[0, 1])).numpy().item()
print(f"Theory: {theory}")
print(f"Experiment: {measure}")
