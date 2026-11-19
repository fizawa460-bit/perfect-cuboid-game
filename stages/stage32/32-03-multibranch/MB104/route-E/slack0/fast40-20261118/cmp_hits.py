"""Compare the |Omega|<=4 hits of search2 (res2_*.pkl) and search3 (res3_*.pkl): same (f, q, Omega, M up to scale)."""
import sys, pickle, numpy as np
def keys(fns):
    out = {}
    for fn in fns:
        R = pickle.load(open(fn, 'rb'))
        for h in R.get('hitsM', R['hits']):      # degree6-20261118/search2.py stores (f, q, M, om) under 'hitsM'
            fi, qi, M, om = h[:4]; Mf = np.asarray(M).reshape(4); Mf = Mf / Mf[np.argmax(np.abs(Mf))]
            out.setdefault((int(fi), int(qi), int(om)), []).append(Mf)
    return out
A = keys(sys.argv[1].split(',')); B = keys(sys.argv[2].split(','))
na = sum(map(len, A.values())); nb = sum(map(len, B.values()))
miss = []
for k in set(A) | set(B):
    la, lb = A.get(k, []), B.get(k, [])
    for M in la:
        if not any(np.abs(M - M2).max() < 1e-5 for M2 in lb): miss.append(('only in first', k))
    for M in lb:
        if not any(np.abs(M - M2).max() < 1e-5 for M2 in la): miss.append(('only in second', k))
print(f'hits: first {na}, second {nb}; differences: {len(miss)}', miss[:10])
