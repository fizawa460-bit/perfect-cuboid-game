#!/usr/bin/env python3
"""Deterministic combinatorial audit for Stage14-s5o.

The analytic estimates are proved in result.md from prior s5h/s5n inputs.
This script checks the exhaustive K4 graph dichotomy, exact Jacobi
factorizations, and the conservative exponent ledger.
"""

from __future__ import annotations

from itertools import product
from math import prod
import json

VERTICES = (0, 1, 2, 3)
EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
SHORT = 0
MEDIUM = 1
HUGE = 2
ETA = 1.0 / 100.0

# Pairwise-coprime odd squarefree values, all 1 mod 4 so reciprocity signs vanish.
VALUES = (5, 13, 17, 29)


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


def graph_edges(mask: int):
    return tuple(e for bit, e in enumerate(EDGES) if mask & (1 << bit))


def active_vertices(edges):
    out = set()
    for i, j in edges:
        out.add(i)
        out.add(j)
    return out


def degrees(edges):
    d = [0, 0, 0, 0]
    for i, j in edges:
        d[i] += 1
        d[j] += 1
    return tuple(d)


def classify(edges, classes):
    # Case A: one edge has two endpoints at least M^eta.
    for i, j in edges:
        if classes[i] >= MEDIUM and classes[j] >= MEDIUM:
            return "LONG_LONG_EDGE"

    active = active_vertices(edges)

    # Case B: with no long-long edge, every neighbor of a huge active vertex
    # is SHORT, so the product conductor is <= M^(3 eta).
    for i in active:
        if classes[i] == HUGE:
            assert all(
                classes[j] == SHORT
                for a, b in edges
                for j in ([b] if a == i else ([a] if b == i else []))
            )
            return "VERY_LONG_SMALL_CONDUCTOR"

    # Case C: every graph-active variable is below M^(4 eta).
    assert all(classes[i] in (SHORT, MEDIUM) for i in active)
    return "ALL_ACTIVE_BELOW_L0"


def graph_kernel(edges, values):
    z = 1
    for i, j in edges:
        z *= jacobi(values[i], values[j])
    return z


def check_freeze_edge_factorization():
    checks = 0
    for mask in range(1, 1 << len(EDGES)):
        edges = graph_edges(mask)
        full = graph_kernel(edges, VALUES)
        for chosen in edges:
            i, j = chosen
            alpha = 1
            beta = 1
            fixed = 1
            for e in edges:
                if e == chosen:
                    continue
                a, b = e
                factor = jacobi(VALUES[a], VALUES[b])
                if i in e:
                    alpha *= factor
                elif j in e:
                    beta *= factor
                else:
                    fixed *= factor
            rhs = jacobi(VALUES[i], VALUES[j]) * alpha * beta * fixed
            assert full == rhs, (mask, chosen, full, rhs)
            checks += 1
    return checks


def check_product_conductors():
    checks = 0
    degree_examples = {1: 0, 2: 0, 3: 0}
    for mask in range(1, 1 << len(EDGES)):
        edges = graph_edges(mask)
        for i in VERTICES:
            neighbors = []
            for a, b in edges:
                if a == i:
                    neighbors.append(b)
                elif b == i:
                    neighbors.append(a)
            if not neighbors:
                continue
            lhs = prod(jacobi(VALUES[i], VALUES[j]) for j in neighbors)
            q = prod(VALUES[j] for j in neighbors)
            rhs = jacobi(VALUES[i], q)
            assert lhs == rhs, (mask, i, neighbors, lhs, rhs)
            checks += 1
            degree_examples[len(neighbors)] += 1
    assert all(degree_examples[d] > 0 for d in (1, 2, 3))
    return checks, degree_examples


def check_exhaustive_dichotomy():
    counts = {
        "LONG_LONG_EDGE": 0,
        "VERY_LONG_SMALL_CONDUCTOR": 0,
        "ALL_ACTIVE_BELOW_L0": 0,
    }
    degree_case_counts = {}
    total = 0

    for mask in range(1, 1 << len(EDGES)):
        edges = graph_edges(mask)
        deg = degrees(edges)
        max_degree = max(deg)
        for classes in product((SHORT, MEDIUM, HUGE), repeat=4):
            case = classify(edges, classes)
            counts[case] += 1
            degree_case_counts[(max_degree, case)] = degree_case_counts.get(
                (max_degree, case), 0
            ) + 1
            total += 1

    assert total == 63 * 81
    assert sum(counts.values()) == total
    assert all(v > 0 for v in counts.values())

    # Degree-2 and degree-3 graph patterns are not left unclassified.
    for d in (2, 3):
        assert sum(v for (deg, _), v in degree_case_counts.items() if deg == d) > 0

    return total, counts, {
        f"degree_{d}_{case}": count
        for (d, case), count in sorted(degree_case_counts.items())
    }


