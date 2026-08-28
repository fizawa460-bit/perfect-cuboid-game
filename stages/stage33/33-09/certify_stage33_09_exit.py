#!/usr/bin/env python3
"""Certify Stage33-09 Picard-equivariant transport by local exact replay.

The one-time remote producer is evidence acquisition only.  This verifier does
not trust its algebra booleans: it reloads the independently retained old
Picard Gram/actions and the current INDLIST geometry, then recomputes the
64x64 bridge, intertwining, isometry, involution and S3 identities over Z.
"""
from __future__ import annotations

import hashlib
import json
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
SOURCE = HERE / "marked-picard-basis-source.json"
BRIDGE = HERE / "marked-picard-basis-bridge-certified.json"
OUT = HERE / "stage33-09-closure.json"
GALOIS_SCRIPT = LEGACY / "certify_actual_galois_at2_actions.py"
OLD_BASE_SCRIPT = LEGACY / "picard_base_rows_retained.py"
OLD_SIGN_SCRIPT = LEGACY / "picard_coordinate_sign_rows_retained.py"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
NAMES = ["cc", "ct", "a1", "a2", "a3", "b1", "b2", "b3", "c"]
RANK = 64


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path: Path) -> dict:
    x = json.loads(path.read_text(encoding="utf-8"))
    body = dict(x)
    claimed = body.pop("canonical_sha256", None)
    if claimed != csha(body):
        raise SystemExit(f"canonical hash regression: {path.name}")
    return x


