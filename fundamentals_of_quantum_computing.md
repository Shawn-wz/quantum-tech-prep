# 量子计算基础

## 一、 单量子比特基础 (Single-Qubit Foundations)

### 1. 量子比特的状态表示
经典比特只能处于 $0$ 或 $1$ 状态，而量子比特（Qubit）可以处于叠加态。
单量子比特的状态通常用狄拉克符号（Dirac Notation）表示为二维复向量：
$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$$

其中，计算基底 $|0\rangle$ 和 $|1\rangle$ 分别对应二维空间的标准正交基：
$$|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$

*   **归一化条件（概率幅）：** $\alpha$ 和 $\beta$ 是复数，称为**概率幅**。系统在被测量时会坍缩，其满足归一化条件：
    $$|\alpha|^2 + |\beta|^2 = 1$$
    其中，测量得到 $|0\rangle$ 的概率为 $|\alpha|^2$，得到 $|1\rangle$ 的概率为 $|\beta|^2$。
*   **相位分类：**
    *   **全局相位（Global Phase）：** 在状态前乘上一个常数相位 $e^{i\theta}|\psi\rangle$。由于 $|e^{i\theta}|^2 = 1$，全局相位在物理上不可观测，通常可以忽略。
    *   **相对相位（Relative Phase）：** 如 $|0\rangle + e^{i\theta}|1\rangle$ 中的 $\theta$。相对相位会改变态在不同基底下的干涉结果，具有重要的物理意义。
*   **Bloch 球表征：** 消除全局相位并利用归一化条件后，单量子比特的状态可参数化映射到三维单位球面上：
    $$|\psi\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle$$
    其中，$\theta \in [0, \pi]$，$\phi \in [0, 2\pi)$。

### 2. 单量子比特门
单量子比特操作在数学上表示为 $2 \times 2$ 的**幺正矩阵** $U$（满足 $U^\dagger U = I$），从而保证了量子操作的保模长（概率守恒）与可逆性。

| 门名称 (Gate) | 符号表示 | 矩阵形式 $U$ | 作用效果 | 几何意义 (Bloch球) |
| :--- | :---: | :---: | :--- | :--- |
| **Pauli-X (NOT)** | $X$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | $X\|0\rangle = \|1\rangle$<br>$X\|1\rangle = \|0\rangle$ | 绕 X 轴旋转 $\pi$ 弧度 |
| **Pauli-Y** | $Y$ | $\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ | $Y\|0\rangle = i\|1\rangle$<br>$Y\|1\rangle = -i\|0\rangle$ | 绕 Y 轴旋转 $\pi$ 弧度 |
| **Pauli-Z** | $Z$ | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | $Z\|0\rangle = \|0\rangle$<br>$Z\|1\rangle = -\|1\rangle$ | 绕 Z 轴旋转 $\pi$ 弧度（翻转相对相位） |
| **Hadamard** | $H$ | $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ | $H\|0\rangle = \|+\rangle$<br>$H\|1\rangle = \|-\rangle$ | 将计算基转换为叠加基，绕对角轴旋转 |
| **Phase Gate** | $S$ | $\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$ | $S\|0\rangle = \|0\rangle$<br>$S\|1\rangle = i\|1\rangle$ | 绕 Z 轴旋转 $\pi/2$ 弧度（引入 $\pi/2$ 相位）|
| **$\pi/8$ Gate** | $T$ | $\begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$ | $T\|0\rangle = \|0\rangle$<br>$T\|1\rangle = e^{i\pi/4}\|1\rangle$ | 绕 Z 轴旋转 $\pi/4$ 弧度 |
| **任意旋转门** | $R_y(\theta)$ | $\begin{pmatrix} \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix}$ | $R_y(\theta)\|0\rangle = \cos\frac{\theta}{2}\|0\rangle + \sin\frac{\theta}{2}\|1\rangle$ | 绕 Y 轴旋转 $\theta$ 弧度 |

*注：其中 $|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$，$-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$。*

---

