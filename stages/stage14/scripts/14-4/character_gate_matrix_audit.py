#!/usr/bin/env python3
"""Stage14-4an: compress the selected-prime s5c Hilbert rows and audit gate reach.

This stage deliberately studies the *selected odd support-prime subsystem* only.
It does not pretend that omitted bad primes or Q_2 are automatic.  For a fixed
odd support and fixed p-unit normalization, the global square-class relation

    d1*d2*d3 = square

makes the two s5c character equations at an S- or H-prime redundant, and
separates the X-prime sign obstruction.  In F_2 character notation:

    S / 12 : chi_p(a3) = 0
    X / 13 : chi_p(a2) = 0 and chi_p(-1) = 0
    H / 23 : chi_p(a1) = 0.

For the homogeneous odd-only normalization (no 2/sign affine offset), this is
a three-block reciprocity system between selected primes dividing S, X, H.
The audit enumerates every primitive oriented Pythagorean base through H<=20k
and every odd support subset, checks equivalence with the original s5c rows,
and records how much the selected-prime subsystem thins *support choices*.

Crucially, this subsystem alone cannot sieve bases: every genuine base has a
nonempty singleton support at an S- or H-prime satisfying all selected-prime
rows.  Exact A->Sigma control therefore requires the omitted-bad-prime rows and
the complete Q_2 table.  Even exact Sigma is only the first gate; 4am shows the
observed finite thinning is dominated later by R->V.
"""

from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-4/character_gate_matrix_audit.json"
AM = ROOT / "stages/stage14/data/14-4/rank_smallpoint_factor_summary.json"
CUTS = (2000, 5000, 10000, 20000)

LABEL = {
    "S": (1, 1, 0),  # selected p|S -> 12
    "X": (1, 0, 1),  # selected p|X -> 13
    "H": (0, 1, 1),  # selected p|H -> 23
}


def odd_prime_factors(n):
    n = abs(int(n))
    out = []
    while n % 2 == 0:
        n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.append(n)
    return out


