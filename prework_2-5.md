## 前述问题用 Dirac 符号表示
*   **初始向量**：$v = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \Rightarrow |0\rangle$。另一基矢为 $|1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$。
*   **旋转矩阵 $R(\theta)$**：
    在狄拉克符号下，算符可以写为外积的线性组合：
    $$
    R(\theta) = \cos\theta |0\rangle\langle0| + \sin\theta |0\rangle\langle1| - \sin\theta |1\rangle\langle0| + \cos\theta |1\rangle\langle1|
    $$
*   **矩阵乘向量 $v' = R(\theta)v$**：
    $$
    |v'\rangle = R(\theta)|0\rangle = \cos\theta |0\rangle - \sin\theta |1\rangle
    $$
*   **泡利矩阵**：
    $$
    \sigma_x = \hat{X} = |0\rangle\langle1| + |1\rangle\langle0|
    $$
    $$
    \sigma_y = \hat{Y} = -\mathrm{i}|0\rangle\langle1| + \mathrm{i}|1\rangle\langle0|
    $$
    $$
    \sigma_z = \hat{Z} = |0\rangle\langle0| - |1\rangle\langle1|
    $$
*   **单位矩阵**：
    $$
    I = |0\rangle\langle0| + |1\rangle\langle1|
    $$
*   **期望值**：
    $$
    v^\dagger \hat{Q} v \Rightarrow \langle v | \hat{Q} | v \rangle
    $$
*   **多粒子态**：$Z_i$ 表示只作用于第 $i$ 个比特的 $\sigma_z$ 算符（其余比特上为单位算符 $I$）：
    $$
    Z_i = I^{\otimes i} \otimes \hat{Z} \otimes I^{\otimes (n-i-1)}
    $$
*   **哈密顿量算符 $H$**：
    $$
    H = \sum_{i=0}^{n-1} Z_i + \sum_{i=0}^{n-2} X_i X_{i+1}
    $$
*   **初始状态 $(1, 0, 0, \dots)^T$**：
    该状态对应全零态：$|00\dots0\rangle = |0\rangle^{\otimes n}$。
*   **期望值**：
    $$
    \langle 00\dots0 | H | 00\dots0 \rangle
    $$

## 计算 $\frac{1}{\sqrt{2}}(\ket{010}-\ket{101})$ 对应的列向量
$$
\ket{010} =\begin{pmatrix} 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 0 \\ 1 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix}=\begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix} =\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$    $$
\ket{101} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \otimes \begin{pmatrix} 1 \\ 0 \end{pmatrix}\otimes \begin{pmatrix} 0 \\ 1 \end{pmatrix}  = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix} \otimes \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}
$$
$$
\frac{1}{\sqrt{2}}(\ket{010}-\ket{101}) = \frac{1}{\sqrt{2}}\begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ -1 \\ 0 \\ 0 \end{pmatrix}
$$