#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import sympy as sp
ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-26/base-involution-receiver-descent.md"
CERT = ROOT / "stages/stage35-ex/35ex-26/base-involution-receiver-certificate.json"
AUDIT = ROOT / "stages/stage35-ex/35ex-25/post-single-elliptic-receiver-breadth-audit.json"
S30 = ROOT / "docs/arsenal/cards/formal/S30-W02.md"
S34 = ROOT / "docs/arsenal/cards/formal/S34-W03.md"
V25 = "STAGE35_EX_PESCH_E1_STATE_V25_POST_35EX26_BASE_INVOLUTION_RECEIVER_DESCENT"
CURRENT_MAIN = "dca962cdf37d4252316885dc57f3c0a591db4ecb"
def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
state = json.loads(STATE.read_text()); cert = json.loads(CERT.read_text()); audit = json.loads(AUDIT.read_text()); doc = DOC.read_text()
assert state["schema"] == V25 and state["stage"] == "35-EX" and state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] == CURRENT_MAIN
parent = state["parent_authority"]
assert parent["unit"] == "35EX-25" and parent["status"] == "AUDITED_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT"
assert parent["hostile_audit_verdict"] == "PASS" and parent["pass_source"] == "USER_CONFIRMED_AFTER_FRESHNESS_ONLY_REPAIR"
assert parent["audited_head_sha"] == "7a2d70e04dcd679881630267cb2e1810f209e44c" and parent["merged_main_sha"] == "3cadfd55d91f1e3267f31f9d7384b62d38678cc3"
assert parent["audited_theorem_credit"] is False
u25 = state["completed_units"]["35EX-25"]
assert u25["status"] == "AUDITED_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT" and u25["hostile_audit_verdict"] == "PASS"
assert u25["pass_source"] == "USER_CONFIRMED_AFTER_FRESHNESS_ONLY_REPAIR" and u25["audited_head_sha"] == "7a2d70e04dcd679881630267cb2e1810f209e44c"
assert u25["merged_main_sha"] == "3cadfd55d91f1e3267f31f9d7384b62d38678cc3" and u25["audited_theorem_credit"] is False
u25b = state["completed_units"]["35EX-25B"]
assert u25b["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT" and u25b["exhaustive_view_audit"] is True and u25b["blind_rediscovery"] is True and u25b["arsenal_comparison"] is True
assert u25b["selected_candidate"] == "E1-BASE-INVOLUTION-A-INVERSE-DESCENT" and u25b["selected_next_unit"] == "35EX-26_BASE_INVOLUTION_RECEIVER_DESCENT_OR_NO_REDUCTION_BLOCKER" and u25b["audited_theorem_credit"] is False
u26 = state["completed_units"]["35EX-26"]
assert u26["status"] == "PROVISIONAL_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT"
for key in ("base_involution_full_receiver_equivariant","fixed_field_quotient_conic_exact","descended_elliptic_model_exact","descended_full_square_receiver_iff","reciprocal_source_fibers_identified"): assert u26[key] is True
assert u26["arithmetic_dimension_drop"] is False and u26["descended_receiver_closed"] is False and u26["audited_theorem_credit"] is False
current = state["current"]
assert current["unit"] == "35EX-26_BASE_INVOLUTION_RECEIVER_DESCENT_OR_NO_REDUCTION_BLOCKER" and current["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
assert current["candidate"] == "E1-BASE-INVOLUTION-A-INVERSE-DESCENT" and current["next_if_audited_pass"] == "FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION"
assert audit["schema"] == "STAGE35_EX_25B_POST_SINGLE_ELLIPTIC_RECEIVER_FRESH_BREADTH_AUDIT_V1"
assert audit["authority"]["audited_exact_head_sha"] == "7a2d70e04dcd679881630267cb2e1810f209e44c" and audit["authority"]["merged_main_sha"] == "3cadfd55d91f1e3267f31f9d7384b62d38678cc3"
assert audit["blind_rediscovery"]["performed_before_arsenal_comparison"] is True and audit["arsenal_comparison"]["performed_after_blind_generation"] is True
assert audit["selection"]["selected_candidate"] == "E1-BASE-INVOLUTION-A-INVERSE-DESCENT" and audit["selection"]["selected_next_unit"] == "35EX-26_BASE_INVOLUTION_RECEIVER_DESCENT_OR_NO_REDUCTION_BLOCKER"
assert audit["preserved_untested_candidates"] == ["E1-DESCENDED-RECEIVER-JOINT-LOCAL-CLASSIFICATION","E1-UNIFORM-ELLIPTIC-SURFACE-SPECIALIZATION-HEIGHT","E1-NONOBVIOUS-BRAUER-FROM-ELLIPTIC-FIBRATION"]
assert audit["cycle_exit"]["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True and audit["cycle_exit"]["CYCLE_BLIND_REDISCOVERY"] is True and audit["cycle_exit"]["CYCLE_LIVE_CANDIDATES"] == 1 and audit["cycle_exit"]["CYCLE_UNTESTED_CANDIDATES"] == 3
assert cert["schema"] == "STAGE35_EX_26_BASE_INVOLUTION_RECEIVER_DESCENT_CERTIFICATE_V1" and cert["status"] == "PROVISIONAL_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT"
assert cert["authority"]["parent_audited_exact_head_sha"] == "7a2d70e04dcd679881630267cb2e1810f209e44c" and cert["authority"]["parent_merged_main_sha"] == "3cadfd55d91f1e3267f31f9d7384b62d38678cc3"
assert cert["descended_elliptic_model"]["j_nonconstant"] is True and cert["descended_elliptic_model"]["fixed_elliptic_curve_reduction"] is False
assert cert["descended_receiver"]["forward_map_exact"] is True and cert["descended_receiver"]["converse_reconstruction_exact"] is True
assert cert["descended_receiver"]["converse_q"] == "(b*(x+1)-(x-1)/b)/2" and cert["descended_receiver"]["converse_z"] == "(b*(x+1)+(x-1)/b)/2"
assert cert["result"]["arithmetic_dimension_drop"] is False and cert["result"]["descended_receiver_closed"] is False
assert git_blob_sha(S30) == cert["arsenal"]["S30_W02"]["blob_sha"] and git_blob_sha(S34) == cert["arsenal"]["S34_W03"]["blob_sha"]
assert cert["arsenal"]["S30_W02"]["decision"] == "ADJACENT_PATTERN_ONLY_NOT_APPLICABLE_FOR_MATHEMATICAL_CREDIT" and cert["arsenal"]["S34_W03"]["decision"] == "DOWNSTREAM_ROUTER_AFTER_EXACT_DESCENT_DICTIONARY" and cert["arsenal"]["S34_W02_unlocked"] is False
x,p,X,Y = sp.symbols("x p X Y", nonzero=True); u=x+1/x; h=p*(x+1)/x
fixed=sp.together(h**2-u*(u+2)); fixed_num=sp.expand(fixed.as_numer_denom()[0]).subs(p**2,1+x**2); assert sp.factor(fixed_num)==0
base_sigma=sp.together((p/x)**2-(1+(1/x)**2)); base_sigma_num=sp.expand(base_sigma.as_numer_denom()[0]).subs(p**2,1+x**2); assert sp.factor(base_sigma_num)==0
source_rhs=(X+1)*(X+x**2)*(X+1+x**2); target_rhs=(X/x**2+1)*(X/x**2+1/x**2)*(X/x**2+1+1/x**2); assert sp.factor(sp.together(source_rhs/x**6-target_rhs))==0
R=X/x; V=Y/(x*(x+1)); desc=sp.together((u+2)*V**2-(R+u)*(R**2+u*R+1)); desc_num=sp.expand(desc.as_numer_denom()[0]).subs(Y**2,source_rhs); assert sp.factor(desc_num)==0
j_a=256*(x**4-x**2+1)**3/(x**4*(x**2-1)**2); j_u=256*(u**2-3)**3/(u**2-4); assert sp.factor(sp.together(j_a-j_u))==0
y,q,z,w=sp.symbols("y q z w", nonzero=True); Rr=y**2/x; r=y/(x+1); s=w/(x+1); B=q*z/x; b=(q+z)/(x+1)
assert sp.factor(sp.together(Rr-(u+2)*r**2))==0
q2=y**2+1; z2=y**2+x**2; w2=y**2+1+x**2
q2check=sp.expand((Rr+u)-(u+2)*s**2).subs(w**2,w2); assert sp.factor(sp.together(q2check))==0
q3=sp.expand(B**2-(Rr**2+u*Rr+1)).subs(q**2,q2).subs(z**2,z2); assert sp.factor(sp.together(q3))==0
q4=sp.together(b**2-(2*Rr+u+2*B)/(u+2)); q4_num=sp.expand(q4.as_numer_denom()[0]).subs(q**2,q2).subs(z**2,z2); assert sp.factor(q4_num)==0
RR,BB,bb,uu=sp.symbols("R B b u", nonzero=True); prod=sp.expand((2*RR+uu+2*BB)*(2*RR+uu-2*BB)-(uu**2-4)).subs(BB**2,RR**2+uu*RR+1); assert sp.factor(prod)==0
bb2=(2*RR+uu+2*BB)/(uu+2); recip=sp.together(bb2*(2*RR+uu-2*BB)-(uu-2)); recip_num=sp.expand(recip.as_numer_denom()[0]).subs(BB**2,RR**2+uu*RR+1); assert sp.factor(recip_num)==0
assert sp.factor(sp.together(x*(u-2)-(x-1)**2))==0 and sp.factor(sp.together((x+1)**2-x*(u+2)))==0
S=bb*(x+1); D=-(x-1)/bb; assert sp.factor(sp.together(S*D-(1-x**2)))==0
for marker in ("BASE_INVOLUTION_FULL_RECEIVER_EQUIVARIANT=true","FIXED_FIELD_QUOTIENT_CONIC_EXACT=true","DESCENDED_ELLIPTIC_MODEL_EXACT=true","DESCENDED_FULL_SQUARE_RECEIVER_IFF=true","RECIPROCAL_SOURCE_FIBERS_IDENTIFIED=true","QUOTIENT_BASE_DIMENSION=1","DESCENDED_J_NONCONSTANT=true","FIXED_ELLIPTIC_CURVE_REDUCTION=false","DESCENDED_RECEIVER_EMPTY=false","E1_PROVED=false","STAGE35_CLOSED=false"): assert marker in doc
for key in ("uniform_receiver_emptiness","uniform_full_MW_group","uniform_Selmer_or_specialization_closure","new_Brauer_obstruction","E1_proved","R29_PESCH_E1_closed","R29_FIB2_closed","J12_PARAMETRIC_closed","stage35_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","audited_theorem_credit"): assert cert["claims"][key] is False
for key in ("new_theorem_credit","primitive_source_population_reverse_adapter_proved","global_surface_rational_points_classified","brauer_obstruction_proved","E1_proved","R29_PESCH_E1_closed","R29_FIB2_closed","J12_PARAMETRIC_closed","stage35_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"): assert state["claims"][key] is False
print("PASS STAGE35_EX_26_BASE_INVOLUTION_RECEIVER_DESCENT")
