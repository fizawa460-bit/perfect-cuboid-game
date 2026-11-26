"""Seeds for a profile from covers of another profile that differs by exchanging two entries, by moving the two branch
points into each other's places (the monodromy group, e.g. AGL(2,3), is kept along any such path).

usage: python3 swapseed.py pack_9_<tagA>.npz a b out.pkl [classes.pkl]
  pack (pack9.py) of profile A; a, b: branch indices to exchange (b in 2..5, a any other); the result is a seed file
  (P, Q, crit points, branch index of each) for profile A with entries a, b exchanged (mono_par --seedfile).
  classes.pkl (agl_classes.py output, dict prof -> {canonical tuple: aut}): only refined members whose class is in it.
The two points move along the circle (line) through B[b] with direction exp(i pi/3) and infinity, which meets no other
point of B = {0, inf, 1, -1, i, -i} when b = 5 (-i); each step is tracked at 40 digits (hp_track)."""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); SL = os.path.join(HERE, '..')
for d in ('fastmono-20261119', 'speedup-20261118'): sys.path.insert(0, os.path.join(SL, d))
import hp_track, monodromy as md
from mono import System, homB

def main():
    pk, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    z = np.load(pk); meta = pickle.loads(z['meta'].tobytes()); n = int(z['n']); tag = str(z['tag'])
    prof = tuple(int(c) for c in tag); fixed = np.asarray(meta['fixed']); L = np.asarray(meta['L'])
    S = System(n, prof, fixed, L); reps = z['reps']; sols = z['sols']; TT = z['tuples']
    sel = list(range(len(reps)))
    if len(sys.argv) > 5:
        C = pickle.load(open(sys.argv[5], 'rb'))[prof]
        sel = [k for k in sel if md.canon(tuple(map(tuple, TT[reps[k]].tolist())))[0] in C]
    print(f'{tag}: {len(sel)} start covers', flush=True)
    B0 = homB(); e = np.exp(1j * np.pi / 3); zb = B0[b, 0] / B0[b, 1]
    assert a == 1, 'only the point at infinity is implemented as a'
    def pt(al): return np.array([zb * np.cos(al) + e * np.sin(al), np.cos(al)])     # line zb + r e, r = tan(al)
    m = 24; Ws = []
    for k in range(m + 1):
        al = -np.pi / 2 + (np.pi / 2) * k / m; W = B0.copy()
        W[a] = pt(al); W[b] = pt(al + np.pi / 2); Ws.append(W)
    # Ws[0]: W[a] = (-e, 0) ~ infinity, W[b] = B[b]; Ws[-1]: W[a] = B[b], W[b] = (e, 0) ~ infinity
    seeds = []
    for k in sel:
        u = sols[k]
        try: uh = hp_track.track_path(S, u, Ws, dps=40)
        except Exception as ex: print(k, 'failed', ex, flush=True); continue
        if uh is None: print(k, 'track failed', flush=True); continue
        un = hp_track.to_np(uh); p, q, c = S.unpack(un[None]); ys = S.ys.copy()
        ys2 = np.where(ys == a, b, np.where(ys == b, a, ys))
        seeds.append((p[0].copy(), q[0].copy(), c[0].copy(), list(ys2)))
        print(k, 'ok', flush=True)
        pickle.dump(seeds, open(out + '.tmp', 'wb')); os.replace(out + '.tmp', out)
    print(f'{len(seeds)} seeds -> {out}', flush=True)

if __name__ == '__main__': main()
