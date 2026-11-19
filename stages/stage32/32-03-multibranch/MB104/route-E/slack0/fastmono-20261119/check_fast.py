import sys, os, pickle, time, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../speedup-20261118'))
import mono, monodromy as md, fasttuples as ft
from mono import System
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = (2,) * 6
S = System(n, prof, d['fixed'], d['L']); U = d['sols'][:int(sys.argv[2])]; p, q, _ = S.unpack(U)
t = time.time(); T0 = md.tuples(p, q); t1 = time.time() - t
for m in (6, 12, 20):
    t = time.time(); T1 = ft.tuples(p, q, m); t2 = time.time() - t
    print(f'm={m}: identical {sum(a == b for a, b in zip(T0, T1))}/{len(T0)}  time {t1/len(U)*1e3:.1f} -> {t2/len(U)*1e3:.1f} ms/cover', flush=True)
