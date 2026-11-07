"""32R-69c: recompute h0 of every judged rep with the corrected v2 spaces and compare with the recorded (v1) h0."""
import sys, os, re, json
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fasth0v2 as F
def ref_h0(paths):
    for o in paths:
        if os.path.exists(o):
            m = re.search(r"h0\): (\d+)", open(o, errors="replace").read())
            if m: return int(m.group(1))
    return None
which = sys.argv[1]
res = Counter(); changed = []
if which in ("12", "14", "16"):
    d = which; pre = {"12": "f12", "14": "f14/f14", "16": "f16/f16"}[d]
    import glob
    files = sorted(glob.glob(f"{pre}_*_p.sing")) if d != "12" else sorted(glob.glob("f12_*_p.sing"))
    for f in files:
        i = re.search(r"_(\d+)_p\.sing$", f).group(1)
        base = f[:-7]
        r0 = ref_h0([base + "_p.out", base + "_s.out", base + ".out"])
        if r0 is None: res["noref"] += 1; continue
        m, comps = F.comps_from_sing(f)
        if any((c, m) not in F.ANN for c in comps): res["skip"] += 1; continue
        h = F.h0(m, comps); res[(r0, h)] += 1
        if h != r0: changed.append((int(i), r0, h))
else:
    H = json.load(open("fasth0/d18_h0.json"))
    for i, (m, h0v, D) in H.items():
        if m is None: res["nodec"] += 1; continue
        comps = [f"C{k}_{c}" for k, c in D.items() if int(k) <= 92] + [f"N{k}_{c}" for k, c in D.items() if int(k) > 92]
        if any((c, m) not in F.ANN for c in comps): res["skip"] += 1; continue
        h = F.h0(m, comps); res[(h0v, h)] += 1
        if h != h0v: changed.append((int(i), h0v, h))
print(which, dict(res))
inc = [c for c in changed if c[2] > c[1]]; dec = [c for c in changed if c[2] < c[1]]
print("h0 increased (old h0=0 claims at risk if old was 0):", len(inc), "of which old 0:", sum(1 for c in inc if c[1] == 0), inc[:15])
print("h0 decreased:", len(dec))
json.dump({"changed": changed}, open(f"fasth0/recheck_v2_d{which}.json", "w"))
