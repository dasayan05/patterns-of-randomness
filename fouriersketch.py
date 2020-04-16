import numpy as np
import matplotlib.pyplot as plt
# plt.ion()

def complex2vector(c):
    # reinterprets the complex number a+ib as [a, b]^T
    return np.array([c.real, c.imag])

def fourier(t, fs, C):
    Cr, Ci = C
    S = 0.
    for f, cr_f, ci_f in zip(fs, Cr, Ci):
        c = np.complex(cr_f, ci_f)
        S += c * np.exp(f * 2 * np.pi * I * t)
    return complex2vector(S)

I = np.complex(0, 1) # the complex constant 'i'

def main( args ):
    L = args.range
    fs = np.arange(-L, L + 1) # The frequency range [-L, L]

    fig, ax = plt.subplots(3, 5, figsize=(12, 6))
    T = np.linspace(0., 1., num = 500)

    ALL = []
    for s in range(3):
        S = []
        for X in range(1, 6):
            c0r, cpr, cnr = np.random.rand(1,) * 5, 5 * np.random.rand(L,), 5 * np.random.rand(L,)
            c0i, cpi, cni = np.random.rand(1,) * 5, 5 * np.random.rand(L,), 5 * np.random.rand(L,)
            Cr = np.array([*cnr, *c0r, *cpr])
            Ci = np.array([*cni, *c0i, *cpi]) * (1. if args.complexcoeff else 0.)

            Q = []
            for t in T:
                Q.append( fourier(t, fs[X:-X], (Cr[X:-X], Ci[X:-X])) )
            Q = np.stack(Q, 0)
            S.append(Q)
        ALL.append(S)

    for t_i, t in enumerate(T):
        for s in range(3):
            for X in range(1, 6):
                Q = ALL[s-1][X-1]
                xmin, xmax = Q[:,0].min(), Q[:,0].max()
                ymin, ymax = Q[:,1].min(), Q[:,1].max()
                ax[s, X-1].set_xlim([xmin-0.5, xmax+0.5])
                ax[s, X-1].set_ylim([ymin-0.5, ymax+0.5])
                ax[s, X-1].plot(Q[:t_i+1, 0], Q[:t_i+1, 1], color='b')
                ax[s, X-1].scatter(Q[t_i, 0], Q[t_i, 1], color='b', s=6)
                ax[s, X-1].set_xticks([]); ax[s, X-1].set_yticks([])
        plt.draw()
        plt.savefig(f'junk/{t_i}.png', bbox_inches='tight', inches=0)
        for s in range(3):
            for X in range(1, 6):
                ax[s, X-1].cla()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', '--range', type=int, required=False, default=10, help='Frequency range on both side')
    parser.add_argument('--complexcoeff', action='store_true', help='Coeffs to be complex ?')
    args = parser.parse_args()

    main( args )
