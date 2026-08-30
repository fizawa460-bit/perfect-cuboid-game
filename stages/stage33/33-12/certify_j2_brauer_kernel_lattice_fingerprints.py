#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATH = HERE / "j2-brauer-kernel-lattice-fingerprints.json"

def det2(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]

def gram_for_basis(G, B):
    # B rows are basis vectors in the marked T basis.
    out = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            out[i][j] = sum(B[i][a] * G[a][a] * B[j][a] for a in range(2))
    return out

def minimum_norm(g, bound=24):
    best = None
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            if x == 0 and y == 0:
                continue
            q = g[0][0]*x*x + 2*g[0][1]*x*y + g[1][1]*y*y
            if best is None or q < best:
                best = q
    return best

c = json.loads(PATH.read_text())
assert c["schema"] == "STAGE33_12_J2_BRAUER_KERNEL_LATTICE_FINGERPRINTS_V1"
G = c["source"]["transcendental_lattice_gram"]
assert G == [[4, 0], [0, 8]]
expected = {
    "1,0": ([[2,0],[0,1]], 8),
    "0,1": ([[1,0],[0,2]], 4),
    "1,1": ([[1,1],[1,-1]], 12),
}
mins = {}
for key, (basis, mn) in expected.items():
    row = c["kernel_lattices"][key]
    assert row["basis_in_T"] == basis
    g = gram_for_basis(G, basis)
    assert g == row["gram"]
    assert det2(g) == 128 == row["determinant"]
    assert minimum_norm(g) == mn == row["minimum_norm"]
    mins[key] = mn
assert len(set(mins.values())) == 3
assert c["exact_conclusion"]["all_three_kernel_lattices_pairwise_nonisometric"] is True
assert c["exact_conclusion"]["minimum_norm_to_functional"] == {"4":[0,1], "8":[1,0], "12":[1,1]}
payload = dict(c)
claimed = payload.pop("canonical_sha256")
actual = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
assert actual == claimed
print(json.dumps({"status":"PASS_EXACT", "canonical_sha256":claimed, "minimum_norms":mins}, sort_keys=True))
