#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-25/single-elliptic-full-square-receiver.md"
CERT = ROOT / "stages/stage35-ex/35ex-25/single-elliptic-full-square-certificate.json"
AUDIT = ROOT / "stages/stage35-ex/35ex-24/post-isogeny-compression-breadth-audit.json"
CARD = ROOT / "docs/arsenal/cards/formal/S34-W03.md"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


state = json.loads(STATE.read_text())
cert = json.loads(CERT.read_text())
audit = json.loads(AUDIT.read_text())
doc = DOC.read_text()

V24 = "STAGE35_EX_PESCH_E1_STATE_V24_POST_35EX25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER"
assert state["schema"] == V24
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] == "26fb608cb2551ab2102ae36ad3b57c063959df58"

parent = state["parent_authority"]
assert parent["unit"] == "35EX-24"
assert parent["status"] == "AUDITED_EXACT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_NO_CREDIT"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["hostile_audit_review"] == 5112867152
assert parent["audited_head_sha"] == "529c550c742e75025cdcc1a6b9666582f26697a1"
assert parent["merged_main_sha"] == "81569110952b348692e688c5e1d7148dca10b163"
assert parent["audited_theorem_credit"] is False

u24 = state["completed_units"]["35EX-24"]
assert u24["status"] == "AUDITED_EXACT_FIVE_ELLIPTIC_ISOGENY_TWIST_COMPRESSION_NO_CREDIT"
assert u24["hostile_audit_verdict"] == "PASS"
assert u24["hostile_audit_review"] == 5112867152
assert u24["audited_head_sha"] == "529c550c742e75025cdcc1a6b9666582f26697a1"
assert u24["merged_main_sha"] == "81569110952b348692e688c5e1d7148dca10b163"
assert u24["audited_theorem_credit"] is False

