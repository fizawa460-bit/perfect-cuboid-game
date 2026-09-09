#!/usr/bin/env python3
"""Verify Goal4AW: explicit canonical-height lower-bound applicability and comparison blockers."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4aw-marked-elliptic-height-lower-vs-goal4m-upper.json")
SRC = P("stages/stage35-ex/35ex-35/goal4aw-marked-elliptic-height-lower-vs-goal4m-upper-source-lock.md")
AV = P("stages/stage35-ex/35ex-35/goal4av-cross-face-marked-kummer-common-cover.json")
L = P("stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json")
M = P("stages/stage35-ex/35ex-35/goal4m-stage14-global-triple-population-height-transfer.json")
AT = P("stages/stage35-ex/35ex-35/goal4at-marked-residual-kummer-local-support.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "0605861581bac2571889a58bfe2a7ef0f1f1e167372fc434d285187af1988488"
SRC_BLOB = "5c4ef04e5d064a3d92b5a8b8bbd46b93a1d82145"
AV_BLOB = "13f2e4c386d8cbe4b986171dc5eda9b7e38e9403"
L_BLOB = "0717ca307162d5559a005801848288daa91285fd"
M_BLOB = "1c7a3e9e23dd8bbc41fc331b8c43e4023f5d3909"
AT_BLOB = "3e6949c18b044e38632ba840c3cb7b45b7e62302"
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
assert blob(AV) == AV_BLOB
assert blob(L) == L_BLOB
assert blob(M) == M_BLOB
assert blob(AT) == AT_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

av = json.loads(AV.read_text())
assert av["canonical_sha256"] == "fcae350aa2144919750d26a65045e0dda7b917137ccc196faee19ae819abe3dd"
assert av["result"]["common_endpoint_two_cover_constructed"] is False
assert av["next"]["unit"] == "35EX-35_GOAL4AW_MARKED_ELLIPTIC_HEIGHT_LOWER_VS_GOAL4M_UPPER_PREFLIGHT"

l = json.loads(L.read_text())
assert l["birational_adapter"]["elliptic_curve"] == "E_q: Y^2=X*(X-1)*(X+q^2)"
assert l["torsion_exclusion_on_physical_endpoint"]["conclusion"] == "every physical endpoint maps to a non-torsion E_q(Q) point"

m = json.loads(M.read_text())
assert m["stage14_exact_inputs"]["physical_height_window"].endswith("this is O(log B)")
assert m["rankjump_height_interpretation"]["least_nontorsion_height_upper_bound_for_a_physical_hit"] == "lambda(E_q)<=O(log B)"
assert m["source_locks"]["stage14_s3"]["blob_sha"] == "830f124e3b22e47693eec101f407e7d402b437d9"
assert m["credit_boundary"]["finite_height_reduction_obtained"] is False

at = json.loads(AT.read_text())
assert at["source_recovery"]["q"] == "(C^2-B^2)/(2*B*C)"

# Exact invariant replay on the reduced Pythagorean integral model.
x, r, s, t = sp.symbols("x r s t", nonzero=True)
f = sp.expand(x*(x-s**2)*(x+r**2))
a2 = r**2-s**2
a4 = -r**2*s**2
b2 = 4*a2
b4 = 2*a4
b6 = 0
b8 = -a4**2
c4 = sp.factor(b2**2 - 24*b4)
Delta = sp.factor(-b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6)
assert sp.expand(c4 - 16*(r**4+r**2*s**2+s**4)) == 0
assert Delta == 16*r**4*s**4*(r**2+s**2)**2
assert sp.factor(Delta.subs(r**2+s**2, t**2) - 16*r**4*s**4*t**4) == 0
j = sp.factor(c4**3 / (16*r**4*s**4*t**4))
assert sp.factor(j - 256*(r**4+r**2*s**2+s**4)**3/(r**4*s**4*t**4)) == 0

# Odd-prime c4-unit residue identities used for minimality/multiplicative reduction.
R2, S2 = sp.symbols("R2 S2")
bracket = R2**2 + R2*S2 + S2**2
assert sp.expand(bracket.subs(R2, 0)) == S2**2
assert sp.expand(bracket.subs(S2, 0)) == R2**2
assert sp.expand(bracket.subs(R2, -S2)) == S2**2

src = SRC.read_text()
for marker in (
    "(AW-1)",
    "(AW-2)",
    "(AW-5)",
    "(AW-P)",
    "(AW-C1)",
    "(AW-C4)",
    "10^15 * sigma(E)^6 * log^2(104613*sigma(E)^2)",
    "EXPLICIT_GOAL4M_UPPER_COEFFICIENT_LOCKED=false",
    "UNIFORM_SZPIRO_RATIO_BOUND_PROVED=false",
    "BLOCKED_MISSING_UNIFORM_HEIGHT_DISCRIMINANT_SZPIRO_ADAPTERS",
    "35EX-35_GOAL4AX_CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4aw_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4av"]["blob_sha1"] == AV_BLOB
assert art["source_locks"]["goal4l"]["blob_sha1"] == L_BLOB
assert art["source_locks"]["goal4m"]["blob_sha1"] == M_BLOB
assert art["source_locks"]["goal4at"]["blob_sha1"] == AT_BLOB

ext = art["external_source"]
assert ext["author"] == "Clayton Petsche"
assert ext["arxiv"] == "math/0508160v2"
assert ext["theorem"] == "Theorem 2"
assert "10^15*sigma^6" in ext["q_specialization"]
assert ext["uniform_sigma_bound_in_theorem"] is False

ip = art["integral_pythagorean_model"]
assert ip["Delta_raw"] == "16*r^4*s^4*t^4"
assert ip["odd_prime_minimality"] == "for odd ell|r*s*t, c4 is an ell-adic unit"
assert ip["odd_conductor_exponent"] == "ord_ell(N_E)=1"
assert ip["two_adic_minimal_model_classified"] is False

req = art["comparison_requirements"]
assert req["C1_obtained"] is False
assert req["C2_obtained"] is False
assert req["C3_obtained"] is False
assert req["C4_obtained"] is False

res = art["result"]
assert res["physical_nontorsion_applicability_obtained"] is True
assert res["exact_integral_pythagorean_model_obtained"] is True
assert res["odd_prime_minimal_discriminant_conductor_adapter_obtained"] is True
assert res["petsche_explicit_lower_bound_source_locked"] is True
assert res["strict_lower_vs_upper_coefficient_win_obtained"] is False
assert res["eventual_endpoint_elimination_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4AX_CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4AW_MARKED_ELLIPTIC_HEIGHT_LOWER_VS_UPPER=PASS")
print("physical_nontorsion=true")
print("petsche_lower_bound=APPLICABLE")
print("comparison_status=BLOCKED_THREE_MISSING_ADAPTERS")
print("canonical_sha256=" + EXPECTED)
