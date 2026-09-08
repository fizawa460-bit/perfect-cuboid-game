#!/usr/bin/env python3
"""Verify Goal4AU: three-direction marked Kummer gcd allocation and product-one coupling."""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
SRC = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation-source-lock.md")
AT = P("stages/stage35-ex/35ex-35/goal4at-marked-residual-kummer-local-support.json")
GCDSRC = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
J = P("stages/stage35-ex/35ex-35/goal4j-linked-congruent-number-selmer-coupling-preflight.json")
PW01 = P("docs/arsenal/cards/provisional/S35-PW01.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "4d23730b7ec3a2d5b1986d270924c2c34a5019cabd5171ddc1552055bf0971b2"
SRC_BLOB = "773b104c65454ae307bb59e87a15c74f505fdcbf"
AT_BLOB = "3e6949c18b044e38632ba840c3cb7b45b7e62302"
GCD_BLOB = "d0cd03a5ff744d5f6536b6d2784c0e0d543fea48"
J_BLOB = "f74b4bfb3128ada4312255371e35d3473744cb13"
PW01_BLOB = "2e92dc779ff6a8f3828c3a66ec2025a94dbe634d"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"
PARENT_HEAD = "f499b3e8b4f3e723b1046e2eff0e9f8ac3be24a5"
PARENT_RUN = 34291537497
PARENT_JOB = 102280319029

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)

assert blob(SRC) == SRC_BLOB
assert blob(AT) == AT_BLOB
assert blob(GCDSRC) == GCD_BLOB
assert blob(J) == J_BLOB
assert blob(PW01) == PW01_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

at = json.loads(AT.read_text())
assert at["canonical_sha256"] == "50778f7b5d65ffd5744916e26ef2545c2a1cef366cbf52b5bf72da92379b0141"
assert at["gcd_reservoir"]["kummer_gcd_formula"] == "d=[G/(2*B*C)]=[(2*B*C)/G]"
assert at["next"]["unit"] == "35EX-35_GOAL4AU_MARKED_KUMMER_GCD_RESERVOIR_PRIME_ALLOCATION_PREFLIGHT"

gcdsrc = json.loads(GCDSRC.read_text())
assert gcdsrc["goal2_primitive_parity_coprimality_dictionary"]["edge_parity_theorem"] == "exactly one of A,B,C is odd; the two even edges are divisible by 4"
assert len(gcdsrc["goal2_primitive_parity_coprimality_dictionary"]["branches"]) == 3

j = json.loads(J.read_text())
assert j["three_face_twists"]["squareclass_relation"] == "[N_AB]*[N_AC]*[N_BC]=[2] in Q*/Q*2"
assert j["selmer_coupling_verdict"]["cross_twist_selmer_pruning_obtained"] is False
assert "no source-locked inter-twist isogeny" in j["selmer_coupling_verdict"]["reason"]

pw = PW01.read_text()
assert "PARAMETRIC_SQUARECLASS_COMPATIBILITY_GRAPH" in pw
assert "DO_NOT_USE_FOR=fixed finite squareclass enumeration" in pw

# Exact symbolic replay of the three complementary-product identities AU-2.
x, y, z, a, b, c, rab, rac, rbc, W = sp.symbols(
    "x y z a b c r_AB r_AC r_BC W", nonzero=True
)
face_subs = {
    rab**2: y**2*a**2 + z**2*b**2,
    rac**2: x**2*a**2 + z**2*c**2,
    rbc**2: x**2*b**2 + y**2*c**2,
    W**2: x**2*y**2*a**2 + x**2*z**2*b**2 + y**2*z**2*c**2,
}
checks = [
    (rab*rac-z**2*b*c)*(rab*rac+z**2*b*c) - a**2*W**2,
    (rab*rbc-y**2*a*c)*(rab*rbc+y**2*a*c) - b**2*W**2,
    (rac*rbc-x**2*a*b)*(rac*rbc+x**2*a*b) - c**2*W**2,
]
for expr in checks:
    rem = sp.expand(expr).subs(face_subs)
    rem = sp.expand(rem).subs(face_subs)
    assert sp.factor(sp.expand(rem)) == 0

# AU-1 is literal extraction of the pair-gcd factors.
Dab, Dac, Dbc, A, B, C = sp.symbols("D_AB D_AC D_BC A B C", nonzero=True)
assert sp.expand((x*rab)*(y*rac) - (x*z*b)*(y*z*c) - x*y*(rab*rac-z**2*b*c)) == 0
assert sp.expand((x*rab)*(z*rbc) - (x*y*a)*(y*z*c) - x*z*(rab*rbc-y**2*a*c)) == 0
assert sp.expand((y*rac)*(z*rbc) - (x*y*a)*(x*z*b) - y*z*(rac*rbc-x**2*a*b)) == 0

# Exhaust the six parity subcases retained by the primitive dictionary.
# 1=odd, 0=even for (x,y,z,a,b,c).
parity_cases = [
    (1,1,0,1,1,0), (1,1,0,1,0,1),  # A odd
    (1,0,1,1,1,0), (1,0,1,0,1,1),  # B odd
    (0,1,1,1,0,1), (0,1,1,0,1,1),  # C odd
]
for xp, yp, zp, ap, bp, cp in parity_cases:
    epsA = 2 if (zp and bp and cp) else 1
    epsB = 2 if (yp and ap and cp) else 1
    epsC = 2 if (xp and ap and bp) else 1
    assert sorted((epsA, epsB, epsC)) == [1,1,2]
    assert epsA*epsB*epsC == 2
    kA, kB, kC = 2//epsA, 2//epsB, 2//epsC
    assert sorted((kA,kB,kC)) == [1,2,2]
    assert kA*kB*kC == 4

