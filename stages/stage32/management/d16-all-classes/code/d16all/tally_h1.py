"""32R-82/83: tally d18/h1 outputs.  A finished job has a FASTGENUS line, a 'FAST:' give-up line,
'residual not a curve', or a known-curve hit.  Any other .out (e.g. a killed job) is incomplete.
usage: python tally_h1.py [--clean]   (--clean deletes incomplete .out files so the run redoes them)"""
import os, re, sys, glob
from collections import Counter
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "h1")
jobs = [l.strip() for l in open(os.path.join(H, "jobs.txt")) if l.strip()]
c = Counter(); low = []; inc = []; giveup = []
for j in jobs:
    p = os.path.join(H, j + ".out")
    if not os.path.exists(p): c["not run yet"] += 1; continue
    s = open(p).read()
    m = re.findall(r"FASTGENUS(?: lower bound)? (-?\d+)", s)
    if m:
        g = int(m[-1]); c["bound>=2" if g >= 2 else "bound<=1"] += 1
        if g < 2: low.append(j)
    elif "FAST:" in s: c["fast gave up"] += 1; giveup.append(j)
    elif "residual not a curve" in s: c["residual not a curve"] += 1
    elif re.search(r"known curve .*inside|contains known", s) and "no known curve inside" not in s: c["contains known curve"] += 1
    else: c["incomplete"] += 1; inc.append(p)
print(dict(c)); print("bound<=1:", low[:20]); print("gave up:", giveup[:20])
if "--clean" in sys.argv:
    for p in inc: os.remove(p)
    print("removed incomplete:", len(inc))
