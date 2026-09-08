#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-05n-hurwitz-simultaneous-cover-dimension-preflight.json"
UP05G = HERE.parent / "ex1-05g-h4-common-cover-correspondence-coupling.json"
UP05H = HERE.parent / "ex1-05h-upstairs-conductor-discriminant-off-cusp-coupling.json"
PARENT05M = HERE / "ex1-05m-castelnuovo-severi-two-projection-preflight.json"

with ART.open(encoding="utf-8") as f:
    d = json.load(f)
with UP05G.open(encoding="utf-8") as f:
    g5 = json.load(f)
with UP05H.open(encoding="utf-8") as f:
    h5 = json.load(f)
with PARENT05M.open(encoding="utf-8") as f:
    m5 = json.load(f)

assert d["schema"] == "STAGE32EX1_EX1_05N_HURWITZ_SIMULTANEOUS_COVER_DIMENSION_PREFLIGHT_V1"
assert d["authority"] == "SCRATCH_NONAUTHORITATIVE"
assert d["base_main_sha"] == "d5545b32e6b3088bca53318998d434f2745b03e9"
assert d["parent_scratch_head"] == "fa56fed74f34609728067dde0421a98405f599f4"

# Re-establish source-locked simultaneous-cover inputs.
assert g5["notation_adapter"]["projection_degrees"] == [105, 81]
assert g5["fixed_correspondence_arithmetic"]["pair_map_birational"] is True
assert g5["common_cover_consequence"]["torsor_isomorphism"] == "f1^*Z ~= f2^*Z"
assert h5["upstairs_defect_ladder"]["R105_values"] == [2 * r for r in range(29)]
assert h5["upstairs_defect_ladder"]["R81_values"] == [48 + 2 * r for r in range(29)]
assert m5["decision"]["Q_states_excluded"] == 0

E = d["exact_normal_sheaf_replay"]
assert E["deg_T_C2"] == -2
assert E["deg_phi_pullback_T_X"] == -2 * 105 - 2 * 81 == -372

# Exact 29-state normal-sheaf and virtual-dimension replay.
for r in range(29):
    genus = 106 + r
    R105 = 2 * r
    R81 = 48 + 2 * r
    deg_T_D = 2 - 2 * genus
    deg_N = -372 - deg_T_D
    chi_N = deg_N + 1 - genus
    vdim = -(1 - genus) - 372

    assert deg_T_D == -210 - 2 * r
    assert deg_N == -162 + 2 * r
    assert chi_N == r - 267
    assert vdim == r - 267 == chi_N
    assert R105 <= R81

    # tau is not fixed without support; replay every admissible endpoint bound.
    for tau in (0, R105):
        deg_L = deg_N - tau
        assert deg_L < 0
        h0_N = tau
        h1_N = h0_N - chi_N
        assert h1_N == 267 - r + tau
        assert h1_N >= 267 - r > 0

assert E["deg_N_phi_range"] == [-162, -106]
assert E["virtual_dimension_range"] == [-267, -239]

T = d["common_ramification_torsion"]
assert T["tau_range_global"] == [0, 56]
assert T["deg_L_upper_bound"] == -106
assert T["h0_L"] == 0
assert T["obstruction_dimension_lower_bound_range"] == [239, 267]

# Same-target counterexample: the diagonal in C2 x C2 exists although vdim=-3.
C = d["same_target_negative_virtual_dimension_counterexample"]
assert C["degrees"] == [1, 1]
assert C["source_genus"] == 2
assert C["K_X_dot_Delta"] == 4
vdim_diag = -(1 - 2) - 4
assert vdim_diag == C["virtual_dimension"] == -3
assert C["normal_degree"] == -2
assert C["h0_normal"] == 0
assert C["h1_normal"] == 3
assert C["exists"] is True

D = d["decision"]
assert D["route_status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert D["Q_states_entering"] == 29
assert D["Q_states_excluded"] == 0
assert D["Q_states_leaving"] == 29
assert D["negative_expected_dimension_promoted_to_nonexistence"] is False

B = d["breadth_audit"]
assert B["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert B["CYCLE_BLIND_REDISCOVERY"] is True
assert B["CYCLE_SPLIT_TRIGGERED"] is False

L = d["candidate_ledger"]
assert L["LIVE"] == ["COMMON_V4_BRANCH_CYCLE_MONODROMY_LIFT_COMPATIBILITY"]
assert "ACTUAL_V6_SECTION_MATERIALIZATION" in L["UNTESTED"]
assert "PLAIN_SIMULTANEOUS_HURWITZ_EXPECTED_DIMENSION_WITHOUT_OBSTRUCTION_OR_MONODROMY_INPUT" in L["BLOCKED"]

N = d["next_route"]
assert N["route_id"] == "EX1_05O_COMMON_V4_BRANCH_CYCLE_MONODROMY_LIFT_PREFLIGHT"

FW = d["firewalls"]
for key in [
    "negative_virtual_dimension_promoted_to_empty_moduli",
    "large_obstruction_space_promoted_to_existence",
    "common_v4_discrete_condition_charged_as_continuous_codimension",
    "tau_assumed_without_branch_support",
    "Q_state_exclusion_claimed",
    "O210_exclusion_claimed",
    "Q602_exclusion_claimed",
    "V6_population_wide_exclusion_claimed",
    "stage32_main_credit",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_claim",
]:
    assert FW[key] is False, key

print("PASS_EX1_05N_HURWITZ_OBSTRUCTION_PATTERN")
print("vdim_range", -267, -239)
print("tangent_bound_global", 56)
print("obstruction_lower_bound_range", 239, 267)
print("Q_states_excluded", 0)
