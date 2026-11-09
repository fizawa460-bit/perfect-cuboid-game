"""Lemma G for the d16all h0 = 1 classes closed so far only by the containment prefilter (964) or found non-reduced
(14): member residual Bp (script_v2), components over F_p, genus of each, sum (R2 package T4', as cg/).
usage (from stoll/): python d16all/mkcg.py"""
import sys, json
sys.path.insert(0, "fasth0")
from script_v2 import script
CG = open("p16all/mkcg.py").read().split("CG = '''")[1].split("'''")[0]
END = " }\nquit;\n"
L = [l.split(chr(9)) for l in open("//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt").read().split(chr(10))[:-1]]
cont = json.load(open("d16all/h1_cont.json"))
sel = [int(k) for k, v in cont.items() if v] + [666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679]
jobs = []
for k in sorted(set(sel)):
    t = L[k][2].split(); m = int(t[0]); D = {int(a): int(b) for a, b in (q.split(":") for q in t[2].split(","))}
    s = script(D, m); assert s.endswith(END)
    # Lemma G right after the residual is known (before the containment tests, which may stop the script)
    kk = s.index('if (dim(Bp) != 2) { "residual not a curve"; quit; }'); kk = s.index("\n", kk) + 1
    body = s[:kk] + 'LIB "primdec.lib"; LIB "normal.lib";\n' + CG
    open(f"d16all/h1/cg_{k}.sing", "w", newline="\n").write(body); jobs.append(f"cg_{k}")
open("d16all/h1/cgjobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
print("cg jobs", len(jobs))