## 二、 多量子比特系统与多比特门 (Multi-Qubit Systems & Gates)

### 1. 系统空间的组合
两个量子比特 $A$ 和 $B$ 各自的状态空间通过**张量积（Tensor Product）**进行组合。两比特复合系统的基底为：
$$|00\rangle = |0\rangle \otimes |0\rangle, \quad |01\rangle = |0\rangle \otimes |1\rangle, \quad |10\rangle = |1\rangle \otimes |0\rangle, \quad |11\rangle = |1\rangle \otimes |1\rangle$$

对于 $N$ 个量子比特，其状态空间维度为 $2^N$。

*   **状态的分类：**
    *   **可分态（Separable States）：** 可以写成单个量子比特状态乘积的形式，如 $|+0\rangle = \frac{|00\rangle + |10\rangle}{\sqrt{2}}$。
    *   **纠缠态（Entangled States）：** 无法分解为单个比特独立状态的形式。最典型的纠缠态为 **Bell 态**（例如 $\frac{|00\rangle + |11\rangle}{\sqrt{2}}$）。
*   **端序（Endianness）：** 在量子编程中，比特数组的排列顺序决定了状态向量中的索引。Q# 采用大端序（Big-Endian），即在状态 $|q_0 q_1 \rangle$ 中，$q_0$ 代表最高有效位（在数组中索引为0的比特）。

### 2. 多量子比特门
多量子比特操作在数学上表现为大小为 $2^N \times 2^N$ 的幺正矩阵。

| 门名称 (Gate) | 符号表示 | 矩阵形式 (以2比特为例) | 作用效果与逻辑说明 |
| :--- | :---: | :---: | :--- |
| **Controlled-NOT** | CNOT (或 $CX$) | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$ | 若控制比特（第一位）为 $|1\rangle$，则反转目标比特（第二位）。<br>$|x, y\rangle \rightarrow |x, x \oplus y\rangle$ |
| **Controlled-Z** | $CZ$ | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \end{pmatrix}$ | 若两个比特均为 $|1\rangle$，则引入 $-1$ 的相对相位。两比特地位对称。 |
| **SWAP** | $SWAP$ | $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$ | 交换两个量子比特的状态。<br>$|x, y\rangle \rightarrow |y, x\rangle$ |
| **Toffoli** | CCNOT | (8 $\times$ 8 矩阵) | 含有两个控制比特和一个目标比特。当且仅当两个控制比特均为 $|1\rangle$ 时，反转目标比特。可用作构建通用可逆经典计算。 |

---

## 三、 量子测量理论 (Quantum Measurement)

### 1. 单量子比特测量
测量是将量子系统中的量子信息转化为经典信息的过程。根据波恩规则（Born's Rule），测量是一个具有随机性且不可逆的投影过程。

*   **测量坍缩：** 在对处于 $\alpha|0\rangle + \beta|1\rangle$ 的比特进行计算基测量时，系统会以 $|\alpha|^2$ 的概率坍缩到 $|0\rangle$，或以 $|\beta|^2$ 的概率坍缩到 $|1\rangle$。
*   **非计算基测量（基底转换）：** 
    除了在计算基底（$Z$ 基底：$\{|0\rangle, |1\rangle\}$）上测量，还可以在其他正交基底上测量。
    *   **$X$ 基底测量（$\{|+\rangle, |-\rangle\}$）：** 无法直接在物理层面上对 $X$ 基底进行探测。方法是先施加 $H$ 门进行**基底旋转**，将 $|+\rangle$ 映射到 $|0\rangle$，$|-\rangle$ 映射到 $|1\rangle$，然后再进行 $Z$ 测量。
    *   **任意基底测量：** 施加幺正变换 $U^\dagger$，使目标基底映射到标准计算基 $\{|0\rangle, |1\rangle\}$ 后进行测量。

### 2. 用投影算符理解测量 (Projective Measurements)
在量子力学中，最常使用的测量框架是**投影测量**。对于一个给定的可观测物理量（Hermitian 算符）$M$，其谱分解为：
$$M = \sum_m \lambda_m P_m$$

