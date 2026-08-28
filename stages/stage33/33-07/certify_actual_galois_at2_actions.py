#!/usr/bin/env python3
"""Recover the actual cc/ct Picard and intrinsic A[2] actions locally.

The retained geometry-only certificate gives complex conjugation and
sqrt(2)-conjugation as exact permutations of the same 140 known divisor
classes used by the Stage32 H-perp marking.  Therefore the integral Picard
matrices are reconstructed in the same INDLIST basis as the actual coordinate
swaps, with no Magma Picard basis and no Smith transport.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE / "certify_actual_coordinate_swap_at2_actions.py"
PERM_PATH = HERE / "galois-known-class-permutations.json"
OUT = HERE / "actual-galois-at2-actions.json"
EXPECTED_PERM = "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
RANK = 64
N = 14


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


base = runpy.run_path(str(BASE_SCRIPT))
pic = base["ns"]
known = base["known"]
gram = base["gram"]
indlist = base["indlist"]
kernel_masks = base["kernel_masks"]
solve_kernel = base["solve_kernel"]
row_action_mask = base["row_action_mask"]
row_from_mask = base["row_from_mask"]
mm2 = base["mm2"]
I14 = base["I14"]
A12 = base["A12"]
A13 = base["A13"]
signs7 = base["signs7"]
qdiag = base["qdiag"]
qcoords = base["qcoords"]

perm_obj = json.loads(PERM_PATH.read_text(encoding="utf-8"))
body = dict(perm_obj); claimed = body.pop("canonical_sha256", None)
if claimed != EXPECTED_PERM or csha(body) != EXPECTED_PERM:
    raise SystemExit("retained Galois known-class permutation lock moved")
if perm_obj["source"]["git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("retained Galois source blob moved")
if perm_obj["schema"] != "STAGE33_07_GALOIS_KNOWN_CLASS_PERMUTATIONS_V1":
    raise SystemExit("retained Galois permutation schema moved")


def reconstruct(label: str, perm: list[int]):
    if len(perm) != 140 or sorted(perm) != list(range(1, 141)):
        raise SystemExit(f"{label}: bad 140-class permutation")
    action = [known[int(perm[j - 1]) - 1] for j in indlist]
    for j in range(140):
        got = pic["row_times_matrix"](known[j], action)
        want = known[int(perm[j]) - 1]
        if got != want:
            raise SystemExit(f"{label}: failed all-class transport at {j+1}")
    if pic["mm"](pic["mm"](action, gram), pic["transpose"](action)) != gram:
        raise SystemExit(f"{label}: integral Picard action is not an isometry")
    I64 = [[int(i == j) for j in range(RANK)] for i in range(RANK)]
    if pic["mm"](action, action) != I64:
        raise SystemExit(f"{label}: integral Picard action is not involutive")
    det = pic["det_bareiss"](action)
    if abs(det) != 1:
        raise SystemExit(f"{label}: integral Picard action is not unimodular")
    hyperplane = pic["hyperplane"]
    if pic["row_times_matrix"](hyperplane, action) != hyperplane:
        raise SystemExit(f"{label}: hyperplane not fixed")
    at2 = []
    for mask in kernel_masks:
        image = row_action_mask(mask, action)
        coords = solve_kernel(image)
        at2.append(row_from_mask(coords, N))
    if mm2(at2, at2) != I14:
        raise SystemExit(f"{label}: intrinsic A[2] action is not involutive")
    for i in range(N):
        if qcoords(at2[i]) != qdiag[i]:
            raise SystemExit(f"{label}: intrinsic A[2] quadratic form not preserved")
    return action, at2, det


cc_pic, A_cc, cc_det = reconstruct("cc", [int(x) for x in perm_obj["cc_permutation_1based"]])
ct_pic, A_ct, ct_det = reconstruct("ct", [int(x) for x in perm_obj["ct_permutation_1based"]])
if pic["mm"](cc_pic, ct_pic) != pic["mm"](ct_pic, cc_pic):
    raise SystemExit("cc/ct integral Picard actions do not commute")
if mm2(A_cc, A_ct) != mm2(A_ct, A_cc):
    raise SystemExit("cc/ct intrinsic A[2] actions do not commute")

# The two coordinate swaps and seven coordinate signs are Q-defined, so they
# must commute with the Galois V4.  This also fixes the marking convention.
for name, Q in [("swap12", A12), ("swap13", A13)] + [
    (f"sign_{j+1}", S) for j, S in enumerate(signs7)
]:
    for gname, G in (("cc", A_cc), ("ct", A_ct)):
        if mm2(Q, G) != mm2(G, Q):
            raise SystemExit(f"{name} failed {gname} commutation on intrinsic A[2]")

out = {
    "schema": "STAGE33_07_ACTUAL_GALOIS_AT2_ACTIONS_V1",
    "source": {
        "known_class_permutation_certificate_sha256": EXPECTED_PERM,
        "upstream_git_blob_sha1": SOURCE_BLOB,
        "retained_stage32_marking_bundle_sha256": base["marking"]["canonical_sha256"],
    },
    "integral_picard_actions": {
        "basis": "upstream primitive INDLIST known-class basis",
        "cc_action_64x64": cc_pic,
        "ct_action_64x64": ct_pic,
        "cc_determinant": cc_det,
        "ct_determinant": ct_det,
        "all_140_known_classes_transport_exactly": True,
        "picard_gram_preserved": True,
        "hyperplane_fixed": True,
        "v4_relations_exact": True,
    },
    "intrinsic_discriminant_two_torsion": {
        "model": "ker(Picard_Gram_mod_2) represented by y/2 modulo Picard",
        "dimension_f2": N,
        "cc_action_14x14": A_cc,
        "ct_action_14x14": A_ct,
        "v4_relations_exact": True,
        "quadratic_form_preserved": True,
        "commutes_with_two_coordinate_swaps_and_seven_coordinate_signs": True,
    },
    "execution": {
        "remote_cas_used": False,
        "smith_form_used": False,
        "magma_picard_basis_used": False,
        "method": "transport source-locked 140-class Galois permutations through retained Stage32 INDLIST marking",
    },
    "exact_consequence": {
        "actual_cc_ct_identified_intrinsically_on_at2": True,
        "intrinsic_to_retained_transport_can_now_require_named_v4_equivariance": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "actual_cc_ct_intrinsic_at2_identified": True,
    "v4_relations_exact": True,
    "q_defined_swap_sign_commutation_exact": True,
    "certificate_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
