"""Lemma G (R2 package T4') for the p16all member jobs left open by the fast tail (bound <= 1) or reducible:
components of the residual Bp over F_p (minAssGTZ), geometric genus of each (normal.lib; as cg/*.sing), sum.
Sum >= 2 => g(C_0) >= 2.  usage (from stoll/): python p16all/mkcg.py"""
import re, glob, os
CG = '''list MA = minAssGTZ(Bp); int ia; int GS = 0; int GL;
for (ia = 1; ia <= size(MA); ia++) { ideal QA = std(MA[ia]); if (dim(QA) == 2) { intvec HQ = hilbPoly(QA); int paq = 1 - HQ[1];
  if (mult(QA) <= 2 || paq <= 0) { GL = 0; } else { GL = genus(QA); }
  "COMP degree", mult(QA), " pa", paq, " genus", GL; if (GL > 0) { GS = GS + GL; } kill HQ; kill paq; } kill QA; }
"GENUS-SUM", GS;
quit;
'''
jobs = []
for f in sorted(glob.glob("p16all/sx_*.out")):
    o = open(f).read(); m = re.findall(r"FASTGENUS(?: lower bound)? (-?\d+)", o)
    if m and int(m[-1]) >= 2: continue
    j = os.path.basename(f)[:-4]; s = open(f"p16all/{j}.sing").read()
    k = s.index("if (mult(Bp) < ")
    s2 = s[:k] + 'LIB "primdec.lib"; LIB "normal.lib";\n' + CG
    open(f"p16all/cg_{j}.sing", "w", newline="\n").write(s2); jobs.append(f"cg_{j}")
open("p16all/cgjobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
print("cg jobs", len(jobs))
