#!/usr/bin/env python3
"""Stage14-4ba: deterministic audit of K4 2-core local assembly reduction."""

import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
AZ = ROOT / "stages/stage14/14-4az/result.md"
S5N = ROOT / "stages/stage14/14-s5n/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/k4_2core_assembly_summary.json"

VERTICES = ("A", "B", "C", "D")
EDGES = tuple(itertools.combinations(VERTICES, 2))


def two_core(edge_set):
    vertices = set(VERTICES)
    edges = set(edge_set)
    while True:
        degree = {v: 0 for v in vertices}
        for a, b in edges:
            if a in vertices and b in vertices:
                degree[a] += 1
                degree[b] += 1
        remove = {v for v in vertices if degree[v] <= 1}
        if not remove:
            break
        vertices -= remove
        edges = {e for e in edges if e[0] in vertices and e[1] in vertices}
    degree = {v: 0 for v in vertices}
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    return frozenset(edges), tuple(sorted(degree.values(), reverse=True))


def shape_name(core_edges, degree_sequence):
    e = len(core_edges)
    v = len({x for edge in core_edges for x in edge})
    if e == 0:
        return "empty"
    if (v, e, degree_sequence) == (3, 3, (2, 2, 2)):
        return "triangle_C3"
    if (v, e, degree_sequence) == (4, 4, (2, 2, 2, 2)):
        return "cycle_C4"
    if (v, e, degree_sequence) == (4, 5, (3, 3, 2, 2)):
        return "diamond_K4_minus_edge"
    if (v, e, degree_sequence) == (4, 6, (3, 3, 3, 3)):
        return "complete_K4"
    raise AssertionError((v, e, degree_sequence, core_edges))


def main():
    az = AZ.read_text()
    s5n = S5N.read_text()
    assert "LOWER_DIMENSIONAL_BULK_MODE_INDUCTION_CLOSED=true" in az
    assert "UPPER_COMPLEMENTARY_STATE_FOURIER_SWITCH_CLOSED=true" in az
    assert "ALL_LINEAR_ENDPOINT_MODES_REDUCED_TO_CENTRAL_OR_ONE_SMALL_VARIABLE=true" in az
    assert "SINGLE_LINEAR_EDGE_FULL_DYADIC_SUMMATION_PROVED=true" in s5n
    assert "ALL_SIX_LINEAR_EDGES_INDIVIDUALLY_CLOSED=true" in s5n
    assert "MULTI_EDGE_PRODUCT_CONDUCTOR_OBSTRUCTION_ISOLATED=true" in s5n

    counts = Counter()
    nonempty_peelable = 0
    max_edges = 0
    for mask in range(1 << len(EDGES)):
        edge_set = {EDGES[i] for i in range(len(EDGES)) if (mask >> i) & 1}
        max_edges = max(max_edges, len(edge_set))
        core_edges, degree_sequence = two_core(edge_set)
        name = shape_name(core_edges, degree_sequence)
        counts[name] += 1
        if edge_set and not core_edges:
            nonempty_peelable += 1

        # Core has minimum degree >=2 by construction.
        if core_edges:
            vertices = {x for e in core_edges for x in e}
            deg = {v: 0 for v in vertices}
            for a, b in core_edges:
                deg[a] += 1
                deg[b] += 1
            assert min(deg.values()) >= 2

    expected = {
        "empty": 38,
        "triangle_C3": 16,
        "cycle_C4": 3,
        "diamond_K4_minus_edge": 6,
        "complete_K4": 1,
    }
    assert dict(counts) == expected, (counts, expected)
    assert sum(counts.values()) == 64
    assert nonempty_peelable == 37
    assert max_edges == 6

    # Product-conductor exponent ledger at regular scale M.
    # Incomplete squarefree completion: M^(1/2) * (M^d)^(1/4).
    degree_ledger = []
    for d in (1, 2, 3):
        completion_exp = Fraction(1, 2) + Fraction(d, 4)
        effective_exp = min(Fraction(1, 1), completion_exp)
        saving = Fraction(1, 1) - effective_exp
        degree_ledger.append(
            {
                "degree": d,
                "completion_exponent": str(completion_exp),
                "effective_exponent_after_trivial_cap": str(effective_exp),
                "power_saving_exponent": str(saving),
            }
        )
    assert degree_ledger[0]["power_saving_exponent"] == "1/4"
    assert degree_ledger[1]["power_saving_exponent"] == "0"
    assert degree_ledger[2]["power_saving_exponent"] == "0"

    report = {
        "stage": "14-4ba",
        "classification": "K4_2CORE_ASSEMBLY_REDUCTION_AND_LOCAL_EXPONENT_GATE",
        "imports": {
            "stage14_4az_linear_endpoint_reduction": True,
            "stage14_s5n_one_small_boundary_averaging": True,
            "single_linear_edge_worst_saving_exponent": "1/20",
        },
        "k4_enumeration": {
            "vertex_count": 4,
            "edge_count": 6,
            "edge_subset_count": 64,
            "empty_2core_count": 38,
            "nonempty_peelable_count": 37,
            "nonempty_2core_count": 26,
            "triangle_2core_count": 16,
            "c4_2core_count": 3,
            "diamond_2core_count": 6,
            "k4_2core_count": 1,
        },
        "leaf_peeling": {
            "degree_zero_removable": True,
            "degree_one_uses_single_edge_theory": True,
            "new_reciprocal_edges_created": False,
            "empty_2core_reduces_to_existing_theory": True,
            "first_persistent_linear_object": "K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR",
        },
        "product_conductor": {
            "identity": "prod_j (u/v_j)=(u/prod_j v_j)",
            "completion_template": "T^(1/2) Q^(1/4)",
            "regular_scale_degree_ledger": degree_ledger,
            "degree_two_already_no_saving": True,
            "degree_three_requires_trivial_cap": True,
        },
        "conditional_contract": {
            "reciprocal_exponent": "min(1/20,delta_core,delta_E)",
            "requires_positive_delta_core": True,
            "requires_positive_delta_E": True,
            "diagonal_local_density_term_separate": True,
        },
        "decision": {
            "STAGE14_4BA": "K4_2CORE_ASSEMBLY_REDUCTION_AND_LOCAL_EXPONENT_GATE",
            "S5N_ONE_SMALL_BOUNDARY_AVERAGING_IMPORTED": True,
            "LINEAR_RECIPROCITY_GRAPH_K4": True,
            "EMPTY_2CORE_EDGE_SUBSET_COUNT": 38,
            "NONEMPTY_2CORE_EDGE_SUBSET_COUNT": 26,
            "DEGREE_ONE_LEAF_PEELING_VALID": True,
            "EMPTY_LINEAR_2CORE_MONOMIALS_REDUCE_TO_SINGLE_EDGE_THEORY": True,
            "K4_NONEMPTY_2CORE_PRODUCT_CONDUCTOR_CLOSED": False,
            "STATE_SPLIT_E_BOUNDARY_ASSEMBLY_CLOSED": False,
            "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": False,
            "EXPLICIT_E_LOC_PROVED": False,
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4bb import Stage14-s5o if available and control the four nonempty K4 2-core types by graph-oriented or iterated quadratic-large-sieve bounds; keep the state-split E boundary assembly as a separate exponent gate",
        },
    }

    committed = json.loads(SUMMARY.read_text())
    assert committed == report
    print(json.dumps(report["k4_enumeration"], indent=2))
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
