"""E06 should-fix S1: the three subgroups of G of order 4 that contain two singular involutions (involutions with
8 fixed points on C8) are conjugate under Aut(C8) = Delta/Gamma (192 elements, built exactly in ../hecke).
usage: python -I -O k4_conjugacy.py   (from the repository root or anywhere)"""
import os, sys, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hecke"))
import hecke as H
sing = [g for g in H.G if g != 0 and H.FP[g] == 8]
subs = []
for a, b in itertools.combinations(sing, 2):
    S = frozenset({0, a, b, H.gmul(a, b)})
    if S not in subs: subs.append(S)
orbit = {frozenset(H.conj(x, c) for x in subs[0]) for c in range(H.NG)}
ok = len(sing) == 3 and len(subs) == 3 and set(subs) <= orbit
print("singular involutions:", len(sing), " order-4 subgroups with two of them:", len(subs),
      " all conjugate:", set(subs) <= orbit)
print("PASS" if ok else "FAIL")
if not ok: raise SystemExit(1)
