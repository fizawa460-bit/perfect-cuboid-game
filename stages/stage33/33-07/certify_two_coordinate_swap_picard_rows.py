#!/usr/bin/env python3
"""Recover the two Q-defined coordinate-swap Picard actions over Z, locally.

This certifier uses only two non-expiring retained packets already locked in
Stage33-07:

* the Stage32 H-perp pairing marking plus the nine source-locked geometric
  permutations; and
* the independently retained Picard Gram matrix.

The upstream primitive ``indlist`` classes are a Z-basis of Pic. Their
64 pairing vectors (H-pairing plus 63 H-perp pairings) therefore give an
invertible change-of-marking matrix. Inverting that matrix over Q recovers
all 140 known classes in the actual primitive Picard basis. The first two
geometric permutations are involutions, so their pullback/action direction
coincides with the same permutation on these classes. The resulting 64x64
matrices are checked on all 140 classes, against the retained Gram matrix,
and against the hyperplane class. No remote CAS and no Smith form are used.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from picard_base_rows_retained import load as load_base
from stage32_picard_marking_retained import load as load_marking

HERE = Path(__file__).resolve().parent
OUT = HERE / "picard-two-coordinate-swap-actions.json"

MAGIC = "S32_D16_AUT_CANON_HPERP_V1"
CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
RANK = 64
HPERP_RANK = 63
KNOWN_COUNT = 140
CURVE_COUNT = 92
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,
    93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,
    117,118,119,120,121,125,126,127,129,133,135,
]
MODES = [
    ("swap12", "swap_a1_a2_b1_b2", 1),
    ("swap13", "swap_a1_a3_b1_b3", 2),
]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse_hperp(text: str) -> dict:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if len(lines) != 5 + HPERP_RANK + KNOWN_COUNT:
        raise SystemExit(f"retained Hperp line-count regression: {len(lines)}")
    if lines[0] != MAGIC or lines[1] != CORE_SHA or lines[2] != SOURCE_BLOB:
        raise SystemExit("retained Hperp source/core lock moved")
    prepared_sha = lines[3]
    r, m = map(int, lines[4].split())
    if (r, m) != (HPERP_RANK, KNOWN_COUNT):
        raise SystemExit("retained Hperp shape regression")
    q = [list(map(int, lines[5 + i].split())) for i in range(HPERP_RANK)]
    if any(len(row) != HPERP_RANK for row in q):
        raise SystemExit("retained Hperp Gram width regression")
    p0, caps, lin = [], [], []
    off = 5 + HPERP_RANK
    for i in range(KNOWN_COUNT):
        row = list(map(int, lines[off + i].split()))
        if len(row) != 2 + HPERP_RANK:
            raise SystemExit(f"retained Hperp class-row width regression at {i+1}")
        p0.append(row[0])
        caps.append(row[1])
        lin.append(row[2:])
    payload = {
        "core_sha": CORE_SHA,
        "source_blob": SOURCE_BLOB,
        "q": q,
        "p0": p0,
        "caps": caps,
        "lin": lin,
    }
    if csha(payload) != prepared_sha:
        raise SystemExit("retained Hperp prepared-input hash regression")
    return {
        "prepared_sha": prepared_sha,
        "q": q,
        "p0": p0,
        "caps": caps,
        "lin": lin,
        "pairing_rows": [[p0[i]] + lin[i] for i in range(KNOWN_COUNT)],
    }


def invert_matrix(a: list[list[int]]) -> list[list[Fraction]]:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise SystemExit("attempted to invert a non-square matrix")
    m = [
        [Fraction(x) for x in a[i]]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if m[r][col]), None)
        if pivot is None:
            raise SystemExit("primitive indlist pairing marking is singular")
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r == col:
                continue
            q = m[r][col]
            if q:
                m[r] = [m[r][j] - q * m[col][j] for j in range(2 * n)]
    return [row[n:] for row in m]


def row_times_fraction_matrix(
    row: list[int], matrix: list[list[Fraction]]
) -> list[Fraction]:
    return [
        sum(Fraction(row[k]) * matrix[k][j] for k in range(len(row)))
        for j in range(len(matrix[0]))
    ]


def integral_row(row: list[Fraction], label: str) -> list[int]:
    if any(x.denominator != 1 for x in row):
        bad = next(x for x in row if x.denominator != 1)
        raise SystemExit(f"non-integral recovered Picard coordinate in {label}: {bad}")
    return [int(x) for x in row]


def row_times_matrix(row: list[int], matrix: list[list[int]]) -> list[int]:
    return [
        sum(row[k] * matrix[k][j] for k in range(len(row)))
        for j in range(len(matrix[0]))
    ]


def mm(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def det_bareiss(a: list[list[int]]) -> int:
    a = [row[:] for row in a]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def pairing(u: list[int], v: list[int], gram: list[list[int]]) -> int:
    gv = [sum(gram[i][j] * v[j] for j in range(RANK)) for i in range(RANK)]
    return sum(u[i] * gv[i] for i in range(RANK))


marking = load_marking()
base = load_base()
if marking["stage32_picard_core_sha256"] != CORE_SHA:
    raise SystemExit("retained Stage32 core SHA moved")
if base["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("retained Picard-base upstream source moved")

parsed = parse_hperp(marking["hperp_text"])
aut = marking["aut_action"]
if aut.get("schema") != "STAGE32_AUT_PERM_SOURCELOCK_V1":
    raise SystemExit("retained Aut permutation schema regression")
perms = aut.get("permutations_1based")
if not isinstance(perms, list) or len(perms) != 9:
    raise SystemExit("retained Aut permutation count regression")
if any(len(p) != KNOWN_COUNT or sorted(p) != list(range(1, KNOWN_COUNT + 1)) for p in perms):
    raise SystemExit("retained Aut permutation shape regression")

pairing_rows = parsed["pairing_rows"]
basis_pairing = [pairing_rows[j - 1] for j in INDLIST]
basis_pairing_inv = invert_matrix(basis_pairing)
known = [
    integral_row(
        row_times_fraction_matrix(row, basis_pairing_inv),
        f"known class {i+1}",
    )
    for i, row in enumerate(pairing_rows)
]

for k, j in enumerate(INDLIST):
    expected = [0] * RANK
    expected[k] = 1
    if known[j - 1] != expected:
        raise SystemExit(f"indlist class {j} failed primitive-basis reconstruction")

hyperplane = integral_row(
    row_times_fraction_matrix([16] + [0] * HPERP_RANK, basis_pairing_inv),
    "hyperplane",
)
gram = [[int(v) for v in row] for row in base["picard_gram_64x64"]]
if len(gram) != RANK or any(len(row) != RANK for row in gram):
    raise SystemExit("retained Picard Gram shape regression")
if pairing(hyperplane, hyperplane, gram) != 16:
    raise SystemExit("recovered hyperplane square regression")
for i in range(KNOWN_COUNT):
    if pairing(known[i], hyperplane, gram) != parsed["p0"][i]:
        raise SystemExit(f"recovered degree/H-pairing mismatch at class {i+1}")

I = [[1 if i == j else 0 for j in range(RANK)] for i in range(RANK)]
actions = []
boundaries = []
individual = []

for mode, label, idx in MODES:
    perm = [int(x) for x in perms[idx - 1]]
    if any(perm[perm[i] - 1] != i + 1 for i in range(KNOWN_COUNT)):
        raise SystemExit(f"{mode} geometric permutation is not involutive")

    action = [known[perm[j - 1] - 1] for j in INDLIST]
    if len(action) != RANK or any(len(row) != RANK for row in action):
        raise SystemExit(f"{mode} action shape regression")

    for j in range(KNOWN_COUNT):
        got = row_times_matrix(known[j], action)
        want = known[perm[j] - 1]
        if got != want:
            raise SystemExit(f"{mode} failed all-class transport at class {j+1}")

    if mm(action, action) != I:
        raise SystemExit(f"{mode} Picard action is not involutive")
    if mm(mm(action, gram), transpose(action)) != gram:
        raise SystemExit(f"{mode} Picard action does not preserve the retained Gram")
    if row_times_matrix(hyperplane, action) != hyperplane:
        raise SystemExit(f"{mode} does not fix the hyperplane")
    determinant = det_bareiss(action)
    if abs(determinant) != 1:
        raise SystemExit(f"{mode} Picard action is not unimodular")

    sidep = perm[:24]
    pointp = [x - CURVE_COUNT for x in perm[CURVE_COUNT:]]
    if sorted(sidep) != list(range(1, 25)):
        raise SystemExit(f"{mode} side-boundary permutation regression")
    if sorted(pointp) != list(range(1, 49)):
        raise SystemExit(f"{mode} exceptional-boundary permutation regression")

    one = {
        "schema": "STAGE33_07_PICARD_COORDINATE_SWAP_ROWS_V2",
        "action": mode,
        "coordinate_swap": label,
        "upstream_automorphism_index_1based": idx,
        "upstream_git_blob_sha1": SOURCE_BLOB,
        "picard_action_64x64": action,
        "boundary_side_permutation_1based": sidep,
        "boundary_exceptional_permutation_1based": pointp,
        "exact_recovery": {
            "primitive_indlist_basis_recovered_from_retained_hperp_pairings": True,
            "all_140_known_classes_integral": True,
            "all_140_known_classes_transport_exactly": True,
            "picard_gram_preserved": True,
            "hyperplane_fixed": True,
            "determinant": determinant,
            "smith_form_used": False,
            "remote_cas_used": False,
        },
        "source_locks": {
            "retained_stage32_marking_bundle_sha256": marking["canonical_sha256"],
            "stage32_picard_core_sha256": marking["stage32_picard_core_sha256"],
            "stage32_aut_action_sha256": marking["stage32_aut_action_sha256"],
            "prepared_hperp_input_sha256": parsed["prepared_sha"],
            "retained_picard_base_bundle_sha256": base["canonical_sha256"],
        },
        "stage33_progress": "6/11",
        "stage33_08_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
    }
    one["canonical_sha256"] = csha(one)
    (HERE / f"picard-action-{mode}.json").write_text(
        json.dumps(one, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    actions.append(action)
    boundaries.append(
        {
            "action": mode,
            "side_permutation_1based": sidep,
            "exceptional_permutation_1based": pointp,
        }
    )
    individual.append(
        {"action": mode, "canonical_sha256": one["canonical_sha256"], "determinant": determinant}
    )

cert = {
    "schema": "STAGE33_07_TWO_COORDINATE_SWAP_PICARD_ROWS_V2",
    "source_locks": {
        "testa_stoll_cuboids_magma_blob_sha1": SOURCE_BLOB,
        "retained_stage32_marking_bundle_sha256": marking["canonical_sha256"],
        "stage32_picard_core_sha256": marking["stage32_picard_core_sha256"],
        "stage32_aut_action_sha256": marking["stage32_aut_action_sha256"],
        "prepared_hperp_input_sha256": parsed["prepared_sha"],
        "retained_picard_base_bundle_sha256": base["canonical_sha256"],
    },
    "basis_recovery": {
        "basis_kind": "upstream primitive indlist known-class basis",
        "basis_known_indices_1based": INDLIST,
        "pairing_coordinate_rank": RANK,
        "all_140_known_classes_integral": True,
        "hyperplane_integral_and_square_16": True,
        "all_140_hyperplane_pairings_rechecked": True,
    },
    "coordinate_swaps": [x[1] for x in MODES],
    "picard_actions_64x64": actions,
    "boundary_permutations": boundaries,
    "individual_certificates": individual,
    "exact_checks": {
        "both_geometric_permutations_involutions": True,
        "both_actions_involutions": True,
        "both_actions_unimodular": True,
        "both_actions_preserve_retained_picard_gram": True,
        "both_actions_fix_hyperplane": True,
        "both_actions_transport_all_140_known_classes": True,
        "smith_form_used": False,
        "remote_cas_used": False,
    },
    "execution": {
        "method": "stdlib exact rational marking inversion plus integer verification",
        "remote_cas_used": False,
    },
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    json.dumps(
        {
            "success": True,
            "swap_count": 2,
            "all_140_classes_recovered_integrally": True,
            "all_140_classes_transport_exactly": True,
            "remote_cas_used": False,
            "smith_form_used": False,
            "individual": individual,
            "certificate_sha256": cert["canonical_sha256"],
        },
        indent=2,
        sort_keys=True,
    )
)
