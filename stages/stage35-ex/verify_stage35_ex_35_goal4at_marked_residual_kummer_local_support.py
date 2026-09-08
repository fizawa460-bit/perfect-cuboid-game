#!/usr/bin/env python3
"""Verify Goal4AT: source recovery and marked residual Kummer gcd support."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4at-marked-residual-kummer-local-support.json")
SRC = P("stages/stage35-ex/35ex-35/goal4at-marked-residual-kummer-local-support-source-lock.md")
AS = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer.json")
F = P("stages/stage35-ex/35ex-35/goal4f-forced-prime-squareclass-parity-lift.json")
GCDSRC = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
PW01 = P("docs/arsenal/cards/provisional/S35-PW01.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "50778f7b5d65ffd5744916e26ef2545c2a1cef366cbf52b5bf72da92379b0141"
SRC_BLOB = "63a15adf45d03b8398b0991386d8a8f3834ce9f3"
AS_BLOB = "5f17e0ec3d325127b517ac2afb418ec4cb309868"
F_BLOB = "61760ef52c84f7202567cc3ca85245fa8c17e74c"
GCD_BLOB = "d0cd03a5ff744d5f6536b6d2784c0e0d543fea48"
PW01_BLOB = "2e92dc779ff6a8f3828c3a66ec2025a94dbe634d"
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
assert blob(AS) == AS_BLOB
assert blob(F) == F_BLOB
assert blob(GCDSRC) == GCD_BLOB
assert blob(PW01) == PW01_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

as_art = json.loads(AS.read_text())
assert as_art["canonical_sha256"] == "a17b7100e82c2fa81e4ca150384c7ebe3e076ed10ee3b28e9d26304afc987f29"
assert as_art["marked_kummer_derivation"]["kummer_shape"] == "delta(P)=([X],[X-1],[X+q^2])=(d,d,1)"
assert as_art["next"]["unit"] == "35EX-35_GOAL4AT_MARKED_RESIDUAL_KUMMER_SQUARECLASS_LOCAL_SUPPORT_PREFLIGHT"

f = json.loads(F.read_text())
inj = f["arbitrary_nonforced_prime_injection"]
assert inj["statement"] == "for every odd prime q other than 3 and 5, and every m>=1, (A,B,C)=(q^m,3,4) is a full Q_q-local four-square endpoint"
assert inj["global_existence_not_claimed"] is True

gcdsrc = json.loads(GCDSRC.read_text())
assert gcdsrc["population"]["A_B_C"] == "positive integers with gcd(A,B,C)=1"
assert gcdsrc["goal2_primitive_parity_coprimality_dictionary"]["edge_parity_theorem"] == "exactly one of A,B,C is odd; the two even edges are divisible by 4"

pw = PW01.read_text()
assert "PARAMETRIC_SQUARECLASS_COMPATIBILITY_GRAPH" in pw
assert "permit the reservoirs to remain parameter-dependent and of non-fixed prime support" in pw
assert "DO_NOT_USE_FOR=fixed finite squareclass enumeration" in pw

# Exact symbolic replay on the primitive endpoint equations.
A, B, C, Dab, Dac, Dbc, W = sp.symbols("A B C D_AB D_AC D_BC W", nonzero=True)
p = -B/C
q = (p**2 - 1)/(2*p)
hq = (p**2 + 1)/(2*p)
c = (p**2 - 1)/(2*p**2)
z = Dab/Dac
Xraw = sp.factor(sp.together(c*(z-p)/(z+1/p)))

assert sp.factor(sp.together(q - (C**2-B**2)/(2*B*C))) == 0
assert sp.factor(sp.together(hq + (B**2+C**2)/(2*B*C))) == 0
assert sp.factor(sp.together(c - (B**2-C**2)/(2*B**2))) == 0

# The rationalization identity needed for AT-1.
rat = sp.expand((B**2-C**2)*(A**2+B**2+C**2) - (B*Dab-C*Dac)*(B*Dab+C*Dac))
rat = rat.subs(Dab**2, A**2+B**2).subs(Dac**2, A**2+C**2)
assert sp.expand(rat) == 0

Xsrc = (C*Dab+B*Dac)*(B*Dab+C*Dac)/(2*B*C*W**2)
# Cross-multiplied Xraw = Xsrc modulo the four endpoint square equations.
endpoint_ideal = sp.groebner(
    [
        Dab**2-A**2-B**2,
        Dac**2-A**2-C**2,
        Dbc**2-B**2-C**2,
        W**2-A**2-B**2-C**2,
    ],
    Dab, Dac, Dbc, W, A, B, C,
    order="lex",
)
cross = sp.together(Xraw-Xsrc).as_numer_denom()[0]
assert sp.factor(endpoint_ideal.reduce(sp.expand(cross))[1]) == 0

Nminus = Dab*Dac-B*C
Nplus = Dab*Dac+B*C
Xm1 = Dbc**2*Nminus/(2*B*C*W**2)
# AT-2 after clearing the common denominator.
at2 = sp.expand((C*Dab+B*Dac)*(B*Dab+C*Dac) - 2*B*C*W**2 - Dbc**2*Nminus)
rels = {
    W**2: A**2+B**2+C**2,
    Dbc**2: B**2+C**2,
    Dab**2: A**2+B**2,
    Dac**2: A**2+C**2,
}
for old, new in rels.items():
    at2 = sp.expand(at2).subs(old, new)
assert sp.factor(sp.expand(at2)) == 0

# AT-4 complementary-factor square identity.
at4 = sp.expand(Nminus*Nplus - A**2*W**2).subs(W**2, A**2+B**2+C**2)
at4 = sp.expand(at4).subs(Dab**2, A**2+B**2).subs(Dac**2, A**2+C**2)
assert sp.factor(sp.expand(at4)) == 0
assert sp.expand(Nplus-Nminus-2*B*C) == 0

# Elementary integer gcd-square lemma used in AT-6.
def gcd_square_strip(nm: int, np: int) -> tuple[int, int, int]:
    import math
    g = math.gcd(nm, np)
    r0, s0 = nm // g, np // g
    assert math.gcd(r0, s0) == 1
    rr, ss = math.isqrt(r0), math.isqrt(s0)
    assert rr*rr == r0 and ss*ss == s0
    return g, rr, ss

for g0, r, s in ((1, 3, 5), (6, 5, 7), (35, 2, 9), (22, 7, 11)):
    nm, np = g0*r*r, g0*s*s
    g, rr, ss = gcd_square_strip(nm, np)
    assert (g, rr, ss) == (g0, r, s)
    assert g0 * (s*s-r*r) == np-nm

# Goal4F local relabeling: at ell != 3,5, N_± are ell-adic units
# because D_AB = +/-3 mod ell and D_AC = 5.
for ell in (7, 11, 13, 17, 19, 23, 29, 31):
    assert 15 % ell != 0
    for sign in (1, -1):
        assert (5*(sign*3)) % ell != 0
    # with B=ell^m and C=4, v_ell(2BC)=m while v_ell(G)=0.

src = SRC.read_text()
for marker in (
    "(AT-1)",
    "(AT-2)",
    "(AT-3)",
    "(AT-4)",
    "(AT-6)",
    "(AT-KUMMER-GCD)",
    "d = [G/(2*B*C)] = [(2*B*C)/G]",
    "odd and ell not dividing B*C",
    "GOAL4AT_ONE_GCD_RESERVOIR_REDUCTION=true",
    "FIXED_FINITE_GLOBAL_SQUARECLASS_FAMILY_PROVED=false",
    "35EX-35_GOAL4AU_MARKED_KUMMER_GCD_RESERVOIR_PRIME_ALLOCATION_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4at_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4as"]["blob_sha1"] == AS_BLOB
assert art["source_locks"]["goal4f"]["blob_sha1"] == F_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == GCD_BLOB
assert art["source_locks"]["s35_pw01"]["blob_sha1"] == PW01_BLOB

rec = art["source_recovery"]
assert rec["d_formula"] == "[(D_AB*D_AC-B*C)/(2*B*C)]"
assert rec["d_positive"] is True
assert rec["minus_one_squareclass_support"] is False

gr = art["gcd_reservoir"]
assert gr["G_divides_2BC"] is True
assert gr["square_quotients"] is True
assert gr["kummer_gcd_formula"] == "d=[G/(2*B*C)]=[(2*B*C)/G]"

ls = art["local_support"]
assert ls["outside_BC_odd_valuation_even"] is True
assert ls["fixed_constant_prime_support_obtained"] is False

ln = art["local_nonfiniteness_test"]
assert ln["odd_m_puts_ell_in_local_d"] is True
assert ln["global_endpoint_existence_claimed"] is False
assert ln["global_unbounded_support_claimed"] is False

res = art["result"]
assert res["one_gcd_reservoir_reduction_obtained"] is True
assert res["odd_support_subset_BC_obtained"] is True
assert res["arbitrary_nonforced_odd_prime_local_entry_obtained"] is True
assert res["d_trivial_proved"] is False
assert res["fixed_finite_global_squareclass_family_proved"] is False
assert res["new_global_obstruction_obtained"] is False

assert art["next"]["unit"] == "35EX-35_GOAL4AU_MARKED_KUMMER_GCD_RESERVOIR_PRIME_ALLOCATION_PREFLIGHT"

fw = art["credit_firewall"]
for key in (
    "goal4as_hostile_audited",
    "goal4at_hostile_audited",
    "d_trivial_proved",
    "global_d_nontrivial_proved",
    "finite_squareclass_family_proved",
    "two_selmer_group_computed",
    "two_divisibility_proved",
    "infinite_descent_proved",
    "brauer_manin_obstruction_obtained",
    "E1_proved",
    "R29_PESCH_E1_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert fw[key] is False, key

print("STAGE35_EX_GOAL4AT_MARKED_RESIDUAL_KUMMER_LOCAL_SUPPORT=PASS")
print("d_squareclass=[(2BC)/G]")
print("odd_support_subset=BC")
print("route_status=PASS_SHARPENED_LIVE_GATE_ONE_DYNAMIC_GCD_RESERVOIR")
print("canonical_sha256=" + EXPECTED)
