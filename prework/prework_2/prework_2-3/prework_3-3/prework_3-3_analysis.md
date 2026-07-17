$$
f(\theta) = \langle 0 | \left( \cos\frac{\theta}{2} - i \sin\frac{\theta}{2} \hat{P}_1 \right) \hat{P}_2 \left( \cos\frac{\theta}{2} + i \sin\frac{\theta}{2} \hat{P}_1 \right) | 0 \rangle
$$

$$
= \langle 0 | \left( \cos^2\frac{\theta}{2} \hat{P}_2 + i \cos\frac{\theta}{2}\sin\frac{\theta}{2} (\hat{P}_2\hat{P}_1 - \hat{P}_1\hat{P}_2) + \sin^2\frac{\theta}{2} \hat{P}_1\hat{P}_2\hat{P}_1 \right) | 0 \rangle
$$

$$
= \cos^2\frac{\theta}{2} \langle \hat{P}_2 \rangle + \sin^2\frac{\theta}{2} \langle \hat{P}_1\hat{P}_2\hat{P}_1 \rangle + i \cos\frac{\theta}{2}\sin\frac{\theta}{2} \langle [\hat{P}_2, \hat{P}_1] \rangle
$$

| $\hat{P}_1$ | $\hat{P}_2$ | $\langle \hat{P}_2 \rangle$ | $\langle \hat{P}_1\hat{P}_2\hat{P}_1 \rangle$ | $\langle [\hat{P}_2, \hat{P}_1] \rangle$ |  $f(\theta)$  |
| :---------: | :---------: | :-------------------------: | :-------------------------------------------: | :--------------------------------------: | :-----------: |
|     $X$     |     $X$     |             $0$             |                      $0$                      |                   $0$                    |      $0$      |
|     $X$     |     $Y$     |             $0$             |                      $0$                      |                  $-2i$                   | $\sin\theta$  |
|     $X$     |     $Z$     |             $1$             |                     $-1$                      |                   $0$                    | $\cos\theta$  |
|     $Y$     |     $X$     |             $0$             |                      $0$                      |                   $2i$                   | $-\sin\theta$ |
|     $Y$     |     $Y$     |             $0$             |                      $0$                      |                   $0$                    |      $0$      |
|     $Y$     |     $Z$     |             $1$             |                     $-1$                      |                   $0$                    | $\cos\theta$  |
|     $Z$     |     $X$     |             $0$             |                      $0$                      |                   $0$                    |      $0$      |
|     $Z$     |     $Y$     |             $0$             |                      $0$                      |                   $0$                    |      $0$      |
|     $Z$     |     $Z$     |             $1$             |                      $1$                      |                   $0$                    |      $1$      |

均为三角函数，有周期性，参数平移适用