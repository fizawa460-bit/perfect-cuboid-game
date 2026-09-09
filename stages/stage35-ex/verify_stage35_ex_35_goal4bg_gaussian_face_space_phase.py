#!/usr/bin/env python3
"""Verify Goal4BG: Gaussian face/space square roots and the residual leading-unit phase gap."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bg-gaussian-square-root-face-phase-compatibility-source-lock.md")
BF = P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift.json")
BF_SRC = P("stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift-source-lock.md")
GCD = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "6697be54daad10e65c247b63b79c3edd7085133e4b0a41f86f78ebf6551e0dc4"
SRC_BLOB = "659e4a08b9eec65f9a6e25f4aaa980b8472d3f09"
BF_BLOB = "b015280d80c958608bdbabd3a590c0bf482b25bc"
BF_SRC_BLOB = "a54aa70b1a9e7b3a1f2a1b7daa77afcab1b4face"
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


assert blob(SRC) == SRC_BLOB
assert blob(BF) == BF_BLOB
assert blob(BF_SRC) == BF_SRC_BLOB
assert blob(GCD) == GCD_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bf = json.loads(BF.read_text())
assert bf["canonical_sha256"] == "73145db6fd0f1faa9622ccce183c06f09893ce3fe8497d65cb9f84df46fd799a"
assert bf["result"]["cross_conjugate_phase_gauge_remains"] is True
assert bf["next"]["unit"] == "35EX-35_GOAL4BG_GAUSSIAN_SQUARE_ROOT_FACE_PHASE_COMPATIBILITY_PREFLIGHT"

gcdj = json.loads(GCD.read_text())
assert gcdj["goal1_exact_decomposition"]["reconstruction"] == ["A=x*y*a", "B=x*z*b", "C=y*z*c"]
assert len(gcdj["goal2_primitive_parity_coprimality_dictionary"]["reduced_face_pairs"]) == 3
assert gcdj["goal3_exact_square_rewrite"]["space_equation"] == "W^2=(x*y*a)^2+(x*z*b)^2+(y*z*c)^2"

# Exact norm identities underlying the three face and three space Gaussian factors.
x,y,z,a,b,c,hab,hac,hbc,rab,rac,rbc,W = sp.symbols("x y z a b c h_a h_b h_c r_AB r_AC r_BC W", nonzero=True)
assert sp.expand((y*a)**2 + (z*b)**2 - rab**2) == (a**2*y**2 + b**2*z**2 - rab**2)
assert sp.expand((x*a)**2 + (z*c)**2 - rac**2) == (a**2*x**2 + c**2*z**2 - rac**2)
assert sp.expand((x*b)**2 + (y*c)**2 - rbc**2) == (b**2*x**2 + c**2*y**2 - rbc**2)
A=x*y*a; B=x*z*b; C=y*z*c
DAB=x*rab; DAC=y*rac; DBC=z*rbc
assert sp.factor((A/hab)**2 + (DBC/hab)**2 - W**2/hab**2) == (A**2 + DBC**2 - W**2)/hab**2
assert sp.factor((B/hac)**2 + (DAC/hac)**2 - W**2/hac**2) == (B**2 + DAC**2 - W**2)/hac**2
assert sp.factor((C/hbc)**2 + (DAB/hbc)**2 - W**2/hbc**2) == (C**2 + DAB**2 - W**2)/hbc**2

src = SRC.read_text()
for marker in (
    "(BG-FSQ)",
    "(BG-Sigma)",
    "(BG-gcd)",
    "(BG-SSQ)",
    "(BG-unequal)",
    "(BG-lambda-square)",
    "(BG-sigma)",
    "BF_CROSS_CONJUGATE_GAUGE_FIXED=false",
    "35EX-35_GOAL4BH_RESERVOIR_LEADING_UNIT_SPACE_FACE_SIGN_CYCLE_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4bg_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bf"]["blob_sha1"] == BF_BLOB
assert art["source_locks"]["goal4bf_source"]["blob_sha1"] == BF_SRC_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == GCD_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "ab134d4cd9d21efb9f90f89e3215e81caa3561e2"
assert parent["aggregate_run"] == 34306382710
assert parent["aggregate_job"] == 102324844711
assert parent["hostile_audited"] is False

fg = art["face_gaussian_squares"]
assert fg["primary_square_roots_source_locked"] is True
assert fg["conjugation_free_choice"] is False
assert art["oriented_kernel_embedding"]["Sigma_a_divides"] == "bar(Theta_BC)"
assert art["oriented_kernel_embedding"]["Sigma_b_divides"] == "bar(Theta_AC)"
assert art["oriented_kernel_embedding"]["Sigma_c_divides"] == "bar(Theta_AB)"

sg = art["space_gcds"]
assert sg["gcd_A_DBC"] == "h_a"
assert sg["gcd_B_DAC"] == "h_b"
assert sg["gcd_C_DAB"] == "h_c"
assert sg["h_a_h_b_h_c_divide_W"] is True
assert art["space_gaussian_squares"]["primary_square_roots_source_locked"] is True

rp = art["reservoir_prime_comparison"]
assert "no secondary space sqrt(-1) orientation" in rp["unequal_valuation_case"]
assert rp["lambda_A_square"] == "-1 mod ell"
assert rp["sigma_A"] == "lambda_A=sigma_A*iota_A, sigma_A in {+1,-1}"

res = art["phase_result"]
assert res["face_roots_fix_oriented_kernel_location"] is True
assert res["space_roots_fix_all_cross_conjugate_phases"] is False
assert res["new_secondary_sigma_bits_exposed"] is True
assert res["sigma_cycle_relation_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BH_RESERVOIR_LEADING_UNIT_SPACE_FACE_SIGN_CYCLE_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BG_GAUSSIAN_FACE_SPACE_PHASE=PASS")
print("six_gaussian_square_roots=true")
print("secondary_sigma_bits_exposed=true")
print("cross_conjugate_phase_gauge_fixed=false")
print("canonical_sha256=" + EXPECTED)
