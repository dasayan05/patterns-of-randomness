'''
clc; clear;

delta = 0.01;
ts = 0:delta:500;

for r = 1:10
    X = []; Y = [];
    X_prev = 0; Y_prev = 0;
    for t = ts
        Xt = X_prev + randn(1) * sqrt(delta);
        Yt = Y_prev + randn(1) * sqrt(delta);
        X = [X, Xt]; Y = [Y, Yt];
        X_prev = Xt; Y_prev = Yt;
    end
%     subplot(311); plot(ts, X);
%     subplot(312); plot(ts, Y);
%     subplot(313); plot(X, Y);
    plot(X, Y);
    hold on;
end
'''

import numpy as np
import matplotlib.pyplot as plt
# plt.ion()

delta = 0.01
ts = np.arange(0., 300., delta)

R = 1

points = [np.zeros((1,2), dtype=np.float32)] * R
colors = ['b']
for i, t in enumerate(ts):
    handles = []
    for r in range(R):
        next_point = points[r] + np.random.randn(1, 2) * np.sqrt(delta)
        segment = np.vstack((points[r], next_point))
        plt.plot(segment[:,0], segment[:,1], linewidth=1, color=colors[r])
        points[r] = next_point
        handle = plt.scatter(next_point[:,0], next_point[:,1], color=colors[r])
        handles.append(handle)
    # plt.draw()
    # plt.pause(0.001)
    plt.savefig(f'junk/{i}.png', bbox_inches='tight', inches=0)
    print(i)
    for handle in handles:
        handle.remove()