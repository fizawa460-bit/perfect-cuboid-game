#!/usr/bin/env python3
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-05q-q602-effective-correspondence-class-materialization-preflight.json"

d = json.loads(ART.read_text(encoding="utf-8"))
assert d["schema"] == "STAGE32EX1_EX1_05Q_Q602_EFFECTIVE_CORRESPONDENCE_CLASS_MATERIALIZATION_PREFLIGHT_V1"
assert d["authority"] == "SCRATCH_NONAUTHORITATIVE"

Q = 602
L1, L2 = 105, 81
K1 = K2 = 2
N1, N2 = L1-K1, L2-K2

assert [N1, N2] == d["adjoint_positive_part"]["N_bidegree"] == [103, 79]
assert 2*L1*L2 - 2*Q == d["class_materialization_setup"]["L_square"] == 15806
assert 2*(L1+L2) == d["class_materialization_setup"]["K_dot_L"] == 372
assert 1 + (15806 + 372)//2 == d["class_materialization_setup"]["arithmetic_genus"] == 8090
assert (15806-372)//2 + 1 == d["class_materialization_setup"]["chi_L"] == 7718
assert 2*N1*N2 - 2*Q == d["adjoint_positive_part"]["N_square"] == 15070

# Uniform positivity lower bound for any nonfibral genuine correspondence curve C.
# Its Rosati Gram matrix gives Q(S)<=2ab; Cauchy for the polarized Q-form gives
# |B_Q(T,S)|<=2 sqrt(Q(T)Q(S)).
base_general = 2*(math.sqrt(N1*N2)-math.sqrt(2*Q))
assert base_general > 111
for a in range(1, 50):
    for b in range(1, 50):
        lower = 2*(math.sqrt(N1*N2)-math.sqrt(2*Q))*math.sqrt(a*b)
        assert lower > 0

# Reider's E^2=0 exceptional case has the sharper Q(S)=ab.
base_square_zero = 2*(math.sqrt(N1*N2)-math.sqrt(Q))
assert base_square_zero > 131
assert min(N1, N2) == 79 > 1

# The three mod-2 residues are class-level nonexcluded and all 29 Q states remain.
assert d["class_materialization_setup"]["surviving_residues_decimal"] == [73, 97, 235]
assert d["decision"]["Q602_residues_excluded"] == 0
assert d["decision"]["Q_states_excluded"] == 0
assert d["decision"]["V6_carrier_excluded"] is False

# Exact downstairs linear-system dimension and required low-genus singularity ladder.
assert d["reider_basepoint_replay"]["h0_L"] == 7718
assert d["reider_basepoint_replay"]["linear_system_dimension"] == 7717
assert d["low_genus_firewall"]["required_normalization_genus_range"] == [106, 134]
assert d["low_genus_firewall"]["required_delta_range"] == [7956, 7984]
for r in range(29):
    g = 106+r
    delta = 8090-g
    deficit = 7717-delta
    assert delta == 7984-r
    assert deficit == r-267

assert d["decision"]["route_status"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
assert d["next_route"]["route_id"] == "EX1_05R_CONDUCTOR_ADJOINT_IDEAL_GLOBAL_EVALUATION_PREFLIGHT"
assert d["cycle_exit"]["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert d["cycle_exit"]["CYCLE_BLIND_REDISCOVERY"] is True

for key in [
    "integral_endomorphism_promoted_to_actual_fixed_V6_correspondence",
    "smooth_general_member_promoted_to_low_genus_carrier",
    "class_level_effectivity_promoted_to_common_cover_realizability",
    "basepoint_free_system_promoted_to_equigeneric_transversality",
    "negative_expected_dimension_promoted_to_empty_equigeneric_locus",
    "Q_state_exclusion_claimed",
    "Q602_exclusion_claimed",
    "O210_exclusion_claimed",
    "V6_population_wide_exclusion_claimed",
    "stage32_main_credit",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_claim",
]:
    assert d["firewalls"][key] is False, key

print("PASS_EX1_05Q_Q602_CLASS_MATERIALIZATION")
print("N_square", 15070)
print("general_nonfibral_lower_coefficient", base_general)
print("square_zero_lower_coefficient", base_square_zero)
print("linear_system_dimension", 7717)
