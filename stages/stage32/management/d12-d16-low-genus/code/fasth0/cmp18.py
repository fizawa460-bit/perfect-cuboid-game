"""32R-70: compare GLPK d18 type sorting (new symmetry-broken rep order) with the old d18 results
(d18_h0.json: m; d18_h0_v2.json: corrected h0), matching reps by orbit hash."""
import json
from collections import Counter
D = "C:/Users/fizaw/claudework/stage32_research/stoll/fasth0/"
W = "//wsl.localhost/Ubuntu/root/"
old_m = json.load(open(D + "d18_h0.json")); old_h = json.load(open(D + "d18_h0_v2.json"))
ho = [l.strip() for l in open(W + "hash18_old.txt")]; hn = [l.strip() for l in open(W + "hash18_new.txt")]
O = {h: (old_m[str(i)][0], old_h[str(i)]) for i, h in enumerate(ho)}
assert len(O) == len(ho)
L = open(D + "j18_glpk.txt").read().split("\n")[:-1]
assert len(L) == len(hn)
dif = []; cnt = Counter()
for h, l in zip(hn, L):
    t = l.split(); m = None if t[0] == "None" else int(t[0]); x = None if t[1] == "None" else int(t[1])
    cnt[(m, x)] += 1
    if (m, x) != O[h]: dif.append((h, (m, x), O[h]))
print("reps", len(hn), "mismatch", len(dif), dif[:5])
print(sorted(cnt.items(), key=str))