其中，$\lambda_m$ 是物理量 $M$ 的本征值（即测量可能得到的经典结果），$P_m$ 是对应本征空间的**投影算符（Projection Operator）**。

#### 投影算符的基本性质：
投影算符在数学上必须满足以下完备性与正交性关系：
1.  **自伴性（Hermitian）：** $P_m^\dagger = P_m$
2.  **幂等性（Idempotent）：** $P_m^2 = P_m$
3.  **完备性（Completeness）：** $\sum_m P_m = I$ （保证所有可能结果的概率之和为 1）
4.  **正交性（Orthogonality）：** $P_m P_{m'} = \delta_{mm'} P_m$

#### 测量规则：
设系统在测量前的状态为 $|\psi\rangle$，当我们对该物理量进行测量时：
*   **获得测量结果 $\lambda_m$ 的概率为：**
    $$p(m) = \langle \psi | P_m^\dagger P_m | \psi \rangle = \langle \psi | P_m | \psi \rangle$$
*   **测量后，系统的状态会发生坍缩，新状态为：**
    $$|\psi_m\rangle = \frac{P_m |\psi\rangle}{\sqrt{p(m)}}$$

### 3. 多量子比特系统测量

#### 3.1 全测量 (Full Measurement)
**全测量**是指对多量子比特复合系统中的**所有**比特同时执行投影测量。

*   **投影算符：** 
    对于 $n$ 比特系统，全测量通常在复合计算基下进行。其投影算符为：
    $$P_x = |x\rangle\langle x|, \quad x \in \{0, 1\}^n$$
    例如，2 比特系统有 4 个投影算符：$P_{00}=|00\rangle\langle00|$， $P_{01}=|01\rangle\langle01|$ 等。
*   **物理结果：** 
    测量后，整个系统的量子相干性完全丧失，状态会确定性地坍缩到某一个经典基态 $|x\rangle$。由于所有比特均被测量，系统不再保留任何未坍缩的量子状态。
-   **说明：** 实际上需要逐个对每个比特测量。

#### 3.2 部分测量 (Partial Measurement)
**部分测量**是指仅对多量子比特系统中的 **某一部分（子集）** 比特进行测量，而保持其余比特不作测量。这是量子算法（如隐形传态、量子纠错码）中更常用的精细操作。

*   **投影算符的构造：**
    假设复合系统由被测子系统 $A$ 和未测子系统 $B$ 组成，系统整体状态为 $|\psi_{AB}\rangle$。若在 $A$ 上执行投影算符为 $P_m^A$ 的测量，则对应整体系统的联合投影算符为：
    $$P_m = P_m^A \otimes I_B$$
    其中 $I_B$ 为作用在未测子系统 $B$ 上的单位算符（表示不对其做任何改变）。
*   **概率与状态坍缩：**
    *   测量获得结果 $m$ 的概率为：
        $$p(m) = \langle \psi_{AB} | (P_m^A \otimes I_B) | \psi_{AB} \rangle$$
    *   测量后，复合系统的状态坍缩为：
        $$|\psi'_{AB}\rangle = \frac{(P_m^A \otimes I_B)|\psi_{AB}\rangle}{\sqrt{p(m)}}$$
*   **对系统关联性的影响：**
    *   **可分态下的部分测量：** 若 $|\psi_{AB}\rangle = |\phi_A\rangle \otimes |\chi_B\rangle$，对 $A$ 进行部分测量只会使 $A$ 部分发生坍缩，而 $B$ 部分的状态 $|\chi_B\rangle$ 保持完全不受影响。
    *   **纠缠态下的部分测量：** 若 $A$ 和 $B$ 处于纠缠态，对 $A$ 的部分测量虽然没有直接作用在 $B$ 上，但由于量子关联性，$B$ 的状态也会发生相应的关联坍缩。然而，**$B$ 随后仍然作为一个处于确定量子态的系统存在**，可以继续进行后续的量子门操作和计算。

