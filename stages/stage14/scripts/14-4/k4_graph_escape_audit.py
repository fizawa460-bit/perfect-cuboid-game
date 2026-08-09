#!/usr/bin/env python3
"""Stage14-4bb: audit merged s5o import and updated reciprocal exponent gate."""

import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BA = ROOT / "stages/stage14/14-4ba/result.md"
S5O = ROOT / "stages/stage14/14-s5o/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/k4_graph_escape_summary.json"

VERTICES = tuple(range(4))
EDGES = tuple(itertools.combinations(VERTICES, 2))
ETA = Fraction(1, 100)


def two_core(edge_set):
    current = {tuple(sorted(e)) for e in edge_set}
    while True:
        deg = {v: 0 for v in VERTICES}
        for a, b in current:
            deg[a] += 1
            deg[b] += 1
        peel = {v for v, d in deg.items() if 0 < d < 2}
        if not peel:
            return frozenset(current)
        current = {e for e in current if e[0] not in peel and e[1] not in peel}


def classify(edge_set, classes):
    active = set()
    for i, j in edge_set:
        active.add(i)
        active.add(j)
    case_a = any(classes[i] >= 1 and classes[j] >= 1 for i, j in edge_set)
    case_b = (not case_a) and any(classes[i] == 2 for i in active)
    case_c = (not case_a) and (not case_b)
    assert int(case_a) + int(case_b) + int(case_c) == 1
    return "A" if case_a else "B" if case_b else "C"


def main() -> None:
    ba = BA.read_text()
    s5o = S5O.read_text()

    assert "STAGE14_4BA=K4_2CORE_ASSEMBLY_REDUCTION_AND_LOCAL_EXPONENT_GATE" in ba
    assert "NONEMPTY_2CORE_EDGE_SUBSET_COUNT=26" in ba
    assert "K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR_CLOSED=false" in ba

    assert "STAGE14_S5O=COMPLETE_K4_GRAPH_ESCAPE_AND_PRODUCT_CONDUCTOR_ELIMINATION" in s5o
    assert "K4_GRAPH_DICHOTOMY_EXHAUSTIVE=true" in s5o
    assert "DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false" in s5o
    assert "DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false" in s5o
    assert "PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND=false" in s5o
    assert "SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED=true" in s5o
    assert "ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED=true" in s5o
    assert "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=false" in s5o
    assert "STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED=false" in s5o

    # Reproduce the exact K4 2-core ledger inherited from 4ba.
    core_sizes = Counter()
    for mask in range(1 << len(EDGES)):
        edge_set = [EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1]
        core_sizes[len(two_core(edge_set))] += 1
    assert core_sizes == Counter({0: 38, 3: 16, 4: 3, 5: 6, 6: 1})

    # Reproduce the exhaustive s5o graph trichotomy at the abstract size-class level.
    cases = Counter()
    for mask in range(1, 1 << len(EDGES)):
        edge_set = [EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1]
        for classes in itertools.product(range(3), repeat=4):
            cases[classify(edge_set, classes)] += 1
    assert cases == Counter({"A": 3568, "B": 840, "C": 695})
    assert sum(cases.values()) == 63 * 81 == 5103

    # Exact conservative graph exponent at eta=1/100.
    case_a = ETA / 2
    case_b = 5 * ETA / 4
    case_c = min(2 - (1 + 32 * ETA), 2 - 48 * ETA)
    delta_k4 = min(case_a, case_b, case_c)
    assert case_a == Fraction(1, 200)
    assert case_b == Fraction(1, 80)
    assert case_c == Fraction(17, 25)
    assert delta_k4 == Fraction(1, 200)

    report = {
        "stage": "14-4bb",
        "classification": "K4_GRAPH_ESCAPE_IMPORTED_AND_LOCAL_EXPONENT_GATE_UPDATED",
        "imports": {
            "stage14_4ba_k4_2core_reduction": True,
            "stage14_s5o_k4_graph_escape": True,
            "s5o_graph_saving_exponent": "1/200",
        },
        "k4_2core_ledger": {
            "all_edge_subsets": 64,
            "empty_2core": 38,
            "triangle_core": 16,
            "c4_core": 3,
            "diamond_core": 6,
            "k4_core": 1,
            "nonempty_2core_total": 26,
            "nonempty_2core_intrinsic_obstruction_closed": True,
        },
        "linear_graph_sector": {
            "separable_k4_multi_edge_monomials_averaged": True,
            "one_small_variable_k4_boundary_assembly_proved": True,
            "degree_2_product_conductor_intrinsic_obstruction": False,
            "degree_3_product_conductor_intrinsic_obstruction": False,
            "persistent_resonant_k4_subgraph_found": False,
            "conservative_saving_exponent": "1/200",
        },
        "remaining_reciprocal_gates": {
            "auxiliary_incidence_uniformity_proved": False,
            "state_split_E_multi_edge_assembly_proved": False,
            "updated_frontier": "AUXILIARY_INCIDENCE_UNIFORMITY_PLUS_STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY",
        },
        "reciprocal_error_contract": {
            "decomposition": "E_rec=E_K4+E_aux+E_E",
            "E_K4": "M^(2-1/200+o(1))",
            "conditional_delta_rec": "min(1/200,delta_aux,delta_E)",
            "conditional_bound": "E_rec(M)<<M^(2-delta_rec+o(1))",
        },
        "local_domination_boundary": {
            "form": "S_W<=D_loc+E_rec",
            "diagonal_local_density_separate": True,
            "rho_loc_identified_with_graph_saving": False,
            "full_local_character_polynomial_averaged": False,
            "explicit_nontrivial_rho_loc_proved": False,
            "explicit_E_loc_proved": False,
        },
        "decision": {
            "STAGE14_4BB": "K4_GRAPH_ESCAPE_IMPORTED_AND_LOCAL_EXPONENT_GATE_UPDATED",
            "S5O_K4_GRAPH_ESCAPE_IMPORTED": True,
            "K4_2CORE_TYPES_CONTROLLED": True,
            "K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR_CLOSED": True,
            "K4_GRAPH_ASSEMBLY_SAVING_EXPONENT": "1/200",
            "DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION": False,
            "DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION": False,
            "PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND": False,
            "SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED": True,
            "ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED": True,
            "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED": False,
            "STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED": False,
            "CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA": "min(1/200,delta_aux,delta_E)",
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4bc import Stage14-s5p if available; prove auxiliary-progression-uniform linear/E discrepancy estimates, assemble the remaining E sector, and attempt the first explicit complete reciprocal E_loc exponent",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report
    print(f"k4_2core_ledger={dict(core_sizes)}")
    print(f"graph_case_counts={dict(cases)}")
    print(f"delta_k4={delta_k4.numerator}/{delta_k4.denominator}")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
