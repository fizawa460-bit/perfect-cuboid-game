#!/usr/bin/env python3
"""Deterministic audit for Stage14-s6-10.

Checks:
- merged s6-09 and 4bm boundaries;
- universal rational anchor on the target quartic family;
- actual finite physical fibers and active-direction/edge inequalities;
- abstract matching obstruction to degree-only active-vertex saving;
- exact exponent ledger for the residual receiver and s6 closure.
"""
from fractions import Fraction
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S609 = ROOT / 'stages/stage14/14-s6-09/result.md'
BM = ROOT / 'stages/stage14/14-4bm/result.md'
S607_AUDIT = ROOT / 'stages/stage14/scripts/14-s6-07/dual_half_angle_gcd_matrix_audit.py'


def fab(a, b, p, q):
    return (b*b*p*p-a*a*q*q) * (b*b*q*q-a*a*p*p)


def main():
    s609 = S609.read_text()
    bm = BM.read_text()
    assert 'STAGE14_S6_09=COMPLETE_FIXED_DIRECTION_SQUARECLASS_ENERGY_TRANSFER_AND_ACTIVE_DIRECTION_BARRIER' in s609
    assert 'FIXED_F2_PHYSICAL_F3_MULTIPLICITY=B^o(1)' in s609
    assert 'PHYSICAL_EDGE_ACTIVE_DIRECTION_EXPONENT_EQUIVALENCE=true' in s609
    assert 'STAGE14_4BM=CROSS_SECTOR_POWER_SAVING_AND_SQUARE_NEUTRAL_GCD_CELL_BARRIER' in bm
    assert 'CROSS_SECTOR_BOUND=B^(61/63+o(1))' in bm
    assert 'UNRESOLVED_GOOD_GCD_CELL_SCALE=4/21' in bm

    # Universal soluble boundary anchor for every direction 0<a<b.
    anchor_checks = 0
    for a in range(1, 25):
        for b in range(a + 1, 30):
            assert fab(a, b, 0, 1) == -(a*b)**2
            anchor_checks += 1

    # Finite physical graph: group exact transferred edges by active F2.
    mod = runpy.run_path(str(S607_AUDIT))
    rows = mod['ordered_physical_edges']()
    audit_row = mod['audit_row']
    assert rows
    fibers = {}
    reverse = {}
    for F1, F2, space_d in rows:
        out = audit_row(F1, F2, space_d)
        F3 = out['F3']
        fibers.setdefault(F2, set()).add(F3)
        reverse.setdefault(F3, set()).add(F2)

    edge_count = len(rows)
    active_left = len(fibers)
    active_right = len(reverse)
    max_left_degree = max(map(len, fibers.values()))
    max_right_degree = max(map(len, reverse.values()))
    assert active_left <= edge_count
    assert active_right <= edge_count
    assert edge_count <= active_left * max_left_degree
    assert edge_count <= active_right * max_right_degree

    # Degree/collision information alone cannot force active-vertex sparsity:
    # a perfect matching has degree one and all vertices active.
    for n in (1, 2, 7, 64):
        edges = {(i, i) for i in range(n)}
        left = {i for i, _ in edges}
        right = {j for _, j in edges}
        assert len(edges) == len(left) == len(right) == n
        assert max(sum(1 for x, _ in edges if x == i) for i in left) == 1
        assert max(sum(1 for _, y in edges if y == j) for j in right) == 1

    # Exact exponent ledger.
    assert Fraction(41, 42) - Fraction(61, 63) == Fraction(1, 126)
    assert Fraction(61, 63) - Fraction(1, 2) == Fraction(59, 126)
    assert Fraction(20, 21) - Fraction(1, 2) == Fraction(19, 42)
    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)

    print(f'ordered physical incidences audited={edge_count}')
    print(f'active frozen F2 directions={active_left}')
    print(f'active frozen F3 directions={active_right}')
    print(f'max frozen F2->F3 degree={max_left_degree}')
    print(f'max frozen F3->F2 degree={max_right_degree}')
    print(f'universal boundary anchor checks={anchor_checks}')
    print('MERGED_S6_09_BOUNDARY_AUDIT=true')
    print('MERGED_4BM_BOUNDARY_AUDIT=true')
    print('UNIVERSAL_BOUNDARY_RATIONAL_ANCHOR_AUDIT=true')
    print('ACTIVE_DIRECTION_EDGE_INEQUALITY_AUDIT=true')
    print('MATCHING_OBSTRUCTION_AUDIT=true')
    print('S6_10_EXPONENT_LEDGER_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
