import tensorcircuit as tc
import numpy as np
import matplotlib.pyplot as plt

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
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        unitary=tc.gates._x_matrix,
        ctrl=[1, 1, 1, 1, 1, 1, 1],
    )

    # 擦除辅助比特
    c.cnot(0, 6)
    c.cnot(1, 6)
    c.cnot(0, 7)
    c.cnot(2, 7)
    c.cnot(1, 8)
    c.cnot(3, 8)
    c.cnot(2, 9)
    c.cnot(3, 9)
    c.cnot(2, 10)
    c.cnot(4, 10)
    c.cnot(3, 11)
    c.cnot(5, 11)
    c.cnot(4, 12)
    c.cnot(5, 12)


def diffusion(c: tc.Circuit):
    """
    均值翻转算符：将状态关于均匀叠加态翻转
    """
    for i in range(6):
        c.H(i)
        c.X(i)
    c.multicontrol(*range(6), unitary=tc.gates.z(), ctrl=[1 for _ in range(5)])
    for i in range(6):
        c.X(i)
        c.H(i)


def grover(iteration):
    c = tc.Circuit(14)
    # 初始化
    for i in range(6):
        c.H(i)
    # 将目标比特制备为 |-⟩，实现 phase kickback trick
    c.X(13)
    c.H(13)
    # 迭代
    for _ in range(iteration):
        oracle(c)
        diffusion(c)
    # 模拟 1000 次测量，获取二进制测量结果的计数统计
    counts = c.sample(allow_state=True, batch=1000, format="count_dict_bin")
    # 统计前 6 个比特为目标状态（"011001" 或 "100110"）的次数
    success_count = 0
    for bitstring, count in counts.items():
        # counts 的 key 是一个 14 位的二进制字符串，我们只截取前 6 位进行验证
        if bitstring[:6] in ["011001", "100110"]:
            success_count += int(count)
    # 计算近似概率
    prob_success = success_count / 1000
    return prob_success


Iteration = np.arange(0, 10)
Prob_success = [grover(iteration) for iteration in Iteration]
plt.plot(Iteration, Prob_success)
plt.xlabel("iteration")
plt.ylabel("success probability")
plt.show()

