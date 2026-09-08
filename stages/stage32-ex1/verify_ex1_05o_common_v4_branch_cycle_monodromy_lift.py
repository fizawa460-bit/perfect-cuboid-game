#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
EX1 = HERE.parent
S32 = EX1.parent / "stage32" / "residual-32-01-production"

ART = HERE / "ex1-05o-common-v4-branch-cycle-monodromy-lift-preflight.json"
UP05B = EX1 / "ex1-05b-inertia-parity-stabilizer.json"
UP05C = EX1 / "ex1-05c-inertia-class-capacity.json"
UP05F = EX1 / "ex1-05f-h4-local-cusp-projection-ramification-adapter.json"
UP05G = EX1 / "ex1-05g-h4-common-cover-correspondence-coupling.json"
INC = S32 / "post1473-x8-marked-exceptional-incidence.json"
DOUBLE = S32 / "post1484-o210-q4-common-double-cover-cartesian-identity.json"
REL = S32 / "post1503-o210-q4-relative-v4-torsor-mod2-coupling.json"
WAD = S32 / "post1505-o210-q4-x8-v4-torsor-plane-retained-f2-4-adapter.json"
TR = S32 / "post1505-o210-q602-weierstrass-parity-transvection-refinement.json"
GAUGE = S32 / "post1505-o210-q602-marked-w-line-gauge-orbit.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


d = load(ART)
u05b = load(UP05B)
u05c = load(UP05C)
u05f = load(UP05F)
u05g = load(UP05G)
inc = load(INC)
double = load(DOUBLE)
rel = load(REL)
wad = load(WAD)
tr = load(TR)
gauge = load(GAUGE)

assert d["schema"] == "STAGE32EX1_EX1_05O_COMMON_V4_BRANCH_CYCLE_MONODROMY_LIFT_PREFLIGHT_V1"
assert d["authority"] == "SCRATCH_NONAUTHORITATIVE"
assert d["base_main_sha"] == "d5545b32e6b3088bca53318998d434f2745b03e9"

# Source-lock replay.
locks = d["source_locks"]
assert u05c["canonical_sha256_without_this_field"] == locks["ex1_05c_source_order"]["canonical_sha256"]
assert u05f["canonical_sha256_without_this_field"] == locks["ex1_05f"]["canonical_sha256"]
assert u05g["canonical_sha256_without_this_field"] == locks["ex1_05g"]["canonical_sha256"]
assert inc["canonical_sha256_without_this_field"] == locks["marked_exceptional_incidence"]["canonical_sha256"]
assert double["canonical_sha256_without_this_field"] == locks["common_double_cover"]["canonical_sha256"]
assert rel["canonical_sha256_without_this_field"] == locks["relative_v4_stage32"]["canonical_sha256"]
assert wad["canonical_sha256_without_this_field"] == locks["exact_W_adapter"]["canonical_sha256"]
assert tr["canonical_sha256_without_this_field"] == locks["weierstrass_transvection"]["canonical_sha256"]
assert gauge["canonical_sha256_without_this_field"] == locks["marked_gauge_orbit"]["canonical_sha256"]

# Exact source-order adapter: the 48 exceptional pairings are pts[1]..pts[48]
# after the first 92 known curves. The incidence certificate labels them 93..140.
assert u05c["source_order_adapter"]["exceptional_order"].startswith("The pairing matrix appends pts[1]..pts[48]")
rows = inc["rows"]
assert [row["exceptional_label"] for row in rows] == list(range(93, 141))
P = u05b["target"]["exceptional_pairings"]
assert len(P) == len(rows) == 48
assert sum(P) == 266

# Recompute the 12 ordered marked-pair masses directly from EX1's fixed V6 pairings.
pair_mass = defaultdict(int)
for m, row in zip(P, rows):
    key = (row["first_factor_boundary_label"], row["second_factor_boundary_label"])
    pair_mass[key] += m

expected_order = [
    (43,41),(42,44),(39,37),(38,40),(35,33),(34,36),
    (35,36),(34,33),(38,37),(39,40),(43,44),(42,41),
]
expected_masses = [5,5,21,25,24,18,19,35,28,34,32,20]
assert [pair_mass[p] for p in expected_order] == expected_masses
assert sum(expected_masses) == 266

art_pairs = d["uniform_marked_pair_mass_replay"]["ordered_pair_masses"]
assert [(tuple(x["pair"]), x["M"]) for x in art_pairs] == list(zip(expected_order, expected_masses))
tr_pairs = tr["weierstrass_parity_action"]["ordered_pair_masses"]
assert [(tuple(x["pair"]), x["M"]) for x in tr_pairs] == list(zip(expected_order, expected_masses))

# The historical file name says O210, but the common-double-cover certificate itself
# is a fixed-V6 group-quotient statement and its fixed_target carries no O specialization.
assert double["fixed_target"]["row_id"] == "g1-d186"
assert "O" not in double["fixed_target"]
assert double["carrier_consequence"]["same_quadratic_extension"] is True
assert double["group_quotient_square"]["H"].endswith("V4, order 4, normal index 2")

