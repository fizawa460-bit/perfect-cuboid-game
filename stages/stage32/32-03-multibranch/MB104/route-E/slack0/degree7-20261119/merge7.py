"""Merge the degree-7 list: build_all output (all_7.pkl) + 60-digit extras (extras_all.pkl) + the 112323 cover whose
extra entry drifts (taken as the exact Aut(B) image of a regular cover) + the 2,2,2,2,2,2 covers that build_all
produced only as symmetry images (exact classes by fastmono exact_dedupe).  Output all_7m.pkl: reps (every cover of
the 21 representative profiles) and all = one image per coset of Stab(profile)."""
import sys, os, pickle, numpy as np, subprocess
FM = '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fastmono-20261119'
sys.path.insert(0, FM); sys.path.insert(0, FM + '/../speedup-20261118')
import mpmath as mp; mp.mp.dps = 60
import mono, monodromy as md, autact
from common import AUT
n = 7
A = pickle.load(open('all_7.pkl', 'rb')); X = pickle.load(open('extras_all.pkl', 'rb'))
prof_of = lambda an: tuple(len(an[y][1]) for y in range(6))
T6 = (2,) * 6
# --- 2,2,2,2,2,2: exact classes over build_all's entries
ri6 = [i for i, r in enumerate(A['reps']) if prof_of(r[2]) == T6]; m6 = {r: k for k, r in enumerate(ri6)}
sub = {'reps': [A['reps'][i] for i in ri6], 'all': [], 'src': []}
for c, (ri, ui) in zip(A['all'], A['src']):
    if ri in m6: sub['all'].append(c); sub['src'].append((m6[ri], ui))
pickle.dump(sub, open('sub222.pkl', 'wb'))
subprocess.run([sys.executable, FM + '/exact_dedupe.py', 'sub222.pkl', 'full_7_222222.pkl', 'aut_rules_7_222222.pkl'], check=True)
E6 = pickle.load(open('sub222_exact.pkl', 'rb'))
assert len(E6['all']) == 66640 and len(set(E6['class'])) == 66640
reps6 = [c for c in E6['all'] if prof_of(c[2]) == T6]; assert len(reps6) == 66640
# --- 112323 #21 = image of full[1541] under the symmetry with perm (1,0,4,5,2,3)
F = pickle.load(open('full_7_112323.pkl', 'rb'))
def nv(x): x = np.asarray(x, complex); x = x / x[np.argmax(np.abs(x))]; return np.r_[x.real, x.imag]
v = nv(F['sols'][1541][:2 * n + 2])
P1 = (1, 1, 2, 3, 2, 3)
cand = [(np.abs(nv(np.r_[r[0], r[1]]) - v).max(), i) for i, r in enumerate(A['reps']) if prof_of(r[2]) == P1]
d, i1541 = min(cand); print('match of full[1541] in reps: distance %.1e' % d); assert d < 1e-8
ui = [u for u, (M, perm) in enumerate(AUT) if tuple(perm) == (1, 0, 4, 5, 2, 3)]; assert len(ui) == 1; ui = ui[0]
p, q, an, aut = A['reps'][i1541]; M, perm = AUT[ui]
an2 = {perm[y]: an[y] for y in range(6)}; an2['hp'] = {perm[y]: w for y, w in an['hp'].items()}
c21 = (M[0, 0] * p + M[0, 1] * q, M[1, 0] * p + M[1, 1] * q, an2, aut); assert prof_of(an2) == P1
# check: its tuple is the target one (40-digit numbering)
sys.path.insert(0, '/home/user/work7'); import md_hp
E = pickle.load(open('extra_7_112323.pkl', 'rb'))
assert md.canon(md_hp.tuple1(c21[0], c21[1]))[0] == md.canon(E['tuples'][21])[0]; print('#21 tuple confirmed')
hp = [z for y in range(6) for z in an2['hp'][y] if z is not None] + [mp.mpc(z) for y in range(6) for z in an2[y][1]]
# --- reps
reps = [r for r in A['reps'] if prof_of(r[2]) != T6] + [tuple(r[:4]) for r in X['reps']] + [c21] + [tuple(c[:4]) for c in reps6]
allc = []; src = []
for ri, (p, q, an, aut) in enumerate(reps):
    prof = prof_of(an); seen = set()
    for ui, (M, perm) in enumerate(AUT):
        t2 = tuple(prof[[y for y in range(6) if perm[y] == z][0]] for z in range(6))
        if t2 in seen: continue
        seen.add(t2)
        an2 = {perm[y]: an[y] for y in range(6)}; an2['hp'] = {perm[y]: w for y, w in an['hp'].items()}
        allc.append((M[0, 0] * p + M[0, 1] * q, M[1, 0] * p + M[1, 1] * q, an2, aut)); src.append((ri, ui))
print('reps', len(reps), 'weighted', sum(1 / r[3] for r in reps), 'all', len(allc), 'weighted', sum(1 / c[3] for c in allc))
pickle.dump({'reps': reps, 'all': allc, 'src': src}, open('all_7m.pkl', 'wb'))
