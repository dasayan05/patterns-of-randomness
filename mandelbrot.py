import numpy as np
import matplotlib.pyplot as plt
 
d, n = 250, 50  # pixel density & number of iterations
r = 2.5  # escape radius (must be greater than 2)
 
x = np.linspace(-2.5, 1.5, 4 * d + 1)
y = np.linspace(-1.5, 1.5, int(2.5 * d + 1))
 
A, B = np.meshgrid(x, y)
C = A + B * 1j
 
Z = np.zeros_like(C)
T = np.zeros(C.shape)

for k in range(n):
    M = abs(Z) < r
    Z[M] = Z[M] ** 2 + C[M]
    T[M] = k + 1

plt.imshow(T, cmap=plt.cm.twilight_shifted)
plt.axis('off')
plt.savefig("mandelbrot2.png", dpi=500, bbox_inches='tight', inches=0)
