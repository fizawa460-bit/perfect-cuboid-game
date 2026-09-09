#!/usr/bin/env python3
"""Verify Goal4AY: classical derived-cuboid involution and nonlinear descent boundary."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent-source-lock.md")
AX = P("stages/stage35-ex/35ex-35/goal4ax-cross-face-lattice-norm-torsor-compatibility.json")
AS = P("stages/stage35-ex/35ex-35/goal4as-fresh-exhaustive-view-marked-kummer.json")
I = P("stages/stage35-ex/35ex-35/goal4i-v2-infinite-descent-self-map-preflight.json")
L = P("stages/stage35-ex/35ex-35/goal4l-stage14-pythagorean-elliptic-rankjump-receiver.json")
AU = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
AV = P("stages/stage35-ex/35ex-35/goal4av-cross-face-marked-kummer-common-cover.json")
GCD = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "513e4085d1f5309a52580c3f716db0de6e549a07619351e4098e3b159766c41d"
SRC_BLOB = "a1c48a95f230ef42366f8152ac49d5ebdc4e54b3"
AX_BLOB = "208e153181185f9234f688f524432ae10579f5d4"
AS_BLOB = "5f17e0ec3d325127b517ac2afb418ec4cb309868"
I_BLOB = "d9121d2fdb9b202bc0ffc72678e74e9ccb5a87c2"
L_BLOB = "0717ca307162d5559a005801848288daa91285fd"
AU_BLOB = "d0dd0597046daf54ad9fcc74991221710a27f12c"
AV_BLOB = "13f2e4c386d8cbe4b986171dc5eda9b7e38e9403"
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


for path, expected in (
    (SRC, SRC_BLOB), (AX, AX_BLOB), (AS, AS_BLOB), (I, I_BLOB),
    (L, L_BLOB), (AU, AU_BLOB), (AV, AV_BLOB), (GCD, GCD_BLOB),
):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

ax = json.loads(AX.read_text())
assert ax["canonical_sha256"] == "586bbe7f7889ff9b6fe89756a66b9cf7aaaa4f7206d62afe3664e9ab62627c5d"
assert ax["result"]["positive_endpoint_open_reconstructed"] is True
assert ax["next"]["unit"] == "35EX-35_GOAL4AY_GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT_PREFLIGHT"

as_ = json.loads(AS.read_text())
assert "GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT" in as_["candidate_ledger"]["untested"]

i = json.loads(I.read_text())
assert i["descent_gate"]["common_scalar_two_descent"]["available"] is False
assert i["descent_gate"]["nonlinear_v2_self_map"]["source_locked_formula_available"] is False
assert i["result"]["genuine_nonlinear_v2_infinite_descent_constructed"] is False

l = json.loads(L.read_text())
assert l["credit_boundary"]["Goal4K_receiver_endpoint_equivalence_claimed"] is False

au = json.loads(AU.read_text())
assert au["cross_face_relation"]["marked_product"] == "d_A*d_B*d_C=1 in Q*/Q*^2"
assert au["result"]["new_branch_pruning_obtained"] is False

av = json.loads(AV.read_text())
assert av["canonical_sha256"] == "fcae350aa2144919750d26a65045e0dda7b917137ccc196faee19ae819abe3dd"
assert av["result"]["common_endpoint_two_cover_constructed"] is False

gcdj = json.loads(GCD.read_text())
assert gcdj["definitions"] == {
    "x":"gcd(A,B)", "y":"gcd(A,C)", "z":"gcd(B,C)",
    "a":"A/(x*y)", "b":"B/(x*z)", "c":"C/(y*z)"
}

# Symbolic three-face preservation of the pair-product construction.
A, B, C = sp.symbols("A B C")
assert sp.expand((A*B)**2 + (A*C)**2 - A**2*(B**2+C**2)) == 0
assert sp.expand((A*B)**2 + (B*C)**2 - B**2*(A**2+C**2)) == 0
assert sp.expand((A*C)**2 + (B*C)**2 - C**2*(A**2+B**2)) == 0

# Six-variable primitive reduction formulas and involution.
x,y,z,a,b,c = sp.symbols("x y z a b c", positive=True, integer=True)
A0=x*y*a; B0=x*z*b; C0=y*z*c
g=x*y*z
AD=sp.cancel(A0*B0/g); BD=sp.cancel(A0*C0/g); CD=sp.cancel(B0*C0/g)
assert sp.expand(AD-x*a*b) == 0
assert sp.expand(BD-y*a*c) == 0
assert sp.expand(CD-z*b*c) == 0
# Applying the dictionary swap a second time returns the original ordered edges.
A2=a*x*y; B2=b*x*z; C2=c*y*z
assert sp.expand(A2-A0) == 0
assert sp.expand(B2-B0) == 0
assert sp.expand(C2-C0) == 0

# Deterministic finite replay of the gcd consequence under exactly the retained
# six-variable coprimality dictionary. This is a diagnostic replay; the source
# lock contains the primewise proof.
def ok(vals: tuple[int,int,int,int,int,int]) -> bool:
    X,Y,Z,aa,bb,cc=vals
    return (
        math.gcd(X,Y)==math.gcd(X,Z)==math.gcd(Y,Z)==1
        and math.gcd(aa,bb)==math.gcd(aa,cc)==math.gcd(bb,cc)==1
        and math.gcd(aa,Z)==math.gcd(bb,Y)==math.gcd(cc,X)==1
    )

seen=0
for X in range(1,6):
  for Y in range(1,6):
    for Z in range(1,6):
      for aa in range(1,6):
        for bb in range(1,6):
          for cc in range(1,6):
            vals=(X,Y,Z,aa,bb,cc)
            if not ok(vals):
                continue
            AA=X*Y*aa; BB=X*Z*bb; CC=Y*Z*cc
            gg=math.gcd(math.gcd(AA*BB,AA*CC),BB*CC)
            assert gg == X*Y*Z
            A1=AA*BB//gg; B1=AA*CC//gg; C1=BB*CC//gg
            assert (A1,B1,C1)==(X*aa*bb,Y*aa*cc,Z*bb*cc)
            assert (math.gcd(A1,B1),math.gcd(A1,C1),math.gcd(B1,C1))==(aa,bb,cc)
            seen += 1
assert seen > 100

# Fourth-square completion identity.
Q=A**2*B**2+A**2*C**2+B**2*C**2
lhs=(A**2+B**2)*(A**2+C**2)*(B**2+C**2)+(A*B*C)**2
rhs=(A**2+B**2+C**2)*Q
assert sp.expand(lhs-rhs) == 0

src = SRC.read_text()
for marker in (
    "(AY-D0)", "(AY-D1)", "(AY-SIX)", "(AY-D2)", "(AY-D3)",
    "(AY-D4)", "(AY-D5)", "(AY-D6)", "(AY-SWAP)", "(AY-D7)",
    "(AY-D8)", "(AY-W0)", "(AY-W1)", "(AY-W2)", "(AY-I1)",
    "(AY-I2)", "(AY-I3)", "10.4153/CMB-1974-102-6",
    "10.4153/CMB-1981-058-1", "2602.00239v2",
    "FAIL_CLOSE_CURRENT_SOURCE_LOCKED_CANDIDATES",
    "ALL_POSSIBLE_NONLINEAR_DESCENT_MAPS_PROVED_IMPOSSIBLE=false",
    "35EX-35_GOAL4AZ_SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_PREFLIGHT",
):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
assert art["stacked_parent"]["exact_head_sha"] == "0d620e70ff36b5c508fa3c59f6fde995eda25c90"
assert art["stacked_parent"]["aggregate_run"] == 34298150005
assert art["stacked_parent"]["aggregate_job"] == 102300427187
assert art["source_locks"]["goal4ay_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4ax"]["blob_sha1"] == AX_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == GCD_BLOB

lit=art["literature_audit"]
assert lit["spohn_1974"]["doi"] == "10.4153/CMB-1974-102-6"
assert lit["spohn_1974"]["arbitrary_full_endpoint_descent_proved"] is False
assert lit["leech_1981"]["doi"] == "10.4153/CMB-1981-058-1"
assert lit["yelle_2026_v2"]["arxiv"] == "2602.00239v2"
assert lit["yelle_2026_v2"]["paper_explicitly_claims_full_resolution"] is False
assert lit["scoped_not_exhaustive"] is True

d=art["derived_operator"]
assert d["raw_common_gcd"] == "gcd(AB,AC,BC)=x*y*z"
assert d["six_variable_action"] == "(x,y,z ; a,b,c) -> (a,b,c ; x,y,z)"
assert d["involution"] is True

fg=art["fourth_square_gate"]
assert fg["derived_fourth_square_from_original_proved"] is False
assert fg["full_endpoint_self_map_obtained"] is False

sd=art["strict_descent_obstruction"]
assert sd["D_squared_identity"] is True
assert sd["classical_derived_operator_can_be_universal_strict_descent"] is False
assert sd["independent_of_height_choice"] is True

res=art["result"]
assert res["classical_derived_pair_product_recovered"] is True
assert res["primitive_pair_gcd_residual_involution_obtained"] is True
assert res["classical_operator_universal_strict_descent_ruled_out"] is True
assert res["source_locked_total_strict_full_endpoint_descent_found"] is False
assert res["all_possible_nonlinear_descent_maps_proved_impossible"] is False
assert res["infinite_descent_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4AZ_SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_PREFLIGHT"

for key,val in art["credit_firewall"].items():
    assert val is False, (key,val)

print("STAGE35_EX_GOAL4AY_DERIVED_CUBOID_INVOLUTION=PASS")
print("derived_three_face_self_map=true")
print("primitive_action=PAIR_GCD_RESIDUAL_SWAP_INVOLUTION")
print("full_endpoint_self_map=false")
print("universal_strict_descent=false")
print("canonical_sha256="+EXPECTED)
