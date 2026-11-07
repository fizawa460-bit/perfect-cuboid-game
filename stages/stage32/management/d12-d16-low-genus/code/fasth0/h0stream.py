"""32R-70: stdin = decglpk output lines (m c[140] | NONE | UNK ...), stdout = one line per rep:
   m h0 k:c,k:c,...   (k = 1-based generator index as in judge_fast)   |  None None -  |  UNK ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fasth0v2 as F
out = sys.stdout
for line in sys.stdin:
    t = line.split()
    if not t: continue
    if t[0] == "NONE": out.write("None None -\n"); continue
    if t[0] == "UNK": out.write(line); continue
    m = int(t[0]); c = list(map(int, t[1:141]))
    comps = [f"C{i+1}_{c[i]}" for i in range(92) if c[i] > 0] + [f"N{i+1}_{c[i]}" for i in range(92, 140) if c[i] > 0]
    out.write(f"{m} {int(F.h0(m, comps))} " + ",".join(f"{i+1}:{c[i]}" for i in range(140) if c[i] > 0) + "\n")
