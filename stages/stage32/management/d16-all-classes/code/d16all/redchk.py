"""d16all h0=1 jobs left open by the fast tail (bound <= 1 or singular superset not finite): reducibility of the
residual curve Bp (radical + minAssGTZ over F_p), as n16/r_*.sing.  If irreducible and reduced over F_p, the exact
genus of the P3 image (normal.lib genus) is computed next (separate g3_ job).  usage: python d16all/redchk.py jobs..."""
import sys
T = open("gfast/tail_fast_v2.sing").read()
ADD = '''LIB "primdec.lib";
"residual: dim", dim(Bp), " degree", mult(Bp);
ideal Br = std(radical(Bp)); "residual reduced:", size(reduce(Br, Bp)) == 0, " radical degree", mult(Br);
list PA = minAssGTZ(Bp); int q; "components", size(PA);
for (q = 1; q <= size(PA); q++) { ideal Pq = std(PA[q]); "  comp", q, " dim", dim(Pq), " degree", mult(Pq); kill Pq; }
if (size(PA) >= 2) { "RESIDUAL-REDUCIBLE"; } else { if (mult(Br) < mult(Bp)) { "RESIDUAL-NONREDUCED"; } else { "RESIDUAL-IRREDUCIBLE-OVER-FP"; } }
quit;
'''
for j in sys.argv[1:]:
    s = open(f"d16all/h1/{j}.sing").read(); assert T in s
    open(f"d16all/h1/rc_{j}.sing", "w", newline="\n").write(s.replace(T, ADD)); print("rc", j)
