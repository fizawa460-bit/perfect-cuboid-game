#!/usr/bin/env python3
"""Network-free replay of the six corrected-J2 Kc support pullbacks."""
from __future__ import annotations

import hashlib
import json
import runpy
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
CERT = HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json"
AUDIT = HERE / "first-exact-kummer-column-support-reduction-audit.json"
CONTROLLER = S33 / "controller.json"
MARKED = S33 / "33-09" / "marked-picard-basis-source.json"
MARKING = S33 / "33-07" / "stage32_picard_marking_retained.py"

EXPECTED = "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"
AUDIT_SHA = "040b2c0ecbd0b2e7ca8aef82952c6c71e84f9eea84aef407fc08b765a63fafe6"
MARKED_SHA = "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"
CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
TARGETS = [26, 35, 42, 47, 49, 52]
INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,
    105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135,
]


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body)
    return obj


def invert(a):
    n = len(a)
    m = [[Fraction(x) for x in a[i]] +
         [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
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


cert = locked(CERT, EXPECTED)
audit = locked(AUDIT, AUDIT_SHA)
controller = json.loads(CONTROLLER.read_text(encoding="utf-8"))
marked = locked(MARKED, MARKED_SHA)
assert cert["schema"] == "STAGE33_12_J2_CT_SIX_KC_SUPPORT_FULLPIC64_PULLBACKS_V1"
assert cert["target_BigK_support_1based"] == TARGETS
assert cert["source_locks"]["stoll_git_blob_sha1"] == SOURCE_BLOB
assert cert["source_locks"]["stage32_picard_core_sha256"] == CORE_SHA
assert cert["source_locks"]["stage33_09_marked_basis_sha256"] == MARKED_SHA

marking = runpy.run_path(str(MARKING))["load"]()
assert marking["stage32_picard_core_sha256"] == CORE_SHA
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
    e = [0]*64
    e[k] = 1
    assert known[j-1] == e

B = marked["indlist_to_magma_picard_matrix_64x64"]
assert len(B) == 64 and all(len(row) == 64 for row in B)
sum_ind = [0]*64
sum_mag = [0]*64
assert [r["BigK_index_1based"] for r in cert["pullbacks"]] == TARGETS
for rec in cert["pullbacks"]:
    idx = rec["full_surface_known_preimage_indices_1based"]
    mult = rec["full_surface_known_preimage_multiplicities"]
    assert idx and len(idx) == len(mult) and len(set(idx)) == len(idx)
    assert all(1 <= j <= 140 for j in idx) and all(m > 0 for m in mult)
    ind = [sum(m*known[j-1][c] for j, m in zip(idx, mult)) for c in range(64)]
    mag = ints(rowmul(ind, B))
    assert ind == rec["fullPic64_INDLIST_coordinates"]
    assert mag == rec["fullPic64_historical_Magma_coordinates"]
    sum_ind = [a+b for a, b in zip(sum_ind, ind)]
    sum_mag = [a+b for a, b in zip(sum_mag, mag)]

assert [x & 1 for x in sum_ind] == cert["ct_sum_fullPic64_INDLIST_coordinates_mod2"]
assert [x & 1 for x in sum_mag] == cert["ct_sum_fullPic64_historical_Magma_coordinates_mod2"]
assert cert["exact_checks"] == {
    "only_six_required_support_rows_materialized": True,
    "all_preimages_are_full_surface_known_classes_1_to_140": True,
    "all_six_rows_reconstructed_from_retained_140_class_marking": True,
    "all_six_rows_transport_through_stage33_09_marked_basis_exactly": True,
    "historical_full_Kc20_to_fullPic64_matrix_regenerated": False,
}
assert cert["remaining_interfaces"] == [
    "J2_CC_ACTUAL_CECH_PARITY",
    "NAMED_CV_d2_TO_SEMANTIC_DISCRIMINANT_ORIENTATION",
]
assert not any(cert["promotion_firewall"].values())
assert audit["exact_progress"]["ct_six_support_fullPic64_pullbacks_materialized"]
assert audit["exact_progress"]["ct_six_support_fullPic64_pullbacks_canonical_sha256"] == EXPECTED
assert audit["next_exact_leaf"] == controller["current"]["next_exact_leaf"]
assert controller["stage33_12"]["j2_support_reduction_audit_sha256"] == AUDIT_SHA
assert controller["stage33_12"]["corrected_J2_ct_defect_fullPic64_pullbacks_sha256"] == EXPECTED
assert controller["stage33_12"]["finite_v4_kummer_columns_materialized"] == 0
assert controller["stage33_12"]["first_exact_kummer_column_materialized"] is False
print(json.dumps({
    "success": True,
    "certificate_sha256": EXPECTED,
    "six_support_pullbacks_replayed": True,
    "ct_sum_weight_indlist_mod2": sum(cert["ct_sum_fullPic64_INDLIST_coordinates_mod2"]),
}, sort_keys=True))
