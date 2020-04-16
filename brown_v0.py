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

delta = 0.01
ts = np.arange(0., 200., delta)

fig = plt.figure(figsize=(10,9))

point = np.zeros((1,2), dtype=np.float32)
for t in ts:
    next_point = point + np.random.randn(1, 2) * np.sqrt(delta)
    segment = np.vstack((point, next_point))
    plt.plot(segment[:,0], segment[:,1], linewidth=1, color='b')
    point = next_point

plt.savefig('junk/brown_full_1.png', bbox_inches='tight', inches=0)