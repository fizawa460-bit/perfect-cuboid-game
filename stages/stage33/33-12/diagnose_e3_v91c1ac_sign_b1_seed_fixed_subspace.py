#!/usr/bin/env python3
"""V91C1AC source-bound sign_b1 seed fixedness and proper14 reduction.

The literal A2_02 Cech-Cartier acted-minus-original divisor under sign_b1 is
zero on both actual strict primes and all exceptional primes by V91C1AB.  The
V91C1X Kummer functoriality theorem therefore gives literal H2(mu2) seed
fixedness.  Intersect the already source-bound V91C1Y cc/ct/swap23 fixed
subspace with the exact proper14 sign_b1 fixed space.  The marked Brauer image
itself remains uncomputed.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AB = HERE / "diagnose_e3_v91c1ab_sign_prime_attached_cech_difference.py"
Z = HERE / "diagnose_e3_v91c1z_next_stabilizer_reducers.py"
NOTE = HERE / "e3-v91c1ac-kummer-sign-b1-source-lock.md"
X = HERE / "e3-v91c1x-a2-02-kummer-naturality-mask20-exclusion.json"

AB_BLOB = "d787830a712c6a0639fe35d6d57ba6c8cba39e90"
Z_BLOB = "1a17331e2b939389075be2571e21c2619ea2d704"
NOTE_BLOB = "382c156ab1d5ca26e0b9313ebe2ff5509666bef0"
X_SHA = "aca4d8929f9cc04b24da6e8a7ba0ec0b89be18ac1bc2bf3e6e1f870808bdf29f"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), path
    return obj


assert gitblob(AB.read_bytes()) == AB_BLOB
assert gitblob(Z.read_bytes()) == Z_BLOB
assert gitblob(NOTE.read_bytes()) == NOTE_BLOB
x = load(X, X_SHA)
assert x["exact_consequence"]["a2_02_swap23_seed_fixed_mod_pic2"] is True
assert x["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False

abns = runpy.run_path(str(AB))
ab = abns["result"]
assert ab["success"] is True
b1 = ab["actions"]["sign_b1"]
assert b1["actual_prime_involution_verified"] is True
assert b1["components_with_zero_full_attached_divisor_difference"] == 8
assert b1["strict_package_difference_nonzero_coefficients"] == 0
assert b1["exceptional_package_difference_nonzero_coefficients"] == 0
assert b1["full_codim1_package_difference_zero"] is True
assert b1["needed_strict_prime_class_count"] == 0

zns = runpy.run_path(str(Z))
z = zns["result"]
assert z["success"] is True
assert any(r["word"] == ["sign_b1"] for r in z["greedy_selected_reducers"])
y = zns["y"]
entry_basis = [list(v) for v in y["fixed_basis_f2"]]
assert len(entry_basis) == 7
sign_b1 = zns["target_matrix"](["sign_b1"], zns["gens14"])
fixed_basis = zns["intersect_basis_with_fixed_action"](entry_basis, sign_b1)
fixed_dim = len(fixed_basis)
assert fixed_dim < len(entry_basis)

# Minimal coordinate projection on the resulting fixed subspace.
_, pivots = zns["rref"](fixed_basis, 14)
assert len(pivots) == fixed_dim
coords = [p + 1 for p in pivots]
restriction = [[row[p] for p in pivots] for row in fixed_basis]
assert len(zns["rref"](restriction, fixed_dim)[1]) == fixed_dim

result = {
    "success": True,
    "marker": "V91C1AC_SIGN_B1_LITERAL_SEED_FIXED_SUBSPACE",
    "source_lock_blob_sha1": NOTE_BLOB,
    "sign_b1_full_codim1_difference_literal_zero": True,
    "sign_b1_pic2_difference_zero": True,
    "sign_b1_literal_h2_seed_fixed": True,
    "marked_brauer_image_must_be_sign_b1_fixed": True,
    "entry_cc_ct_swap23_fixed_dimension_f2": len(entry_basis),
    "cc_ct_swap23_sign_b1_fixed_dimension_f2": fixed_dim,
    "cc_ct_swap23_sign_b1_fixed_cardinality": 1 << fixed_dim,
    "dimension_drop": len(entry_basis) - fixed_dim,
    "fixed_basis_f2": fixed_basis,
    "minimal_coordinate_discriminator_positions_one_based": coords,
    "minimal_coordinate_discriminator_bit_count": fixed_dim,
    "sign_a2_literal_h2_seed_fixed": False,
    "actual_marked_brauer_image_computed": False,
    "e3_genuine_full_surface_h2_mu2_lift_materialized": False,
    "e3_kummer_column_materialized": False,
    "stage33_progress": "6/11",
    "theorem_credit": False,
    "receiver_credit": False,
    "endpoint_credit": False,
    "merge_allowed": False,
}
print(json.dumps(result, sort_keys=True))
print(
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1ac_sign_b1_seed_fixed_subspace.py,"
    "title=V91C1AC_SIGN_B1_FIXED::"
    + json.dumps(result, sort_keys=True, separators=(",", ":"))
)
