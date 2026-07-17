# 布洛赫球物理规律讨论

初态 $v_0 = |0\rangle$（在布洛赫球上位于北极点，即 $z$ 轴正方向）。

## 1. 当 $\hat{P} = \sigma_z$ 时（对应图中的第三行 $p=\sigma_z$）
* **规律**：$\langle \sigma_x \rangle = 0$, $\langle \sigma_y \rangle = 0$, $\langle \sigma_z \rangle = 1$（均为常数，不随 $\theta$ 变化）。
* **物理讨论**：
  由于初态 $v_0$ 本身就是 $\sigma_z$ 的本征态，算符 $e^{i\frac{\theta}{2}\sigma_z}$ 作用在 $v_0$ 上只会引入一个全局相位：$v(\theta) = e^{i\theta/2}|0\rangle$。全局相位不改变任何可观测量的测量期望。因此，量子态在整个演化过程中始终保持在北极点，测量期望值不发生改变。

## 2. 当 $\hat{P} = \sigma_x$ 时（对应图中的第一行 $p=\sigma_x$）
* **规律**：
  * $\langle \sigma_x \rangle = 0$
  * $\langle \sigma_y \rangle = \sin\theta$
  * $\langle \sigma_z \rangle = \cos\theta$
* **物理讨论**：
  算符 $e^{i\frac{\theta}{2}\sigma_x}$ 对应于在布洛赫球上绕着 $-x$ 轴进行旋转。
  * 因为演化轨迹始终在 $y-z$ 平面上，所以它在 $x$ 方向的投影 $\langle \sigma_x \rangle$ 始终为 0。
  * 随着旋转角 $\theta$ 的增加，状态从 $z$ 轴正方向（$\theta=0$ 时 $\langle \sigma_z \rangle = 1$）出发，转到 $y$ 轴正方向（$\theta=\pi/2$ 时 $\langle \sigma_y \rangle = 1$），再转到 $z$ 轴负方向（$\theta=\pi$ 时 $\langle \sigma_z \rangle = -1$）。这正对应了余弦与正弦的变化曲线。

## 3. 当 $\hat{P} = \sigma_y$ 时（对应图中的第二行 $p=\sigma_y$）
* **规律**：
  * $\langle \sigma_x \rangle = -\sin\theta$
  * $\langle \sigma_y \rangle = 0$
  * $\langle \sigma_z \rangle = \cos\theta$
* **物理讨论**：
  类似地，算符 $e^{i\frac{\theta}{2}\sigma_y}$ 对应于在布洛赫球上绕着 $-y$ 轴进行旋转。
  * 演化轨迹始终在 $x-z$ 平面上，因此在 $y$ 方向的投影 $\langle \sigma_y \rangle$ 始终为 0。
  * 状态从 $z$ 轴正方向出发向 $-x$ 轴方向旋转。因此 $\langle \sigma_z \rangle$ 呈余弦变化，而 $\langle \sigma_x \rangle$ 则呈现出带有负号的正弦变化（$-\sin\theta$）。

## 总结
这 9 张图完美地展现了**量子态在布洛赫球上的旋转动力学**。只要演化算符的生成元 $\hat{P}$ 与测量算符 $\hat{Q}$ 相同（即对角线位置 $p=q$），由于 $[\hat{P}, \hat{P}]=0$，期望值便会守恒不变；而当两者正交时，期望值则会在 $[-1, 1]$ 之间做简谐振荡，振荡周期为 $2\pi$。