def legendre_bit(a, p):
    """0 for quadratic residue, 1 for nonresidue; p odd and p∤a."""
    a %= p
    if a == 0:
        raise AssertionError((a, p))
    v = pow(a, (p - 1) // 2, p)
    if v == 1:
        return 0
    if v == p - 1:
        return 1
    raise AssertionError((a, p, v))


def euclid_rows(B):
    rows = []
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            if gcd(m, n) != 1 or ((m - n) & 1) == 0:
                continue
            u = m * m - n * n
            v = 2 * m * n
            h = m * m + n * n
            if h > B:
                continue
            # Both oriented first-face choices belong to A(B).
            rows.append((u, v, h, m, n, "odd-leg-shared"))
            rows.append((v, u, h, m, n, "even-leg-shared"))
        m += 1
    return rows


def factor_columns(m, n):
    return {
        "m": m,
        "n": n,
        "m-n": m - n,
        "m+n": m + n,
        "m2+n2": m * m + n * n,
    }


def prime_groups(S, X, H):
    groups = {}
    for g, value in (("S", S), ("X", X), ("H", H)):
        for p in odd_prime_factors(value):
            assert p not in groups, (S, X, H, p, groups[p], g)
            groups[p] = g
    return groups


def check_five_factor_odd_separation(m, n):
    cols = factor_columns(m, n)
    names = list(cols)
    supports = {k: set(odd_prime_factors(v)) for k, v in cols.items()}
    for a, b in combinations(names, 2):
        assert supports[a].isdisjoint(supports[b]), (m, n, a, b, supports[a] & supports[b])


def truth_table_redundancy():
    """Check the compression for arbitrary local unit character bits.

    ci=chi_p(ai), with c1+c2+c3=0 from d1*d2*d3 being a local square.
    s=chi_p(-1).
    """
    checked = 0
    for c1 in (0, 1):
        for c2 in (0, 1):
            for c3 in (0, 1):
                if c1 ^ c2 ^ c3:
                    continue
                for s in (0, 1):
                    S_original = ((c1 ^ c2) == 0 and c3 == 0)
                    S_compact = (c3 == 0)
                    H_original = ((c2 ^ c3) == 0 and c1 == 0)
                    H_compact = (c1 == 0)
                    X_original = ((c1 ^ c3) == 0 and (s ^ c2) == 0)
                    X_compact = (c2 == 0 and s == 0)
                    assert S_original == S_compact
                    assert H_original == H_compact
                    assert X_original == X_compact
                    checked += 1
    return checked


def unit_parts(selected, p, groups):
    """Homogeneous odd-only p-unit parts a1,a2,a3 for a fixed support."""
    a = [1, 1, 1]
    for q in selected:
        if q == p:
            continue
        lab = LABEL[groups[q]]
        for i in range(3):
            if lab[i]:
                a[i] *= q
    return a


def original_s5c_row_ok(selected, p, groups):
    a1, a2, a3 = unit_parts(selected, p, groups)
    g = groups[p]
    if g == "S":
        return legendre_bit(a1 * a2, p) == 0 and legendre_bit(a3, p) == 0
    if g == "X":
        return legendre_bit(a1 * a3, p) == 0 and legendre_bit(-a2, p) == 0
    if g == "H":
        return legendre_bit(a2 * a3, p) == 0 and legendre_bit(a1, p) == 0
    raise AssertionError(g)


def compact_row_ok(selected, p, groups):
    """Three-block compact form for the homogeneous odd-only normalization."""
    g = groups[p]
    if g == "X" and p % 4 == 3:
        return False
    bit = 0
    for q in selected:
        if q == p:
            continue
        if groups[q] != g:
            bit ^= legendre_bit(q, p)
    return bit == 0


def support_census(S, X, H):
    groups = prime_groups(S, X, H)
    ps = sorted(groups)
    omega = len(ps)
    admissible = 0
    nonempty = 0
    sizes = Counter()

    # Every S/H singleton passes; an X singleton passes iff p=1 mod 4.
    guaranteed_singletons = sum(
        1 for p, g in groups.items() if g in ("S", "H") or (g == "X" and p % 4 == 1)
    )
    assert guaranteed_singletons >= 1

    for mask in range(1 << omega):
        selected = tuple(ps[i] for i in range(omega) if (mask >> i) & 1)
        ok_original = True
        ok_compact = True
        for p in selected:
            ok_original &= original_s5c_row_ok(selected, p, groups)
            ok_compact &= compact_row_ok(selected, p, groups)
        assert ok_original == ok_compact, (S, X, H, selected)
        if ok_compact:
            admissible += 1
            sizes[len(selected)] += 1
            nonempty += bool(selected)

    assert nonempty >= guaranteed_singletons >= 1
    return {
        "omega_odd_SXH": omega,
        "all_odd_support_subsets": 1 << omega,
        "selected_row_admissible_supports_including_empty": admissible,
        "selected_row_admissible_nonempty_supports": nonempty,
        "guaranteed_singleton_supports": guaranteed_singletons,
        "support_size_histogram": dict(sorted(sizes.items())),
    }


def quantile(xs, q):
    ys = sorted(xs)
    if not ys:
        return None
    k = (len(ys) - 1) * q
    lo = int(k)
    hi = min(lo + 1, len(ys) - 1)
    t = k - lo
    return ys[lo] * (1 - t) + ys[hi] * t


def profile_at(B):
    rows = euclid_rows(B)
    support_counts = []
    ratios = []
    omegas = []
    singletons = []
    no_nonempty = 0
    orientations = Counter()

    for S, X, H, m, n, orientation in rows:
        assert S * S + X * X == H * H and gcd(S, X) == 1
        check_five_factor_odd_separation(m, n)
        c = support_census(S, X, H)
        support_counts.append(c["selected_row_admissible_supports_including_empty"])
        ratios.append(c["selected_row_admissible_supports_including_empty"] / c["all_odd_support_subsets"])
        omegas.append(c["omega_odd_SXH"])
        singletons.append(c["guaranteed_singleton_supports"])
        no_nonempty += int(c["selected_row_admissible_nonempty_supports"] == 0)
        orientations[orientation] += 1

    return {
        "B": B,
        "eligible_oriented_bases": len(rows),
        "orientation_counts": dict(orientations),
        "odd_bad_prime_count": {
            "mean": sum(omegas) / len(omegas),
            "median": quantile(omegas, 0.5),
            "max": max(omegas),
        },
        "homogeneous_selected_row_supports": {
            "mean_admissible_including_empty": sum(support_counts) / len(support_counts),
            "median_admissible_including_empty": quantile(support_counts, 0.5),
            "max_admissible_including_empty": max(support_counts),
            "mean_fraction_of_all_support_subsets": sum(ratios) / len(ratios),
            "bases_with_no_nonempty_admissible_support": no_nonempty,
            "mean_guaranteed_singletons": sum(singletons) / len(singletons),
            "min_guaranteed_singletons": min(singletons),
            "max_guaranteed_singletons": max(singletons),
        },
    }


def main():
    truth_checks = truth_table_redundancy()
    imported = json.loads(AM.read_text())
    profile = [profile_at(B) for B in CUTS]
    expected_A = {r["B"]: r["A"] for r in imported["cuts"]}
    for r in profile:
        assert r["eligible_oriented_bases"] == expected_A[r["B"]]
        assert r["homogeneous_selected_row_supports"]["bases_with_no_nonempty_admissible_support"] == 0

    report = {
        "metadata": {
            "stage": "14-4an",
            "title": "Euclid-factor selected-prime character matrix and gate-reach audit",
            "max_B": max(CUTS),
            "truth_table_redundancy_checks": truth_checks,
        },
        "structural": {
            "five_factor_support": ["m", "n", "m-n", "m+n", "m^2+n^2"],
            "odd_factor_columns_pairwise_disjoint": True,
            "forced_selected_labels": {"S": "12", "X": "13", "H": "23"},
            "compressed_selected_rows": {
                "S/12": "chi_p(a3)=0",
                "X/13": "chi_p(a2)=0 and chi_p(-1)=0, hence selected X-prime p=1 mod 4",
                "H/23": "chi_p(a1)=0",
            },
            "homogeneous_three_block_rows": {
                "p_in_S": "sum_{q selected in X union H} [q/p] = 0",
                "p_in_X": "p=1 mod 4 and sum_{q selected in S union H} [q/p] = 0",
                "p_in_H": "sum_{q selected in S union X} [q/p] = 0",
            },
            "affine_offset_note": (
                "For a general covering, p-unit sign/2 normalization contributes affine character offsets. "
                "Quadratic reciprocity supplies the odd cross-prime matrix; mod-8/2-adic data are additionally required."
            ),
            "global_support_equations_are_support_gated": (
                "For fixed selected support the rows are linear character equations; allowing support itself to vary gates "
                "each row by the support bit and produces a quadratic F2 support-selection system."
            ),
        },
        "profile": profile,
        "imported_4am_B20000": imported["B20000"],
        "gate_reach": {
            "selected_odd_rows_alone_exclude_any_base": False,
            "reason": (
                "Every primitive oriented Pythagorean base has an odd prime in S or H; selecting that prime alone "
                "satisfies every selected-prime row in the homogeneous odd subsystem. Omitted bad-prime rows and Q2 "
                "are therefore indispensable even to turn the character skeleton into an A->Sigma base sieve."
            ),
            "full_exact_Sigma_gate_at_20k": imported["B20000"]["Sigma_over_A"],
            "first_hit_given_rank_interval_at_20k": imported["B20000"]["V_over_R_interval"],
            "interpretation": (
                "The reciprocity matrix is a local-Selmer interface. It does not control Sha/global representability "
                "or the physical first-small-point height. Stage14-4am shows the latter is the dominant finite thinning gate."
            ),
        },
        "decision": {
            "STAGE14_4AN": "COMPLETE_SELECTED_PRIME_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY",
            "S5C_SUPPORTED_ROWS_COMPRESSED_USING_GLOBAL_SQUARECLASS": True,
            "SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2": True,
            "SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4": True,
            "SELECTED_ODD_ROWS_ALONE_FORM_COMPLETE_SELMER_TEST": False,
            "SELECTED_ODD_ROWS_ALONE_SIEVE_BASES": False,
            "UNSELECTED_ODD_AND_Q2_REQUIRED_FOR_A_TO_SIGMA": True,
            "CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R": False,
            "CHARACTER_MATRIX_CONTROLS_R_TO_V": False,
            "HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING": True,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ao complete the full local matrix via s5d handoff, then formulate a height-weighted descent-class count for R->V",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(profile[-1], indent=2))
    print(json.dumps(report["gate_reach"], indent=2))
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
