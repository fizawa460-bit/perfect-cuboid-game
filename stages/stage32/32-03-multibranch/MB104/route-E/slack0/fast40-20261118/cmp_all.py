"""Compare two all_n.pkl files (flint vs mpmath refinement): same covers, same order, 40-digit odd points agree."""
import sys, pickle, mpmath as mp
mp.mp.dps = 50   # before unpickling (mpmath rounds unpickled numbers to the current precision)
A = pickle.load(open(sys.argv[1], 'rb')); B = pickle.load(open(sys.argv[2], 'rb'))
assert len(A['reps']) == len(B['reps']) and len(A['all']) == len(B['all']) and A['src'] == B['src']
dmax = 0.0; cmax = 0.0; npt = 0
for key in ('reps', 'all'):
    for a, b in zip(A[key], B[key]):
        assert a[3] == b[3]
        cmax = max(cmax, float(max(abs(x - y) for x, y in zip(list(a[0]) + list(a[1]), list(b[0]) + list(b[1])))))
        for y in range(6):
            for z1, z2 in zip(a[2]['hp'].get(y, []), b[2]['hp'].get(y, [])):
                assert (z1 is None) == (z2 is None)
                if z1 is not None: dmax = max(dmax, float(abs(z1 - z2) / (1 + abs(z2)))); npt += 1
print(f'reps {len(A["reps"])} all {len(A["all"])}: same covers and order; {npt} 40-digit odd points, max relative difference {dmax:.1e}; '
      f'max coefficient difference (double) {cmax:.1e}')
