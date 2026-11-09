"""Fast Lemma G for the d16all h0 = 1 classes (containment 964 + non-reduced 14): residual Bp (script_v2), remove every
contained known curve by saturation (known curves counted with genus 0: a lower bound), then on the remainder R:
fast tail (tail_fast_v2) with an extra irreducibility check of the plane image (factorize over F_p).
R integral => Lemma G: g(C_0) >= g(R) >= FASTGENUS bound.  Remainder reducible / not birational -> flagged.
usage (from stoll/): python d16all/mklg.py"""
import sys, json
sys.path.insert(0, "fasth0")
from script_v2 import script
T = open("gfast/tail_fast_v2.sing").read()
k = T.index("if (size(Fq) != 1"); k = T.index("\n", k) + 1
FACT = 'list FFR = factorize(Fp[1]); if (size(FFR[1]) - 1 >= 2 || FFR[2][size(FFR[1])] >= 2) { "LG-REMAINDER-REDUCIBLE plane factors", size(FFR[1]) - 1; quit; } "LG-REMAINDER-INTEGRAL";\n'
TAIL = T[:k] + FACT + T[k:]
PRE = '''ideal RR = Bp; int kq; int nk = 0;
for (kq = 1; kq <= 92; kq++) { int nk0 = nk; execute("if (size(reduce(RR, Q" + string(kq) + ")) == 0) { def TT = sat(RR, Q" + string(kq) + "); if (typeof(TT) == \\"list\\") { RR = std(TT[1]); } else { RR = std(TT); } kill TT; nk++; }"); if (nk > nk0) { "  removed known curve", kq; } kill nk0; }
"remainder after known curves: dim", dim(RR), " degree", mult(RR), " known removed", nk;
if (dim(RR) < 2) { "LG-ONLY-KNOWN"; quit; }
Bp = RR; kill RR;
'''
END = " }\nquit;\n"
L = [l.split(chr(9)) for l in open("//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt").read().split(chr(10))[:-1]]
cont = json.load(open("d16all/h1_cont.json"))
sel = sorted(set([int(c) for c, v in cont.items() if v] + list(range(666, 680))))
jobs = []
for c in sel:
    t = L[c][2].split(); m = int(t[0]); D = {int(a): int(b) for a, b in (q.split(":") for q in t[2].split(","))}
    s = script(D, m); assert s.endswith(END)
    kk = s.index("if (hit == 0) {")
    open(f"d16all/h1/lg_{c}.sing", "w", newline="\n").write(s[:kk] + PRE + TAIL + "\nquit;\n"); jobs.append(f"lg_{c}")
open("d16all/h1/lgjobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n")
print("lg jobs", len(jobs))
