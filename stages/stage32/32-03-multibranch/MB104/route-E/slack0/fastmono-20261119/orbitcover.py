import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, autact
d = pickle.load(open('t222_dir/ckpt_dir_7_222222.pkl', 'rb')); R = pickle.load(open('aut_rules_7_222222.pkl', 'rb'))['rules']
syms = autact.sym_list((2,) * 6); nonconj = [k for k, s in enumerate(syms) if s[0] == 0]
keep = set(pickle.load(open('t222_dir/full_7_222222.pkl', 'rb'))['in_cov_file']); bad = set(range(len(d['TT']))) - keep
TT = d['TT']; idx = {md.canon(t)[0]: i for i, t in enumerate(TT)}
seen = np.zeros(len(TT), bool); orbits = 0; nogood = 0; sizes = []
for i in range(len(TT)):
    if seen[i]: continue
    orb = set()
    for k in nonconj:
        j = idx[md.canon(autact.apply(TT[i], R[k]))[0]]; orb.add(j)
    for j in orb: seen[j] = True
    orbits += 1; sizes.append(len(orb))
    if all(j in bad for j in orb): nogood += 1
from collections import Counter
print('Aut(24) orbits', orbits, 'sizes', Counter(sizes), 'orbits without a double-precision-good member', nogood)
