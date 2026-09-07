#!/usr/bin/env python3
"""V91C1AF source-bound sign_a2 H2 seed fixedness and proper14 reduction.

V91C1AE computes the complete sign_a2 Cech-Cartier divisor difference as zero
in retained Pic/2. The V91C1X Kummer action-difference theorem, source-bound
for sign_a2 in the accompanying V91C1AF note, therefore fixes the literal
A2_02 H2(mu2) seed under sign_a2. Intersect the already source-bound
cc/ct/swap23/sign_b1 fixed subspace from V91C1AC with the exact proper14
sign_a2 action. The marked Brauer image itself remains uncomputed.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
AE = HERE / "diagnose_e3_v91c1ae_sign_a2_picard64_reduction.py"
AC = HERE / "diagnose_e3_v91c1ac_sign_b1_seed_fixed_subspace.py"
Z = HERE / "diagnose_e3_v91c1z_next_stabilizer_reducers.py"
NOTE = HERE / "e3-v91c1af-kummer-sign-a2-source-lock.md"
AE_BLOB = "baa4426ed838d21df58f94eaea34b62ee761e1b8"
AC_BLOB = "5b6adc720f7c470ffd8aae326143e782f0b9b2a5"
Z_BLOB = "1a17331e2b939389075be2571e21c2619ea2d704"
NOTE_BLOB = "dde3a20cc91021cc8d2a504e1d2f9d1c577cffb8"


def gitblob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


assert gitblob(AE.read_bytes()) == AE_BLOB
assert gitblob(AC.read_bytes()) == AC_BLOB
assert gitblob(Z.read_bytes()) == Z_BLOB
assert gitblob(NOTE.read_bytes()) == NOTE_BLOB
note = NOTE.read_text(encoding="utf-8")
assert "Stacks Project Tag 03PL" in note
assert "Stacks Project Tag 0117" in note
assert "sign_a2(seed)=seed" in note

aens = runpy.run_path(str(AE))
ae = aens["result"]
assert ae["success"] is True
assert ae["strict_prime_exact_known92_locator_materialized"] is True
assert ae["strict_prime_known92_index_set"] == list(range(1, 9))
assert ae["sign_a2_pic2_difference_computed"] is True
assert ae["sign_a2_pic2_difference_zero"] is True
assert ae["complete_sign_a2_difference_mod2_support_one_based"] == []
assert ae["sign_a2_literal_h2_seed_fixedness_promoted"] is False

acns = runpy.run_path(str(AC))
ac = acns["result"]
assert ac["success"] is True
assert ac["sign_b1_literal_h2_seed_fixed"] is True
assert ac["marked_brauer_image_must_be_sign_b1_fixed"] is True
assert ac["cc_ct_swap23_sign_b1_fixed_dimension_f2"] == 6
assert ac["actual_marked_brauer_image_computed"] is False
entry_basis = [list(v) for v in ac["fixed_basis_f2"]]
assert len(entry_basis) == 6

zns = runpy.run_path(str(Z))
z = zns["result"]
assert z["success"] is True
assert any(r["word"] == ["sign_a2"] for r in z["greedy_selected_reducers"])
sign_a2 = zns["target_matrix"](["sign_a2"], zns["gens14"])
fixed_basis = zns["intersect_basis_with_fixed_action"](entry_basis, sign_a2)
fixed_dim = len(fixed_basis)
assert fixed_dim == 5
assert z["conditional_final_dimension_f2"] == 5

_, pivots = zns["rref"](fixed_basis, 14)
assert len(pivots) == fixed_dim
coords = [p + 1 for p in pivots]
restriction = [[row[p] for p in pivots] for row in fixed_basis]
assert len(zns["rref"](restriction, fixed_dim)[1]) == fixed_dim

result = {
    "success": True,
    "marker": "V91C1AF_SIGN_A2_LITERAL_SEED_FIXED_SUBSPACE",
    "source_lock_blob_sha1": NOTE_BLOB,
    "sign_a2_complete_pic2_difference_zero": True,
    "sign_a2_literal_h2_seed_fixed": True,
    "marked_brauer_image_must_be_sign_a2_fixed": True,
    "entry_cc_ct_swap23_sign_b1_fixed_dimension_f2": len(entry_basis),
    "cc_ct_swap23_sign_b1_sign_a2_fixed_dimension_f2": fixed_dim,
    "cc_ct_swap23_sign_b1_sign_a2_fixed_cardinality": 1 << fixed_dim,
    "dimension_drop": len(entry_basis) - fixed_dim,
    "fixed_basis_f2": fixed_basis,
    "minimal_coordinate_discriminator_positions_one_based": coords,
    "minimal_coordinate_discriminator_bit_count": fixed_dim,
    "actual_marked_brauer_image_computed": False,
    "source_bound_proper14_evaluation_bits_materialized": 0,
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
    "::warning file=stages/stage33/33-12/diagnose_e3_v91c1af_sign_a2_seed_fixed_subspace.py,"
    "title=V91C1AF_SIGN_A2_FIXED::"
    + json.dumps(result, sort_keys=True, separators=(",", ":"))
)
