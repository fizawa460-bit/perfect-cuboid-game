#!/usr/bin/env python3
"""Materialize the named J2 order-4 source coordinate without network/CAS.

The six doubled rows come from the locked semantic-u1 certificate, row 35
from the locked ct pullbacks, row 39 from its retained symmetry transport,
and rows 20/67 from the v17 exact source lock.  Every support row is replayed
through the retained 140-class marking and the certified INDLIST-to-Magma
Picard bridge before the mixed Smith and proper-Br2 calculations are made.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import runpy
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
S07 = S33 / "33-07"
S09 = S33 / "33-09"
OUT = HERE / "j2-order4-source-coordinate-v18.json"

LOCKS = {
    "u1": (HERE / "j2-semantic-u1-full-surface-smith-source.json", "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec"),
    "reduction": (HERE / "j2-order4-brauer-lift-reduction.json", "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0"),
    "ct": (HERE / "j2-ct-six-kc-support-fullpic64-pullbacks.json", "592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d"),
    "row39": (HERE / "j2-order4-row39-retained-symmetry-transport-v11.json", "a83d558fc96822d9b8a01512e7d1afa3cf9db0958718325a27fddb32ba753604"),
    "rows20_67": (HERE / "j2-order4-row20-row67-exact-source-lock-v17.json", "04b47064db73e02068aa51301c94ab0576d927c0b71b2d3df093012028f061d2"),
    "marked": (S09 / "marked-picard-basis-source.json", "0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f"),
    "proper": (S07 / "proper-brauer2-from-discriminant.json", "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"),
    "target": (HERE / "full-surface-pic2-kummer-target.json", "384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"),
}
STAGE32_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
STOLL_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
TERMS = [(2, 1), (4, 3), (9, 3), (10, 1), (20, 2), (35, 2), (39, 2), (47, 3), (49, 3), (67, 2)]
INDLIST = [
    1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20,
    21, 22, 23, 25, 26, 27, 29, 33, 34, 35, 37, 38, 41, 45, 49, 53, 69,
    93, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 109,
    110, 111, 113, 117, 118, 119, 120, 121, 125, 126, 127, 129, 133, 135,
]


def csha(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


def invert(a):
    n = len(a)
    m = [[Fraction(x) for x in a[i]] + [Fraction(i == j) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if m[r][col])
        m[col], m[pivot] = m[pivot], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                f = m[r][col]
                m[r] = [m[r][j] - f * m[col][j] for j in range(2 * n)]
    return [row[n:] for row in m]


def rowmul(a, b):
    return [sum(a[k] * b[k][j] for k in range(len(a))) for j in range(len(b[0]))]


def ints(row):
    row = [Fraction(x) for x in row]
    assert all(x.denominator == 1 for x in row)
    return [int(x) for x in row]


def rowmul_f2(a, b):
    return [sum((a[k] & 1) * (int(b[k][j]) & 1) for k in range(len(a))) & 1 for j in range(len(b[0]))]


def retained_known_classes():
    marking = runpy.run_path(str(S07 / "stage32_picard_marking_retained.py"))["load"]()
    assert marking["stage32_picard_core_sha256"] == STAGE32_CORE_SHA
    lines = [x.strip() for x in marking["hperp_text"].splitlines() if x.strip()]
    assert lines[:3] == ["S32_D16_AUT_CANON_HPERP_V1", STAGE32_CORE_SHA, STOLL_BLOB]
    assert tuple(map(int, lines[4].split())) == (63, 140)
    pair = []
    for i in range(140):
        raw = list(map(int, lines[68 + i].split()))
        assert len(raw) == 65
        pair.append([raw[0]] + raw[2:])
    basis_inv = invert([pair[j - 1] for j in INDLIST])
    known = [ints(rowmul(row, basis_inv)) for row in pair]
    for k, j in enumerate(INDLIST):
        e = [0] * 64
        e[k] = 1
        assert known[j - 1] == e
    return known


data = {name: locked(path, digest) for name, (path, digest) in LOCKS.items()}
assert data["reduction"]["semantic_order4_generator"]["BigK_terms_row_and_coefficient_mod4"] == [list(x) for x in TERMS]
assert data["rows20_67"]["rows"] == {
    "20": [[32, 2], [117, 1], [122, 1], [125, 1], [130, 1], [133, 1], [138, 1]],
    "67": [[110, 1], [115, 1]],
}

known = retained_known_classes()
B = data["marked"]["indlist_to_magma_picard_matrix_64x64"]
rows = {int(r["BigK_index_1based"]): dict(r) for r in data["u1"]["semantic_u1_pullback"]["pullbacks"]}
rows[35] = dict(next(r for r in data["ct"]["pullbacks"] if int(r["BigK_index_1based"]) == 35))
rows[39] = dict(data["row39"]["row39"])
rows[39]["full_surface_known_preimage_indices_1based"] = [57]
rows[39]["full_surface_known_preimage_multiplicities"] = [1]

for j in (20, 67):
    support = data["rows20_67"]["rows"][str(j)]
    idx = [x[0] for x in support]
    mult = [x[1] for x in support]
    ind = [sum(m * known[k - 1][c] for k, m in zip(idx, mult)) for c in range(64)]
    rows[j] = {
        "BigK_index_1based": j,
        "full_surface_known_preimage_indices_1based": idx,
        "full_surface_known_preimage_multiplicities": mult,
        "fullPic64_INDLIST_coordinates": ind,
        "fullPic64_historical_Magma_coordinates": ints(rowmul(ind, B)),
    }

# Replay every support through the same retained 140-class marking and basis bridge.
for j, _ in TERMS:
    rec = rows[j]
    ind = [
        sum(m * known[k - 1][c] for k, m in zip(
            rec["full_surface_known_preimage_indices_1based"],
            rec["full_surface_known_preimage_multiplicities"],
        ))
        for c in range(64)
    ]
    assert ind == rec["fullPic64_INDLIST_coordinates"], j
    assert ints(rowmul(ind, B)) == rec["fullPic64_historical_Magma_coordinates"], j

weighted_ind = [0] * 64
weighted_mag = [0] * 64
for j, coefficient in TERMS:
    weighted_ind = [a + coefficient * b for a, b in zip(weighted_ind, rows[j]["fullPic64_INDLIST_coordinates"])]
    weighted_mag = [a + coefficient * b for a, b in zip(weighted_mag, rows[j]["fullPic64_historical_Magma_coordinates"])]
assert ints(rowmul(weighted_ind, B)) == weighted_mag

base = runpy.run_path(str(S07 / "picard_base_rows_retained.py"))["load"]()
assert base["canonical_sha256"] == "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
prod4 = ints(rowmul(weighted_mag, base["picard_gram_64x64"]))
if not all(x % 4 == 0 for x in prod4):
    residues = [x % 4 for x in prod4]
    out = {
        "schema": "STAGE33_12_J2_ORDER4_SOURCE_COORDINATE_BLOCKER_V18",
        "stage": "33-12",
        "status": "PASS_EXACT_ALL_REQUIRED_ROWS_MATERIALIZED_BLOCKED_AT_ORDER4_DUAL_INTEGRALITY",
        "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
        "retained_marking": {
            "stage32_picard_core_sha256": STAGE32_CORE_SHA,
            "pinned_stoll_git_blob_sha1": STOLL_BLOB,
            "INDLIST_1based": INDLIST,
            "known_class_count": 140,
            "marked_picard_rank": 64,
            "basis_orientation": "row coordinates; INDLIST64 multiplied on the right by the certified bridge gives historical Magma Pic64",
        },
        "rows20_67_reconstruction": {str(j): rows[j] for j in (20, 67)},
        "required_rows": {str(j): rows[j] for j, _ in TERMS},
        "semantic_order4_numerator": {
            "terms_row_and_coefficient_mod4": [list(x) for x in TERMS],
            "weighted_fullPic64_INDLIST_numerator": weighted_ind,
            "weighted_fullPic64_historical_Magma_numerator": weighted_mag,
            "n4_times_picard_gram": prod4,
            "n4_times_picard_gram_residues_mod4": residues,
            "nondivisible_positions_1based": [i + 1 for i, x in enumerate(residues) if x],
            "divisible_by_2": all(x % 2 == 0 for x in prod4),
            "divisible_by_4": False,
            "integral_dual_quotient_representative_z4": None,
        },
        "exact_blocker": {
            "last_failed_interface": "SEMANTIC_KC_ORDER4_NUMERATOR_TO_FULL_SURFACE_DUAL_LATTICE_NORMALIZATION",
            "known": "All ten required BigK pullback rows are exact and replay through the retained 140-class marking and certified marked64 bridge.",
            "failure": "The resulting n4 pairs only evenly, not four-divisibly, with the retained Picard lattice; therefore n4/4 is not a genuine full-surface dual-lattice representative under the currently locked raw pullback normalization.",
            "minimal_missing_object": "A source-locked correction/normalization for the semantic Kc t1/4 generator under pullback to the full-surface dual Picard lattice, or an exact proof that the candidate n4 formula must be replaced, sufficient to make the order-4 pairing numerator divisible by 4.",
            "same_row_search_cannot_advance": "Rows 20 and 67 and the other eight inputs are now exact; repeating their extraction or the forbidden qPic/Smith/S3 searches cannot change this divisibility obstruction under the locked basis and formula.",
        },
        "named_j2_source_coordinate": {
            "materialized": False,
            "proper_Br2_14D_coordinate_f2": None,
            "retained_10D_coordinate_f2": None,
            "historical_mask6_assumed": False,
            "target_compatibility_used": False,
            "s3_fixedness_used_to_select_label": False,
        },
        "promotion_firewall": {
            "mathematical_state_promotion_performed": False,
            "named_j2_source_coordinate_materialized": False,
            "first_75D_matrix_column_materialized": False,
            "finite_v4_kummer_columns_materialized": 0,
            "stage33_progress": "6/11",
            "stage33_12_closed_exact": False,
            "stage33_13_released": False,
            "Q_defined_descent_credit_restored": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
        },
    }
    out["canonical_sha256"] = csha(out)
    if "--check" in sys.argv:
        assert locked(OUT, out["canonical_sha256"]) == out
    else:
        OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "status": out["status"],
        "nondivisible_positions_1based": out["semantic_order4_numerator"]["nondivisible_positions_1based"],
        "canonical_sha256": out["canonical_sha256"],
        "marker": "PROOF_REPLAY_COMPLETE",
    }, sort_keys=True))
    raise SystemExit(0)
z4 = [x // 4 for x in prod4]
mods = data["u1"]["retained_common_smith_source"]["discriminant_moduli"]
C = data["u1"]["retained_common_smith_source"]["v_nontrivial_columns_mod8_64x14"]
y4 = [sum(z4[k] * C[k][j] for k in range(64)) % mods[j] for j in range(14)]
doubled = [(2 * y4[j]) % mods[j] for j in range(14)]
assert doubled == data["u1"]["exact_normalization"]["nontrivial_smith_coordinates_mixed_moduli"]

b8 = data["u1"]["retained_common_smith_source"]["discriminant_bilinear_numerator_over_8_reduced"]
scales = [m // 2 for m in mods]
pairing = [sum(y4[i] * scales[j] * int(b8[i][j]) for i in range(14)) for j in range(14)]
assert all(x % 4 == 0 for x in pairing)
proper14 = [(x // 4) & 1 for x in pairing]
proper = data["proper"]
assert rowmul_f2(proper14, proper["proper_Br2_cc_action_f2"]) == proper14
assert rowmul_f2(proper14, proper["proper_Br2_ct_action_f2"]) == proper14

basis10 = data["target"]["proper_invariant_domain"]["basis_rows_original_proper_br2_coordinates_f2"]
retained10 = None
for bits in itertools.product((0, 1), repeat=10):
    v = [0] * 14
    for bit, row in zip(bits, basis10):
        if bit:
            v = [a ^ (int(b) & 1) for a, b in zip(v, row)]
    if v == proper14:
        assert retained10 is None
        retained10 = list(bits)
assert retained10 is not None

out = {
    "schema": "STAGE33_12_J2_ORDER4_SOURCE_COORDINATE_V18",
    "stage": "33-12",
    "status": "PASS_EXACT_NAMED_J2_ORDER4_SOURCE_COORDINATE_MATERIALIZED",
    "source_locks": {name: digest for name, (_, digest) in LOCKS.items()},
    "retained_marking": {
        "stage32_picard_core_sha256": STAGE32_CORE_SHA,
        "pinned_stoll_git_blob_sha1": STOLL_BLOB,
        "INDLIST_1based": INDLIST,
        "known_class_count": 140,
        "marked_picard_rank": 64,
        "basis_orientation": "row coordinates; INDLIST64 multiplied on the right by the certified bridge gives historical Magma Pic64",
    },
    "rows20_67_reconstruction": {str(j): rows[j] for j in (20, 67)},
    "required_rows": {str(j): rows[j] for j, _ in TERMS},
    "semantic_order4_numerator": {
        "terms_row_and_coefficient_mod4": [list(x) for x in TERMS],
        "weighted_fullPic64_INDLIST_numerator": weighted_ind,
        "weighted_fullPic64_historical_Magma_numerator": weighted_mag,
        "n4_times_picard_gram": prod4,
        "integral_dual_quotient_representative_z4": z4,
        "mixed_smith_order4_coordinate": y4,
        "doubling_matches_locked_semantic_u1": True,
    },
    "named_j2_source_coordinate": {
        "proper_Br2_14D_coordinate_f2": proper14,
        "proper_Br2_cc_fixed": True,
        "proper_Br2_ct_fixed": True,
        "retained_10D_coordinate_f2": retained10,
        "retained_10D_mask_decimal": sum(bit << i for i, bit in enumerate(retained10)),
        "source_side_exact_marking_only": True,
        "historical_mask6_assumed": False,
        "target_compatibility_used": False,
        "s3_fixedness_used_to_select_label": False,
    },
    "promotion_firewall": {
        "named_j2_source_coordinate_materialized": True,
        "first_75D_matrix_column_materialized": False,
        "finite_v4_kummer_columns_materialized": 0,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "Q_defined_descent_credit_restored": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "proper14": proper14,
    "retained10": retained10,
    "retained10_mask_decimal": out["named_j2_source_coordinate"]["retained_10D_mask_decimal"],
    "canonical_sha256": out["canonical_sha256"],
}, sort_keys=True))
