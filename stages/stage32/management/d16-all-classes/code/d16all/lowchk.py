"""d16all h0=1 jobs with FASTGENUS bound <= 1: exact check.  Same member and projections as the fast tail
(tail_fast_v2 lines up to the birational plane image), then factorize the plane image (reducible image => reducible
curve) and, if irreducible over F_p, the geometric genus of the plane curve (normal.lib genus).
usage (from stoll/): python d16all/lowchk.py t_21 ... -> d16all/h1/lc_<job>.sing"""
import sys
T = open("gfast/tail_fast_v2.sing").read().split("\n")
k = [i for i, l in enumerate(T) if l.startswith('if (size(Fq) != 1')][0]
HEAD = "\n".join(T[:k + 1])
ADD = '''list FF = factorize(Fp[1]); "plane image factors", size(FF[1]) - 1;
if (size(FF[1]) - 1 >= 2 || FF[2][size(FF[1])] >= 2) { "PLANE-IMAGE-REDUCIBLE: member reducible"; quit; }
int gg = genus(ideal(Fp[1])); "EXACT GENUS (plane curve, over F_p-bar)", gg;
quit;'''
END = " }\nquit;\n"
for j in sys.argv[1:]:
    s = open(f"d16all/h1/{j}.sing").read(); a = s.index('LIB "sing.lib"; LIB "normal.lib"; LIB "primdec.lib";')
    open(f"d16all/h1/lc_{j}.sing", "w", newline="\n").write(s[:a] + HEAD + "\n" + ADD + "\n" + END)
    print("lc", j)
