#!/usr/bin/env python3
"""Replay the retained common Smith basis and descend the actual Picard swaps.

The retained q256 endpoint was produced from one exact Magma SmithForm of the
64x64 Picard Gram.  Its source lock preserves the exact submitted-code SHA and
the induced cc/ct + seven coordinate-sign matrices, but not the transient
14x64 rows of V^-1 and 64x14 columns of V that define that Smith basis.

Reconstruct the same Picard Gram locally from the retained Stage32 marking,
re-submit *the byte-identical Smith program*, and accept its compact R,C output
only if it reproduces every retained named action exactly.  This identifies the
literal retained mixed-order Smith basis.  The two actual integral coordinate
swaps can then be transported into that basis with no SAT basis ambiguity.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import runpy
from pathlib import Path

from stoll_cuboid_source import run_magma

HERE = Path(__file__).resolve().parent
OUT = HERE / "retained-common-smith-transport-actual-swaps.json"
GAL_SCRIPT = HERE / "certify_actual_galois_at2_actions.py"
RETAINED_PATH = HERE / "retained-q256-geometric-sign-endpoint.json"

EXPECTED_RETAINED = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
EXPECTED_OLD_ENDPOINT = "9f9dec186d3401d75f4aad4e7e4b819529362880091f0070548cb2bf3b13fbf3"
EXPECTED_GRAM_MATRIX_SHA256 = "bfaeff6efd59945da50ce59ffec13d15bc1229e04da7f2727480d4dc7542ed1a"
MODS = [2] * 4 + [4] * 6 + [8] * 4
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    out = [[0] * len(B[0]) for _ in range(len(A))]
    nz = [[j for j, x in enumerate(row) if x] for row in B]
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j in nz[k]:
                    out[i][j] += int(a) * int(B[k][j])
    return out


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(x) for x in zip(*A)]


def sparse_literal(M: list[list[int]]) -> str:
    ts = [
        f"<{i},{j},{int(M[i-1][j-1])}>"
        for i in range(1, 65)
        for j in range(1, 65)
        if M[i - 1][j - 1]
    ]
    return "Matrix(SparseMatrix(Integers(),64,64,[" + ",".join(ts) + "]))"


def grab(stdout: str, name: str):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing common-Smith output {name}")
    return ast.literal_eval(m.group(1))


def well(M: list[list[int]]) -> bool:
    return all((MODS[i] * int(M[i][j])) % MODS[j] == 0 for i in range(14) for j in range(14))


def comp(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    return [
        [sum(int(A[i][k]) * int(B[k][j]) for k in range(14)) % MODS[j] for j in range(14)]
        for i in range(14)
    ]


def at2_restriction(M: list[list[int]]) -> list[list[int]]:
    scales = [m // 2 for m in MODS]
    rows = []
    for i in range(14):
        row = []
        for j in range(14):
            num = scales[i] * int(M[i][j])
            if num % scales[j]:
                raise SystemExit("mixed action does not preserve the canonical order-two subgroup")
            row.append((num // scales[j]) & 1)
        rows.append(row)
    return rows


def transform_form(M: list[list[int]], b8: list[list[int]]) -> list[list[int]]:
    return [
        [
            sum(int(M[i][a]) * int(b8[a][b]) * int(M[j][b]) for a in range(14) for b in range(14))
            for j in range(14)
        ]
        for i in range(14)
    ]


def preserves_q(M: list[list[int]], b8: list[list[int]]) -> bool:
    B = transform_form(M, b8)
    return all(
        (B[i][j] - int(b8[i][j])) % (16 if i == j else 8) == 0
        for i in range(14)
        for j in range(14)
    )


retained = json.loads(RETAINED_PATH.read_text(encoding="utf-8"))
body = dict(retained)
claimed = body.pop("canonical_sha256", None)
if claimed != EXPECTED_RETAINED or csha(body) != EXPECTED_RETAINED:
    raise SystemExit("retained q256 geometric-sign endpoint lock moved")
if retained["source_artifact"]["original_canonical_sha256"] != EXPECTED_OLD_ENDPOINT:
    raise SystemExit("retained q256 source endpoint lock moved")
if retained["discriminant_moduli"] != MODS:
    raise SystemExit("retained mixed discriminant moduli moved")

gal = runpy.run_path(str(GAL_SCRIPT))
at2 = gal["base"]
pic = at2["ns"]
gram = [[int(x) for x in row] for row in at2["gram"]]
if csha(gram) != EXPECTED_GRAM_MATRIX_SHA256:
    raise SystemExit("locally reconstructed Picard Gram differs from the historical q256 Gram")
if pic["det_bareiss"](gram) != -268435456:
    raise SystemExit("Picard Gram determinant regression")

all_picard = at2["all_picard"]
swap12_pic = all_picard[0]
swap13_pic = all_picard[1]
six_sign_pic = all_picard[3:9]
c_sign_pic = [[int(i == j) for j in range(64)] for i in range(64)]
for G in six_sign_pic:
    c_sign_pic = pic["mm"](c_sign_pic, G)
sign_pic = six_sign_pic + [c_sign_pic]
cc_pic = gal["cc_pic"]
ct_pic = gal["ct_pic"]

# This block is byte-for-byte the historical producer's common-Smith program.
extra = r'''
D,_,V:=SmithForm(P); ds:=[Abs(Integers()!D[j,j]):j in [1..64]];
pos:=[j:j in [1..64]|ds[j] gt 1]; mods:=[ds[j]:j in pos];
assert mods eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
Vin:=V^-1; assert V*Vin eq IdentityMatrix(Integers(),64);
Pinv:=ChangeRing(P,Rationals())^-1; Vq:=ChangeRing(Vin,Rationals()); B8:=8*Vq*Pinv*Transpose(Vq);
printf "STAGE33_07_COMMON_SMITH_BEGIN\n"; printf "MODS=%o\n",mods;
for a in [1..14] do printf "R_%o=%o\n",a,[Integers()!Vin[pos[a],j] mod 8:j in [1..64]]; end for;
for j in [1..64] do printf "C_%o=%o\n",j,[Integers()!V[j,pos[b]] mod 8:b in [1..14]]; end for;
for a in [1..14] do printf "B8_%o=%o\n",a,[Integers()!B8[pos[a],pos[b]] mod (a eq b select 16 else 8):b in [1..14]]; end for;
printf "STAGE33_07_COMMON_SMITH_END\n";
'''
code = "SetColumns(0);\nP:=" + sparse_literal(gram) + ";\n" + extra
code_sha = hashlib.sha256(code.encode()).hexdigest()
expected_code_sha = retained["source_locks"]["common_smith_submitted_code_sha256"]
if code_sha != expected_code_sha:
    raise SystemExit(f"historical common-Smith submitted code did not replay byte-identically: {code_sha}")

stdout, attempt = run_magma(code, 180, "Stage33-07 retained common Smith transport replay")
if "STAGE33_07_COMMON_SMITH_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("retained common Smith transport replay failed")
mods = [int(x) for x in grab(stdout, "MODS")]
if mods != MODS:
    raise SystemExit(f"replayed Smith invariant regression: {mods}")
R = [[int(x) % 8 for x in grab(stdout, f"R_{a}")] for a in range(1, 15)]
C = [[int(x) % 8 for x in grab(stdout, f"C_{j}")] for j in range(1, 65)]
b8 = [[int(x) for x in grab(stdout, f"B8_{a}")] for a in range(1, 15)]
if any(len(r) != 64 for r in R) or any(len(r) != 14 for r in C + b8):
    raise SystemExit("replayed common-Smith compact shape regression")
if mm(R, C) != [[int(i == j) for j in range(14)] for i in range(14)]:
    # R,C are reduced mod 8, so reduce the check explicitly.
    if [[x % 8 for x in row] for row in mm(R, C)] != [[int(i == j) for j in range(14)] for i in range(14)]:
        raise SystemExit("replayed reduced Smith inverse regression")


def induced(G: list[list[int]]) -> list[list[int]]:
    raw = mm(mm(R, transpose(G)), C)
    return [[int(x) % MODS[j] for j, x in enumerate(row)] for row in raw]

# Literal-basis verification: the replay is accepted only if all nine named
# retained actions are exactly reproduced in the already-retained basis.
replayed_cc = induced(cc_pic)
replayed_ct = induced(ct_pic)
replayed_signs = [induced(G) for G in sign_pic]
if replayed_cc != retained["cc_action_mixed_moduli"]:
    raise SystemExit("replayed Smith basis does not literally match retained cc action")
if replayed_ct != retained["ct_action_mixed_moduli"]:
    raise SystemExit("replayed Smith basis does not literally match retained ct action")
if replayed_signs != retained["sign_actions_mixed_moduli"]:
    raise SystemExit("replayed Smith basis does not literally match retained seven sign actions")
if b8 != retained["discriminant_bilinear_numerator_over_8_reduced"]:
    raise SystemExit("replayed Smith basis does not literally match retained quadratic form")

swap12 = induced(swap12_pic)
swap13 = induced(swap13_pic)
I = [[int(i == j) % MODS[j] for j in range(14)] for i in range(14)]
for name, M in (("swap12", swap12), ("swap13", swap13)):
    if not well(M) or comp(M, M) != I:
        raise SystemExit(f"{name}: mixed Smith action is not a well-defined involution")
    if not preserves_q(M, b8):
        raise SystemExit(f"{name}: mixed Smith action does not preserve q")
    if comp(M, replayed_cc) != comp(replayed_cc, M) or comp(M, replayed_ct) != comp(replayed_ct, M):
        raise SystemExit(f"{name}: mixed Smith action lost Q-defined Galois commutation")
if comp(comp(swap12, swap13), swap12) != comp(comp(swap13, swap12), swap13):
    raise SystemExit("actual mixed Smith swaps lost the S3 braid relation")

perm12 = [1, 0, 2, 4, 3, 5, 6]
perm13 = [2, 1, 0, 5, 4, 3, 6]
for swap, perm, name in ((swap12, perm12, "swap12"), (swap13, perm13, "swap13")):
    for i in range(7):
        got = comp(comp(swap, replayed_signs[i]), swap)
        if got != replayed_signs[perm[i]]:
            raise SystemExit(f"{name}: mixed Smith sign conjugation failed at sign {i+1}")

swap12_at2 = at2_restriction(swap12)
swap13_at2 = at2_restriction(swap13)
cc_at2 = at2_restriction(replayed_cc)
ct_at2 = at2_restriction(replayed_ct)
sign_at2 = [at2_restriction(M) for M in replayed_signs]

out = {
    "schema": "STAGE33_07_RETAINED_COMMON_SMITH_TRANSPORT_ACTUAL_SWAPS_V1",
    "source_locks": {
        "retained_q256_endpoint_sha256": EXPECTED_RETAINED,
        "historical_q256_endpoint_sha256": EXPECTED_OLD_ENDPOINT,
        "historical_picard_gram_matrix_sha256": EXPECTED_GRAM_MATRIX_SHA256,
        "historical_common_smith_submitted_code_sha256": expected_code_sha,
        "retained_stage32_marking_bundle_sha256": at2["marking"]["canonical_sha256"],
        "actual_galois_at2_certificate_sha256": gal["out"]["canonical_sha256"],
    },
    "common_smith_replay": {
        "discriminant_moduli": MODS,
        "vin_nontrivial_rows_mod8_14x64": R,
        "v_nontrivial_columns_mod8_64x14": C,
        "discriminant_bilinear_numerator_over_8_reduced": b8,
        "submitted_code_byte_identical_to_historical_producer": True,
        "all_retained_cc_ct_and_seven_sign_actions_reproduced_literally": True,
        "retained_quadratic_form_reproduced_literally": True,
        "magma_request_attempt": attempt,
    },
    "actual_coordinate_swaps_mixed_discriminant": {
        "basis": "literal retained q256 common-Smith basis",
        "swap12_action_mixed_moduli_14x14": swap12,
        "swap13_action_mixed_moduli_14x14": swap13,
        "swap12_at2_restriction_14x14": swap12_at2,
        "swap13_at2_restriction_14x14": swap13_at2,
        "both_well_defined_q_isometric_involutions": True,
        "s3_relations_exact": True,
        "commute_with_named_cc_ct": True,
        "seven_coordinate_sign_conjugations_exact": True,
        "identified_without_sat_basis_choice": True,
    },
    "retained_named_at2_actions": {
        "cc_action_14x14": cc_at2,
        "ct_action_14x14": ct_at2,
        "seven_sign_actions_14x14": sign_at2,
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
        "remote_cas_role": "one bounded exact SmithForm on an already-retained 64x64 integer Gram",
        "remote_geometry_recomputed": False,
        "local_picard_geometry_reconstructed_from_retained_stage32_marking": True,
    },
    "next_exact_leaf": "induce the literal retained swap12/swap13 actions on finite H1(V4,K) and impose corresponding exact source/receiver naturality on the 26x16 middle-Gersten extension space",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "literal_retained_smith_basis_replayed": True,
    "actual_swap_pair_uniquely_materialized": True,
    "remote_geometry_recomputed": False,
    "certificate_sha256": out["canonical_sha256"],
    "next": out["next_exact_leaf"],
}, indent=2, sort_keys=True))
