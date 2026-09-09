#!/usr/bin/env python3
"""Verify Goal4BL: fixed-i quartic character collapses to rational norm mod 16."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bl-xi-two-adic-ray-class-parity.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bl-xi-two-adic-ray-class-parity-source-lock.md")
BK = P("stages/stage35-ex/35ex-35/goal4bk-fixed-i-quartic-dual-two-adic-ray-class.json")
BJ = P("stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter.json")
GCD = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "c8121ba4b36cbc27c418dd7651f32849044833bed375fa62fa6e0ae757515bc3"
SRC_BLOB = "df45f398b235cb4ae7434e37a9d9f6dda961bc5a"
ART_BLOB = "14afdead8287398f76d8b5dff481dd1eea839ae1"
BK_BLOB = "3b7e6a7f51ede0ba87a64ee10aed679fc8e6dc5b"
BJ_BLOB = "b8a20fd879a80215e9fa3fa8094bf979565de3c8"
GCD_BLOB = "d0cd03a5ff744d5f6536b6d2784c0e0d543fea48"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


def vlambda(a: int, b: int) -> int:
    """v_{1+i}(a+b*i) for nonzero Gaussian integer."""
    if a == 0 and b == 0:
        return 99
    v = 0
    while (a - b) % 2 == 0:
        a, b = (a + b) // 2, (b - a) // 2
        v += 1
        if a == 0 and b == 0:
            return 99
    return v


def primary(a: int, b: int) -> bool:
    return a % 2 != 0 and b % 2 == 0 and (a + b - 1) % 4 == 0


def chi_exp_from_A(a: int) -> int:
    return ((1 - a) // 2) % 4


def chi_label(e: int) -> str:
    return ("1", "i", "-1", "-i")[e % 4]


def legendre(a: int, p: int) -> int:
    z = pow(a % p, (p - 1) // 2, p)
    return -1 if z == p - 1 else z


assert blob(SRC) == SRC_BLOB
assert blob(ART) == ART_BLOB
assert blob(BK) == BK_BLOB
assert blob(BJ) == BJ_BLOB
assert blob(GCD) == GCD_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bk = json.loads(BK.read_text())
assert bk["canonical_sha256"] == "9d2ce7bedca1d38716903027d05aa58b6672c2fd069dc4121a0e7c579c94a636"
assert bk["result"]["canonical_fixed_i_quartic_dual_obtained"] is True
assert bk["next"]["unit"] == "35EX-35_GOAL4BL_XI_TWO_ADIC_RAY_CLASS_PARITY_PREFLIGHT"

bj = json.loads(BJ.read_text())
assert bj["canonical_sha256"] == "a1208a9ac7ec291074a36fe4d795e13b31eee22653fa83bcdef3b7eae120ac4e"
assert bj["result"]["global_gaussian_orientation_carrier_constructed"] is True

src = SRC.read_text()
for marker in (
    "(BL-primary)",
    "(BL-ray-table)",
    "(BL-chi-N)",
    "(BL-witness-real)",
    "(BL-witness-imag)",
    "(BL-Xi-character)",
    "(BL-Xi-square)",
    "(BL-prime-table)",
    "(BL-four-classes)",
    "(BL-product)",
    "(BL-boundary)",
    "35EX-35_GOAL4BM_RAMIFIED_ONE_PLUS_I_QUARTIC_DUAL_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bl_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bk"]["blob_sha1"] == BK_BLOB
assert art["source_locks"]["goal4bj"]["blob_sha1"] == BJ_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == GCD_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "9c72ebb551f2d8580a929b07c5dfcf2caa0f236e"
assert parent["aggregate_run"] == 34313690442
assert parent["aggregate_job"] == 102346571027
assert parent["hostile_audited"] is False

rows = []
for A in (1, 3, 5, 7):
    for B in (0, 2, 4, 6):
        if primary(A, B):
            N16 = (A * A + B * B) % 16
            eA = chi_exp_from_A(A)
            eN = ((N16 - 1) // 4) % 4
            assert N16 == (3 - 2 * A) % 16
            assert eA == eN
            rows.append((A, B % 4, N16, chi_label(eA)))
assert rows == [
    (1, 0, 1, "1"),
    (1, 0, 1, "1"),
    (3, 2, 13, "-i"),
    (3, 2, 13, "-i"),
    (5, 0, 9, "-1"),
    (5, 0, 9, "-1"),
    (7, 2, 5, "i"),
    (7, 2, 5, "i"),
]

assert vlambda(-4, -4) == 5
assert primary(1, 0) and primary(-3, -4)
assert (1 * 1 + 0 * 0) % 8 == ((-3) ** 2 + (-4) ** 2) % 8 == 1
assert chi_label(chi_exp_from_A(1)) == "1"
assert chi_label(chi_exp_from_A(-3)) == "-1"

assert vlambda(4, 4) == 5
assert primary(-1, -2) and primary(3, 2)
assert ((-1) ** 2 + (-2) ** 2) % 8 == (3 * 3 + 2 * 2) % 8 == 5
assert chi_label(chi_exp_from_A(-1)) == "i"
assert chi_label(chi_exp_from_A(3)) == "-i"

expected = {1: ("1", False), 5: ("i", True), 9: ("-1", False), 13: ("-i", True)}
got = {}
for r in (1, 5, 9, 13):
    e = ((r - 1) // 4) % 4
    label = chi_label(e)
    sensitive = label in ("i", "-i")
    got[r] = (label, sensitive)
assert got == expected
assert [(x["ell_mod16"], x["chi_i_pi"], x["orientation_sensitive"]) for x in art["mod16_sensitivity"]] == [
    (1, "1", False), (5, "i", True), (9, "-1", False), (13, "-i", True)
]

for d in art["local_reservoir_compatibility"]["diagnostics"]:
    ell, iota = d["ell"], d["iota"]
    assert ell % 4 == 1
    assert (iota * iota + 1) % ell == 0
    assert legendre(2 * iota, ell) == 1
assert {d["ell_mod16"] for d in art["local_reservoir_compatibility"]["diagnostics"]} == {1, 5, 9, 13}

xf = art["xi_norm_formula"]
assert xf["chi_i_Xi"] == "i^((R_minus-R_plus)/4)"
assert xf["chi_i_Xi_square"] == "(2/S_sec)"
assert xf["square_orientation_independent"] is True

res = art["result"]
assert res["lambda6_ray_depth_sufficient"] is True
assert res["lambda5_plus_norm_mod8_insufficient"] is True
assert res["fixed_i_character_descends_to_norm_mod16_on_primary"] is True
assert res["chi_i_Xi_exact_norm_formula_obtained"] is True
assert res["fixed_i_orientation_sensitive_classes"] == [5, 13]
assert res["fixed_i_orientation_blind_classes"] == [1, 9]
assert res["all_four_reservoir_mod16_classes_locally_compatible"] is True
assert res["fixed_i_global_product_new_relation"] is False
assert res["fixed_i_dual_universal_orientation_obstruction"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BM_RAMIFIED_ONE_PLUS_I_QUARTIC_DUAL_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BL_XI_TWO_ADIC_RAY_CLASS=PASS")
print("fixed_i_character_descends_to_norm_mod16=true")
print("orientation_sensitive_mod16=5,13")
print("orientation_blind_mod16=1,9")
print("new_reciprocity_relation=false")
print("canonical_sha256=" + EXPECTED)
