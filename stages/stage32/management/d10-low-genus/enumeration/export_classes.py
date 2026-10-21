#!/usr/bin/env python3
"""Stage32 D10-LOW-GENUS: expand the representative classes of results.jsonl by the slice symmetry groups and
write classes_d10.json (sorted). usage: python export_classes.py REPO"""
import json, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import slice_lib as L, run_d10 as RD
from flint import fmpq_mat, fmpq, fmpz_mat
L.load(sys.argv[1]); Cn = L.D["Cn"]
grp = L.group(json.loads((HERE / "symmetry_generators.json").read_text())["generators"])
bi, rk = [], 0
for i in range(140):
    if fmpz_mat([[int(v) for v in Cn[k]] for k in bi + [i]]).rank() > rk:
        bi.append(i); rk += 1
    if rk == 64: break
Binv = fmpq_mat([[fmpq(int(v)) for v in Cn[i]] for i in bi]).inv()
out = set()
for l in (HERE / "results.jsonl").read_text().splitlines():
    r = json.loads(l)
    if not r["classes"]: continue
    for g in RD.slice_use(grp, r["n1"]):
        Q = Binv * fmpq_mat([[fmpq(int(v)) for v in Cn[g[i]]] for i in bi])
        Qn = np.array([[int(Q[a, b].p) for b in range(64)] for a in range(64)], dtype=object)
        for x in r["classes"]:
            out.add(tuple(int(v) for v in np.array(x, dtype=object).dot(Qn)))
(HERE / "classes_d10.json").write_bytes(('{"classes": [\n' + ",\n".join(json.dumps(list(x), separators=(",", ":")) for x in sorted(out)) + "\n]}\n").encode())
print("classes:", len(out))
