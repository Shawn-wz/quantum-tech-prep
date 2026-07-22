import tensorcircuit as tc

K = tc.set_backend("tensorflow")


def oracle(c: tc.Circuit):
    """
    在已有电路 c 上应用 oracle 门，在输入量子态相邻比特均不同时将目标 qubit 变为 |1⟩。

    约定 qubit 分配:
      - 0~5: 输入 qubit
      - 6~12: 辅助 qubit
      - 13: 目标 qubit

    """
    # 检查每对相邻关系是否不同（异或结果为 1）
    c.cnot(0, 6)
    c.cnot(1, 6)  # q6 = q0 XOR q1
    c.cnot(0, 7)
    c.cnot(2, 7)  # q7 = q0 XOR q2
    c.cnot(1, 8)
    c.cnot(3, 8)  # q8 = q1 XOR q3
    c.cnot(2, 9)
    c.cnot(3, 9)  # q9 = q2 XOR q3
    c.cnot(2, 10)
    c.cnot(4, 10)  # q10 = q2 XOR q4
    c.cnot(3, 11)
    c.cnot(5, 11)  # q11 = q3 XOR q5
    c.cnot(4, 12)
    c.cnot(5, 12)  # q12 = q4 XOR q5

    # 所有辅助比特为 1（即所有相邻对都不同）时翻转目标比特
    c.multicontrol(
        6, 7, 8, 9, 10, 11, 12, 13,
        unitary=tc.gates._x_matrix,
        ctrl=[1, 1, 1, 1, 1, 1, 1],
    )


bits = input("Please enter the 6-bit string: ")

c = tc.Circuit(14)
for i in range(6):
    if bits[i] == "1":
        c.X(i)

oracle(c)
print("Target qubit: ", c.measure(13)[0].numpy().item())
