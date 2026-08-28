#!/usr/bin/env python3
"""Certify the marked bridge between the Stage32 INDLIST and retained Magma Picard bases.

The bridge is accepted only if it simultaneously transports:
- the full Picard Gram form;
- named cc and ct;
- all seven coordinate-sign actions.
It then transports the already-certified actual swap12/swap13 integral Picard
actions into the historical retained Magma Picard basis.  No Smith form or
finite quotient basis is used here.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import runpy
from pathlib import Path

from picard_base_rows_retained import load as load_old_base
from picard_coordinate_sign_rows_retained import load as load_old_signs

HERE = Path(__file__).resolve().parent
BRIDGE_PATH = HERE / "indlist-to-magma-picard-basis.json"
GALOIS_SCRIPT = HERE / "certify_actual_galois_at2_actions.py"
OUT = HERE / "marked-picard-basis-bridge-certified.json"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
OLD_BASE_LOCK = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
OLD_SIGN_LOCK = "5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9"
RANK = 64


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    bt = list(zip(*B))
    return [[sum(int(x) * int(y) for x, y in zip(row, col)) for col in bt] for row in A]


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*A)]


def integral_matrix(M: list[list[Fraction]], label: str) -> list[list[int]]:
    if any(x.denominator != 1 for row in M for x in row):
        bad = next(x for row in M for x in row if x.denominator != 1)
        raise SystemExit(f"{label} ceased to be integral: {bad}")
    return [[int(x) for x in row] for row in M]


bridge = json.loads(BRIDGE_PATH.read_text(encoding="utf-8"))
body = dict(bridge); claimed = body.pop("canonical_sha256", None)
if claimed != csha(body):
    raise SystemExit("marked Picard bridge canonical hash regression")
if bridge["schema"] != "STAGE33_07_INDLIST_TO_MAGMA_PICARD_BASIS_V1":
    raise SystemExit("marked Picard bridge schema moved")
if bridge["source"]["git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("marked Picard bridge source blob moved")
B = [[int(x) for x in row] for row in bridge["indlist_to_magma_picard_matrix_64x64"]]
if len(B) != RANK or any(len(row) != RANK for row in B):
    raise SystemExit("marked Picard bridge shape regression")

# Current marked INDLIST geometry and actions.
gal = runpy.run_path(str(GALOIS_SCRIPT))
at2 = gal["base"]
pic = at2["ns"]
Gcur = [[int(x) for x in row] for row in at2["gram"]]
Acur_all = [[[int(x) for x in row] for row in M] for M in at2["all_picard"]]
Acur_cc = [[int(x) for x in row] for row in gal["cc_pic"]]
Acur_ct = [[int(x) for x in row] for row in gal["ct_pic"]]
Acur_swap12, Acur_swap13 = Acur_all[0], Acur_all[1]
six_cur_signs = Acur_all[3:9]
I64 = [[int(i == j) for j in range(RANK)] for i in range(RANK)]
c_cur = I64
for S in six_cur_signs:
    c_cur = mm(c_cur, S)
cur_signs = six_cur_signs + [c_cur]

# Historical retained Magma-basis geometry and named actions.
old = load_old_base()
sign = load_old_signs()
if old["canonical_sha256"] != OLD_BASE_LOCK or sign["canonical_sha256"] != OLD_SIGN_LOCK:
    raise SystemExit("historical retained Picard bundle lock moved")
if old["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("historical retained Picard upstream source moved")
Gold = [[int(x) for x in row] for row in old["picard_gram_64x64"]]
Aold_cc = [[int(x) for x in row] for row in old["picard_action_cc_64x64"]]
Aold_ct = [[int(x) for x in row] for row in old["picard_action_ct_64x64"]]
order = list(sign["coordinate_order"])
if order != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
    raise SystemExit(f"retained coordinate-sign order moved: {order}")
old_signs = [
    [[int(x) for x in row] for row in sign["picard_actions_64x64"][name]]
    for name in order
]

# The upstream primitive-surjectivity assertion implies B is unimodular; certify it
# independently from the emitted integers before using it as a basis change.
detB = pic["det_bareiss"](B)
if abs(detB) != 1:
    raise SystemExit(f"marked INDLIST-to-Magma bridge is not unimodular: det={detB}")
BinvF = pic["invert_matrix"](B)
Binv = integral_matrix(BinvF, "inverse marked Picard bridge")
if mm(B, Binv) != I64 or mm(Binv, B) != I64:
    raise SystemExit("marked Picard bridge inverse regression")

# e_IND = B e_Magma, hence Gram_IND = B Gram_Magma B^T and
# B A_Magma = A_IND B for every named automorphism in row convention.
if mm(mm(B, Gold), transpose(B)) != Gcur:
    raise SystemExit("marked Picard bridge does not transport the full Gram form")
checks = [("cc", Acur_cc, Aold_cc), ("ct", Acur_ct, Aold_ct)]
checks.extend((name, cur_signs[i], old_signs[i]) for i, name in enumerate(order))
for name, Acur, Aold in checks:
    if mm(B, Aold) != mm(Acur, B):
        raise SystemExit(f"marked Picard bridge failed named action intertwining for {name}")


def to_old(Acur: list[list[int]]) -> list[list[int]]:
    return mm(mm(Binv, Acur), B)


Aold_swap12 = to_old(Acur_swap12)
Aold_swap13 = to_old(Acur_swap13)
for name, A in (("swap12", Aold_swap12), ("swap13", Aold_swap13)):
    if mm(A, A) != I64:
        raise SystemExit(f"{name}: transported old-basis action is not involutive")
    if mm(mm(A, Gold), transpose(A)) != Gold:
        raise SystemExit(f"{name}: transported old-basis action does not preserve old Gram")
    if abs(pic["det_bareiss"](A)) != 1:
        raise SystemExit(f"{name}: transported old-basis action is not unimodular")
    for gname, G in (("cc", Aold_cc), ("ct", Aold_ct)):
        if mm(A, G) != mm(G, A):
            raise SystemExit(f"{name}: transported old-basis action lost {gname} commutation")
if mm(mm(Aold_swap12, Aold_swap13), Aold_swap12) != mm(mm(Aold_swap13, Aold_swap12), Aold_swap13):
    raise SystemExit("transported old-basis swaps lost S3 braid relation")
perm12 = [1, 0, 2, 4, 3, 5, 6]
perm13 = [2, 1, 0, 5, 4, 3, 6]
for name, A, perm in (("swap12", Aold_swap12, perm12), ("swap13", Aold_swap13, perm13)):
    for i in range(7):
        if mm(mm(A, old_signs[i]), A) != old_signs[perm[i]]:
            raise SystemExit(f"{name}: old-basis sign conjugation regression at {order[i]}")

out = {
    "schema": "STAGE33_07_MARKED_PICARD_BASIS_BRIDGE_CERTIFIED_V1",
    "source_locks": {
        "upstream_git_blob_sha1": SOURCE_BLOB,
        "marked_bridge_certificate_sha256": bridge["canonical_sha256"],
        "retained_old_picard_base_sha256": OLD_BASE_LOCK,
        "retained_old_picard_signs_sha256": OLD_SIGN_LOCK,
        "current_stage32_marking_bundle_sha256": at2["marking"]["canonical_sha256"],
        "actual_galois_at2_certificate_sha256": gal["out"]["canonical_sha256"],
    },
    "basis_bridge": {
        "from": "upstream primitive INDLIST known-class basis",
        "to": "historical retained Magma Basis(Pic)",
        "matrix_64x64": B,
        "inverse_64x64": Binv,
        "determinant": detB,
        "full_gram_transport_exact": True,
        "named_action_intertwining_verified": ["cc", "ct"] + order,
    },
    "actual_coordinate_swaps_in_historical_magma_picard_basis": {
        "swap12_action_64x64": Aold_swap12,
        "swap13_action_64x64": Aold_swap13,
        "both_integral_unimodular_gram_isometries": True,
        "both_involutions": True,
        "s3_braid_exact": True,
        "commute_with_cc_ct": True,
        "seven_sign_conjugations_exact": True,
    },
    "exact_consequence": {
        "historical_retained_picard_basis_now_marked_by_actual_140_class_geometry": True,
        "actual_integral_swaps_now_available_in_historical_q256_picard_basis": True,
        "common_smith_transport_can_be_replayed_without_basis_guess": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "execution": {
        "generic_lattice_isometry_search_used": False,
        "bridge_obtained_from_pinned_upstream_qPic_marking": True,
        "smith_form_used": False,
    },
    "next_exact_leaf": "replay the historical common Smith transform on the historical Picard Gram and descend these two now-marked actual swaps into the literal retained mixed (2,4,8) basis",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "bridge_determinant": detB,
    "gram_and_nine_named_actions_intertwined": True,
    "actual_swaps_transported_to_historical_picard_basis": True,
    "certificate_sha256": out["canonical_sha256"],
    "next": out["next_exact_leaf"],
}, indent=2, sort_keys=True))
