#!/usr/bin/env python3
"""Verify Goal4BH: primewise face/space Gaussian orientation torsor."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bh-reservoir-leading-unit-space-face-sign-cycle-source-lock.md")
BG = P("stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility.json")
BG_SRC = P("stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility-source-lock.md")
BF = P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "33ccfe71c590b5f5515c44361bbf85558a1768827de88fb4e1c2f76c952b1a6b"
SRC_BLOB = "ca664fa4c7a66651115cff3c433ddc1fa8c04124"
BG_BLOB = "831e25e134e03659e555a2b0b0703c4fe53d36c4"
BG_SRC_BLOB = "659e4a08b9eec65f9a6e25f4aaa980b8472d3f09"
BF_BLOB = "b015280d80c958608bdbabd3a590c0bf482b25bc"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


assert blob(SRC) == SRC_BLOB
assert blob(BG) == BG_BLOB
assert blob(BG_SRC) == BG_SRC_BLOB
assert blob(BF) == BF_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bg = json.loads(BG.read_text())
assert bg["canonical_sha256"] == "6697be54daad10e65c247b63b79c3edd7085133e4b0a41f86f78ebf6551e0dc4"
assert bg["phase_result"]["new_secondary_sigma_bits_exposed"] is True
assert bg["phase_result"]["sigma_cycle_relation_obtained"] is False
assert bg["next"]["unit"] == "35EX-35_GOAL4BH_RESERVOIR_LEADING_UNIT_SPACE_FACE_SIGN_CYCLE_PREFLIGHT"

bf = json.loads(BF.read_text())
assert bf["result"]["cross_conjugate_phase_gauge_remains"] is True

src = SRC.read_text()
for marker in (
    "(BH-small)",
    "(BH-rlead)",
    "(BH-unequal)",
    "(BH-tie)",
    "(BH-sigma-explicit)",
    "(BH-orient)",
    "(BH-space-val)",
    "(BH-reduction)",
    "SIGMA_CYCLE_RELATION_OBTAINED=false",
    "35EX-35_GOAL4BI_SECONDARY_ORIENTATION_HILBERT_PRODUCT_FORMULA_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bh_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bg"]["blob_sha1"] == BG_BLOB
assert art["source_locks"]["goal4bg_source"]["blob_sha1"] == BG_SRC_BLOB
assert art["source_locks"]["goal4bf"]["blob_sha1"] == BF_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "0ad450e20e4ce74a3b69d1f91720bc50ef955de3"
assert parent["aggregate_run"] == 34309951404
assert parent["aggregate_job"] == 102335489958
assert parent["hostile_audited"] is False

hl = art["hensel_leading_unit"]["direction_A"]
assert hl["small_factor_valuation"] == "v_ell(u-I_a*v)=2*rho"
assert hl["leading_square"] == "(r_BC/ell^rho)^2=q_a*(u+I_a*v)"

so = art["secondary_orientation"]["direction_A"]
assert so["secondary_requires_tie"] == "alpha=rho=m"
assert so["unequal_valuation_implies"] == "ell does not divide W/h_a"
assert so["sigma_a"] == "lambda_a/iota_a in {+1,-1}"
assert "z*c*" in so["sigma_a_explicit"]

gm = art["gaussian_orientation_matching"]
assert "p_i" in gm["sigma_minus_one"]
assert "conjugate" in gm["sigma_plus_one"]
assert gm["primewise_mu2_orientation_bit"] is True

res = art["result"]
assert res["full_ell_adic_leading_unit_obtained"] is True
assert res["secondary_orientation_requires_valuation_tie"] is True
assert res["sigma_explicit_formula_obtained"] is True
assert res["sigma_equals_gaussian_prime_matching_bit"] is True
assert res["phase_problem_reduced_to_mu2_orientation_torsor"] is True
assert res["sigma_cycle_relation_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BI_SECONDARY_ORIENTATION_HILBERT_PRODUCT_FORMULA_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BH_FACE_SPACE_ORIENTATION_TORSOR=PASS")
print("hensel_leading_unit_exact=true")
print("sigma_is_gaussian_prime_matching_bit=true")
print("sigma_cycle_relation=false")
print("canonical_sha256=" + EXPECTED)
