"""Could any near-threshold distance (1e-20 <= d < 1e-14, rejected) turn a candidate into a |Omega|<=4 hit?
For each recorded candidate: |Omega| lower bound if every such pair were accepted (one-to-one ignored, so this is
generous).  usage: python3 midcheck.py mid_*.pkl"""
import sys, pickle
nA = nB = 18
worst = 99; tot = 0
for fn in sys.argv[1:]:
    M = pickle.load(open(fn, 'rb')); tot += len(M)
    for fi, qi, lst, xs, ys, Mx, nclose in M:
        rows = {a for a, b, d in lst if d >= 1e-20}
        om = nA + nB - 2 * (int(nclose) + len(rows)); worst = min(worst, om)
        if om <= 4: print('POSSIBLE', fn, fi, qi, nclose, len(rows))
    print(fn, len(M), 'records; smallest |Omega| even if all rejected near pairs were accepted:', worst)
