#!/usr/bin/env python3
import ast
import hashlib
import json
import math
import pathlib
import re

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = pathlib.Path(__file__).resolve().parent
stdout = (ROOT / "magma-stdout.txt").read_text(encoding="utf-8")
if "STAGE33_02_BEGIN" not in stdout or "STAGE33_02_END" not in stdout:
    raise SystemExit("missing Stage33-02 completion markers")
if "GALOIS_BOUNDARY_STABLE=true" not in stdout:
    raise SystemExit("missing Galois stability certificate")


def scalar(name):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return m.group(1).strip()


def seq(name):
    return ast.literal_eval(scalar(name).replace(" ", ""))


def numbered(prefix):
    found = {}
    for m in re.finditer(rf"^{re.escape(prefix)}_(\d+)=(.+)$", stdout, re.M):
        found[int(m.group(1))] = ast.literal_eval(m.group(2).strip().replace(" ", ""))
    if not found:
        raise SystemExit(f"no {prefix} rows")
    return [found[i] for i in range(1, max(found) + 1)]

boundary_count = int(scalar("BOUNDARY_COMPONENT_COUNT"))
pic_rank_claim = int(scalar("PIC_RANK"))
image_rank_claim = int(scalar("BOUNDARY_IMAGE_RANK"))
kernel_rank_claim = int(scalar("UNIT_KERNEL_RANK"))
boundary_indices = seq("BOUNDARY_INDICES")
perm_cc = seq("BOUNDARY_PERM_CC")
perm_ct = seq("BOUNDARY_PERM_CT")
phi_rows = numbered("PHI_ROW")
ker_rows = numbered("KER_ROW") if kernel_rank_claim else []
pair_rows = numbered("PAIR_ROW")
picu_rows = numbered("PICU_GEN")
picu_invariants_text = scalar("PICU_INVARIANTS")

assert boundary_count == 72
assert len(boundary_indices) == 72 and len(set(boundary_indices)) == 72
assert len(phi_rows) == 72
assert all(len(r) == pic_rank_claim for r in phi_rows)
assert len(pair_rows) == 72 and all(len(r) == 72 for r in pair_rows)
assert len(picu_rows) == pic_rank_claim
assert sorted(perm_cc) == list(range(1, 73))
assert sorted(perm_ct) == list(range(1, 73))

M = sp.Matrix(phi_rows)
rank = M.rank()
if rank != image_rank_claim:
    raise SystemExit(f"image rank mismatch: Magma {image_rank_claim}, SymPy {rank}")
if kernel_rank_claim != 72 - rank:
    raise SystemExit("kernel rank does not satisfy rank-nullity")

if ker_rows:
    K = sp.Matrix(ker_rows)
    if K.shape != (kernel_rank_claim, 72):
        raise SystemExit(f"kernel shape mismatch: {K.shape}")
    if K.rank() != kernel_rank_claim:
        raise SystemExit("Magma kernel basis is not independent over Q")
    if K * M != sp.zeros(kernel_rank_claim, pic_rank_claim):
        raise SystemExit("Magma kernel basis does not annihilate boundary map")

P = sp.Matrix(pair_rows)
if P != P.T:
    raise SystemExit("boundary intersection matrix is not symmetric")

# Smith diagonal gives a backend-independent integral saturation/index certificate
# for the row lattice im(Div_D -> Pic ~= Z^64).
D = smith_normal_form(M, domain=ZZ)
diag = [abs(int(D[i, i])) for i in range(min(D.rows, D.cols)) if D[i, i] != 0]
if len(diag) != rank:
    raise SystemExit("Smith rank mismatch")
for a, b in zip(diag, diag[1:]):
    if b % a:
        raise SystemExit("Smith divisibility chain failed")
saturation_index = math.prod(diag) if diag else 1
torsion_invariants = [d for d in diag if d != 1]
free_rank = pic_rank_claim - rank

certificate = {
    "schema": "STAGE33_02_BR0A_EXACT_MATRIX_CERTIFICATE_V1",
    "boundary_component_count": boundary_count,
    "pic_rank": pic_rank_claim,
    "boundary_image_rank": rank,
    "unit_divisor_relation_rank": kernel_rank_claim,
    "cokernel_free_rank": free_rank,
    "smith_nonzero_diagonal": diag,
    "saturation_index": saturation_index,
    "boundary_image_saturated": saturation_index == 1,
    "cokernel_torsion_invariants": torsion_invariants,
    "magma_picu_invariants_raw": picu_invariants_text,
    "galois_boundary_permutations_are_bijections": True,
    "galois_boundary_stability_asserted_by_magma": True,
    "kernel_matrix_exactly_verified": True,
    "boundary_pairing_symmetric": True,
    "phi_matrix_sha256": hashlib.sha256(json.dumps(phi_rows, separators=(",", ":")).encode()).hexdigest(),
    "kernel_matrix_sha256": hashlib.sha256(json.dumps(ker_rows, separators=(",", ":")).encode()).hexdigest(),
    "boundary_pairing_sha256": hashlib.sha256(json.dumps(pair_rows, separators=(",", ":")).encode()).hexdigest(),
    "picu_generator_image_sha256": hashlib.sha256(json.dumps(picu_rows, separators=(",", ":")).encode()).hexdigest(),
    "magma_stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
}
(ROOT / "br0a-matrix-certificate.json").write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(certificate, indent=2, sort_keys=True))
