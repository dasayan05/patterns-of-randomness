import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
# plt.style.use('Agg')

# plt.ion()

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.02)

states = odeint(f, state0, t)
N, _ = states.shape
delta = 25

xmin, xmax = states[:,0].min(), states[:,0].max()
ymin, ymax = states[:,1].min(), states[:,1].max()
zmin, zmax = states[:,2].min(), states[:,2].max()

fig = plt.figure(figsize=(12, 5))
ax = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
# plt.axis('off')
# ax.set_xticks([]);ax.set_yticks([]);ax.set_zticks([])

colors = np.ones((delta, 4))
colors[:,1:3] = 0.
alphas = np.arange(0., 1., 1./delta)
colors[:, -1] = alphas
# breakpoint()

# plt.draw()

ax2.plot(states[:, 0], states[:, 1], states[:, 2], color='red')

c = 0
for i in range(0, N - delta, 2):
    ax.set_xlim([xmin, xmax]); ax.set_ylim([ymin, ymax]); ax.set_zlim([zmin, zmax])
    ax.plot(states[i:i+delta, 0],
            states[i:i+delta, 1],
            states[i:i+delta, 2], color='red')
    # dot_handle = ax.scatter(states[i+delta, 0], states[i+delta, 1], states[i+delta, 2], color='r')
    # plt.draw()
    # plt.pause(0.0001)
    if i % 4 == 0:
        ax2.view_init(30, (0.1*i)%360)
        plt.savefig(f'junk/{c}.png', bbox_inches='tight', inches=0); c+=1
        pass
    ax.cla()