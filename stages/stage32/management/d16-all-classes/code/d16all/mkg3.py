"""t_21 (fast bound 1): exact genus of the P^3 image by normal.lib genus.  Same member and generic projection as
gfast/tail_fast_v2.sing up to the P^3 image C3 (birational: the tail checks mult(C3) = deg of the residual), then
genus(C3) instead of the plane projections.  (Also generated for t_1967/2090/2091, which ran out of memory and were
replaced by mkgx.py, Lemma P.)  usage (from stoll/): python d16all/mkg3.py t_21"""
import sys
T = open('gfast/tail_fast_v2.sing').read()
k = T.index('// 32R-71 v2: no slocus(C3).')
add = 'int gC = genus(C3); "EXACT GENUS of the P3 image (normal.lib, over F_p-bar)", gC;\nquit;\n'
for j in sys.argv[1:]:
    s = open(f'd16all/h1/{j}.sing').read()
    open(f'd16all/h1/g3_{j}.sing', 'w', newline='\n').write(s.replace(T, T[:k] + add))
