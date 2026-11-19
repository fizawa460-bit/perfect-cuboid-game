"""Checks of bircheck40 on a data folder: (i) every |Omega|<=4 hit of a search3 result goes through the 40-digit
procedure and must come out 'composite' (all such hits are composites by the double test as well); (ii) for
unrelated pairs (f, r) and a random Möbius M the 40-digit fibre test must say birational (the test can say yes).
usage: python3 test_bircheck.py res3_a_b_0of1.pkl a b [max hits]"""
import os, sys, pickle, time, numpy as np, mpmath as mp
here = os.path.dirname(os.path.abspath(__file__))
for d in ('../numeric-upto5-20261118', '.'): sys.path.insert(0, os.path.join(here, d))
import bircheck40
mp.mp.dps = 40   # before unpickling
R = pickle.load(open(sys.argv[1], 'rb')); a, b = int(sys.argv[2]), int(sys.argv[3]); NMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 10**9
A = pickle.load(open(f'all_{a}.pkl', 'rb')); B = pickle.load(open(f'all_{b}.pkl', 'rb'))
t0 = time.time(); ver = {}; worst = 0.0; best_gap = 1.0
for fi, qi, M, om, j, h in R['hits'][:NMAX]:
    r, u = B['src'][qi]
    res = bircheck40.check(('A', fi), A['reps'][fi], ('B', r), B['reps'][r], u, M)
    ver[res['verdict']] = ver.get(res['verdict'], 0) + 1
    if res['verdict'] == 'composite':
        worst = max(worst, max(f[1] for f in res['fibres']))
print(f'(i) {sum(ver.values())} hits through the 40-digit procedure: {ver}; largest 2nd-smallest fibre distance of the composites {worst:.1e}  ({time.time() - t0:.1f}s)')
rng = np.random.default_rng(1); mins = []
with mp.workdps(40):
    for k in range(20):
        fi = int(rng.integers(len(A['reps']))); r = int(rng.integers(len(B['reps'])))
        cf, _, _, n = bircheck40._ref(('A', fi), *A['reps'][fi][:3]); cr, _, _, m = bircheck40._ref(('B', r), *B['reps'][r][:3])
        M40 = [[mp.mpc(*rng.normal(size=2)) for _ in range(2)] for _ in range(2)]
        fib = bircheck40.fibre_test(cf, n, cr, m, M40)
        mins.append(min(f[1] for f in fib))
print(f'(ii) 20 random (f, r, M): smallest 2nd-smallest fibre distance {min(mins):.1e} (birational needs > 1e-12): '
      f'{sum(x > 1e-12 for x in mins)}/20 birational')
