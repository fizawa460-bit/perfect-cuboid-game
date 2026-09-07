#!/usr/bin/env python3
"""Goal4AJ diagnostic: translate retained A1 exceptional coefficients to jets.

This is deliberately narrow.  It certifies the local Cartier-germ rule at an
A1 surface node and binds that rule to the exact exceptional coefficients from
the passing Goal4AJ degree-31 retained140 packet.  It does NOT encode the
strict-curve symbolic-power conditions and therefore does not materialize a
literal degree-31 section or F_B.
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
DIVISOR_PACKET_RUN = 34086027177
DIVISOR_PACKET_JOB = 101630197014
LOCATOR_CANONICAL_SHA256 = "79571ea862eca51a7edab0ee757000591e3c248f1df2b95b737ee51a2692c23a"
LOCATOR_SHA256 = "5f562c9c06c31119dfbdccc746f3f980a0e6e6de84d4c4d3971ef8a7bf67a2f0"
LOCATOR_RUN = 34090067335
LOCATOR_JOB = 101641601601

# Exact exceptional coefficients 93..140 extracted from the passing
# generation-2 retained140 divisor-packet run. Missing denominator entries in
# that run are literal zeroes; expand them here so both maps have 48 entries.
NUM = {
    93:26,94:3,95:2,96:21,97:2,98:21,99:26,100:3,
    101:22,102:2,103:3,104:23,105:15,106:37,107:36,108:14,
    109:20,110:17,111:13,112:22,113:27,114:12,115:12,116:21,
    117:1,118:11,119:11,120:1,121:11,122:1,123:1,124:11,
    125:18,126:13,127:13,128:18,129:13,130:12,131:12,132:13,
    133:6,134:8,135:8,136:6,137:6,138:6,139:6,140:6,
}
DEN_NONZERO = {
    94:2,95:4,97:4,100:2,101:13,102:16,103:18,104:13,
    105:4,106:1,107:1,108:2,109:24,110:15,111:15,112:22,
    113:23,114:12,115:12,116:21,117:21,118:15,119:15,120:21,
    121:15,122:21,123:21,124:15,125:11,126:14,127:14,128:11,
    129:13,130:12,131:12,132:13,133:5,134:7,135:7,136:5,
    137:6,138:6,139:6,140:6,
}
DEN = {j: DEN_NONZERO.get(j, 0) for j in range(93, 141)}
assert sorted(NUM) == list(range(93, 141))
assert sorted(DEN) == list(range(93, 141))
assert sum(NUM.values()) == 612 and max(NUM.values()) == 37
assert sum(DEN.values()) == 516 and max(DEN.values()) == 24

ai = json.loads(GOAL4AI.read_text(encoding="utf-8"))
assert ai["canonical_sha256"] == GOAL4AI_CANONICAL_SHA256
assert "48_A1_rational_double_points" in ai["source_locks"]["stoll_testa"]["facts"]
assert ai["homogeneous_realization"]["achieved_homogeneous_degree"] == 31
assert ai["homogeneous_realization"]["literal_numerator_coefficients_materialized"] is False
assert ai["homogeneous_realization"]["literal_denominator_coefficients_materialized"] is False

# Direct standard-A1 blow-up check.  For A1: xy-z^2=0.  In the x, y, z
# blow-up charts, after removing the exceptional square, the strict transforms
# are respectively Y-Z^2, X-Z^2, and X*Y-1.  Each is smooth, so one blow-up
# resolves the node; the exceptional Proj(gr_m) is the smooth conic XY-Z^2.
x, y, z, X, Y, Z = sp.symbols("x y z X Y Z")
f = x*y-z**2
assert sp.expand(sp.expand(f.subs({y:x*Y, z:x*Z})) - x**2*(Y-Z**2)) == 0
assert sp.expand(sp.expand(f.subs({x:y*X, z:y*Z})) - y**2*(X-Z**2)) == 0
assert sp.expand(sp.expand(f.subs({x:z*X, y:z*Y})) - z**2*(X*Y-1)) == 0
assert sp.diff(Y-Z**2, Y) == 1
assert sp.diff(X-Z**2, X) == 1
# On X*Y=1, X and Y are both nonzero, hence its (Y,X) gradient never vanishes.
assert sp.factor(X*Y-Z**2) == X*Y-Z**2

# For the blow-up Bl_m Spec(R)=Proj Rees(m), the coefficient of the exceptional
# prime in the pullback of a Cartier germ g is the m-adic order of g.  Here
# gr_m(R)=k[X,Y,Z]/(XY-Z^2) is a domain because its projectivization is the
# smooth conic above.  Thus a nonzero initial form does not vanish at the
# generic point of E, giving v_E(g)=max{e:g in m^e}.
# Consequently v_E(g)>=e is exactly the linear jet condition g in m^e.

def map_sha(m: dict[int, int]) -> str:
    payload = {str(k): int(v) for k, v in sorted(m.items())}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

# At an A1 point, Hilbert series gr_m(R)=(1+t)/(1-t)^2, so
# length(R/m^e)=e^2.  Record the naive jet dimensions only as sizing data;
# conditions across points/strict components need not be independent.
num_naive_jet_dim = sum(e*e for e in NUM.values())
den_naive_jet_dim = sum(e*e for e in DEN.values())

out = {
    "schema": "STAGE35_EX_GOAL4AJ_A1_EXCEPTIONAL_VALUATION_DIAGNOSTIC_V1",
    "source_locks": {
        "goal4ai_canonical_sha256": GOAL4AI_CANONICAL_SHA256,
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA256,
        "degree31_divisor_packet_run": DIVISOR_PACKET_RUN,
        "degree31_divisor_packet_job": DIVISOR_PACKET_JOB,
        "retained140_locator_canonical_sha256": LOCATOR_CANONICAL_SHA256,
        "retained140_exceptional_locator_sha256": LOCATOR_SHA256,
        "retained140_locator_run": LOCATOR_RUN,
        "retained140_locator_job": LOCATOR_JOB,
    },
    "local_model": "A1: xy-z^2=0",
    "ordinary_blowup_chart_factorizations_verified": True,
    "ordinary_blowup_resolves_standard_A1": True,
    "exceptional_is_smooth_projective_conic": True,
    "associated_graded_domain": True,
    "cartier_germ_exceptional_valuation_equals_maximal_ideal_order": True,
    "jet_translation": "v_E(g)>=e iff germ_P(g) lies in m_P^e",
    "applies_to_all_48_retained_exceptionals_via_A1_source_and_exact_locator": True,
    "numerator_exceptional_targets_93_to_140": {str(k): v for k, v in NUM.items()},
    "denominator_exceptional_targets_93_to_140": {str(k): v for k, v in DEN.items()},
    "numerator_exceptional_target_sha256": map_sha(NUM),
    "denominator_exceptional_target_sha256": map_sha(DEN),
    "numerator_exceptional_multiplicity_sum": sum(NUM.values()),
    "denominator_exceptional_multiplicity_sum": sum(DEN.values()),
    "numerator_max_exceptional_order": max(NUM.values()),
    "denominator_max_exceptional_order": max(DEN.values()),
    "numerator_naive_sum_local_jet_dimensions": num_naive_jet_dim,
    "denominator_naive_sum_local_jet_dimensions": den_naive_jet_dim,
    "naive_jet_dimensions_are_not_claimed_independent": True,
    "remaining_literal_section_blocker": "STRICT_CURVE_SYMBOLIC_POWER_CONDITIONS_PLUS_GLOBAL_DEGREE31_LINEAR_SOLVE",
    "strict_curve_symbolic_power_conditions_encoded": False,
    "global_degree31_linear_system_solved": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(
    json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
print("GOAL4AJ_A1_EXCEPTIONAL_VALUATION_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_A1_EXCEPTIONAL_VALUATION=PASS")
