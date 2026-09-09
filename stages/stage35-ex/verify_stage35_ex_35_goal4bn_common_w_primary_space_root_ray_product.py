#!/usr/bin/env python3
"""Verify Goal4BN: common-W space-root ray product and 41-adic order-two secondary witness."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bn-common-w-primary-space-root-ray-product.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bn-common-w-primary-space-root-ray-product-source-lock.md")
BM = P("stages/stage35-ex/35ex-35/goal4bm-ramified-one-plus-i-quartic-dual.json")
BG = P("stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility.json")
BH = P("stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "cb5d180ad3a42762426f9e8a7792600b5a2e43a03f1bb77e07ed20938f277e3a"
SRC_BLOB = "5ecd2b23b4139d4b6633fdea76329adbd0bb5f43"
ART_BLOB = "7da460f1e2d7f3a68a5b093f0bc004155d775523"
BM_BLOB = "0a2f0760752fa28785aca36fa33a6d624834a931"
BG_BLOB = "831e25e134e03659e555a2b0b0703c4fe53d36c4"
BH_BLOB = "80534af2bc071cbc3a2d6426c495cd3d5e6dbefc"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


def vp(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def e_i(a: int, b: int) -> int:
    return ((1 - a) // 2) % 4


def e_lambda(a: int, b: int) -> int:
    n = a - b - b * b - 1
    assert n % 4 == 0
    return (n // 4) % 4


assert blob(SRC) == SRC_BLOB
assert blob(ART) == ART_BLOB
assert blob(BM) == BM_BLOB
assert blob(BG) == BG_BLOB
assert blob(BH) == BH_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bm = json.loads(BM.read_text())
assert bm["canonical_sha256"] == "6aa351a29002286f379e774101c5f30626424f63db2075c9db9ac0a29d57b8ec"
assert bm["result"]["primary_lambda7_ray_class_count"] == 16
assert bm["result"]["order_two_ray_class_locally_compatible"] is True
assert bm["next"]["unit"] == "35EX-35_GOAL4BN_COMMON_W_PRIMARY_SPACE_ROOT_RAY_PRODUCT_PREFLIGHT"

bg = json.loads(BG.read_text())
assert bg["canonical_sha256"] == "6697be54daad10e65c247b63b79c3edd7085133e4b0a41f86f78ebf6551e0dc4"
assert bg["space_gaussian_squares"]["primary_square_roots_source_locked"] is True
assert bg["space_gcds"]["h_a_h_b_h_c_divide_W"] is True

bh = json.loads(BH.read_text())
assert bh["canonical_sha256"] == "33ccfe71c590b5f5515c44361bbf85558a1768827de88fb4e1c2f76c952b1a6b"
assert bh["result"]["secondary_orientation_requires_valuation_tie"] is True
assert bh["result"]["sigma_equals_gaussian_prime_matching_bit"] is True

src = SRC.read_text()
for marker in (
    "(BN-HT)",
    "(BN-Psi-norms)",
    "(BN-R)",
    "(BN-R-norm)",
    "(BN-R-ratio)",
    "(BN-fixed-i)",
    "(BN-pi41)",
    "(BN-41-data)",
    "(BN-mod41-4)",
    "(BN-secondary)",
    "(BN-both-sigma)",
    "(BN-boundary)",
    "35EX-35_GOAL4BO_DEEPER_LAMBDA8_ORDER_LIFT_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bn_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bm"]["blob_sha1"] == BM_BLOB
assert art["source_locks"]["goal4bg"]["blob_sha1"] == BG_BLOB
assert art["source_locks"]["goal4bh"]["blob_sha1"] == BH_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "a77e75db00874d66025d5924b95e4939b8b67500"
assert parent["aggregate_run"] == 34316754364
assert parent["aggregate_job"] == 102355710268
assert parent["hostile_audited"] is False

ha, hb, hc, T = 5, 13, 17, 29
Na = hb * hc * T
Nb = ha * hc * T
Nc = ha * hb * T
assert Nb * Nc == ha * ha * Na * T
assert Na * Nc == hb * hb * Nb * T
assert Na * Nb == hc * hc * Nc * T

cw = art["common_w_norms"]
assert cw["H_divides_W"] is True
assert cw["Psi_a_norm"] == "h_b*h_c*T"
assert cw["Psi_b_norm"] == "h_a*h_c*T"
assert cw["Psi_c_norm"] == "h_a*h_b*T"

rat = art["common_norm_ratios"]
assert rat["common_norm"] == "T"
assert rat["ratio_norm_one"] is True
assert rat["new_obstructive_value_obtained"] is False

ell, t = 41, 9
u, vp_lead, vm_lead, q = 80, 18, -18, 82
assert t * t + 1 == 2 * ell
assert u == t * t - 1
assert vp_lead == 2 * t and vm_lead == -2 * t
assert u * u + vp_lead * vp_lead == q * q
assert u * u + vm_lead * vm_lead == q * q

a = ell * u
r = ell * vp_lead
W = ell * q
assert a * a + r * r == W * W
assert vp(a, ell) == 1
assert vp(r, ell) == 1
assert vp(W, ell) == 2

cert = art["mod_41_power_certificate"]
M = cert["modulus"]
assert M == ell ** 4
a0 = cert["a"]
r0 = cert["r_BC"]
W0 = cert["W"]
b0 = cert["b"]
rab = cert["r_AB"]
rac = cert["r_AC"]
assert b0 % ell == 9
assert (b0 * b0 + 1 - r0 * r0) % M == 0
assert (rab * rab - a0 * a0 - b0 * b0) % M == 0
assert (rac * rac - a0 * a0 - 1) % M == 0
assert (W0 * W0 - a0 * a0 - r0 * r0) % M == 0
assert (W0 * W0 - rab * rab - 1) % M == 0
assert (W0 * W0 - rac * rac - b0 * b0) % M == 0

assert (5 + 4 * 9) % ell == 0
assert e_i(5, 4) == 2
assert e_lambda(5, 4) == 0
g = (2, 0)
assert tuple((-x) % 4 for x in g) == g

inv_u = pow(u % ell, -1, ell)
lam_plus = (vp_lead * inv_u) % ell
lam_minus = (vm_lead * inv_u) % ell
assert lam_plus == 32 == (-9) % ell
assert lam_minus == 9
assert art["local_41_model"]["sigma_plus_branch"]["sigma"] == -1
assert art["local_41_model"]["sigma_minus_branch"]["sigma"] == 1
assert art["local_41_model"]["same_selected_prime_both_sigma"] is True

res = art["result"]
assert res["common_W_cofactor_T_obtained"] is True
assert res["three_common_norm_ratios_obtained"] is True
assert res["ratio_source_norm_one_exact"] is True
assert res["full_41_adic_face_plus_space_model_obtained"] is True
assert res["order_two_pi_5_plus_4i_secondary_locally_compatible"] is True
assert res["both_sigma_signs_same_selected_pi_locally_compatible"] is True
assert res["common_W_forces_proper_lambda7_Xi_subset"] is False
assert res["order_two_ray_class_excluded"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BO_DEEPER_LAMBDA8_ORDER_LIFT_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BN_COMMON_W_PRIMARY_SPACE_ROOT_RAY_PRODUCT=PASS")
print("common_norm_Ra_Rb_Rc=T")
print("pi41_order_two_secondary=true")
print("same_selected_pi_both_sigma=true")
print("lambda7_ray_pruning=false")
print("canonical_sha256=" + EXPECTED)
