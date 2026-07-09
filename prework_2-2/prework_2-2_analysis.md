# 矩阵指数运算与欧拉公式讨论

矩阵指数是矩阵函数的一种，通过 Taylor 展开定义:
$$
f(A) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}A^n
$$
特别地，对于指数函数
$$
e^A = \sum_{n=0}^\infty \frac{1}{n!}A^n
$$
下面讨论矩阵欧拉公式的成立条件。右式对 $\theta$ 做 Taylor 展开：
$$
RHS = (1-\frac{\theta^2}{2!}+\frac{\theta^4}{4!}+\cdots)\hat{I}+i(\theta-\frac{\theta^3}{3!}+\frac{\theta^5}{5!}+\cdots)\hat{P}
$$
按 $\theta$ 的幂次整理：
$$
RHS= \hat{I}+\hat{P}i\theta+\hat{I}\frac{(i\theta)^2}{2!}+\hat{P}\frac{(i\theta)^3}{3!}+\hat{I}\frac{(i\theta)^4}{4!}\cdots
$$
左式的泰勒展开为
$$
LHS = \hat{I}+i\hat{P}\theta+\frac{(i\hat{P}\theta)^2}{2!}+\frac{(i\hat{P}\theta)^3}{3!}+\frac{(i\hat{P}\theta)^4}{4!}\cdots
$$
比较知
$$
\hat{P}^2=\hat{I}
$$
即要求 $\hat{P}$ 为幂等矩阵。泡利矩阵均符合此要求。