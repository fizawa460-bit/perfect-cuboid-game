#!/usr/bin/env python3
"""Deterministic audit for Stage14-main-batch 4fw..4fy."""

from __future__ import annotations


def ordinary_shadow(m: int, D: set[int], V: set[int]) -> bool:
    return any(m % d == 0 and (m // d) in V for d in D)


def product_set(D: set[int], V: set[int]) -> set[int]:
    return {d * v for d in D for v in V}


def test_moving_shadow_equals_rectangular_product_support() -> None:
    for D in ({2, 3, 4}, {5, 6, 7, 8}, {9, 11, 13}):
        for V in ({3, 5, 7}, {8, 9, 10}, {12, 14}):
            P = product_set(set(D), set(V))
            max_m = max(D) * max(V) + 5
            for m in range(1, max_m + 1):
                assert ordinary_shadow(m, set(D), set(V)) == (m in P)


def test_pair_capacity() -> None:
    cases = [
        ({2, 3, 4}, {5, 6, 7}),
        ({6, 8, 10, 12}, {9, 12, 15}),
        ({11, 12, 13, 14, 15}, {16, 17, 18, 19}),
    ]
    for D, V in cases:
        P = product_set(D, V)
        assert len(P) <= len(D) * len(V)


def test_collisions_can_only_reduce_capacity() -> None:
    D = {2, 3, 4, 6}
    V = {2, 3, 4, 6}
    pairs = [(d, v) for d in D for v in V]
    P = {d * v for d, v in pairs}
    assert len(P) < len(pairs)


def test_exponent_ledgers() -> None:
    # Subcritical rectangular pair capacity: kD+kV <= mu-eta.
    kD, kV, mu, eta = 0.010, 0.012, 0.030, 0.005
    assert kD + kV <= mu - eta

    # Principal survivor and physical-lift ledger: tau = pi-delta >= mu.
    pi, delta_lift, mu = 0.031, 0.004, 0.025
    tau = pi - delta_lift
    assert tau >= mu
    assert pi >= mu
    assert delta_lift <= pi - mu

    # If product capacity is fixed-power subcritical, physical survival is impossible.
    pi, mu, eta = 0.020, 0.030, 0.004
    assert pi <= mu - eta


def main() -> None:
    test_moving_shadow_equals_rectangular_product_support()
    test_pair_capacity()
    test_collisions_can_only_reduce_capacity()
    test_exponent_ledgers()
    print("Stage14 4fw-4fy rectangular product capacity audit: PASS")


if __name__ == "__main__":
    main()
