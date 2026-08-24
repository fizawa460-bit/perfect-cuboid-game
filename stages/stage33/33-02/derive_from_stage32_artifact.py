#!/usr/bin/env python3
import hashlib
import io
import json
import math
import os
import pathlib
import urllib.request
import zipfile

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

ROOT = pathlib.Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
ARTIFACT_ID = 9486641560
ARTIFACT_URL = f"https://api.github.com/repos/{REPO}/actions/artifacts/{ARTIFACT_ID}/zip"
ARTIFACT_SHA256 = "cae5c9b5aa00d9a730510c9f0e01ab609acef9d759fcc93f64708da123d6813d"
PICARD_CORE_CANONICAL_SHA256 = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
UPSTREAM_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def download_artifact() -> bytes:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required to download the locked prior-run artifact")
    req = urllib.request.Request(
        ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read()
    got = hashlib.sha256(raw).hexdigest()
    if got != ARTIFACT_SHA256:
        raise SystemExit(f"artifact digest mismatch: expected {ARTIFACT_SHA256}, got {got}")
    return raw


def canonical_core_hash(core: dict) -> str:
    c = dict(core)
    embedded = c.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(c, separators=(",", ":"), sort_keys=True).encode("utf-8")
    got = hashlib.sha256(raw).hexdigest()
    if embedded != got or got != PICARD_CORE_CANONICAL_SHA256:
        raise SystemExit(f"Picard core canonical hash mismatch: embedded={embedded}, got={got}")
    return got


def rows(M: sp.Matrix) -> list[list[int]]:
    out = []
    for i in range(M.rows):
        row = []
        for j in range(M.cols):
            x = M[i, j]
            if not x.is_Integer:
                raise SystemExit("nonintegral matrix entry in exact certificate")
            row.append(int(x))
        out.append(row)
    return out


raw_zip = download_artifact()
with zipfile.ZipFile(io.BytesIO(raw_zip)) as zf:
    names = set(zf.namelist())
    if "picard-core.json" not in names:
        raise SystemExit("locked artifact does not contain picard-core.json")
    core = json.loads(zf.read("picard-core.json"))

canonical_hash = canonical_core_hash(core)
source = core.get("source", {})
assert source.get("repo") == "MichaelStollBayreuth/Verification"
assert source.get("commit") == UPSTREAM_COMMIT
assert source.get("file") == "Cuboids/cuboids.magma"
assert source.get("git_blob_sha1") == UPSTREAM_BLOB
assert core.get("schema") == "STAGE32_PICARD_CORE_INDLIST_V1"
assert core.get("rank") == 64
assert core.get("known_curve_count") == 92
assert core.get("node_count") == 48
assert core.get("known_class_count") == 140
assert len(core["known_classes"]) == 140
assert len(core["basis_gram"]) == 64

# Exact cross-stage adapter. Stage29's BR0A probe defines the physical boundary as
# the first 24 C1 curves followed by all 48 exceptional curves. Stage32 preserved
# the literal upstream order Cs[1..92], pts[1..48] in known_classes[1..140].
boundary_indices_1based = list(range(1, 25)) + list(range(93, 141))
assert len(boundary_indices_1based) == 72
known = core["known_classes"]
G = sp.Matrix(core["basis_gram"])
assert G.shape == (64, 64) and G == G.T
M = sp.Matrix([known[j-1] for j in boundary_indices_1based])  # Div_D -> Pic rows
assert M.shape == (72, 64)

# Exact restrictions/intersections against the primitive Picard basis and among
# physical boundary components.
R = M * G
P = M * G * M.T
assert P == P.T
assert [int(P[i, i]) for i in range(24)] == [-4] * 24
assert [int(P[i, i]) for i in range(24, 72)] == [-2] * 48

# Smith decomposition of the boundary image in Pic ~= Z^64.
Dm, Sm, Tm = smith_normal_decomp(M, domain=ZZ)
assert Dm == Sm * M * Tm
rank = M.rank()
diag = [abs(int(Dm[i, i])) for i in range(min(Dm.rows, Dm.cols)) if Dm[i, i] != 0]
assert len(diag) == rank
assert all(b % a == 0 for a, b in zip(diag, diag[1:]))
saturation_index = math.prod(diag) if diag else 1
free_rank = 64 - rank
torsion = [d for d in diag if d != 1]

# Explicit saturated hull. Since Dm = Sm*M*Tm and Tm is unimodular, row(M)*Tm
# has zero last 64-rank columns. Replacing d_i e_i by e_i gives Sat(row(M)).
Tminv = Tm.inv()
if any(not Tminv[i, j].is_Integer for i in range(Tminv.rows) for j in range(Tminv.cols)):
    raise SystemExit("Smith right transform inverse is not integral")
sat_basis = Tminv[:rank, :]
assert sat_basis.rank() == rank
MT = M * Tm
assert MT[:, rank:] == sp.zeros(72, 64-rank)
assert M == MT[:, :rank] * sat_basis

# Integral kernel of Div_D -> Pic. For A=M^T, zero Smith columns of the
# unimodular right transform Tk are a saturated Z-basis of ker(A).
A = M.T
Dk, Sk, Tk = smith_normal_decomp(A, domain=ZZ)
assert Dk == Sk * A * Tk
kernel_rank = 72 - rank
K = Tk[:, rank:].T
assert K.shape == (kernel_rank, 72)
assert K.rank() == kernel_rank
assert K * M == sp.zeros(kernel_rank, 64)

# Independent consistency against the raw exported pairings stored in the same
# audited artifact. These were the direct Magma intersections with the 64 basis
# classes before conversion to coordinates.
raw_cross = core["raw_cross_pairings_with_basis"]
basis_indices = core["basis_known_indices_1based"]
assert len(raw_cross) == 140 and len(basis_indices) == 64
for row_i, upstream_j in enumerate(boundary_indices_1based):
    reconstructed = [int(R[row_i, k]) for k in range(64)]
    if reconstructed != [int(x) for x in raw_cross[upstream_j-1]]:
        raise SystemExit(f"raw cross-pairing mismatch at upstream class {upstream_j}")

certificate = {
    "schema": "STAGE33_02_BR0A_EXACT_ARTIFACT_CERTIFICATE_V1",
    "cross_stage_adapter": {
        "stage32_workflow_run": 32614857845,
        "stage32_artifact_id": ARTIFACT_ID,
        "stage32_artifact_sha256": ARTIFACT_SHA256,
        "stage32_picard_core_canonical_sha256": canonical_hash,
        "boundary_selection_upstream_indices_1based": boundary_indices_1based,
        "boundary_selection_rule": "C1s[1..24] plus all exceptional pts[1..48] = upstream classes 1..24,93..140",
        "same_pinned_upstream_commit": UPSTREAM_COMMIT,
        "same_pinned_upstream_blob": UPSTREAM_BLOB,
    },
    "picard_rank": 64,
    "physical_boundary_component_count": 72,
    "boundary_image_rank": rank,
    "unit_divisor_relation_kernel_rank": kernel_rank,
    "picard_open_quotient_free_rank": free_rank,
    "smith_nonzero_diagonal": diag,
    "boundary_image_saturation_index": saturation_index,
    "boundary_image_is_saturated": saturation_index == 1,
    "boundary_image_saturation_quotient_invariants": torsion,
    "picard_mod_boundary_invariants": {"free_rank": free_rank, "torsion": torsion},
    "boundary_to_pic_matrix": rows(M),
    "unit_divisor_relation_kernel_basis": rows(K),
    "saturated_boundary_image_basis": rows(sat_basis),
    "restriction_to_primitive_picard_basis_matrix": rows(R),
    "boundary_intersection_matrix": rows(P),
    "exact_checks": {
        "stage32_core_source_lock_verified": True,
        "cross_stage_boundary_order_adapter_verified": True,
        "raw_magma_cross_pairings_reproduced": True,
        "smith_decomposition_verified": True,
        "integral_kernel_basis_verified": True,
        "saturated_hull_basis_verified": True,
        "boundary_pairing_symmetric": True,
        "side_self_intersections_minus4": True,
        "exceptional_self_intersections_minus2": True,
    },
}

# Stable hashes for the large matrices.
for key in (
    "boundary_to_pic_matrix",
    "unit_divisor_relation_kernel_basis",
    "saturated_boundary_image_basis",
    "restriction_to_primitive_picard_basis_matrix",
    "boundary_intersection_matrix",
):
    certificate[key + "_sha256"] = hashlib.sha256(
        json.dumps(certificate[key], separators=(",", ":")).encode("utf-8")
    ).hexdigest()

out = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
(ROOT / "br0a-artifact-certificate.json").write_text(out, encoding="utf-8")
summary = {
    "success": True,
    "boundary_image_rank": rank,
    "unit_kernel_rank": kernel_rank,
    "picard_open_free_rank": free_rank,
    "torsion": torsion,
    "saturation_index": saturation_index,
    "certificate_sha256": hashlib.sha256(out.encode()).hexdigest(),
}
(ROOT / "br0a-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps(summary, indent=2, sort_keys=True))
