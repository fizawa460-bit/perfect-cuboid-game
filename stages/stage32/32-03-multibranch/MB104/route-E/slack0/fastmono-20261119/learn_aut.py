"""learn the action of every symmetry on tuples from sample covers; writes aut_rules_<n>_<prof>.pkl"""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, fasttuples as ft, autact
from mono import System, homB
import mono_dir
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = tuple(int(x) for x in sys.argv[2].split(','))
nsamp = int(sys.argv[3]) if len(sys.argv) > 3 else 40
S = System(n, prof, d['fixed'], d['L']); rng = np.random.default_rng(0)
U = d['sols'][rng.choice(len(d['sols']), min(len(d['sols']), 4 * nsamp), replace=False)]
def an_simple(u):
    _, _, cc = S.unpack(u[None]); return {y: ([], [cc[0][k] for k in range(S.K) if S.ys[k] == y]) for y in range(6)}
to_u = mono_dir.make_to_u(S, n)
syms = autact.sym_list(prof); rules = []
def num1(u):
    try:
        t = ft.tuples(*S.unpack(u[None])[:2], 12)[0]; return t if md.check(t, prof) else None
    except (RuntimeError, AssertionError): return None
T = [num1(u) for u in U]; U = np.array([u for u, t in zip(U, T) if t is not None]); T = [t for t in T if t is not None]
for k, (cj, M, pi) in enumerate(syms):
    pairs = []
    for u, t in zip(U, T):
        pp, qq, _ = S.unpack(u[None]); x2, an2 = autact.image_cover(np.concatenate([pp[0], qq[0]]), an_simple(u), n, cj, M, pi)
        u2 = to_u(x2, an2)
        if u2 is None: continue
        try: t2 = ft.tuples(*S.unpack(u2[None])[:2], 12)[0]
        except Exception: continue
        if md.check(t2, prof): pairs.append((t, t2))
        if len(pairs) >= nsamp: break
    T0 = [a for a, _ in pairs]; T2 = [b for _, b in pairs]
    w = autact.learn(T0[:12], T2[:12], pi, n)
    ok = sum(md.canon(autact.apply(a, (pi, w)))[0] == md.canon(b)[0] for a, b in pairs) if w else 0
    print(k, 'conj', cj, 'pi', pi, 'words', w, f'verified {ok}/{len(pairs)}', flush=True)
    rules.append((pi, w))
pickle.dump({'prof': prof, 'rules': rules}, open(f'aut_rules_{n}_{"".join(map(str, prof))}.pkl', 'wb'))