# The F2 linear graph has rank two and diagonal kernel.
M = ((0,1,1),(1,0,1),(1,1,0))
def mv(v):
    return tuple(sum(row[i]*v[i] for i in range(3)) % 2 for row in M)
kernel = [v for v in itertools.product((0,1), repeat=3) if mv(v) == (0,0,0)]
assert kernel == [(0,0,0),(1,1,1)]
# Three rows span four vectors -> rank 2.
image = {mv(v) for v in itertools.product((0,1), repeat=3)}
assert len(image) == 4

# Literal AU-6/AU-7 algebra after gcd allocation.
ha, hb, hc, epsA, epsB, epsC = sp.symbols("h_a h_b h_c eps_A eps_B eps_C", nonzero=True)
a0, b0, c0, kA, kB, kC = sp.symbols("a0 b0 c0 k_A k_B k_C", nonzero=True)
GA = x*y*epsA*hb*hc
GB = x*z*epsB*ha*hc
GC = y*z*epsC*ha*hb
Bedge = x*z*b
Cedge = y*z*c
Aedge = x*y*a
KA = sp.factor(2*Bedge*Cedge/GA)
KB = sp.factor(2*Aedge*Cedge/GB)
KC = sp.factor(2*Aedge*Bedge/GC)
assert sp.factor(KA.subs({b:hb*b0,c:hc*c0,epsA:2/kA}) - z**2*kA*b0*c0) == 0
assert sp.factor(KB.subs({a:ha*a0,c:hc*c0,epsB:2/kB}) - y**2*kB*a0*c0) == 0
assert sp.factor(KC.subs({a:ha*a0,b:hb*b0,epsC:2/kC}) - x**2*kC*a0*b0) == 0
prod = (z**2*kA*b0*c0)*(y**2*kB*a0*c0)*(x**2*kC*a0*b0)
assert sp.factor(prod.subs(kA*kB*kC, 4) - (2*x*y*z*a0*b0*c0)**2) == 0

# In squareclass coordinates every reservoir appears twice; exactly two kappa_i contribute [2].
for two_index in range(3):
    kappas = [1,1,1]  # bit 1 means squareclass [2]
    kappas[two_index] = 0  # epsilon=2 -> kappa=[1]
    for av,bv,cv in itertools.product((0,1), repeat=3):
        dA = (kappas[0] + bv + cv) % 2
        dB = (kappas[1] + av + cv) % 2
        dC = (kappas[2] + av + bv) % 2
        assert (dA+dB+dC) % 2 == 0

src = SRC.read_text()
for marker in (
    "(AU-1)", "(AU-2)", "(AU-3)", "(AU-4)", "(AU-5)",
    "(AU-6)", "(AU-7)", "(AU-KUMMER)", "(AU-CROSS)",
    "d_A*d_B*d_C = 1 in Q*/Q*^2",
    "GOAL4AU_CROSS_FACE_MARKED_KUMMER_PRODUCT_ONE=true",
    "GOAL4AU_NEW_BRANCH_PRUNING=false",
    "35EX-35_GOAL4AV_CROSS_FACE_MARKED_KUMMER_COMMON_COVER_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["stacked_parent"]["exact_head_sha"] == PARENT_HEAD
assert art["stacked_parent"]["aggregate_run"] == PARENT_RUN
assert art["stacked_parent"]["aggregate_job"] == PARENT_JOB
assert art["source_locks"]["goal4au_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4at"]["blob_sha1"] == AT_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == GCD_BLOB
assert art["source_locks"]["goal4j"]["blob_sha1"] == J_BLOB
assert art["source_locks"]["s35_pw01"]["blob_sha1"] == PW01_BLOB

assert art["two_adic_allocation"]["exactly_one_epsilon_equals_2"] is True
assert art["two_adic_allocation"]["epsilon_product"] == 2
assert art["marked_kummer_graph"]["linear_rank_F2"] == 2
assert art["marked_kummer_graph"]["linear_kernel"] == [[0,0,0],[1,1,1]]
assert art["cross_face_relation"]["marked_product"] == "d_A*d_B*d_C=1 in Q*/Q*^2"
assert art["cross_face_relation"]["new_branch_pruning_obtained"] is False
assert art["literal_representatives"]["k_product"] == 4
assert art["literal_representatives"]["exact_product_square"] == "K_A*K_B*K_C=(2*x*y*z*a0*b0*c0)^2"
assert art["next"]["unit"] == "35EX-35_GOAL4AV_CROSS_FACE_MARKED_KUMMER_COMMON_COVER_PREFLIGHT"

fw = art["credit_firewall"]
for key in (
    "goal4at_hostile_audited", "goal4au_hostile_audited",
    "any_global_d_i_trivial_proved", "any_global_d_i_nontrivial_proved",
    "finite_squareclass_family_proved", "common_two_cover_constructed",
    "common_selmer_complex_constructed", "cassels_pairing_obstruction_obtained",
    "two_divisibility_proved", "infinite_descent_proved",
    "brauer_manin_obstruction_obtained", "E1_proved", "R29_PESCH_E1_closed",
    "stage35_closed", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
):
    assert fw[key] is False, key

print("STAGE35_EX_GOAL4AU_THREE_DIRECTION_MARKED_KUMMER=PASS")
print("marked_product=d_A*d_B*d_C=1")
print("literal_product=K_A*K_B*K_C=square")
print("branch_pruning=false")
print("canonical_sha256=" + EXPECTED)