#### 3.3 联合测量（Joint / Parity Measurement）
  - 使用**多比特张量积算符**（如 $Z \otimes Z$ 或 $X \otimes X$）对多个量子比特进行协同投影测量。(通常使用多个泡利算符的张量积)
  - 以 $Z \otimes Z$ 联合测量为例，其对应的本征空间被划分为偶宇称空间（$|00\rangle, |11\rangle$，对应本征值
    +1）与奇宇称空间（$|01\rangle, |10\rangle$，对应本征值 -1）。若对叠加纠缠态$\alpha|00\rangle + \beta|11\rangle$ 施加 $Z \otimes Z$ 测量，由于该状态整体处于 +1 ,本征空间内，测量将以 100% 的概率得到结果+1，且系统状态在测量后保持原有的叠加与相干性不发生改变。
  - 这种测量允许我们在不破坏量子信息、不泄露单个比特具体状态的前提下，仅提取比特之间的相对关联信息（如宇称或错误信号），是量子稳定器码（StabilizerCodes）与量子纠错的核心技术之一。

## 四、量子状态制备(Preparing Quantum States)

状态制备的目标是将初始的零态 $|0\rangle^{\otimes n}$ 变换为目标叠加态 $|\psi\rangle = \sum_x \alpha_x |x\rangle$。

### 1. 级联纠缠法 (Cascade / Entanglement Spread)
常用于制备高度对称的纠缠态，如 **GHZ 态** ($\frac{|0\dots0\rangle + |1\dots1\rangle}{\sqrt{2}}$)。
*   **方法逻辑：**
    1.  对第 $1$ 个量子比特施加 $H$ 门，创造基底叠加：$\frac{|0\rangle + |1\rangle}{\sqrt{2}}$。
    2.  以第 $1$ 个比特为控制位，向第 $2$ 个比特施加 CNOT 门。
    3.  依次以第 $k$ 个比特控制第 $k+1$ 个比特，将叠加效应像多米诺骨牌一样传递。

### 2. W 态制备（受控旋转级联法）
W 态的形式为：$|\text{W}_n\rangle = \frac{1}{\sqrt{n}} (|10\dots0\rangle + |01\dots0\rangle + \dots + |00\dots1\rangle)$，即有且仅有一个比特为 $|1\rangle$。由于 $n$ 不一定是 $2$ 的幂次，不能直接施加 $H$ 门。
*   **方法逻辑：** 通过**依次改变角度的受控旋转门**分配概率。
    对于 $n$ 个比特，我们的旋转角度需要保证当前的比特有 $1/n$ 的概率转为 $|1\rangle$，而剩下的 $(n-1)/n$ 的概率继续向后传递：
    1.  对第 $1$ 个比特进行旋转：$Ry(\theta_1) |0\rangle$，其中 $\theta_1 = 2 \arccos\left(\sqrt{\frac{n-1}{n}}\right)$。此时状态为：$\sqrt{\frac{n-1}{n}}|0\rangle + \sqrt{\frac{1}{n}}|1\rangle$。
    2.  如果第 $1$ 个比特为 $|0\rangle$（即进入了 $(n-1)/n$ 的分支），则对第 $2$ 个比特施加受控旋转：以第 $1$ 比特为 $|0\rangle$（即 Anti-controlled）控制第 $2$ 比特旋转 $\theta_2 = 2 \arccos\left(\sqrt{\frac{n-2}{n-1}}\right)$。
    3.  重复此过程，直到最后一个比特。最后使用一系列受控非门（CNOT）调整 $|1\rangle$ 的位置，保证当某位置为 $|1\rangle$ 时，其他位置均坍缩为 $|0\rangle$。

