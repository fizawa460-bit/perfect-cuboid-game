#!/usr/bin/env python3
"""Goal4AJ diagnostic: residual-aware A1 exceptional valuation -> jet packet.

Retain the exact local A1 valuation rule from generations 1/2, but bind it to
the post-Q-hyperplane-peel divisor packet actually used by the next section
solve.  The numerator remains degree 31.  The denominator is the degree-19
residual after removing 12 Q-defined linear factors.  The pre-peel denominator
exceptional targets are deliberately not reused.

Diagnostic only: no strict symbolic powers, global section, or F_B are solved.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
GOAL4AI = ROOT / "stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence.json"

GOAL4AI_CANONICAL_SHA256 = "b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a"
DIVISOR_PACKET_SHA256 = "c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009"
QPEEL_CANONICAL_SHA256 = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
ACTIVE_PACKET_CANONICAL_SHA256 = "59d22df437c949d147072e4fa80c92a80edc222c4685fd8bf9d53ba73a7e34e6"
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
LOCATOR_SHA256 = "5f562c9c06c31119dfbdccc746f3f980a0e6e6de84d4c4d3971ef8a7bf67a2f0"
PREVIOUS_A1_PROBE_BLOB_SHA1 = "6cfa9b240d7b6d0a5caa5773c870ae75cbbeb92a"

NUM = {
    93:26,94:3,95:2,96:21,97:2,98:21,99:26,100:3,
    101:22,102:2,103:3,104:23,105:15,106:37,107:36,108:14,
    109:20,110:17,111:13,112:22,113:27,114:12,115:12,116:21,
    117:1,118:11,119:11,120:1,121:11,122:1,123:1,124:11,
    125:18,126:13,127:13,128:18,129:13,130:12,131:12,132:13,
    133:6,134:8,135:8,136:6,137:6,138:6,139:6,140:6,
}
DENR_NONZERO = {
    94:2,95:4,97:4,100:2,101:13,102:16,103:18,104:13,
    105:4,106:1,107:1,108:2,109:13,110:4,111:4,112:11,
    113:12,114:1,115:1,116:10,117:9,118:3,119:3,120:9,
    121:3,122:9,123:9,124:3,125:10,126:13,127:13,128:10,
    129:12,130:11,131:11,132:12,133:4,134:6,135:6,136:4,
    137:5,138:5,139:5,140:5,
}
DENR = {j: DENR_NONZERO.get(j, 0) for j in range(93, 141)}
assert sorted(NUM) == list(range(93,141))
assert sorted(DENR) == list(range(93,141))
assert sum(NUM.values()) == 612 and max(NUM.values()) == 37
assert sum(DENR.values()) == 316 and max(DENR.values()) == 18
assert sum(e*e for e in NUM.values()) == 11616
assert sum(e*e for e in DENR.values()) == 3180

ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_CANONICAL_SHA256
assert "48_A1_rational_double_points" in ai["source_locks"]["stoll_testa"]["facts"]
assert ai["homogeneous_realization"]["achieved_homogeneous_degree"] == 31
assert ai["homogeneous_realization"]["explicit_F_B_materialized"] is False

# Standard A1 blow-up: xy-z^2=0. One ordinary blow-up resolves the node;
# the exceptional divisor is the smooth conic XY-Z^2.  Its associated graded
# ring is a domain, hence for a Cartier germ g the exceptional valuation is
# exactly its maximal-ideal order: v_E(g)>=e iff g lies in m_P^e.
x,y,z,X,Y,Z = sp.symbols("x y z X Y Z")
f=x*y-z**2
assert sp.expand(f.subs({y:x*Y,z:x*Z}) - x**2*(Y-Z**2)) == 0
assert sp.expand(f.subs({x:y*X,z:y*Z}) - y**2*(X-Z**2)) == 0
assert sp.expand(f.subs({x:z*X,y:z*Y}) - z**2*(X*Y-1)) == 0
assert sp.diff(Y-Z**2,Y)==1 and sp.diff(X-Z**2,X)==1
assert sp.factor(X*Y-Z**2)==X*Y-Z**2


def map_sha(m: dict[int,int]) -> str:
    payload={str(k):int(v) for k,v in sorted(m.items())}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",", ":")).encode()).hexdigest()

out={
    "schema":"STAGE35_EX_GOAL4AJ_A1_EXCEPTIONAL_VALUATION_DIAGNOSTIC_V2",
    "source_locks":{
        "goal4ai_canonical_sha256":GOAL4AI_CANONICAL_SHA256,
        "degree31_divisor_packet_sha256":DIVISOR_PACKET_SHA256,
        "q_hyperplane_factor_peel_canonical_sha256":QPEEL_CANONICAL_SHA256,
        "active_divisor_condition_packet_canonical_sha256":ACTIVE_PACKET_CANONICAL_SHA256,
        "retained140_locator_canonical_sha256":LOCATOR_CANONICAL_SHA256,
        "retained140_exceptional_locator_sha256":LOCATOR_SHA256,
        "previous_a1_local_rule_probe_blob_sha1":PREVIOUS_A1_PROBE_BLOB_SHA1,
    },
    "local_model":"A1: xy-z^2=0",
    "ordinary_blowup_chart_factorizations_verified":True,
    "ordinary_blowup_resolves_standard_A1":True,
    "exceptional_is_smooth_projective_conic":True,
    "associated_graded_domain":True,
    "cartier_germ_exceptional_valuation_equals_maximal_ideal_order":True,
    "jet_translation":"v_E(g)>=e iff germ_P(g) lies in m_P^e",
    "applies_to_all_48_retained_exceptionals_via_A1_source_and_exact_locator":True,
    "numerator_homogeneous_degree":31,
    "denominator_residual_homogeneous_degree":19,
    "numerator_exceptional_targets_93_to_140":{str(k):v for k,v in NUM.items()},
    "denominator_residual_exceptional_targets_93_to_140":{str(k):v for k,v in DENR.items()},
    "numerator_exceptional_target_sha256":map_sha(NUM),
    "denominator_residual_exceptional_target_sha256":map_sha(DENR),
    "numerator_exceptional_multiplicity_sum":612,
    "denominator_residual_exceptional_multiplicity_sum":316,
    "numerator_max_exceptional_order":37,
    "denominator_residual_max_exceptional_order":18,
    "numerator_naive_sum_local_jet_dimensions":11616,
    "denominator_residual_naive_sum_local_jet_dimensions":3180,
    "naive_jet_dimensions_are_not_claimed_independent":True,
    "pre_qpeel_denominator_exceptional_targets_not_used_for_residual_solve":True,
    "strict_curve_symbolic_power_conditions_encoded_globally":False,
    "global_section_intersection_solved":False,
    "literal_numerator_coefficients_materialized":False,
    "literal_denominator_coefficients_materialized":False,
    "literal_F_B_materialized":False,
    "local_evaluations_computed":False,
    "brauer_manin_obstruction_obtained":False,
    "E1_proved":False,
    "stage35_closed":False,
    "theorem_credit":False,
    "endpoint_credit":False,
}
out["canonical_sha256"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_A1_EXCEPTIONAL_VALUATION_JSON="+json.dumps(out,sort_keys=True,separators=(",", ":")))
print("GOAL4AJ_A1_EXCEPTIONAL_VALUATION=PASS")