def imat(M: object, label: str) -> list[list[int]]:
    if not isinstance(M, list) or len(M) != RANK or any(not isinstance(r, list) or len(r) != RANK for r in M):
        raise SystemExit(f"{label}: expected 64x64 matrix")
    if any(type(x) is not int for r in M for x in r):
        raise SystemExit(f"{label}: non-integral JSON entry")
    return [[int(x) for x in r] for r in M]


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(r) for r in zip(*A)]


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Exact integer product, skipping zero entries in the right factor."""
    if not A or not B or len(A[0]) != len(B):
        raise SystemExit("matrix product shape mismatch")
    nz = [[(j, int(x)) for j, x in enumerate(row) if x] for row in B]
    out = [[0] * len(B[0]) for _ in range(len(A))]
    for i, row in enumerate(A):
        oi = out[i]
        for k, a in enumerate(row):
            if a:
                aa = int(a)
                for j, b in nz[k]:
                    oi[j] += aa * b
    return out


def require_eq(got: object, want: object, label: str) -> None:
    if got != want:
        raise SystemExit(f"local exact replay failed: {label}")


src = load_locked(SOURCE)
cert = load_locked(BRIDGE)
if src["schema"] != "STAGE33_07_INDLIST_TO_MAGMA_PICARD_BASIS_V1":
    raise SystemExit("marked source bridge schema moved")
if cert["schema"] != "STAGE33_07_MARKED_PICARD_BASIS_BRIDGE_CERTIFIED_V1":
    raise SystemExit("marked certified bridge schema moved")
if src["source"]["git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("upstream source blob moved")
if cert["source_locks"]["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("certified bridge upstream source blob moved")
if cert["source_locks"]["marked_bridge_certificate_sha256"] != src["canonical_sha256"]:
    raise SystemExit("certified bridge does not consume the retained marked source bridge")

# Make legacy deterministic helpers importable when their runpy leaves import
# statements relative to stages/stage33/33-07.
sys.path.insert(0, str(LEGACY))

# Independently retained historical q256 Picard data.
old = runpy.run_path(str(OLD_BASE_SCRIPT))["load"]()
sign = runpy.run_path(str(OLD_SIGN_SCRIPT))["load"]()
if old["canonical_sha256"] != cert["source_locks"]["retained_old_picard_base_sha256"]:
    raise SystemExit("retained old Picard base lock differs from certificate input")
if sign["canonical_sha256"] != cert["source_locks"]["retained_old_picard_signs_sha256"]:
    raise SystemExit("retained old Picard signs lock differs from certificate input")
if old["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("retained old Picard base upstream source moved")
Gold = imat(old["picard_gram_64x64"], "historical Gram")
Aold_cc = imat(old["picard_action_cc_64x64"], "historical cc")
Aold_ct = imat(old["picard_action_ct_64x64"], "historical ct")
order = list(sign["coordinate_order"])
if order != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
    raise SystemExit(f"retained coordinate-sign order moved: {order}")
old_signs = [imat(sign["picard_actions_64x64"][name], f"historical sign {name}") for name in order]

# Current exact INDLIST geometry/actions are reconstructed locally from retained
# Stage32 marking + retained 140-class permutations.  No remote CAS is used.
gal = runpy.run_path(str(GALOIS_SCRIPT))
base = gal["base"]
pic = base["ns"]
if base["marking"]["canonical_sha256"] != cert["source_locks"]["current_stage32_marking_bundle_sha256"]:
    raise SystemExit("current Stage32 marking lock differs from certificate input")
if gal["out"]["canonical_sha256"] != cert["source_locks"]["actual_galois_at2_certificate_sha256"]:
    raise SystemExit("actual Galois action lock differs from certificate input")
Gcur = imat(base["gram"], "current INDLIST Gram")
Acur_cc = imat(gal["cc_pic"], "current cc")
Acur_ct = imat(gal["ct_pic"], "current ct")
all_picard = [imat(M, f"current Picard action {j}") for j, M in enumerate(base["all_picard"])]
Acur_swap12, Acur_swap13 = all_picard[0], all_picard[1]
six_cur_signs = all_picard[3:9]
I64 = [[int(i == j) for j in range(RANK)] for i in range(RANK)]
c_cur = I64
for S in six_cur_signs:
    c_cur = mm(c_cur, S)
cur_signs = six_cur_signs + [c_cur]

# The source JSON and certified JSON must carry the identical literal bridge.
b = cert["basis_bridge"]
if b["from"] != "upstream primitive INDLIST known-class basis":
    raise SystemExit("marked basis source moved")
if b["to"] != "historical retained Magma Basis(Pic)":
    raise SystemExit("historical retained target basis moved")
Bsrc = imat(src["indlist_to_magma_picard_matrix_64x64"], "source marked bridge")
B = imat(b["matrix_64x64"], "certified marked bridge")
Binv = imat(b["inverse_64x64"], "certified marked bridge inverse")
require_eq(B, Bsrc, "source bridge equals certified bridge")
require_eq(mm(B, Binv), I64, "B * B^-1 = I")
require_eq(mm(Binv, B), I64, "B^-1 * B = I")
# Recompute the determinant rather than trusting certificate metadata.
detB = int(pic["det_bareiss"](B))
if abs(detB) != 1 or detB != int(b["determinant"]):
    raise SystemExit(f"local exact replay failed: bridge determinant {detB}")

# Gram transport and all nine named action intertwiners are recomputed from
# independently retained raw matrices.
require_eq(mm(mm(B, Gold), transpose(B)), Gcur, "B Gold B^T = Gcur")
checks = [("cc", Acur_cc, Aold_cc), ("ct", Acur_ct, Aold_ct)]
checks.extend((name, cur_signs[i], old_signs[i]) for i, name in enumerate(order))
for name, Acur, Aold in checks:
    require_eq(mm(B, Aold), mm(Acur, B), f"named intertwiner {name}")
if b["named_action_intertwining_verified"] != NAMES:
    raise SystemExit("certificate named-action coverage metadata moved")

# Recompute the actual swaps in the historical basis and then replay every
# algebraic identity relied on by the Stage33-09 exit.
s = cert["actual_coordinate_swaps_in_historical_magma_picard_basis"]
S12 = imat(s["swap12_action_64x64"], "retained swap12")
S13 = imat(s["swap13_action_64x64"], "retained swap13")
require_eq(S12, mm(mm(Binv, Acur_swap12), B), "swap12 = B^-1 A12 B")
require_eq(S13, mm(mm(Binv, Acur_swap13), B), "swap13 = B^-1 A13 B")
for name, S in (("swap12", S12), ("swap13", S13)):
    require_eq(mm(S, S), I64, f"{name} involution")
    require_eq(mm(mm(S, Gold), transpose(S)), Gold, f"{name} Gram isometry")
    detS = int(pic["det_bareiss"](S))
    if abs(detS) != 1:
        raise SystemExit(f"local exact replay failed: {name} determinant {detS}")
    require_eq(mm(S, Aold_cc), mm(Aold_cc, S), f"{name} commutes with cc")
    require_eq(mm(S, Aold_ct), mm(Aold_ct, S), f"{name} commutes with ct")
require_eq(mm(mm(S12, S13), S12), mm(mm(S13, S12), S13), "S3 braid")
perm12 = [1, 0, 2, 4, 3, 5, 6]
perm13 = [2, 1, 0, 5, 4, 3, 6]
for name, S, perm in (("swap12", S12, perm12), ("swap13", S13, perm13)):
    for i, target in enumerate(perm):
        require_eq(mm(mm(S, old_signs[i]), S), old_signs[target], f"{name} sign conjugation {order[i]}")

# The producer booleans are now only consistency metadata: every mathematical
# assertion below has already been replayed from matrices above.
if not all([
    b["full_gram_transport_exact"],
    s["both_integral_unimodular_gram_isometries"],
    s["both_involutions"],
    s["s3_braid_exact"],
    s["commute_with_cc_ct"],
    s["seven_sign_conjugations_exact"],
]):
    raise SystemExit("producer certificate metadata contradicts local exact replay")

# Downstream firewalls are unchanged.
e = cert["exact_consequence"]
if not e["historical_retained_picard_basis_now_marked_by_actual_140_class_geometry"]:
    raise SystemExit("historical retained Picard marking is not certified")
if not e["actual_integral_swaps_now_available_in_historical_q256_picard_basis"]:
    raise SystemExit("actual integral swaps are not available in retained q256 Picard basis")
if int(e["connecting_matrix_columns_explicitly_materialized"]) != 0:
    raise SystemExit("Stage33-09 must not claim connecting-map columns")
if e["middle_gersten_module_action_materialized"] or e["absolute_delta_loc_computed"] or e["arithmetic_hs_closed"]:
    raise SystemExit("Stage33-09 downstream firewall violated")
if cert["stage33_progress"] != "6/11" or cert["stage33_08_released"] or cert["theorem_credit"] or cert["endpoint_credit"]:
    raise SystemExit("Stage33-09 inherited firewall moved")

out = {
    "schema": "STAGE33_09_PICARD_EQUIVARIANT_TRANSPORT_CLOSURE_V1",
    "parent_big_task": "33-07",
    "source_locks": {
        "upstream_git_blob_sha1": SOURCE_BLOB,
        "marked_picard_source_sha256": src["canonical_sha256"],
        "marked_picard_bridge_certificate_sha256": cert["canonical_sha256"],
        "retained_old_picard_base_sha256": cert["source_locks"]["retained_old_picard_base_sha256"],
        "retained_old_picard_signs_sha256": cert["source_locks"]["retained_old_picard_signs_sha256"],
        "current_stage32_marking_bundle_sha256": cert["source_locks"]["current_stage32_marking_bundle_sha256"],
        "actual_galois_at2_certificate_sha256": cert["source_locks"]["actual_galois_at2_certificate_sha256"],
    },
    "exit_condition": {
        "HISTORICAL_RETAINED_PICARD_MARKING_BRIDGE_CERTIFIED": True,
        "NAMED_INTEGRAL_AND_TWO_TORSION_ACTIONS_SOURCE_LOCKED": True,
        "PICARD_EQUIVARIANT_TRANSPORT_CLOSED": True,
    },
    "named_integral_action_coverage": NAMES + ["swap12", "swap13"],
    "historical_q256_basis_marking_exact": True,
    "stage33_10_released": True,
    "stage33_progress": "6/11",
    "stage33_07_closed": False,
    "stage33_08_released": False,
    "connecting_matrix_columns_explicitly_materialized": 0,
    "absolute_h1_receiver_exact": False,
    "arithmetic_localization_connecting_map_computed": False,
    "arithmetic_hs_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "next_item": "Stage33-10_ABSOLUTE_H1_AND_GALOIS_DESCENT_ADAPTER",
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("STAGE33_09_LOCAL_CERTIFICATE_REPLAY=PASS_EXACT")
print("REPLAYED=BRIDGE_INVERSE,DETERMINANT,GRAM,CC_CT_7SIGNS,SWAPS_INVOLUTIONS_ISOMETRIES,S3,SIGN_CONJUGATION")
print("STAGE33_09_PICARD_EQUIVARIANT_TRANSPORT=PASS_EXACT")
print("CERTIFICATE_SHA256=" + out["canonical_sha256"])
print("NEXT=" + out["next_item"])