### 3. 非 2 阶均匀叠加态制备（二分法 / Bisection Method）
如果需要将 $M$ 个基态等概率叠加（$M$ 不是 $2$ 的整数次幂，例如 $M=3$ 时制备 $\frac{|0\rangle + |1\rangle + |2\rangle}{\sqrt{3}}$）。
*   **方法逻辑：**
    将 $M$ 分解为两部分：左分支大小 $L = \lceil M/2 \rceil$，右分支大小 $R = M - L$。
    1.  在最高有效位上进行角度为 $\theta = 2 \arccos\left(\sqrt{L/M}\right)$ 的 $Ry$ 旋转。
    2.  此时最高位为 $|0\rangle$ 的概率为 $L/M$，为 $|1\rangle$ 的概率为 $R/M$。
    3.  以最高位为控制条件，对剩余的低位比特分别进行递归二分制备，左边分支递归制备 $L$ 项叠加，右边分支递归制备 $R$ 项叠加。

---

## 五、量子状态区分（Distinguishing Quantum States）

给出属于集合 $\{|\psi_1\rangle, \dots, |\psi_k\rangle\}$ 的未知输入态 $|\psi\rangle$，要求设计测量电路判别其身份。

### 1. 正交状态判定：基底变换映射法 (Exact Discrimination)
如果已知候选状态两两正交（即 $\langle \psi_i | \psi_j \rangle = \delta_{ij}$），我们总能无误差地区分它们。
*   **方法逻辑：**
    1.  寻找一个幺正变换 $U$，其满足 $U |\psi_i\rangle = |i\rangle$（即把复杂的正交态映射到标准的计算基底状态，如 $|00\rangle, |01\rangle$ 等）。
    2.  在电路中，对输入的未知态施加算符 $U^\dagger$。
    3.  在计算基下测量所有比特。测得的二进制数值直接对应状态的索引 $i$。
*   **典型应用（Bell 态区分）：**
    四个正交的 Bell 态可以通过如下逆电路（$U^\dagger$）映射到计算基：
    对两比特施加 CNOT（第一个控制第二个），然后对第一个施加 $H$ 门，最后测量两个比特，测得的 $00, 01, 10, 11$ 直接一一对应四个 Bell 态。

### 2. 非正交状态区分：无模糊区分法 (Unambiguous State Discrimination - USD)
当两个候选状态非正交（例如 $|\psi_1\rangle$ 和 $|\psi_2\rangle$，重叠度 $s = \langle \psi_1 | \psi_2 \rangle \neq 0$）时，我们无法在不犯错的前提下 100% 成功区分它们。USD 方法允许我们输出“不知道”，但**一旦输出确定性结论，则必须保证 100% 正确**。
*   **方法逻辑（引入辅助比特）：**
    1.  引入一个处于 $|0\rangle_{\text{anc}}$ 的辅助量子比特。
    2.  设计一个联合幺正操作 $U_{joint}$ 作用在输入态和辅助比特上，将非正交态投影到高维空间：
        $$U_{joint} |\psi_1\rangle |0\rangle_{\text{anc}} = \sqrt{1-s} |0\rangle |0\rangle_{\text{anc}} + \sqrt{s} |\phi_1\rangle |1\rangle_{\text{anc}}$$
        $$U_{joint} |\psi_2\rangle |0\rangle_{\text{anc}} = \sqrt{1-s} |1\rangle |0\rangle_{\text{anc}} + \sqrt{s} |\phi_2\rangle |1\rangle_{\text{anc}}$$
    3.  **首先测量辅助比特**：
        *   若辅助比特测得为 $|0\rangle$（代表投影到了 $0$ 分支，此时原来的两个状态在主比特上已经变得**完全正交**了，分别为 $|0\rangle$ 和 $|1\rangle$）：我们接着测量主比特。主比特若为 $0$ 则必然是 $|\psi_1\rangle$，若为 $1$ 则必然是 $|\psi_2\rangle$（100% 确定）。
        *   若辅助比特测得为 $|1\rangle$：输出“无法确定（Inconclusive）”。

