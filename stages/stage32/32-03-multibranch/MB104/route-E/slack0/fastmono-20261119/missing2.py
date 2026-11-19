"""missing classes of a mono_dir checkpoint that a move or symmetry predicts, and which covers lead there"""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, autact, mono_dir
from collections import defaultdict
def find(d, prof, rules_file):
    R = pickle.load(open(rules_file, 'rb'))
    rkey = {(cj, pi): w for (cj, M, pi), (pi2, w) in zip(autact.sym_list(tuple(R['prof'])), R['rules'])}
    syms = autact.sym_list(prof); rules = [(pi, rkey[(cj, pi)]) for cj, M, pi in syms]
    TT = d['TT']; known = set(md.canon(t)[0] for t in TT); via = defaultdict(list)
    for i, t in enumerate(TT):
        for k, mv in enumerate(mono_dir.MOVES):
            for half in (True, False):
                pt = mono_dir.predict(t, mv); pt = pt if half else mono_dir.predict(pt, mv)
                if not md.check(pt, prof): continue
                c = md.canon(pt)[0]
                if c not in known: via[c].append(('half' if half else 'full', k, i))
        for k, r in enumerate(rules):
            c = md.canon(autact.apply(t, r))[0]
            if c not in known: via[c].append(('sym', k, i))
    return via
if __name__ == '__main__':
    d = pickle.load(open(sys.argv[1], 'rb')); prof = tuple(int(x) for x in sys.argv[2].split(','))
    via = find(d, prof, sys.argv[3])
    import collections
    print('kinds', collections.Counter(x[0] for l in via.values() for x in l))
    print('known', len(d['TT']), 'missing reachable by a prediction', len(via))
    for c, l in via.items(): print(len(l), l[:6])
