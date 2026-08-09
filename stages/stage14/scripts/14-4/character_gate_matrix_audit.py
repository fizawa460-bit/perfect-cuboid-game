#!/usr/bin/env python3
"""Stage14-4an: compress s5c selected rows, import s5d full odd rows, audit gate reach.

For a fixed odd support the s5c supported-prime conditions compress, using
`d1*d2*d3 = square`, to one character row at S/H and one row plus a mod-4
sign obstruction at X.  Merged s5d supplies the complementary unselected
odd-prime rows, so all odd bad-prime local conditions are now explicit.

The audit enumerates every primitive oriented Pythagorean base through H<=20k
and every odd support subset in the homogeneous odd-only normalization.  It
checks the compressed selected rows against s5c, then applies the complete s5d
odd local matrix.  This remains a local-Selmer component: the covering-specific
Q_2 classification, global representability/Sha, and physical small-point
height are separate gates.
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
    "S": (1, 1, 0),  # p|S selected -> 12
    "X": (1, 0, 1),  # p|X selected -> 13
    "H": (0, 1, 1),  # p|H selected -> 23
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
    """0 for residue, 1 for nonresidue; p odd and p does not divide a."""
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
    """Compress s5c rows for arbitrary local unit-character bits."""
    checked = 0
    for c1 in (0, 1):
        for c2 in (0, 1):
            for c3 in (0, 1):
                if c1 ^ c2 ^ c3:
                    continue
                for sign in (0, 1):  # chi_p(-1)
                    s_old = ((c1 ^ c2) == 0 and c3 == 0)
                    s_new = (c3 == 0)
                    h_old = ((c2 ^ c3) == 0 and c1 == 0)
                    h_new = (c1 == 0)
                    x_old = ((c1 ^ c3) == 0 and (sign ^ c2) == 0)
                    x_new = (c2 == 0 and sign == 0)
                    assert s_old == s_new
                    assert h_old == h_new
                    assert x_old == x_new
                    checked += 1
    return checked


def odd_d_values(selected, groups):
    """Homogeneous odd-only representatives of d1,d2,d3."""
    d = [1, 1, 1]
    for q in selected:
        lab = LABEL[groups[q]]
        for i in range(3):
            if lab[i]:
                d[i] *= q
    return d


def unit_parts(selected, p, groups):
    d = odd_d_values(selected, groups)
    lab = LABEL[groups[p]]
    if p in selected:
        for i in range(3):
            if lab[i]:
                assert d[i] % p == 0
                d[i] //= p
    return d


def original_s5c_selected_row_ok(selected, p, groups):
    assert p in selected
    a1, a2, a3 = unit_parts(selected, p, groups)
    g = groups[p]
    if g == "S":
        return legendre_bit(a1 * a2, p) == 0 and legendre_bit(a3, p) == 0
    if g == "X":
        return legendre_bit(a1 * a3, p) == 0 and legendre_bit(-a2, p) == 0
    if g == "H":
        return legendre_bit(a2 * a3, p) == 0 and legendre_bit(a1, p) == 0
    raise AssertionError(g)


def compact_selected_row_ok(selected, p, groups):
    """Compressed s5c row in homogeneous odd-only normalization."""
    assert p in selected
    g = groups[p]
    if g == "X" and p % 4 == 3:
        return False
    bit = 0
    for q in selected:
        if q != p and groups[q] != g:
            bit ^= legendre_bit(q, p)
    return bit == 0


def s5d_unselected_row_ok(selected, p, groups):
    """Exact merged-s5d odd local row for an unselected bad prime."""
    assert p not in selected
    d1, d2, d3 = odd_d_values(selected, groups)
    g = groups[p]
    if g == "S":
        return legendre_bit(d3, p) == 0
    if g == "H":
        return legendre_bit(d1, p) == 0
    if g == "X":
        # s5d: chi(d2)=+1 OR chi(-d2)=+1.
        return legendre_bit(d2, p) == 0 or legendre_bit(-d2, p) == 0
    raise AssertionError(g)


def complete_odd_matrix_ok(selected, ps, groups):
    selected_set = set(selected)
    for p in ps:
        if p in selected_set:
            if not compact_selected_row_ok(selected, p, groups):
                return False
        else:
            if not s5d_unselected_row_ok(selected, p, groups):
                return False
    return True


def support_census(S, X, H):
    groups = prime_groups(S, X, H)
    ps = sorted(groups)
    omega = len(ps)

    selected_only = 0
    selected_only_nonempty = 0
    full_odd = 0
    full_odd_nonempty = 0

    guaranteed_singletons = sum(
        1 for p, g in groups.items() if g in ("S", "H") or (g == "X" and p % 4 == 1)
    )
    assert guaranteed_singletons >= 1

    for mask in range(1 << omega):
        selected = tuple(ps[i] for i in range(omega) if (mask >> i) & 1)

        old_ok = all(original_s5c_selected_row_ok(selected, p, groups) for p in selected)
        compressed_ok = all(compact_selected_row_ok(selected, p, groups) for p in selected)
        assert old_ok == compressed_ok, (S, X, H, selected)

        if compressed_ok:
            selected_only += 1
            selected_only_nonempty += bool(selected)

        odd_ok = complete_odd_matrix_ok(selected, ps, groups)
        if odd_ok:
            full_odd += 1
            full_odd_nonempty += bool(selected)

    assert selected_only_nonempty >= guaranteed_singletons >= 1
    assert full_odd >= 1  # empty odd support always passes the homogeneous odd matrix

    return {
        "omega_odd_SXH": omega,
        "all_odd_support_subsets": 1 << omega,
        "selected_row_admissible_supports_including_empty": selected_only,
        "selected_row_admissible_nonempty_supports": selected_only_nonempty,
        "guaranteed_selected_row_singletons": guaranteed_singletons,
        "complete_odd_matrix_admissible_supports_including_empty": full_odd,
        "complete_odd_matrix_admissible_nonempty_supports": full_odd_nonempty,
    }


def quantile(xs, q):
    ys = sorted(xs)
    k = (len(ys) - 1) * q
    lo = int(k)
    hi = min(lo + 1, len(ys) - 1)
    t = k - lo
    return ys[lo] * (1 - t) + ys[hi] * t


def profile_at(B):
    rows = euclid_rows(B)
    omega = []
    sel_counts = []
    sel_ratios = []
    sel_singletons = []
    odd_counts = []
    odd_ratios = []
    no_sel_nonempty = 0
    no_odd_nonempty = 0
    orientations = Counter()

    for S, X, H, m, n, orientation in rows:
        assert S * S + X * X == H * H and gcd(S, X) == 1
        check_five_factor_odd_separation(m, n)
        c = support_census(S, X, H)
        total = c["all_odd_support_subsets"]
        omega.append(c["omega_odd_SXH"])
        sel_counts.append(c["selected_row_admissible_supports_including_empty"])
        sel_ratios.append(c["selected_row_admissible_supports_including_empty"] / total)
        sel_singletons.append(c["guaranteed_selected_row_singletons"])
        odd_counts.append(c["complete_odd_matrix_admissible_supports_including_empty"])
        odd_ratios.append(c["complete_odd_matrix_admissible_supports_including_empty"] / total)
        no_sel_nonempty += int(c["selected_row_admissible_nonempty_supports"] == 0)
        no_odd_nonempty += int(c["complete_odd_matrix_admissible_nonempty_supports"] == 0)
        orientations[orientation] += 1

    return {
        "B": B,
        "eligible_oriented_bases": len(rows),
        "orientation_counts": dict(orientations),
        "odd_bad_prime_count": {
            "mean": sum(omega) / len(omega),
            "median": quantile(omega, 0.5),
            "max": max(omega),
        },
        "homogeneous_selected_rows": {
            "mean_admissible_including_empty": sum(sel_counts) / len(sel_counts),
            "median_admissible_including_empty": quantile(sel_counts, 0.5),
            "max_admissible_including_empty": max(sel_counts),
            "mean_fraction_of_all_support_subsets": sum(sel_ratios) / len(sel_ratios),
            "bases_with_no_nonempty_admissible_support": no_sel_nonempty,
            "mean_guaranteed_singletons": sum(sel_singletons) / len(sel_singletons),
            "min_guaranteed_singletons": min(sel_singletons),
            "max_guaranteed_singletons": max(sel_singletons),
        },
        "homogeneous_complete_odd_matrix": {
            "mean_admissible_including_empty": sum(odd_counts) / len(odd_counts),
            "median_admissible_including_empty": quantile(odd_counts, 0.5),
            "max_admissible_including_empty": max(odd_counts),
            "mean_fraction_of_all_support_subsets": sum(odd_ratios) / len(odd_ratios),
            "bases_with_no_nonempty_admissible_odd_support": no_odd_nonempty,
        },
    }


def main():
    truth_checks = truth_table_redundancy()
    imported = json.loads(AM.read_text())
    profile = [profile_at(B) for B in CUTS]
    expected_A = {r["B"]: r["A"] for r in imported["cuts"]}
    for r in profile:
        assert r["eligible_oriented_bases"] == expected_A[r["B"]]
        assert r["homogeneous_selected_rows"]["bases_with_no_nonempty_admissible_support"] == 0

    report = {
        "metadata": {
            "stage": "14-4an",
            "title": "Euclid-factor complete odd character matrix and gate-reach audit",
            "max_B": max(CUTS),
            "truth_table_redundancy_checks": truth_checks,
        },
        "structural": {
            "five_factor_support": ["m", "n", "m-n", "m+n", "m^2+n^2"],
            "odd_factor_columns_pairwise_disjoint": True,
            "forced_selected_labels": {"S": "12", "X": "13", "H": "23"},
            "compressed_selected_rows": {
                "S/12": "chi_p(a3)=0",
                "X/13": "chi_p(a2)=0 and chi_p(-1)=0; selected X-prime p=1 mod 4",
                "H/23": "chi_p(a1)=0",
            },
            "s5d_unselected_rows": {
                "p|S": "chi_p(d3)=0",
                "p|H": "chi_p(d1)=0",
                "p|X": "chi_p(d2)=0 OR chi_p(-d2)=0; automatic for p=3 mod 4",
            },
            "all_odd_bad_prime_rows_explicit": True,
            "all_odd_rows_reduced_to_reciprocity_bits": True,
            "q2_boundary": (
                "s5d reduces Q2 to 64 product-square squareclass states; covering-specific Q2 solubility "
                "is not yet classified on this branch."
            ),
        },
        "profile": profile,
        "imported_4am_B20000": imported["B20000"],
        "gate_reach": {
            "selected_odd_rows_alone_exclude_any_base": False,
            "selected_rows_reason": (
                "Every primitive oriented base has an odd prime in S or H; that prime as a singleton support "
                "satisfies the selected-prime subsystem."
            ),
            "complete_odd_matrix_is_full_local_selmer_test": False,
            "reason": (
                "All odd bad-prime rows are explicit after s5d, but Q2 covering-specific solubility remains. "
                "The homogeneous odd-only census is a diagnostic slice, not the full Selmer image."
            ),
            "full_exact_Sigma_gate_at_20k": imported["B20000"]["Sigma_over_A"],
            "first_hit_given_rank_interval_at_20k": imported["B20000"]["V_over_R_interval"],
            "interpretation": (
                "The completed odd reciprocity matrix belongs only to the local A->Sigma interface. It cannot "
                "control Sha/global representability in Sigma->R or the physical first-small-point height in R->V."
            ),
        },
        "decision": {
            "STAGE14_4AN": "COMPLETE_ODD_CHARACTER_MATRIX_AND_GATE_REACH_BOUNDARY",
            "S5C_SUPPORTED_ROWS_COMPRESSED_USING_GLOBAL_SQUARECLASS": True,
            "SELECTED_ODD_SYSTEM_THREE_BLOCK_AFFINE_F2": True,
            "SELECTED_X_PRIME_REQUIRES_P_EQ_1_MOD4": True,
            "S5D_ALL_ODD_BAD_PRIME_ROWS_IMPORTED": True,
            "ALL_ODD_BAD_PRIME_ROWS_EXPLICIT": True,
            "ALL_ODD_ROWS_REDUCED_TO_RECIPROCITY_BITS": True,
            "SELECTED_ODD_ROWS_ALONE_SIEVE_BASES": False,
            "Q2_COVERING_SPECIFIC_SOLUBILITY_CLASSIFIED": False,
            "FULL_LOCAL_SELMER_MATRIX_COMPLETE": False,
            "CHARACTER_MATRIX_CONTROLS_SIGMA_TO_R": False,
            "CHARACTER_MATRIX_CONTROLS_R_TO_V": False,
            "HEIGHT_COUPLING_REQUIRED_FOR_MAIN_THINNING": True,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4ao finish Q2 covering-specific 64-state classification, then formulate a height-weighted descent-class count for R->V",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(profile[-1], indent=2))
    print(json.dumps(report["gate_reach"], indent=2))
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
