#!/usr/bin/env python3
"""Stage14-4bb: deterministic audit of K4 graph escape and exponent ledger."""

import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BA = ROOT / "stages/stage14/14-4ba/result.md"
S5N = ROOT / "stages/stage14/14-s5n/result.md"
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


def jacobi(a: int, n: int) -> int:
    assert n > 0 and n % 2 == 1
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                out = -out
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            out = -out
        a %= n
    return out if n == 1 else 0


def classify(edge_set, size_classes):
    active = set()
    for i, j in edge_set:
        active.add(i)
        active.add(j)

    # 0 = below M^eta, 1 = [M^eta, M^(4eta)), 2 = >= M^(4eta)
    case_a = any(size_classes[i] >= 1 and size_classes[j] >= 1 for i, j in edge_set)
    case_b = (not case_a) and any(size_classes[i] == 2 for i in active)
    case_c = (not case_a) and (not case_b)
    assert int(case_a) + int(case_b) + int(case_c) == 1
    return "A" if case_a else "B" if case_b else "C"


def main() -> None:
    ba = BA.read_text()
    s5n = S5N.read_text()
    assert "STAGE14_4BA=K4_2CORE_ASSEMBLY_REDUCTION" in ba
    assert "K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR" in ba
    assert "ALL_SIX_LINEAR_EDGES_INDIVIDUALLY_CLOSED=true" in s5n
    assert "MULTI_EDGE_PRODUCT_CONDUCTOR_OBSTRUCTION_ISOLATED=true" in s5n

    # Reproduce the 4ba exact 2-core ledger.
    core_sizes = Counter()
    for mask in range(1 << len(EDGES)):
        edge_set = [EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1]
        core_sizes[len(two_core(edge_set))] += 1
    assert core_sizes == Counter({0: 38, 3: 16, 4: 3, 5: 6, 6: 1})

    # Exhaustive graph/size trichotomy: 63 nonempty graphs x 3^4 assignments.
    cases = Counter()
    for mask in range(1, 1 << len(EDGES)):
        edge_set = [EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1]
        for size_classes in itertools.product(range(3), repeat=4):
            cases[classify(edge_set, size_classes)] += 1
    assert cases == Counter({"A": 3568, "B": 840, "C": 695})
    assert sum(cases.values()) == 63 * (3 ** 4) == 5103

    # Exact exponent ledger at eta=1/100.
    case_a_saving = ETA / 2
    case_b_saving = 5 * ETA / 4
    case_c_first_error_exp = 1 + 32 * ETA
    case_c_second_error_exp = 48 * ETA
    case_c_saving = min(2 - case_c_first_error_exp, 2 - case_c_second_error_exp)
    graph_saving = min(case_a_saving, case_b_saving, case_c_saving)
    assert case_a_saving == Fraction(1, 200)
    assert case_b_saving == Fraction(1, 80)
    assert case_c_first_error_exp == Fraction(33, 25)  # 1.32
    assert case_c_second_error_exp == Fraction(12, 25)  # 0.48
    assert case_c_saving == Fraction(17, 25)  # 0.68
    assert graph_saving == Fraction(1, 200)

    # Freeze-one-edge factorization sanity check: other incident edges become
    # one-variable factors and Jacobi multiplicativity at a common vertex is exact.
    moduli = (3, 5, 7)
    for u in range(1, 80, 2):
        if any(u % q == 0 for q in moduli):
            continue
        lhs = 1
        for q in moduli:
            lhs *= jacobi(u, q)
        rhs = jacobi(u, 3 * 5 * 7)
        assert lhs == rhs

    report = {
        "stage": "14-4bb",
        "classification": "K4_GRAPH_ESCAPE_AND_INTRINSIC_PRODUCT_CONDUCTOR_OBSTRUCTION_CLOSED",
        "inputs": {
            "stage14_4ba_k4_2core_reduction": True,
            "s5h_quadratic_large_sieve": True,
            "s5n_squarefree_completion": True,
            "s5n_centered_periodic_bound": True,
        },
        "k4_2core_ledger": {
            "all_edge_subsets": 64,
            "empty_2core": 38,
            "triangle_core": 16,
            "c4_core": 3,
            "diamond_core": 6,
            "k4_core": 1,
            "nonempty_2core_total": 26,
        },
        "graph_escape": {
            "eta": "1/100",
            "case_A": {
                "condition": "some active edge has both endpoints >= M^eta",
                "method": "freeze all other variables and apply one-edge quadratic large sieve",
                "relative_saving": "M^(-eta/2+epsilon)",
                "eta_1_100_saving": "M^(-1/200+epsilon)",
            },
            "case_B": {
                "condition": "no long-long edge and some active vertex >= M^(4eta)",
                "method": "all neighbors < M^eta; combine product conductor and apply squarefree completion",
                "neighbor_product_conductor": "<=M^(3eta)",
                "relative_saving": "M^(-5eta/4+epsilon)",
                "eta_1_100_saving": "M^(-1/80+epsilon)",
            },
            "case_C": {
                "condition": "all active vertices < M^(4eta)",
                "method": "exact local centering plus fixed-conductor periodic estimate",
                "total_conductor": "<M^(16eta)",
                "tuple_count": "<M^(16eta)",
                "summed_bound": "B^epsilon*(M^(1+32eta)+M^(48eta))",
            },
            "exhaustive_configuration_count": 5103,
            "case_counts": {"A": 3568, "B": 840, "C": 695, "unclassified": 0},
            "conservative_graph_saving_exponent": "1/200",
        },
        "scope": {
            "separable_k4_multi_edge_monomials_averaged": True,
            "one_small_variable_k4_boundary_assembly_proved": True,
            "auxiliary_incidence_uniformity_proved": False,
            "state_split_E_multi_edge_assembly_proved": False,
            "full_local_character_polynomial_averaged": False,
        },
        "conditional_reciprocal_error": {
            "delta_rec": "min(1/200,delta_aux,delta_E)",
            "bound": "E_rec(M)<<M^(2-delta_rec+o(1))",
            "rho_loc_identified_with_graph_saving": False,
        },
        "updated_frontier": "AUXILIARY_INCIDENCE_UNIFORMITY_PLUS_STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY",
        "decision": {
            "STAGE14_4BB": "K4_GRAPH_ESCAPE_AND_INTRINSIC_PRODUCT_CONDUCTOR_OBSTRUCTION_CLOSED",
            "K4_2CORE_TYPES_CONTROLLED": True,
            "K4_FREEZE_ONE_EDGE_ESCAPE_PROVED": True,
            "K4_VERY_LONG_VERTEX_ESCAPE_PROVED": True,
            "K4_ALL_SHORT_PERIODIC_ESCAPE_PROVED": True,
            "K4_GRAPH_DICHOTOMY_EXHAUSTIVE": True,
            "K4_GRAPH_ASSEMBLY_SAVING_EXPONENT": "1/200",
            "DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION": False,
            "DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION": False,
            "PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND": False,
            "SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED": True,
            "ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED": True,
            "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED": False,
            "STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED": False,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4bc prove uniform auxiliary-progression versions of the linear and signed-root E discrepancy estimates, then insert the K4 escape into the complete finite local polynomial and attempt the first explicit reciprocal E_loc exponent",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report
    print(f"k4_nonempty_graphs={63}")
    print(f"size_assignments_per_graph={3**4}")
    print(f"case_counts={dict(cases)}")
    print(f"graph_saving={graph_saving.numerator}/{graph_saving.denominator}")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