### 3. 对称状态排除法 (State Exclusion / Peres-Wootters)
例如给定三个对称的单比特状态（在 Bloch 球赤道上呈 $120^\circ$ 夹角），要求绝对排除其中一个状态。
*   **方法逻辑：**
    若要排除状态 $|\psi_i\rangle$，我们需要设计测量，使得输入为 $|\psi_i\rangle$ 时，输出该测量结果的概率为 $0$。
    因此，我们将测量投影轴选在与目标排除状态 $|\psi_i\rangle$  **完全正交（垂直）** 的方向 $|\psi_i^\perp\rangle$ 上。若测量结果坍缩到 $|\psi_i^\perp\rangle$，根据正交性，输入绝对不可能是 $|\psi_i\rangle$，从而实现了对该状态的无误排除。

---

## 六、区分幺正算符 (Distinguishing Unitaries)

给定一个未知的黑盒幺正门 $U$（承诺属于某个集合 $\{U_1, U_2, \dots\}$），我们需要通过设计实验辨别它。

### 1. 状态差异放大法 (Output Orthogonalization)
*   **方法逻辑：**
    1.  分析候选算符 $U_i$。
    2.  设计或寻找一个最佳的输入测试态 $|\psi_{\text{in}}\rangle$，使得不同的算符作用在它上面后，输出状态彼此正交：
        $$\langle \psi_{\text{in}} | U_1^\dagger U_2 | \psi_{\text{in}} \rangle = 0$$
    3.  输入该测试态，对输出态进行“正交状态判定”（第 11 章的方法）。
*   **示例对照表：**
    *   区分 $I$ 与 $X$：输入 $|0\rangle \rightarrow$ 输出为 $|0\rangle$ 和 $|1\rangle$（正交，直接测量）。
    *   区分 $I$ 与 $Z$：输入 $|+\rangle \rightarrow$ 输出为 $|+\rangle$ 和 $|-\rangle$（正交，施加 $H$ 门后测量）。
    *   区分 $Z$ 与 $S$：输入 $|+\rangle \rightarrow$ 输出为 $|-\rangle$ 和 $|i\rangle$（正交，施加 $Ry(-\pi/2)$ 转换为计算基测量）。

### 2. 相位回传探测技术 (Phase Kickback)
若两个算符仅在相对相位或全局相位上有差异（例如 $U_1 = I$ 且 $U_2 = -I$，或在特定基底上引入不同的复数相位），直接在靶比特上进行概率测量无法区分相位。
*   **方法逻辑（引入控制辅助线圈）：**
    1.  引入一个处于 $|+\rangle$ 的辅助比特作为控制位。
    2.  制备靶比特为黑盒算符的**特征态** $|\psi_{\text{eigen}}\rangle$（满足 $U_2 |\psi_{\text{eigen}}\rangle = e^{i\theta} |\psi_{\text{eigen}}\rangle$）。
    3.  施加受控黑盒操作：`Controlled U`。
    4.  此时，靶比特的状态保持不变，但由于控制机制，其特征值相位 $e^{i\theta}$ 被**回传（Kickback）**到了辅助比特的相对相位上：
        $$|0\rangle | \psi_{\text{eigen}}\rangle + |1\rangle U | \psi_{\text{eigen}}\rangle \rightarrow \frac{|0\rangle + e^{i\theta}|1\rangle}{\sqrt{2}} |\psi_{\text{eigen}}\rangle$$
    5.  对辅助比特施加 $H$ 门并测量，通过辅助比特的干涉结果来确定相位 $e^{i\theta}$，从而识别黑盒。

### 3. 纠缠辅助区分法 (Entanglement-Assisted Discrimination)
有些单比特算符无法通过单次输入单比特纯态来达到完全正交的输出，此时需要利用纠缠。
*   **方法逻辑：**
    1.  准备两个比特的最大纠缠态（如 Bell 态 $\frac{|00\rangle + |11\rangle}{\sqrt{2}}$）。
    2.  将未知的单比特黑盒 $U$ 仅作用在第 $1$ 个比特上（即整体施加 $U \otimes I$）。
    3.  由于黑盒作用于纠缠系统的一侧，输出的两比特联合状态之间会带有极高的相干关联性。
    4.  最后对这两个比特执行联合测量（Bell 测量），可以高精度地将单比特算符的所有复数参数解调出来。