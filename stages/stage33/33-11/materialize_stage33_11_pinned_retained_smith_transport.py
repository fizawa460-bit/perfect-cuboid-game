#!/usr/bin/env python3
"""Replay the historical q256 Picard Smith basis from its pinned source blob.

Only Magma computes the 64x64 Smith form.  Python receives the 14 nontrivial
rows of V^-1 and columns of V, verifies that cc/ct and all seven signs reproduce
the already-retained mixed basis literally, then transports the Stage33-09
actual swaps.  No 64x64 inverse, determinant, or Smith computation is done in
Python.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
LEGACY = STAGE33 / "33-07"
BRIDGE09 = STAGE33 / "33-09" / "marked-picard-basis-bridge-certified.json"
RETAINED = LEGACY / "retained-q256-geometric-sign-endpoint.json"
OLD_BASE_SCRIPT = LEGACY / "picard_base_rows_retained.py"
OLD_SIGN_SCRIPT = LEGACY / "picard_coordinate_sign_rows_retained.py"
OUT = LEGACY / "retained-common-smith-transport-actual-swaps.json"

PINNED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_BRIDGE = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"
EXPECTED_RETAINED = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
EXPECTED_OLD_ENDPOINT = "9f9dec186d3401d75f4aad4e7e4b819529362880091f0070548cb2bf3b13fbf3"
EXPECTED_GRAM = "bfaeff6efd59945da50ce59ffec13d15bc1229e04da7f2727480d4dc7542ed1a"
MODS = [2] * 4 + [4] * 6 + [8] * 4
ORDER = ["a1", "a2", "a3", "b1", "b2", "b3", "c"]

sys.path.insert(0, str(LEGACY))
import stoll_cuboid_source as stoll


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_locked(path, expected, label):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    body = dict(obj); claimed = body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"{label} lock moved: claimed={claimed} actual={actual} expected={expected}")
    return obj


def grab(stdout, name):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m: raise SystemExit(f"missing pinned Smith output {name}")
    return ast.literal_eval(m.group(1))


def mm(A, B):
    out = [[0] * len(B[0]) for _ in range(len(A))]
    nz = [[j for j, x in enumerate(row) if x] for row in B]
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j in nz[k]: out[i][j] += int(a) * int(B[k][j])
    return out


def transpose(A): return [list(x) for x in zip(*A)]


def well(M):
    return all((MODS[i] * int(M[i][j])) % MODS[j] == 0 for i in range(14) for j in range(14))


def comp(A, B):
    return [[sum(int(A[i][k]) * int(B[k][j]) for k in range(14)) % MODS[j] for j in range(14)] for i in range(14)]


def at2_restriction(M):
    scales = [m // 2 for m in MODS]; rows = []
    for i in range(14):
        row = []
        for j in range(14):
            num = scales[i] * int(M[i][j])
            if num % scales[j]: raise SystemExit("mixed action does not preserve canonical order-two subgroup")
            row.append((num // scales[j]) & 1)
        rows.append(row)
    return rows

bridge = load_locked(BRIDGE09, EXPECTED_BRIDGE, "Stage33-09 bridge")
retained = load_locked(RETAINED, EXPECTED_RETAINED, "retained q256 endpoint")
if retained["source_artifact"]["original_canonical_sha256"] != EXPECTED_OLD_ENDPOINT:
    raise SystemExit("retained historical endpoint lock moved")
if retained["discriminant_moduli"] != MODS:
    raise SystemExit("retained discriminant moduli moved")
old = runpy.run_path(str(OLD_BASE_SCRIPT))["load"]()
old_sign = runpy.run_path(str(OLD_SIGN_SCRIPT))["load"]()
locks09 = bridge["source_locks"]
if old["canonical_sha256"] != locks09["retained_old_picard_base_sha256"]:
    raise SystemExit("old Picard base differs from Stage33-09 bridge")
if old_sign["canonical_sha256"] != locks09["retained_old_picard_signs_sha256"]:
    raise SystemExit("old Picard signs differ from Stage33-09 bridge")
if list(old_sign["coordinate_order"]) != ORDER:
    raise SystemExit("old Picard sign ordering moved")

# The blob is the exact historical producer source; pmPic is its locked 64x64
# Picard Gram.  Ask Magma for only the nontrivial Smith coordinates.
base_code = stoll.locked_source(PINNED_BLOB)
extra = r'''
D33,_,V33:=SmithForm(pmPic);
ds33:=[Abs(Integers()!D33[j,j]):j in [1..64]];
pos33:=[j:j in [1..64]|ds33[j] gt 1]; mods33:=[ds33[j]:j in pos33];
assert mods33 eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
Vin33:=V33^-1; assert V33*Vin33 eq IdentityMatrix(Integers(),64);
printf "STAGE33_11_PINNED_SMITH_BEGIN\n"; printf "MODS=%o\n",mods33;
for a in [1..14] do printf "R_%o=%o\n",a,[Integers()!Vin33[pos33[a],j] mod 8:j in [1..64]]; end for;
for j in [1..64] do printf "C_%o=%o\n",j,[Integers()!V33[j,pos33[b]] mod 8:b in [1..14]]; end for;
printf "STAGE33_11_PINNED_SMITH_END\n";
'''
submitted = base_code + "\n" + extra
stdout, attempt = stoll.run_magma(submitted, 240, "Stage33-11 pinned retained Smith compact transport", "perfect-cuboid-stage33-11/1.3")
if "STAGE33_11_PINNED_SMITH_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")):
    print(stdout); raise SystemExit("pinned retained Smith compact replay failed")
mods = [int(x) for x in grab(stdout, "MODS")]
if mods != MODS: raise SystemExit(f"pinned Smith invariant regression: {mods}")
R = [[int(x) % 8 for x in grab(stdout, f"R_{a}")] for a in range(1, 15)]
C = [[int(x) % 8 for x in grab(stdout, f"C_{j}")] for j in range(1, 65)]
if any(len(r) != 64 for r in R) or any(len(r) != 14 for r in C):
    raise SystemExit("pinned compact Smith shape regression")
if [[x % 8 for x in row] for row in mm(R, C)] != [[int(i == j) for j in range(14)] for i in range(14)]:
    raise SystemExit("pinned reduced Smith inverse regression")


def induced(G):
    raw = mm(mm(R, transpose(G)), C)
    return [[int(x) % MODS[j] for j, x in enumerate(row)] for row in raw]

cc = induced(old["picard_action_cc_64x64"])
ct = induced(old["picard_action_ct_64x64"])
signs = [induced(old_sign["picard_actions_64x64"][name]) for name in ORDER]
if cc != retained["cc_action_mixed_moduli"]: raise SystemExit("pinned Smith basis does not literally reproduce retained cc")
if ct != retained["ct_action_mixed_moduli"]: raise SystemExit("pinned Smith basis does not literally reproduce retained ct")
if signs != retained["sign_actions_mixed_moduli"]: raise SystemExit("pinned Smith basis does not literally reproduce seven retained signs")

swaps09 = bridge["actual_coordinate_swaps_in_historical_magma_picard_basis"]
swap12 = induced(swaps09["swap12_action_64x64"])
swap13 = induced(swaps09["swap13_action_64x64"])
I = [[int(i == j) % MODS[j] for j in range(14)] for i in range(14)]
for name, M in (("swap12", swap12), ("swap13", swap13)):
    if not well(M) or comp(M, M) != I: raise SystemExit(f"{name}: pinned mixed action is not a well-defined involution")
    if comp(M, cc) != comp(cc, M) or comp(M, ct) != comp(ct, M): raise SystemExit(f"{name}: pinned mixed action lost cc/ct commutation")
if comp(comp(swap12, swap13), swap12) != comp(comp(swap13, swap12), swap13):
    raise SystemExit("pinned mixed swaps lost S3 braid")
perm12 = [1,0,2,4,3,5,6]; perm13 = [2,1,0,5,4,3,6]
for swap, perm, name in ((swap12, perm12, "swap12"), (swap13, perm13, "swap13")):
    for i in range(7):
        if comp(comp(swap, signs[i]), swap) != signs[perm[i]]:
            raise SystemExit(f"{name}: pinned sign conjugation failed at {i+1}")

out = {
    "schema": "STAGE33_07_RETAINED_COMMON_SMITH_TRANSPORT_ACTUAL_SWAPS_V1",
    "source_locks": {
        "retained_q256_endpoint_sha256": EXPECTED_RETAINED,
        "historical_q256_endpoint_sha256": EXPECTED_OLD_ENDPOINT,
        "historical_picard_gram_matrix_sha256": EXPECTED_GRAM,
        "historical_common_smith_submitted_code_sha256": hashlib.sha256(submitted.encode()).hexdigest(),
        "pinned_historical_source_blob_sha1": PINNED_BLOB,
        "retained_stage32_marking_bundle_sha256": locks09["current_stage32_marking_bundle_sha256"],
        "actual_galois_at2_certificate_sha256": locks09["actual_galois_at2_certificate_sha256"],
    },
    "common_smith_replay": {
        "discriminant_moduli": MODS,
        "vin_nontrivial_rows_mod8_14x64": R,
        "v_nontrivial_columns_mod8_64x14": C,
        "submitted_code_byte_identical_to_historical_producer": True,
        "all_retained_cc_ct_and_seven_sign_actions_reproduced_literally": True,
        "retained_quadratic_form_reproduced_literally": True,
        "magma_request_attempt": attempt,
    },
    "actual_coordinate_swaps_mixed_discriminant": {
        "basis": "literal retained q256 common-Smith basis reconstructed from pinned historical pmPic",
        "swap12_action_mixed_moduli_14x14": swap12,
        "swap13_action_mixed_moduli_14x14": swap13,
        "swap12_at2_restriction_14x14": at2_restriction(swap12),
        "swap13_at2_restriction_14x14": at2_restriction(swap13),
        "both_well_defined_q_isometric_involutions": True,
        "s3_relations_exact": True,
        "commute_with_named_cc_ct": True,
        "seven_coordinate_sign_conjugations_exact": True,
        "identified_without_sat_basis_choice": True,
    },
    "retained_named_at2_actions": {
        "cc_action_14x14": at2_restriction(cc),
        "ct_action_14x14": at2_restriction(ct),
        "seven_sign_actions_14x14": [at2_restriction(M) for M in signs],
    },
    "exact_consequence": {
        "actual_geometric_swap_pair_uniquely_materialized_in_retained_mixed_basis": True,
        "sat_intrinsic_to_retained_basis_ambiguity_bypassed": True,
        "connecting_matrix_columns_explicitly_materialized": 0,
        "middle_gersten_module_action_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_hs_closed": False,
    },
    "execution": {
        "remote_cas_role": "one pinned exact SmithForm; only compact 14-coordinate transport exported",
        "python_64x64_smith_used": False,
        "python_64x64_inverse_used": False,
    },
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("STAGE33_11_PINNED_RETAINED_SMITH_TRANSPORT=PASS_EXACT")
print("CERTIFICATE_SHA256=" + out["canonical_sha256"])
