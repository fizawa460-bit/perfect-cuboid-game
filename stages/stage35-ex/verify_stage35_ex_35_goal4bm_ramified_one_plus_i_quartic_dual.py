#!/usr/bin/env python3
"""Verify Goal4BM: ramified one-plus-i quartic dual and complete lambda^7 ray coordinates."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bm-ramified-one-plus-i-quartic-dual.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bm-ramified-one-plus-i-quartic-dual-source-lock.md")
BL = P("stages/stage35-ex/35ex-35/goal4bl-xi-two-adic-ray-class-parity.json")
BJ = P("stages/stage35-ex/35ex-35/goal4bj-global-gaussian-k2-quartic-character-adapter.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "6aa351a29002286f379e774101c5f30626424f63db2075c9db9ac0a29d57b8ec"
SRC_BLOB = "c0ef723f25770607f7d439c028bb844a4b804ea4"
ART_BLOB = "0a2f0760752fa28785aca36fa33a6d624834a931"
BL_BLOB = "14afdead8287398f76d8b5dff481dd1eea839ae1"
BJ_BLOB = "b8a20fd879a80215e9fa3fa8094bf979565de3c8"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


def primary(a: int, b: int) -> bool:
    return a % 2 != 0 and b % 2 == 0 and (a + b - 1) % 4 == 0


def e_i(a: int, b: int) -> int:
    return ((1 - a) // 2) % 4


def e_lambda(a: int, b: int) -> int:
    n = a - b - b * b - 1
    assert n % 4 == 0
    return (n // 4) % 4


def vlambda(a: int, b: int) -> int:
    """v_{1+i}(a+b*i) for nonzero Gaussian integer."""
    assert not (a == 0 and b == 0)
    v = 0
    while (a - b) % 2 == 0:
        a, b = (a + b) // 2, (b - a) // 2
        v += 1
    return v


def legendre(a: int, p: int) -> int:
    z = pow(a % p, (p - 1) // 2, p)
    return -1 if z == p - 1 else z


assert blob(SRC) == SRC_BLOB
assert blob(ART) == ART_BLOB
assert blob(BL) == BL_BLOB
assert blob(BJ) == BJ_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bl = json.loads(BL.read_text())
assert bl["canonical_sha256"] == "c8121ba4b36cbc27c418dd7651f32849044833bed375fa62fa6e0ae757515bc3"
assert bl["result"]["fixed_i_character_descends_to_norm_mod16_on_primary"] is True
assert bl["next"]["unit"] == "35EX-35_GOAL4BM_RAMIFIED_ONE_PLUS_I_QUARTIC_DUAL_PREFLIGHT"

bj = json.loads(BJ.read_text())
assert bj["canonical_sha256"] == "a1208a9ac7ec291074a36fe4d795e13b31eee22653fa83bcdef3b7eae120ac4e"
assert bj["result"]["global_gaussian_orientation_carrier_constructed"] is True

src = SRC.read_text()
for marker in (
    "(BM-chi-i)",
    "(BM-chi-lambda)",
    "(BM-lambda6-witness)",
    "(BM-ray-bijection)",
    "(BM-Xi-lambda)",
    "(BM-41)",
    "(BM-17)",
    "(BM-order2-class)",
    "(BM-boundary)",
    "35EX-35_GOAL4BN_COMMON_W_PRIMARY_SPACE_ROOT_RAY_PRODUCT_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bm_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bl"]["blob_sha1"] == BL_BLOB
assert art["source_locks"]["goal4bj"]["blob_sha1"] == BJ_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "08911659889e93ce242bee3491b6555a5a16b6ab"
assert parent["aggregate_run"] == 34315466300
assert parent["aggregate_job"] == 102351543882
assert parent["hostile_audited"] is False

assert primary(1, 0) and primary(-7, 0)
assert vlambda(-8, 0) == 6
assert e_i(1, 0) == e_i(-7, 0) == 0
assert (1 * 1) % 16 == ((-7) ** 2) % 16 == 1
assert e_lambda(1, 0) == 0
assert e_lambda(-7, 0) == 2

pairs = []
for A in (1, 3, 5, 7):
    Bs = (0, 4, 8, 12) if A in (1, 5) else (2, 6, 10, 14)
    for B in Bs:
        assert primary(A, B)
        pairs.append((e_i(A, B), e_lambda(A, B)))
assert len(pairs) == 16
assert set(pairs) == {(u, v) for u in range(4) for v in range(4)}

for A in range(1, 16, 2):
    for B in range(0, 16, 2):
        if primary(A, B):
            assert e_i(A, B) == e_i(A + 8, B + 8)
            assert e_lambda(A, B) == e_lambda(A + 8, B + 8)

for A, B, norm, ei0, el0 in (
    (5, 4, 41, 2, 0),
    (5, -4, 41, 2, 2),
    (1, 4, 17, 0, 3),
    (1, -4, 17, 0, 1),
):
    assert primary(A, B)
    assert A * A + B * B == norm
    assert e_i(A, B) == ei0
    assert e_lambda(A, B) == el0

for ell, roots in ((41, (9, -9)), (17, (4, -4))):
    for b in roots:
        assert (b * b + 1) % ell == 0
        assert legendre(2 * b, ell) == 1

g = (2, 0)
assert tuple((-x) % 4 for x in g) == g
assert any(g)
assert tuple((2 * x) % 4 for x in g) == (0, 0)
for u in range(4):
    for v in range(4):
        e = (u * g[0] + v * g[1]) % 4
        assert e in (0, 2)
        assert (-e) % 4 == e

ray = art["primary_lambda7_ray_group"]
assert ray["ray_class_count"] == 16
assert ray["character_pair_bijective"] is True
assert ray["abstract_group"] == "(Z/4Z)^2"

blind = art["order_two_blind_class"]
assert blind["ray_coordinates"] == [2, 0]
assert blind["order"] == 2
assert blind["locally_compatible"] is True
assert blind["all_characters_conductor_dividing_lambda7_orientation_blind_here"] is True

res = art["result"]
assert res["one_plus_i_supplementary_character_exact"] is True
assert res["lambda7_sufficient_for_ramified_character"] is True
assert res["lambda6_insufficient"] is True
assert res["primary_lambda7_ray_class_count"] == 16
assert res["chi_i_chi_lambda_pair_bijective_on_primary_lambda7_ray_group"] is True
assert res["chi_lambda_not_norm_only"] is True
assert res["order_two_ray_class_locally_compatible"] is True
assert res["all_conductor_lambda7_characters_universal_sigma_detector"] is False
assert res["global_reciprocity_contradiction_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BN_COMMON_W_PRIMARY_SPACE_ROOT_RAY_PRODUCT_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BM_RAMIFIED_ONE_PLUS_I_QUARTIC_DUAL=PASS")
print("primary_lambda7_ray_classes=16")
print("chi_i_chi_lambda_pair_bijective=true")
print("order_two_blind_class=(2,0)")
print("universal_sigma_detector=false")
print("canonical_sha256=" + EXPECTED)
