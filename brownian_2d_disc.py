import numpy as np
import matplotlib.pyplot as plt
# plt.ion()

point = np.zeros((1, 2), dtype=np.int32)

for e in range(1000):
    delta = np.random.rand(1, 2)
    delta[delta<0.5] = -1.
    delta[delta>=0.5] = 1.
    delta = delta.astype(np.int32)
    # print(delta)

    next_point = point + delta
    segment = np.vstack((point, next_point))
    plt.plot(segment[:,0], segment[:,1], color='r')
    schandle = plt.scatter(next_point[:,0], next_point[:,1], color='r')
    # plt.draw()
    plt.savefig(f'junk/{e}.png', bbox_inches='tight', inches=0)
    # plt.pause(0.001)
    point = next_point
    schandle.remove()