import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, fasttuples as ft
from mono import System, analyse, analyse_loose
d = pickle.load(open('t222_dir/ckpt_dir_7_222222.pkl', 'rb')); n = 7; prof = (2,) * 6
S = System(n, prof, d['fixed'], d['L'])
bad = []
for k in range(3): bad += pickle.load(open(f'ver/verify_{k}_3.pkl', 'rb'))['bad']
TUPI = {md.canon(t)[0]: i for i, t in enumerate(d['TT'])}
for i in sorted(bad):
    u = d['sols'][i]; p, q, cc = S.unpack(u[None])
    out = []
    for m in (12, 30, 60, 120):
        try: t = ft.tuples(p, q, m)[0]; ok = md.check(t, prof); c = md.canon(t)[0] if ok else None
        except Exception as e: out.append(f'm{m}:fail'); continue
        out.append(f'm{m}:' + ('invalid' if not ok else ('label' if c == md.canon(d['TT'][i])[0] else f'other(idx {TUPI.get(c)})')))
    cs = cc[0]; dmin = min(abs(cs[a] - cs[b]) for a in range(12) for b in range(a))
    an = analyse(p[0], q[0], n, prof, cs, list(S.ys))
    print(i, 'rep' if d['ISREP'][i] else 'img', 'conf' if d['CONF'][i] else 'unconf', f'dmin {dmin:.1e}', 'analyse', an is not None, out, flush=True)
