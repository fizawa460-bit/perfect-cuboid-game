"""Random seeds for one profile, written as a --seedfile (P, Q, crit points, branch index), for braid orbits that the
normal run never reaches (0,3,3,3,3,4: 24 covers with AGL(2,3) monodromy in their own orbit, no edge from the rest).
usage: python3 seedhunt.py n t1,..,t6 out.pkl seconds [rng seed]     (run several with different rng seeds)
Then: mono_par ... --seedfile out.pkl (phase 2 resume) reports how many are new."""
import sys, os, time, pickle, numpy as np
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
for sub in ('degree8-20261120', 'fastmono-20261119', 'speedup-20261118'): sys.path.insert(0, os.path.join(HERE, sub))
import seed as _seed
n = int(sys.argv[1]); prof = tuple(int(x) for x in sys.argv[2].split(',')); out = sys.argv[3]; T = float(sys.argv[4])
rng = np.random.default_rng(int(sys.argv[5]) if len(sys.argv) > 5 else None)
fixed = np.array([0.31 + 0.17j, -0.52 + 0.44j, 0.13 - 0.61j])
L = rng.normal(size=2 * (n + 1)) + 1j * rng.normal(size=2 * (n + 1))
seeds = pickle.load(open(out, 'rb')) if os.path.exists(out) else []; t0 = time.time(); last = t0
while time.time() - t0 < T:
    for u_, assign, cc_ in _seed.seq_seed(n, prof, fixed, L, rng, starts=20, verbose=False):
        xg = u_[:2 * n + 2]; seeds.append((xg[:n + 1].copy(), xg[n + 1:].copy(), np.asarray(cc_).copy(), list(assign)))
    if time.time() - last > 300 or time.time() - t0 >= T:
        pickle.dump(seeds, open(out + '.tmp', 'wb')); os.replace(out + '.tmp', out); last = time.time()
        print(f'{len(seeds)} seeds, {time.time() - t0:.0f}s', flush=True)
