#!/usr/bin/env python3
"""Source-bind the V89 e3 retained A_T/2A_T class to the marked Picard dual lattice.

V89 identifies the unique retained mixed-Smith quotient coordinate with support
[1,8,10], but deliberately does not identify those indices with literal Picard
divisors. Stage33-09 subsequently certified an exact unimodular bridge from
the upstream INDLIST Picard basis to the historical retained Magma Basis(Pic).

The historical q256 discriminant endpoint came from one exact SmithForm of the
historical 64x64 Picard Gram. Its retained source lock preserves the exact
submitted Smith program, but not the transient 14x64 rows of V^-1 and 64x14
columns of V. This producer replays that byte-identical program on the now
source-bound historical Gram, verifies the resulting mixed basis against the
retained cc/ct, seven sign actions and current compact discriminant form, then
transports the 14 Smith dual numerators through the certified Stage33-09 basis
bridge.

The output is an exact marked Picard-*dual* source binding. It is NOT a literal
Picard divisor, Kummer function, Cech seed, residue audit, or full-surface
H^2(mu_2) lift.
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
STAGE = HERE.parent
LEGACY = STAGE / "33-07"
MARKED = STAGE / "33-09"
OUT = HERE / "e3-retained-at-marked-picard-dual-source-v91.json"
V89_PATH = HERE / "e3-proper14-dual-to-discriminant-quotient-bridge-v89.json"
COMPACT_PATH = LEGACY / "picard-discriminant-compact.json"
ENDPOINT_PATH = LEGACY / "retained-q256-geometric-sign-endpoint.json"
OLD_BASE_SCRIPT = LEGACY / "picard_base_rows_retained.py"
OLD_SIGN_SCRIPT = LEGACY / "picard_coordinate_sign_rows_retained.py"
BRIDGE_PATH = MARKED / "marked-picard-basis-bridge-certified.json"

V89_SHA = "26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639"
COMPACT_SHA = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"
ENDPOINT_SHA = "19d59e89b87d49681ae8b1b165085d529bef64b40c2d5ab6fe692a6b899fb061"
BRIDGE_SHA = "039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92"
OLD_BASE_SHA = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
OLD_SIGN_SHA = "5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
MODS = [2] * 4 + [4] * 6 + [8] * 4
TARGET = [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]

sys.path.insert(0, str(LEGACY))
from stoll_cuboid_source import run_magma  # noqa: E402


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path: Path, expected: str) -> dict:
    x = json.loads(path.read_text(encoding="utf-8"))
    body = dict(x)
    claimed = body.pop("canonical_sha256", None)
    if claimed != expected or csha(body) != expected:
        raise SystemExit(f"canonical lock moved: {path}")
    return x


def mm(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    if not A or not B or len(A[0]) != len(B):
        raise SystemExit("matrix product shape mismatch")
    out = [[0] * len(B[0]) for _ in range(len(A))]
    nz = [[(j, int(x)) for j, x in enumerate(row) if x] for row in B]
    for i, row in enumerate(A):
        for k, a in enumerate(row):
            if a:
                for j, b in nz[k]:
                    out[i][j] += int(a) * b
    return out


def transpose(A: list[list[int]]) -> list[list[int]]:
    return [list(r) for r in zip(*A)]


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


def induced(
    R: list[list[int]], C: list[list[int]], G: list[list[int]]
) -> list[list[int]]:
    raw = mm(mm(R, transpose(G)), C)
    return [
        [int(x) % MODS[j] for j, x in enumerate(row)]
        for row in raw
    ]


def row_times(row: list[int], M: list[list[int]]) -> list[int]:
    return mm([row], M)[0]


v89 = load_locked(V89_PATH, V89_SHA)
compact = load_locked(COMPACT_PATH, COMPACT_SHA)
endpoint = load_locked(ENDPOINT_PATH, ENDPOINT_SHA)
bridge = load_locked(BRIDGE_PATH, BRIDGE_SHA)
if v89["e3_transport"]["retained_at_mod2_quotient_coordinate_f2"] != TARGET:
    raise SystemExit("V89 retained target moved")
if v89["e3_transport"]["retained_at_mod2_quotient_support_one_based"] != [1, 8, 10]:
    raise SystemExit("V89 retained support moved")
if compact["discriminant_moduli"] != MODS or endpoint["discriminant_moduli"] != MODS:
    raise SystemExit("retained mixed discriminant moduli moved")
if endpoint["source_locks"]["testa_stoll_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("retained q256 upstream source moved")
if bridge["source_locks"]["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("marked Picard bridge upstream source moved")

old = runpy.run_path(str(OLD_BASE_SCRIPT))["load"]()
signs = runpy.run_path(str(OLD_SIGN_SCRIPT))["load"]()
if old["canonical_sha256"] != OLD_BASE_SHA or signs["canonical_sha256"] != OLD_SIGN_SHA:
    raise SystemExit("historical retained Picard source lock moved")
if old["upstream_git_blob_sha1"] != SOURCE_BLOB:
    raise SystemExit("historical Picard Gram upstream source moved")
Gold = [[int(x) for x in row] for row in old["picard_gram_64x64"]]
if len(Gold) != 64 or any(len(r) != 64 for r in Gold):
    raise SystemExit("historical Picard Gram shape moved")

b = bridge["basis_bridge"]
if (
    b["from"] != "upstream primitive INDLIST known-class basis"
    or b["to"] != "historical retained Magma Basis(Pic)"
):
    raise SystemExit("marked Picard bridge orientation moved")
B = [[int(x) for x in row] for row in b["matrix_64x64"]]
Binv = [[int(x) for x in row] for row in b["inverse_64x64"]]
I64 = [[int(i == j) for j in range(64)] for i in range(64)]
if mm(B, Binv) != I64 or mm(Binv, B) != I64:
    raise SystemExit("marked Picard bridge inverse regression")

# Byte-identical historical common-Smith program. The crucial V91 repair is
# that P is Gold, the historical Magma Basis(Pic) Gram now exactly marked by
# Stage33-09, rather than the pre-#1439 INDLIST Gram used by the old diagnostic.
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
code = "SetColumns(0);\nP:=" + sparse_literal(Gold) + ";\n" + extra
code_sha = hashlib.sha256(code.encode()).hexdigest()
expected_code_sha = endpoint["source_locks"]["common_smith_submitted_code_sha256"]
if code_sha != expected_code_sha:
    raise SystemExit(
        f"historical common-Smith program is not byte-identical: {code_sha}"
    )

stdout, _attempt = run_magma(
    code, 180, "Stage33 V91 marked historical common Smith replay"
)
if "STAGE33_07_COMMON_SMITH_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("historical common-Smith replay failed")
if [int(x) for x in grab(stdout, "MODS")] != MODS:
    raise SystemExit("historical Smith invariant regression")
R = [[int(x) % 8 for x in grab(stdout, f"R_{a}")] for a in range(1, 15)]
C = [[int(x) % 8 for x in grab(stdout, f"C_{j}")] for j in range(1, 65)]
b8 = [[int(x) for x in grab(stdout, f"B8_{a}")] for a in range(1, 15)]
if any(len(r) != 64 for r in R) or any(len(r) != 14 for r in C + b8):
    raise SystemExit("common-Smith compact shape regression")
I14 = [[int(i == j) for j in range(14)] for i in range(14)]
if [[x % 8 for x in row] for row in mm(R, C)] != I14:
    raise SystemExit("common-Smith reduced inverse regression")
# The q256 action endpoint intentionally stores actions only.  The exact B8
# lives in the current compact discriminant certificate, which is separately
# canonical-locked above.
if b8 != compact["discriminant_bilinear_numerator_over_8_reduced"]:
    raise SystemExit(
        "historical Smith replay does not reproduce current compact bilinear form"
    )

old_cc = [[int(x) for x in row] for row in old["picard_action_cc_64x64"]]
old_ct = [[int(x) for x in row] for row in old["picard_action_ct_64x64"]]
order = list(signs["coordinate_order"])
if order != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
    raise SystemExit("historical sign order moved")
old_signs = [
    [[int(x) for x in row] for row in signs["picard_actions_64x64"][name]]
    for name in order
]
if induced(R, C, old_cc) != endpoint["cc_action_mixed_moduli"]:
    raise SystemExit("literal Smith basis failed retained cc reproduction")
if induced(R, C, old_ct) != endpoint["ct_action_mixed_moduli"]:
    raise SystemExit("literal Smith basis failed retained ct reproduction")
if [induced(R, C, G) for G in old_signs] != endpoint["sign_actions_mixed_moduli"]:
    raise SystemExit("literal Smith basis failed retained seven-sign reproduction")

# Transport dual-functional numerators from historical Magma coordinates to
# the source-marked INDLIST coordinates. Since B Gold B^T = Gcur, a dual row
# numerator transforms by B^T. The inverse compact columns transform by
# B^{-T}; these formulas are checked by exact cancellation below.
R_marked = [[int(x) % 8 for x in row] for row in mm(R, transpose(B))]
C_marked = [[int(x) % 8 for x in row] for row in mm(transpose(Binv), C)]
if [[x % 8 for x in row] for row in mm(R_marked, C_marked)] != I14:
    raise SystemExit(
        "marked Smith source transport orientation failed R_marked*C_marked=I"
    )

historical_target_num = [
    sum(TARGET[i] * R[i][j] for i in range(14)) % 8 for j in range(64)
]
marked_target_num = [
    sum(TARGET[i] * R_marked[i][j] for i in range(14)) % 8
    for j in range(64)
]
if marked_target_num != [
    x % 8 for x in row_times(historical_target_num, transpose(B))
]:
    raise SystemExit("target dual numerator marked transport mismatch")
decoded = row_times(marked_target_num, C_marked)
decoded = [int(decoded[j]) % MODS[j] for j in range(14)]
if decoded != TARGET:
    raise SystemExit(
        f"marked target failed exact mixed-coordinate roundtrip: {decoded}"
    )

out = {
    "schema": "stage33.e3.retained_at_marked_picard_dual_source.v91",
    "stage": "33-12",
    "role": "EXACT_NONCREDIT_MARKED_PICARD_DUAL_SOURCE_BINDING",
    "micro_goal": "E3_V91_SOURCE_BIND_RETAINED_AT_MOD2_SUPPORT_1_8_10_TO_MARKED_PICARD_DUAL_LATTICE",
    "arsenal_route": {
        "card": "S33-PW04",
        "method_reused": "marked unimodular Picard basis bridge plus exact dual-coordinate transport",
        "rank_or_determinant_only_identification_used": False,
        "basis_orientation_verified_by_inverse_roundtrip": True,
    },
    "source_locks": {
        "v89_canonical_sha256": V89_SHA,
        "picard_discriminant_compact_sha256": COMPACT_SHA,
        "retained_q256_endpoint_sha256": ENDPOINT_SHA,
        "stage33_09_marked_picard_bridge_sha256": BRIDGE_SHA,
        "retained_old_picard_base_sha256": OLD_BASE_SHA,
        "retained_old_picard_signs_sha256": OLD_SIGN_SHA,
        "upstream_git_blob_sha1": SOURCE_BLOB,
        "historical_common_smith_submitted_code_sha256": expected_code_sha,
    },
    "historical_common_smith_replay": {
        "discriminant_moduli": MODS,
        "vin_nontrivial_rows_mod8_14x64": R,
        "v_nontrivial_columns_mod8_64x14": C,
        "discriminant_bilinear_numerator_over_8_reduced": b8,
        "submitted_code_byte_identical_to_historical_producer": True,
        "retained_cc_ct_and_seven_sign_actions_reproduced_literally": True,
        "retained_discriminant_form_reproduced_literally": True,
    },
    "marked_picard_dual_transport": {
        "marked_basis": "upstream primitive INDLIST known-class basis",
        "historical_basis": "historical retained Magma Basis(Pic)",
        "historical_to_marked_basis_matrix": B,
        "marked_to_historical_basis_matrix": Binv,
        "mixed_generator_dual_numerators_mod8_14x64_in_marked_indlist_basis": R_marked,
        "marked_dual_numerator_to_mixed_columns_mod8_64x14": C_marked,
        "all_14_generators_roundtrip_exact_mod8": True,
        "dual_numerator_transport_formula": "R_marked = R_historical * transpose(B)",
        "inverse_formula": "C_marked = transpose(B^{-1}) * C_historical",
    },
    "e3_source_binding": {
        "retained_at_mod2_quotient_coordinate_f2": TARGET,
        "retained_at_mod2_quotient_support_one_based": [1, 8, 10],
        "historical_picard_dual_numerator_mod8_64": historical_target_num,
        "marked_indlist_picard_dual_numerator_mod8_64": marked_target_num,
        "mixed_coordinate_roundtrip_exact": True,
        "source_bound_to_actual_140_class_marking": True,
        "object_type": "marked Picard dual-lattice/discriminant class, not an integral Picard divisor",
    },
    "exact_consequence": {
        "retained_support_1_8_10_source_bound_to_marked_picard_dual_class": True,
        "all_14_retained_mixed_smith_generators_source_bound_to_marked_picard_dual_basis": True,
        "literal_picard_divisor_materialized": False,
        "literal_kummer_function_materialized": False,
        "literal_cech_seed_materialized": False,
        "complete_residue_audit_materialized": False,
        "genuine_full_surface_h2_mu2_lift_for_e3": False,
    },
    "anti_loop": [
        "marked Picard dual numerator is not an integral Picard divisor",
        "retained support 1,8,10 is still not a literal branch/divisor label",
        "source binding of a discriminant class is not a Kummer/Cech seed",
        "proper14 axes 3+5 are not boundary/A2 positions 3+5",
        "J2 literal Cech data cannot be relabeled as e3",
    ],
    "credit_firewall": {
        "stage33_progress": "6/11",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "receiver_credit": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "merge_allowed": False,
    },
    "next_exact_leaf": "V91A_LIFT_MARKED_PICARD_DUAL_CLASS_SUPPORT_1_8_10_TO_LITERAL_DIVISOR_OR_DIRECT_CECH_KUMMER_DATUM",
    "status": "PASS_EXACT_V91_MARKED_PICARD_DUAL_SOURCE_BINDING_LITERAL_GEOMETRY_STILL_OPEN",
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("STAGE33_V91_MARKED_PICARD_DUAL_SOURCE_BINDING=PASS_EXACT")
print("CERTIFICATE_SHA256=" + out["canonical_sha256"])
print(
    "E3_MARKED_DUAL_NUMERATOR_MOD8="
    + json.dumps(marked_target_num, separators=(",", ":"))
)
print(
    "V91_CERTIFICATE_JSON="
    + json.dumps(out, sort_keys=True, separators=(",", ":"))
)
print("NEXT=" + out["next_exact_leaf"])
