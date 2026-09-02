#!/usr/bin/env python3
"""Lightweight exact probe: transport retained BigK row 35 to row 39 by sign(a3)."""
from __future__ import annotations

import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
AVAIL = HERE / "j2-order4-retained-pullback-row-availability-v11.json"
SIX = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
MARKED = S33 / "33-09" / "marked-picard-basis-source.json"
MARKING = S33 / "33-07" / "stage32_picard_marking_retained.py"

AVAIL_SHA = "80331cf22bdb1663bc3834039d2c65e4c006aea8d3c06d3fbf379fe1354cdf72"
SIX_SHA = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
MARKED_SHA = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,
    105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135,
]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


def invert(a):
    n = len(a)
    m = [[Fraction(x) for x in a[i]] + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if m[r][col])
        m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x/p for x in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                f = m[r][col]
                m[r] = [m[r][j] - f*m[col][j] for j in range(2*n)]
    return [row[n:] for row in m]


def rowmul(a, b):
    return [sum(a[k]*b[k][j] for k in range(len(a))) for j in range(len(b[0]))]


def ints(row):
    row = [Fraction(x) for x in row]
    assert all(x.denominator == 1 for x in row)
    return [int(x) for x in row]


avail = locked(AVAIL, AVAIL_SHA)
six = locked(SIX, SIX_SHA)
marked = locked(MARKED, MARKED_SHA)
marking = runpy.run_path(str(MARKING))["load"]()
assert marking["stage32_picard_core_sha256"] == CORE_SHA
assert marking["aut_action"]["schema"] == "STAGE32_AUT_PERM_SOURCELOCK_V1"
perms = marking["aut_action"]["permutations_1based"]
assert len(perms) == 9
sign_a3 = [int(x) for x in perms[5]]  # upstream substs generator 6
assert len(sign_a3) == 140 and sorted(sign_a3) == list(range(1, 141))

# Pinned cuboids.magma: CsK=C1sK(20)+C2sK(6)+C3sK; row35 is C3sK local 9,
# the first member of block 2 with (e1,e2,e3)=(+,+,+).  sign(a3) flips e1 only
# in that block, hence local 9 -> 13, i.e. BigK 35 -> 39.
sgn = [1, -1]
triples = [(e1,e2,e3) for e1 in sgn for e2 in sgn for e3 in sgn]
assert triples[0] == (1,1,1) and triples[4] == (-1,1,1)
source_bigk = 26 + (8 + 1)
target_bigk = 26 + (8 + 5)
assert (source_bigk, target_bigk) == (35, 39)

row35 = next(r for r in six["pullbacks"] if int(r["BigK_index_1based"]) == 35)
assert row35["full_surface_known_preimage_indices_1based"] == [53]
assert row35["full_surface_known_preimage_multiplicities"] == [1]
assert sign_a3[52] == 57
assert sign_a3[56] == 53
row39_preimages = [sign_a3[52]]
assert row39_preimages == [57]
assert 39 in avail["effective_unretained_required_rows_1based"]

lines = [x.strip() for x in marking["hperp_text"].splitlines() if x.strip()]
assert lines[:3] == ["S32_D16_AUT_CANON_HPERP_V1", CORE_SHA, SOURCE_BLOB]
assert tuple(map(int, lines[4].split())) == (63, 140)
off = 5 + 63
pairing_rows = []
for i in range(140):
    raw = list(map(int, lines[off+i].split()))
    assert len(raw) == 65
    pairing_rows.append([raw[0]] + raw[2:])
basis_inv = invert([pairing_rows[j-1] for j in INDLIST])
known = [ints(rowmul(row, basis_inv)) for row in pairing_rows]
for k, j in enumerate(INDLIST):
    e = [0]*64; e[k] = 1
    assert known[j-1] == e

ind = known[56]
B = marked["indlist_to_magma_picard_matrix_64x64"]
assert len(B) == 64 and all(len(row) == 64 for row in B)
mag = ints(rowmul(ind, B))
out = {
    "success": True,
    "source_locks": {
        "availability_sha256": AVAIL_SHA,
        "six_support_sha256": SIX_SHA,
        "marked_basis_sha256": MARKED_SHA,
        "stage32_picard_core_sha256": CORE_SHA,
        "pinned_stoll_git_blob_sha1": SOURCE_BLOB,
    },
    "transport": {
        "automorphism": "sign_a3",
        "stage32_aut_generator_index_1based": 6,
        "BigK_source_row_1based": 35,
        "BigK_target_row_1based": 39,
        "full_surface_known_source_preimage_1based": 53,
        "full_surface_known_target_preimage_1based": 57,
    },
    "row39": {
        "full_surface_known_preimage_indices_1based": [57],
        "full_surface_known_preimage_multiplicities": [1],
        "fullPic64_INDLIST_coordinates": ind,
        "fullPic64_historical_Magma_coordinates": mag,
    },
    "promotion_firewall": {
        "named_j2_order4_source_coordinate_materialized": False,
        "retained10_named_j2_source_coordinate_materialized": False,
        "stage33_12_closed_exact": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
print(json.dumps(out, sort_keys=True))
