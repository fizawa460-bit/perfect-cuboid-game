#!/usr/bin/env python3
"""Verify Goal4AV: common coefficient torsor package and non-pruning boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4av-cross-face-marked-kummer-common-cover.json")
SRC = P("stages/stage35-ex/35ex-35/goal4av-cross-face-marked-kummer-common-cover-source-lock.md")
AU = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
AS_SRC = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer-source-lock.md")
J = P("stages/stage35-ex/35ex-35/goal4j-linked-congruent-number-selmer-coupling-preflight.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "fcae350aa2144919750d26a65045e0dda7b917137ccc196faee19ae819abe3dd"
SRC_BLOB = "deb6c970bec58f3b858c855c394a2d4c84e76f3b"
AU_BLOB = "d0dd0597046daf54ad9fcc74991221710a27f12c"
AS_SRC_BLOB = "d9e249b42fd2c0f446c3513b9f085d5f6d97d581"
J_BLOB = "f74b4bfb3128ada4312255371e35d3473744cb13"
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
assert blob(AU) == AU_BLOB
assert blob(AS_SRC) == AS_SRC_BLOB
assert blob(J) == J_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

au = json.loads(AU.read_text())
assert au["canonical_sha256"] == "4d23730b7ec3a2d5b1986d270924c2c34a5019cabd5171ddc1552055bf0971b2"
assert au["cross_face_relation"]["marked_product"] == "d_A*d_B*d_C=1 in Q*/Q*^2"
assert au["result"]["common_two_cover_constructed"] is False
assert au["next"]["unit"] == "35EX-35_GOAL4AV_CROSS_FACE_MARKED_KUMMER_COMMON_COVER_PREFLIGHT"

as_src = AS_SRC.read_text()
assert "delta(P) = ([X],[X-1],[X+q^2]) = (d,d,1)" in as_src
assert "E1: y^2=x^3+(4*q^2+2)*x^2+x" in as_src
assert "unmarked existence statement" in as_src

j = json.loads(J.read_text())
assert j["selmer_coupling_verdict"]["cross_twist_selmer_pruning_obtained"] is False
assert j["selmer_coupling_verdict"]["same_j_invariant_is_not_a_coupling_theorem"] is True

# Exact literal representative replay from Goal4AU.
x, y, z, a0, b0, c0 = sp.symbols("x y z a0 b0 c0", nonzero=True)
kA, kB, kC = sp.symbols("k_A k_B k_C", nonzero=True)
KA = z**2 * kA * b0 * c0
KB = y**2 * kB * a0 * c0
KC = x**2 * kC * a0 * b0
S = 2*x*y*z*a0*b0*c0
prod_ratio = sp.factor(KA*KB*KC / S**2)
assert prod_ratio == kA*kB*kC/4

# Exactly two k_i are 2 and one is 1; all three cases give the exact square product.
patterns = [(1,2,2),(2,1,2),(2,2,1)]
for pA,pB,pC in patterns:
    assert pA*pB*pC == 4
    assert sp.factor((KA*KB*KC-S**2).subs({kA:pA,kB:pB,kC:pC})) == 0

# Fiber-product reconstruction: on tA^2=KA and tB^2=KB, tC=S/(tA*tB)
# has tC^2=KC whenever KA*KB*KC=S^2.
tA,tB = sp.symbols("t_A t_B", nonzero=True)
tC2_minus_KC = sp.together((S/(tA*tB))**2-KC)
num = sp.expand(tC2_minus_KC.as_numer_denom()[0])
num = num.subs(tA**2, KA).subs(tB**2, KB)
# Substitute k-product=4 via each exact parity pattern.
for pA,pB,pC in patterns:
    rem = sp.factor(sp.expand(num).subs({kA:pA,kB:pB,kC:pC}))
    assert rem == 0

# The rank-two squareclass relation is formally non-pruning.
# Per prime, u,v are arbitrary bits and the third is u+v.
triples = {(u,v,u^v) for u in (0,1) for v in (0,1)}
assert triples == {(0,0,0),(0,1,1),(1,0,1),(1,1,0)}
assert any(t != (0,0,0) for t in triples)
assert all((a ^ b ^ c) == 0 for a,b,c in triples)

src = SRC.read_text()
for marker in (
    "(AV-1)",
    "(AV-3)",
    "(AV-4)",
    "(AV-5)",
    "(AV-6)",
    "COMMON_COEFFICIENT_BIQUADRATIC_PACKAGE=true",
    "COMMON_ENDPOINT_FAMILY_2COVER_CONSTRUCTED=false",
    "BLOCKED_NONPRUNING_COEFFICIENT_TORSOR_SHADOW",
    "GOAL4AV_COMMON_MU2_COEFFICIENT_COUPLING=true",
    "GOAL4AV_NEW_BRANCH_PRUNING=false",
    "35EX-35_GOAL4AW_MARKED_ELLIPTIC_HEIGHT_LOWER_VS_GOAL4M_UPPER_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4av_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4au"]["blob_sha1"] == AU_BLOB
assert art["source_locks"]["goal4as_source"]["blob_sha1"] == AS_SRC_BLOB
assert art["source_locks"]["goal4j"]["blob_sha1"] == J_BLOB

cc = art["coefficient_cohomology"]
assert cc["sum_relation"] == "chi_A+chi_B+chi_C=0"
assert cc["target_E2_modules_identified"] is False
assert cc["local_selmer_conditions_identified"] is False

pkg = art["coefficient_torsor_package"]
assert pkg["common_biquadratic_coefficient_package"] is True
assert pkg["extension_degree_bound"] == 4
assert pkg["third_root"] == "t_C=S/(t_A*t_B)"

rb = art["rational_section_boundary"]
assert rb["physical_endpoint_requires_T_AB_Q_nonempty"] is False
assert rb["product_one_forces_any_d_i_trivial"] is False

fb = art["family_cover_boundary"]
assert fb["K_i_use_gcd_data"] is True
assert fb["K_i_are_source_locked_family_rational_functions"] is False
assert fb["common_endpoint_family_two_cover_constructed"] is False

cb = art["cassels_boundary"]
assert cb["three_curves_identified"] is False
assert cb["inter_curve_isogeny_constructed"] is False
assert cb["common_selmer_complex_constructed"] is False
assert cb["cassels_pairing_identity_constructed"] is False

res = art["result"]
assert res["common_mu2_coefficient_coupling_obtained"] is True
assert res["biquadratic_degree_at_most_four_obtained"] is True
assert res["common_endpoint_two_cover_constructed"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4AW_MARKED_ELLIPTIC_HEIGHT_LOWER_VS_GOAL4M_UPPER_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key,val)

print("STAGE35_EX_GOAL4AV_CROSS_FACE_MARKED_KUMMER_COMMON_COVER=PASS")
print("coefficient_package=BIQUADRATIC_DEGREE_AT_MOST_4")
print("endpoint_common_2cover=false")
print("branch_pruning=false")
print("canonical_sha256=" + EXPECTED)