# Direct relative-V4 branch inertia is not a new local charge: the retained cover is etale.
assert rel["relative_v4_coupling"]["base_torsor"].endswith("connected finite etale degree 4")
assert u05g["common_cover_consequence"]["torsor_isomorphism"] == "f1^*Z ~= f2^*Z"
assert d["direct_relative_v4_local_monodromy_boundary"]["local_ramification_inertia_H_label"] == "zero"

# Recompute the Weierstrass parity matrix from the fixed pair masses only.
label_to_id = {int(k): v for k, v in tr["weierstrass_parity_action"]["boundary_label_to_weierstrass_id"].items()}
B = [[0]*6 for _ in range(6)]
for (a,b), M in pair_mass.items():
    i = label_to_id[a] - 1
    j = label_to_id[b] - 1
    B[i][j] ^= (M & 1)
expected_B = [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
assert B == expected_B
assert B == tr["weierstrass_parity_action"]["parity_matrix_rows_first_cols_second"]
assert B == d["uniform_weierstrass_action"]["parity_matrix_rows_first_cols_second"]
assert tr["weierstrass_parity_action"]["branch_permutation"] == d["uniform_weierstrass_action"]["branch_permutation"] == "(2 4)"

# Uniformity in Q: modulo two, number of odd summands of an integer partition
# equals the total mass. Thus each marked pair has the same branch parity for every Q.
Qvals = u05g["Q_defect_ladder"]["EX1_Q_values"]
assert Qvals == list(range(210, 267, 2))
assert len(Qvals) == 29
assert sum(m & 1 for m in P) == 26
for Q in Qvals:
    assert Q % 2 == sum(P) % 2 == 0
    for M in expected_masses:
        # This is the universal parity identity n_p = M_p - 2*y_p.
        for y in [0, M // 2]:
            n = M - 2*y
            assert (n & 1) == (M & 1)

# Exact W and residue filters are independent of EX1 Q because Q_Rosati=602 is uniform.
assert u05g["fixed_correspondence_arithmetic"]["Q_Rosati"] == 602
assert wad["retained_F2_4_adapter"]["W_basis_vectors"] == [[0,0,1,0],[0,0,0,1]]
res28 = u05g["mod2_shell_replay_adapter"]["fixed_plane_survivors_decimal"]
assert res28 == wad["q602_pointwise_exact_W_test"]["input_residues_decimal"]
res16 = wad["q602_pointwise_exact_W_test"]["surviving_residues_decimal"]
assert res16 == tr["audited_input"]["residues_decimal"]
res3 = tr["retained_residue_filter"]["surviving_residues_decimal"]
assert res3 == [73,97,235]
assert d["uniform_Q602_residue_refinement"]["surviving_residues_decimal"] == res3
assert d["uniform_Q602_residue_refinement"]["coarse_joint_cells_before_05O"] == 29*28 == 812
assert d["uniform_Q602_residue_refinement"]["coarse_joint_cells_after_05O"] == 29*3 == 87
assert d["uniform_Q602_residue_refinement"]["cells_removed"] == 812-87 == 725
assert d["uniform_Q602_residue_refinement"]["Q_states_excluded"] == 0

# Existing gauge result is dedup only, not arithmetic 3->1 pruning.
assert gauge["residue_conjugation"]["orbit"] == [73,97,235]
assert gauge["residue_conjugation"]["single_orbit"] is True
assert gauge["firewalls"]["two_residues_arithmetically_excluded"] is False
assert d["known_gauge_dedup"]["arithmetic_three_to_one_exclusion"] is False

D = d["decision"]
assert D["route_status"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
assert D["Q_states_entering"] == D["Q_states_leaving"] == 29
assert D["Q_states_excluded"] == 0
assert D["mod2_residues_per_Q_before"] == 28
assert D["mod2_residues_per_Q_after"] == 3
assert D["weierstrass_transvection_imported_with_uniform_Q_adapter"] is True
assert d["next_route"]["route_id"] == "EX1_05P_RAMIFICATION_DIFFERENCE_SPIN_PARITY_PREFLIGHT"

FW = d["firewalls"]
for key in [
    "etale_V4_local_inertia_used_as_nontrivial_branch_label",
    "O210_total_odd_contact_count_assumed_for_all_Q",
    "pair_mass_order_guessed",
    "three_residues_promoted_to_three_geometric_correspondences",
    "gauge_three_to_one_promoted_to_arithmetic_exclusion",
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
    assert FW[key] is False, key

print("PASS_EX1_05O_UNIFORM_TRANSVECTION_28_TO_3")
print("Q_states", 29, "residues_per_Q", len(res3), "compatibility_cells", 29*len(res3))
print("uniform_pair_masses", expected_masses)
