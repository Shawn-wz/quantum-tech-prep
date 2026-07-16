# 用 TensorCircuit 实现量子计算的基本操作

## 一、 线路初始化与状态准备

默认情况下，新创建的量子线路其所有比特都处于初始态 $|0\rangle$。但在实际应用中，您经常需要使用自定义的初始态。

### 1. 初始化为全零态
```python
import tensorcircuit as tc

# 初始化一个包含 3 个量子比特的电路，默认初始状态为 |000>
c = tc.Circuit(3)
```

### 2. 使用自定义波函数（态矢量）初始化
若想以特定的初始态开始，例如准备一个最大纠缠态 $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ 作为输入，可通过 `inputs` 参数传入一个复数数组：
```python
import numpy as np

# 定义一个自定义的波函数
init_state = np.array([1, 0, 0, 1]) / np.sqrt(2)

# 初始化一个 2 比特电路，并将该波函数作为输入
c_custom = tc.Circuit(2, inputs=init_state)
```

---

## 二、 施加常用量子门

TensorCircuit 的 `Circuit` 类包含了丰富的预定义量子门操作，同时支持参数化门和自定义任意幺正矩阵门。

### 1. 基础单比特门（固定）
```python
c = tc.Circuit(3)

c.H(0)  # 在比特 0 施加 Hadamard 门
c.X(1)  # 在比特 1 施加 Pauli-X 门 (NOT)
c.Y(2)  # 在比特 2 施加 Pauli-Y 门
c.Z(0)  # 在比特 0 施加 Pauli-Z 门
c.S(1)  # 在比特 1 施加 S 门 (π/4 相移)
c.T(2)  # 在比特 2 施加 T 门 (π/8 相移)
```

### 2. 参数化单比特旋转门
对于变分量子算法，参数化旋转门非常关键。旋转角度 `theta` 等参数可以传入标量，也可以传入深度学习后端（如 JAX、TensorFlow、PyTorch）的张量。
```python
# 绕不同轴的旋转门，角度单位为弧度
c.rx(0, theta=0.5)  # 绕 X 轴旋转
c.ry(1, theta=1.2)  # 绕 Y 轴旋转
c.rz(2, theta=0.8)  # 绕 Z 轴旋转

# 通用单比特旋转门 R(theta, alpha, phi)
c.R(0, theta=0.5, alpha=0.3, phi=0.2)
```

### 3. 双比特门与多比特门
```python
c.cnot(0, 1)  # 施加受控非门 (CNOT)，控制比特为 0，目标比特为 1
c.cz(1, 2)    # 施加受控 Z 门 (CZ)
c.swap(0, 2)  # 交换比特 0 和比特 2 的状态

# 参数化双比特受控旋转门
c.crx(0, 1, theta=0.4)  # 受控 RX 门
```

### 4. 施加自定义矩阵门
如果需要使用非标准门或自定义的幺正矩阵，可以使用 `c.any` 或 `c.unitary` 语法将自定义矩阵作用到特定比特上。
```python
# 定义一个 2x2 的自定义幺正矩阵 (例如一个自定义相位旋转门)
my_matrix = np.array([[1, 0], [0, np.exp(1j * 0.5)]])

# 作用在比特 0 上
c.any(0, unitary=my_matrix)

# 或者是作用在多个比特（例如 0 和 1）上的 4x4 矩阵
my_matrix_4x4 = np.eye(4)  # 仅作结构演示
c.any(0, 1, unitary=my_matrix_4x4)
```

---

## 三、 量子线路的进阶操作

### 1. 拼接量子线路 (Circuit Composition)
您可以分别构建多段子线路，然后通过 `append` 方法将它们拼接到一起：
```python
c1 = tc.Circuit(2)
c1.H(0)

c2 = tc.Circuit(2)
c2.cnot(0, 1)

# 将 c2 拼接到 c1 后面，生成新的电路 c3
c3 = c1.append(c2)
```

### 2. 与 Qiskit 互操作与画图
TensorCircuit 支持直接与 Qiskit 相互转换，这有助于利用 Qiskit 丰富的编译和可视化工具：
```python
# 转换为 Qiskit 的 QuantumCircuit 对象
qiskit_qc = c.to_qiskit()

# 从 Qiskit 导入线路
# c_new = tc.Circuit.from_qiskit(qiskit_qc)

# 快速绘制量子线路图（在 Jupyter 环境中可显示图片）
c.draw()
```

---

## 四、 获取计算结果与测量

线路执行完毕后，您可以通过多种方式提取结果，包括获取精确波函数、计算可观测量的期望值、模拟真实的量子测量。

### 1. 获取完整的波函数 (态矢量)
对于小规模系统，可以直接输出完整的 $2^N$ 维状态向量：
```python
# 获取当前线路的精确波函数向量
state_vector = c.state()  # 或者使用 c.wavefunction()
print("State vector:", state_vector)
```

### 2. 计算可观测量期望值
在 VQE 或物理模拟中，经常需要测量线路关于某些泡利算符的期望值。
* **快捷计算（Pauli String 期望值）：** 使用 `expectation_ps`（最简便，支持单/多比特）。
* **通用计算：** 使用 `expectation` 方法。

```python
# 方式 A：快捷计算比特 0 和 1 上的 Z ⊗ Z 联合测量期望值
exp_z0z1 = c.expectation_ps(z=[0, 1])
print("Expectation of Z0 Z1:", exp_z0z1)

# 方式 B：快捷计算比特 0 上的 X 期望值
exp_x0 = c.expectation_ps(x=[0])

# 方式 C：使用通用的 expectation 接口（传入具体算符和比特位置）
exp_generic = c.expectation((tc.gates.z(), [0]))
```

### 3. 测量采样与完美采样
在真实量子计算机上，我们得到的是通过多次重复实验生成的统计样本。
* **测量比特：** 使用 `measure` 进行单次或部分比特的破坏性测量。
* **模拟大量采样：** 使用 `sample`。

```python
# 1. 测量特定比特（如比特 0），并返回测量结果（0 或 1）和对应的发生概率
res, prob = c.measure(0, with_prob=True)
print(f"Measured qubit 0 result: {res}, with probability: {prob}")

# 2. 模拟采样 1024 次，并以二进制字典形式返回统计频数
counts = c.sample(allow_state=True, batch=1024, format="count_dict_bin")
print("Measurement counts:", counts)
```