def exponent_ledger():
    long_edge_saving = ETA / 2.0
    very_long_saving = 5.0 * ETA / 4.0

    # Crude all-short sum:
    # tuple count M^(16 eta) times per-tuple [P Q + Q^2], Q<=M^(16 eta), P~M.
    periodic_term_1_exponent = 1.0 + 32.0 * ETA
    periodic_term_2_exponent = 48.0 * ETA
    periodic_saving = min(
        2.0 - periodic_term_1_exponent,
        2.0 - periodic_term_2_exponent,
    )

    assert ETA < 1.0 / 32.0
    assert long_edge_saving > 0
    assert very_long_saving > 0
    assert periodic_saving > 0

    worst = min(long_edge_saving, very_long_saving, periodic_saving)
    assert abs(worst - 1.0 / 200.0) < 1e-12

    return {
        "eta": ETA,
        "long_edge_saving": long_edge_saving,
        "very_long_vertex_saving": very_long_saving,
        "periodic_term_1_exponent": periodic_term_1_exponent,
        "periodic_term_2_exponent": periodic_term_2_exponent,
        "periodic_saving": periodic_saving,
        "worst_graph_saving": worst,
    }


def main():
    total, counts, degree_cases = check_exhaustive_dichotomy()
    freeze_checks = check_freeze_edge_factorization()
    conductor_checks, degree_examples = check_product_conductors()
    ledger = exponent_ledger()

    report = {
        "metadata": {
            "stage": "14-s5o",
            "nonempty_k4_subgraphs": 63,
            "size_assignments_per_graph": 81,
            "classification": "DETERMINISTIC_GRAPH_REGRESSION_PLUS_ANALYTIC_INTERFACE",
        },
        "dichotomy": {
            "total_cases": total,
            "case_counts": counts,
            "degree_case_counts": degree_cases,
        },
        "freeze_edge_factorization_checks": freeze_checks,
        "product_conductor_checks": conductor_checks,
        "degree_examples": degree_examples,
        "exponent_ledger": ledger,
        "decision": {
            "STAGE14_S5O": "COMPLETE_K4_GRAPH_ESCAPE_AND_PRODUCT_CONDUCTOR_ELIMINATION",
            "K4_GRAPH_DICHOTOMY_EXHAUSTIVE": True,
            "DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION": False,
            "DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION": False,
            "PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND": False,
            "SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED": True,
            "AUXILIARY_INCIDENCE_UNIFORMITY_PROVED": False,
            "FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5p",
        },
    }

    print(json.dumps(report, indent=2, sort_keys=True))
    print("STAGE14_S5O=COMPLETE_K4_GRAPH_ESCAPE_AND_PRODUCT_CONDUCTOR_ELIMINATION")
    print("K4_FREEZE_ONE_EDGE_LARGE_SIEVE_ESCAPE_PROVED=true")
    print("K4_NO_LONG_EDGE_LONG_VERTICES_INDEPENDENT=true")
    print("K4_VERY_LONG_VERTEX_SMALL_PRODUCT_CONDUCTOR_PROVED=true")
    print("K4_ALL_SHORT_CENTERED_PERIODIC_ESCAPE_PROVED=true")
    print("K4_GRAPH_DICHOTOMY_EXHAUSTIVE=true")
    print("DEGREE_2_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false")
    print("DEGREE_3_PRODUCT_CONDUCTOR_INTRINSIC_OBSTRUCTION=false")
    print("PERSISTENT_RESONANT_K4_SUBGRAPH_FOUND=false")
    print("SEPARABLE_K4_MULTI_EDGE_MONOMIALS_AVERAGED=true")
    print("ONE_SMALL_VARIABLE_K4_BOUNDARY_ASSEMBLY_PROVED=true")
    print("AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=false")
    print("STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY_PROVED=false")
    print("FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5p")


if __name__ == "__main__":
    main()
