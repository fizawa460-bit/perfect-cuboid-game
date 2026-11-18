"""Run braid_orbits on one profile per Aut(B)-orbit and compare with exact Hurwitz numbers."""
import sys, subprocess, pickle, re, itertools
sys.path.insert(0, '../numeric-upto5-20261118')
from common import AUT
from hurwitz_char import C
from fractions import Fraction
from math import factorial
n = int(sys.argv[1]); nseeds = sys.argv[2] if len(sys.argv) > 2 else '20000'
H = {}
for t in itertools.product(range(n // 2 + 1), repeat=6):
    if sum(t) == 2 * n - 2:
        h = Fraction(C(n, t), factorial(n))
        if h: H[t] = h
seen = set(); reps = []
for prof in sorted(H):
    if prof in seen: continue
    orb = set()
    for M, perm in AUT:
        t2 = [0] * 6
        for y in range(6): t2[perm[y]] = prof[y]
        orb.add(tuple(t2))
    seen |= orb; reps.append((prof, H[prof], len(orb)))
print(f'n={n}: {len(reps)} profile representatives, weighted covers in reps {float(sum(h for _,h,_ in reps))}', flush=True)
rows = []
for prof, h, osz in reps:
    out = subprocess.run(['./braid_orbits', str(n), ','.join(map(str, prof)), nseeds], capture_output=True, text=True).stdout
    comps = re.findall(r'pure-braid component \d+: tuples (\d+) weighted ([\d.]+) group (\d+)', out)
    tot = float(re.search(r'profile weighted total ([\d.]+)', out).group(1))
    rows.append((prof, float(h), tot, [(int(a), float(b), int(c)) for a, b, c in comps]))
    flag = 'OK' if abs(tot - float(h)) < 1e-6 else 'MISSING'
    cs = sorted(rows[-1][3], key=lambda c: -c[1])
    print(prof, 'H=', float(h), 'found', tot, flag, 'pure comps (weighted,group):', [(c[1], c[2]) for c in cs], flush=True)
pickle.dump(rows, open(f'census_{n}.pkl', 'wb'))
