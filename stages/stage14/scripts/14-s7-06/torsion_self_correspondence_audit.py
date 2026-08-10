#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-06.

Checks the merged s7-05 physical same-twist receiver and the merged 4bt
squarefree j=1728 torsion gate on the frozen B=50,000 physical graph.

The audit verifies:
- gcd(k,xi)=1 and n=k*xi squarefree;
- n>1 for every frozen physical pair;
- the only possible rational torsion difference on the imported 4bt theorem
  is the unique nonzero 2-torsion point;
- the corresponding quartic involution (z,y)->(-z,-y) cannot pair two
  canonical positive physical lifts;
- the two physical lifts are distinct;
- n<Q^4, n<S^4 and n<(QS)^2<=4B^2;
- fixed-n ordered (k,xi) factorization multiplicity is bounded by 2^omega(n);
- current exponent / required saving ledger remains 20/21, 1/21, 2/21.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S705 = ROOT / "stages/stage14/scripts/14-s7-05/joint_twist_pair_receiver_audit.py"
BT = ROOT / "stages/stage14/14-4bt/result.md"
B = 50_000


def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_squarefree(n):
    if n <= 0:
        return False
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p = 3 if p == 2 else p + 2
    return True


def omega(n):
    out = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            out += 1
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out += 1
    return out


def audit_merged_4bt_boundary():
    txt = BT.read_text()
    required = [
        "STAGE14_4BT=SQUAREFREE_J1728_TWIST_COMPRESSION_AND_TORSION_PAIR_EXCLUSION",
        "XI_K_COPRIME=true",
        "TWIST_PARAMETER_N_SQUAREFREE=true",
        "PHYSICAL_TWIST_PARAMETER_N_GT_1=true",
        "SQUAREFREE_N_GT_1_RATIONAL_TORSION=Z/2Z",
        "PHYSICAL_TWO_POINT_DIFFERENCE_TORSION=false",
        "PHYSICAL_TWO_POINT_DIFFERENCE_INFINITE_ORDER=true",
    ]
    for flag in required:
        assert flag in txt, flag
    return True


def physical_same_twist_rows():
    mod = runpy.run_path(str(S705))
    s703_mod, rows = mod["physical_rows"]()
    half_angles = s703_mod["half_angles"]
    transfer_f3 = s703_mod["transfer_f3"]
    canonical_label = mod["canonical_label"]

    out = []
    for F1, F2, dspace in rows:
        F3, _ = transfer_f3(F1, F2, dspace)
        _, a, b = half_angles(F2)
        _, c, d = half_angles(F3)

        u = Fraction(b * c, a * d)
        w = Fraction(a * c, b * d)
        assert 0 < w < u < 1

        lu = canonical_label(u)
        lw = canonical_label(w)
        assert lu["xi"] == lw["xi"]
        assert lu["k"] == lw["k"]

        k = lu["k"]
        xi = lu["xi"]
        n = k * xi
        Q = lu["Q"]
        S = lw["Q"]
        z1 = lu["z"]
        z2 = lw["z"]

        out.append({
            "k": k,
            "xi": xi,
            "n": n,
            "Q": Q,
            "S": S,
            "z1": z1,
            "z2": z2,
            "Hmult": Q * S,
            "dspace": dspace,
        })
    assert len(out) == 124
    return out


def audit_physical_torsion_gate(rows):
    labels_by_n = defaultdict(set)
    max_n = 0
    max_ratio = Fraction(0, 1)

    for row in rows:
        k = row["k"]
        xi = row["xi"]
        n = row["n"]
        Q = row["Q"]
        S = row["S"]
        z1 = row["z1"]
        z2 = row["z2"]
        Hmult = row["Hmult"]

        # Exact squarefree twist compression.
        assert gcd(k, xi) == 1
        assert is_squarefree(k)
        assert is_squarefree(xi)
        assert is_squarefree(n)
        assert n == k * xi
        assert n > 1

        # No rational 4-torsion branch: for squarefree n>1, n is not a square.
        # The merged 4bt duplication analysis reduces a rational half of (0,0)
        # to y^2=16*n^3, hence n square.  We audit the excluded condition.
        assert not is_square(n)

        # Canonical physical lifts are positive and distinct.  The unique
        # nontrivial torsion self-correspondence sends z to -z, so it cannot
        # map one positive lift to the other.
        assert z1 > 0 and z2 > 0
        assert z1 != z2
        assert z2 != -z1

        # Exact size receiver.
        assert n < Q ** 4
        assert n < S ** 4
        assert n < Hmult ** 2
        assert Hmult <= 2 * B
        assert n < 4 * B * B

        labels_by_n[n].add((k, xi))
        max_n = max(max_n, n)
        max_ratio = max(max_ratio, Fraction(n, Hmult * Hmult))

    # Since n is squarefree, every ordered coprime squarefree factorization
    # is obtained by assigning each prime factor to k or xi.
    for n, labs in labels_by_n.items():
        assert len(labs) <= 2 ** omega(n)
        for k, xi in labs:
            assert k * xi == n and gcd(k, xi) == 1

    return labels_by_n, max_n, max_ratio


def exponent_ledger():
    current = Fraction(20, 21)
    direct = Fraction(1, 1) - current
    squared = 2 * direct
    sqrt_gap = current - Fraction(1, 2)
    assert direct == Fraction(1, 21)
    assert squared == Fraction(2, 21)
    assert sqrt_gap == Fraction(19, 42)
    return current, direct, squared, sqrt_gap


def main():
    assert audit_merged_4bt_boundary()
    rows = physical_same_twist_rows()
    labels_by_n, max_n, max_ratio = audit_physical_torsion_gate(rows)
    current, direct, squared, sqrt_gap = exponent_ledger()

    print(f"ORDERED_PHYSICAL_INCIDENCES={len(rows)}")
    print(f"PHYSICAL_SQUAREFREE_N_COUNT={len(labels_by_n)}")
    print(f"MAX_PHYSICAL_N={max_n}")
    print(f"MAX_N_OVER_HMULT_SQUARED={max_ratio}")
    print(f"CURRENT_WHOLE_FAMILY_EXPONENT={current}")
    print(f"DIRECT_TWIST_SAVING_REQUIRED={direct}")
    print(f"SQUARED_ENERGY_SAVING_REQUIRED={squared}")
    print(f"CURRENT_GAP_TO_SQRT={sqrt_gap}")
    print("MERGED_S7_05_RECEIVER_AUDIT=true")
    print("MERGED_4BT_TORSION_BOUNDARY_AUDIT=true")
    print("XI_K_COPRIME_AUDIT=true")
    print("SQUAREFREE_N_AUDIT=true")
    print("PHYSICAL_N_GT_1_AUDIT=true")
    print("NO_RATIONAL_4_TORSION_CONDITION_AUDIT=true")
    print("POSITIVE_LIFT_TORSION_CORRESPONDENCE_EXCLUSION_AUDIT=true")
    print("PHYSICAL_TWO_POINT_DIFFERENCE_INFINITE_ORDER_THEOREM_IMPORTED=true")
    print("PHYSICAL_TWIST_PAIR_POSITIVE_RANK_GATE=true")
    print("FIXED_N_FACTORIZATION_MULTIPLICITY_AUDIT=true")
    print("PHYSICAL_N_BOUND_B_SQUARED_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
