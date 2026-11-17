"""CHECK-05 C1: types of the near-full coincidences in the F-02 records (../../f02/low3x3.json, low4x4.json).
Record [ia, ib, s, t, omega, j, h, bd]; m := |O| - (j + h) = number of O-points of each map left unmatched (a = b).
Counts all records with m <= 4 by (m, h, omega, birationality degree bd). usage: python -I type_count.py > type_counts.out
"""
import json, os
from collections import Counter
F02 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "f02")
out = []
for f, n in [("low3x3.json", 3), ("low4x4.json", 4)]:
    d = json.load(open(os.path.join(F02, f))); O = 2 * n + 4
    c = Counter((O - (r[5] + r[6]), r[6], r[4], r[7]) for r in d if O - (r[5] + r[6]) <= 4)
    out.append(dict(file=f, key="(m, h, omega, birationality degree)", counts=sorted([list(k) + [v] for k, v in c.items()])))
print(json.dumps(out, indent=1))