u24b = state["completed_units"]["35EX-24B"]
assert u24b["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert u24b["exhaustive_view_audit"] is True
assert u24b["blind_rediscovery"] is True
assert u24b["arsenal_comparison"] is True
assert u24b["historical_block_ledger_comparison"] is True
assert u24b["selected_candidate"] == "E1-SIMULTANEOUS-ELLIPTIC-KUMMER-LIFT-COMPATIBILITY"
assert u24b["selected_next_unit"] == "35EX-25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_OR_KUMMER_INTERSECTION"
assert u24b["audited_theorem_credit"] is False

u25 = state["completed_units"]["35EX-25"]
assert u25["status"] == "PROVISIONAL_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
for key in (
    "Eplus_four_square_receiver_iff_C_lift",
    "single_elliptic_receiver_reduction",
    "pair_2isogeny_image_iff_T_square_on_nonzero_open",
    "three_pair_receiver_T_coordinates_square",
    "five_factor_simultaneous_compatibility_reconstructed_from_Eplus_full_square_locus",
    "S34_W03_single_elliptic_receiver_routing_match",
):
    assert u25[key] is True
assert u25["receiver_intersection_closed"] is False
assert u25["fresh_breadth_audit_required_after_hostile_pass"] is True
assert u25["audited_theorem_credit"] is False

current = state["current"]
assert current["unit"] == "35EX-25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_OR_KUMMER_INTERSECTION"
assert current["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
assert current["candidate"] == "E1-SIMULTANEOUS-ELLIPTIC-KUMMER-LIFT-COMPATIBILITY"
assert current["next_if_audited_pass"] == "FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION"

assert audit["schema"] == "STAGE35_EX_24B_POST_ISOGENY_COMPRESSION_FRESH_BREADTH_AUDIT_V1"
assert audit["authority"]["hostile_audit_review"] == 5112867152
assert audit["authority"]["audited_head_sha"] == "529c550c742e75025cdcc1a6b9666582f26697a1"
assert audit["authority"]["merged_main_sha"] == "81569110952b348692e688c5e1d7148dca10b163"
assert audit["blind_rediscovery"]["performed_before_arsenal_comparison"] is True
assert audit["arsenal_comparison"]["performed_after_blind_generation"] is True
assert audit["selection"]["selected_candidate"] == "E1-SIMULTANEOUS-ELLIPTIC-KUMMER-LIFT-COMPATIBILITY"
assert audit["selection"]["selected_next_unit"] == "35EX-25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_OR_KUMMER_INTERSECTION"
assert audit["selection"]["preserved_untested_candidates"] == [
    "E1-BASE-INVOLUTION-A-INVERSE-DESCENT",
    "E1-UNIFORM-ELLIPTIC-SURFACE-SPECIALIZATION-HEIGHT",
    "E1-NONOBVIOUS-BRAUER-FROM-ELLIPTIC-FIBRATION",
    "E1-FURTHER-INTERFACTOR-ISOGENY-COMPRESSION",
]
assert audit["cycle_exit"]["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert audit["cycle_exit"]["CYCLE_BLIND_REDISCOVERY"] is True
assert audit["cycle_exit"]["CYCLE_LIVE_CANDIDATES"] == 1
assert audit["cycle_exit"]["CYCLE_UNTESTED_CANDIDATES"] == 4
assert audit["cycle_exit"]["CYCLE_SPLIT_TRIGGERED"] is False

assert cert["schema"] == "STAGE35_EX_25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_CERTIFICATE_V1"
assert cert["status"] == "PROVISIONAL_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
assert cert["authority"]["hostile_audit_review"] == 5112867152
assert cert["single_elliptic_receiver"]["iff_C_lift"] is True
assert cert["single_elliptic_receiver"]["full_Eplus_pointset_classified"] is False
assert cert["pair_2isogeny_image_criterion"]["criterion_open"] == "T!=0"
assert cert["pair_2isogeny_image_criterion"]["image_iff"] == "T in F^2"
assert cert["reconstruction"]["five_factor_compatibility_from_single_receiver"] is True
assert cert["arsenal"]["selected_card"] == "S34-W03"
assert cert["arsenal"]["blob_sha"] == "1d5275321f42768a6414d4610ac912c63be43f96"
assert cert["arsenal"]["single_elliptic_receiver_routing_match"] is True
assert cert["arsenal"]["receiver_intersection_closed"] is False
assert cert["arsenal"]["S34_W02_unlocked"] is False
assert git_blob_sha(CARD) == cert["arsenal"]["blob_sha"]

# Exact C -> Eplus identity.
y, q, z, w, a = sp.symbols("y q z w a")
X = y**2
Yp = q*z*w
expr = sp.expand(Yp**2 - (X+1)*(X+a)*(X+1+a))
expr = expr.subs(q**2, y**2+1).subs(z**2, y**2+a).subs(w**2, y**2+1+a)
assert sp.expand(expr) == 0

# The four receiver factors are exactly the defining squares.
assert sp.expand(X - y**2) == 0
assert sp.expand((X+1) - (y**2+1)) == 0
assert sp.expand((X+a) - (y**2+a)) == 0
assert sp.expand((X+1+a) - (y**2+1+a)) == 0

# General pair receiver point has square T-coordinate.
r, s, qr, qs, yy = sp.symbols("r s qr qs yy", nonzero=True)
d = r*s
c = r**2+s**2
V = qr*qs
Tpair = c + 2*d*(V+d)/yy**2
tpair2 = (r*qs+s*qr)**2/yy**2
diff = sp.expand((tpair2-Tpair)*yy**2)
diff = diff.subs(qr**2, yy**2+r**2).subs(qs**2, yy**2+s**2)
assert sp.expand(diff) == 0

# Exact 2-isogeny image converse on T!=0.
T, Y, t, cc, dd = sp.symbols("T Y t cc dd", nonzero=True)
Z = (T-cc-Y/t)/2
W = t*Z
quad = sp.expand(Z**2 + (cc-T)*Z + dd**2)
quad = quad.subs(Y**2, T*((T-cc)**2-4*dd**2)).subs(T, t**2)
assert sp.factor(quad) == 0

# L equation follows from the same quadratic relation.
Z0 = sp.symbols("Z0", nonzero=True)
W0 = t*Z0
Ldiff0 = sp.expand(W0**2 - (Z0**3+cc*Z0**2+dd**2*Z0))
assert sp.factor(Ldiff0 - Z0*(t**2*Z0-Z0**2-cc*Z0-dd**2)) == 0

# The chosen quadratic root reproduces the requested Q Y-coordinate.
Yphi = sp.together(t*(dd**2/Z - Z) - Y)
num = sp.factor(sp.together(Yphi).as_numer_denom()[0])
num = num.subs(Y**2, t**2*((t**2-cc)**2-4*dd**2))
assert sp.factor(num) == 0

# Exact named specializations of the square roots.
x, p = sp.symbols("x p", nonzero=True)
assert cert["receiver_pair_square_coordinates"]["E12"] == "T12=((z+x*q)/y)^2"
assert cert["receiver_pair_square_coordinates"]["E13"] == "T13=((w+p*q)/y)^2"
assert cert["receiver_pair_square_coordinates"]["E23"] == "T23=((x*w+p*z)/y)^2"

for marker in (
    "EPLUS_FOUR_SQUARE_RECEIVER_IFF_C_LIFT=true",
    "SINGLE_ELLIPTIC_RECEIVER_REDUCTION=true",
    "PAIR_2ISOGENY_IMAGE_IFF_T_SQUARE_ON_T_NONZERO=true",
    "THREE_PAIR_RECEIVER_T_COORDINATES_SQUARE=true",
    "FIVE_FACTOR_SIMULTANEOUS_COMPATIBILITY_RECONSTRUCTED_FROM_EPLUS_FULL_SQUARE_LOCUS=true",
    "S34_W03_SINGLE_ELLIPTIC_RECEIVER_ROUTING_MATCH=true",
    "CYCLE_NEW_GATE=SINGLE_MOVING_EPLUS_FOUR_SQUARE_RECEIVER",
    "E1_PROVED=false",
    "STAGE35_CLOSED=false",
):
    assert marker in doc

for key in (
    "uniform_receiver_emptiness",
    "uniform_full_MW_group",
    "uniform_Selmer_or_specialization_closure",
    "new_Brauer_obstruction",
    "E1_proved",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
    "audited_theorem_credit",
):
    assert cert["claims"][key] is False

for key in (
    "new_theorem_credit",
    "primitive_source_population_reverse_adapter_proved",
    "global_surface_rational_points_classified",
    "brauer_obstruction_proved",
    "E1_proved",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False

print("PASS STAGE35_EX_25_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER")
