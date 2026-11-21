"""Check that the covers of an L5 file are pairwise different (as covers: f2 = f1 o phi for a Moebius phi counts as equal).

usage: python3 distinct5.py L5_n_tag.pkl [...]

Fingerprint: the fibre of f = P/Q over two fixed generic points w0, w1 (n points each); for every 4 of them the
j-invariant of their cross ratio (independent of the order of the 4 points and of phi).  The fingerprint is the
first power sums of t = j / (1 + |j|) over all 4-subsets.  Equal covers give equal fingerprints; two covers whose
fingerprints agree to 1e-7 are reported (then compare them exactly).  This guards the names that came only from a
prediction (unconfirmed): a misnamed cover would duplicate another cover of the list.
"""
import sys, pickle, itertools
import numpy as np


def fibre(p, q, w):
    c = p - w * q                     # low -> high
    while abs(c[-1]) < 1e-14 * np.abs(c).max(): c = c[:-1]
    return np.roots(c[::-1])


def jinv(z, idx):
    a, b, c, d = (z[idx[:, k]] for k in range(4))
    lam = (a - c) * (b - d) / ((a - d) * (b - c))
    return (lam * lam - lam + 1) ** 3 / (lam * lam * (lam - 1) ** 2)


def fingerprints(pq, n):
    idx = np.array(list(itertools.combinations(range(n), 4)))
    out = np.zeros((len(pq), 6), complex)
    for i, row in enumerate(pq):
        p, q = row[:n + 1], row[n + 1:]
        fs = []
        for w in (0.3137 + 0.7171j, -0.4421 + 0.2283j):
            z = fibre(p, q, w)
            if len(z) < n: z = np.concatenate([z, [1e12] * (n - len(z))])   # a point at infinity (rare)
            t = jinv(z, idx); t = t / (1 + np.abs(t))
            fs += [t.mean(), (t * t).mean(), (t ** 3).mean()]
        out[i] = fs
    return out


def main():
    bad = 0
    for fn in sys.argv[1:]:
        d = pickle.load(open(fn, 'rb')); n = d['n']; pq = d['pq']; N = len(pq)
        F = fingerprints(pq, n)
        key = F[:, 0].real + 0.37 * F[:, 0].imag
        o = np.argsort(key); close = 0
        for a in range(N - 1):
            b = a + 1
            while b < N and key[o[b]] - key[o[a]] < 1e-6:
                if np.abs(F[o[a]] - F[o[b]]).max() < 1e-7:
                    close += 1
                    print(f'  {fn}: covers {o[a]} and {o[b]} have the same fingerprint (log {d["log"][o[a]][2:]} / {d["log"][o[b]][2:]})')
                b += 1
        # spacing of the fingerprints, to see the test has room
        gaps = [np.abs(F[o[a]] - F[o[a + 1]]).max() for a in range(N - 1)]
        print(f'{fn}: {N} covers, pairs with equal fingerprint {close}; smallest neighbour gap {min(gaps) if gaps else 0:.1e}', flush=True)
        bad += close
    sys.exit(1 if bad else 0)


if __name__ == '__main__': main()
