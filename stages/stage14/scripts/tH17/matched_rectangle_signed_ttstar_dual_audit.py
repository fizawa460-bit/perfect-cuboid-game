#!/usr/bin/env python3
"""Stage14-tH17 R2 deterministic matched-rectangle TT*/dual audit."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
T59 = ROOT / "stages/stage14/14-t59/result.md"
T61 = ROOT / "stages/stage14/14-t61/result.md"
T62 = ROOT / "stages/stage14/14-t62/result.md"
R2 = ROOT / "stages/stage14/14-tH17/r2.md"
SUMMARY = ROOT / "stages/stage14/data/tH17/matched_rectangle_signed_ttstar_dual_summary.json"


def matmul(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def main() -> None:
    t59 = T59.read_text()
    t61 = T61.read_text()
    t62 = T62.read_text()
    r2 = R2.read_text()
    summary = json.loads(SUMMARY.read_text())

    assert "STAGE14_T59=COMPLETE_EXACT_TWO_COMPARATOR_ORTHOGONAL_RECTANGLE_REDUCTION" in t59
    assert "BALANCED_RECTANGLE_ENERGY_PRODUCT_LE_2_R2=true" in t59
    assert "STAGE14_T61=COMPLETE_POLAR_SCHATTEN_OBSTRUCTION_AND_SIGNED_RECTANGLE_REOPENING" in t61
    assert "POLAR_ZERO_LOSS_SHORTCUT_VALID=false" in t61
    assert "STAGE14_T62=COMPLETE_MATCHED_RECTANGLE_FRAME_AND_DUAL_PROJECTION_REDUCTION" in t62
    assert "MATCHED_BLOCK_PROJECTION_BESSEL_ZERO_LOSS=true" in t62
    assert "PHYSICAL_RECEIVER_EQUALS_MASS_VECTOR_RAYLEIGH_BOUND=true" in t62

    # Synthetic disjoint matched blocks on six states: R0={0,1}, R1={2,3,4}, R2={5}.
    blocks = [[0, 1], [2, 3, 4], [5]]
    masses = [len(b) for b in blocks]

    # Exact block Bessel with rational test values.
    f = [Fraction(2), Fraction(-1), Fraction(3), Fraction(1), Fraction(-2), Fraction(4)]
    projected_energy = sum((sum(f[s] for s in block) ** 2) / len(block) for block in blocks)
    source_energy = sum(x * x for x in f)
    assert projected_energy <= source_energy

    # Five synthetic signed auxiliary-pair rows.
    phi = [
        [1, -1, 1, 1, -1, 0],
        [-1, -1, 0, 1, 1, -1],
        [1, 0, -1, -1, 1, 1],
        [0, 1, 1, -1, -1, 1],
        [1, 1, -1, 1, 0, -1],
    ]
    n = [[sum(row[s] for s in block) for block in blocks] for row in phi]

    # z_j*kappa_{a,j}=n_{a,j}; hence the physical Rayleigh form is exactly
    # sum_a (sum_j n_{a,j})^2.  The normalising square roots cancel against z.
    traces_block = [sum(row) for row in n]
    traces_state = [sum(row) for row in phi]
    assert traces_block == traces_state
    physical_moment = sum(t * t for t in traces_state)
    gram_n = matmul(transpose(n), n)
    rayleigh_unnormalised = sum(gram_n[j][k] for j in range(len(blocks)) for k in range(len(blocks)))
    assert rayleigh_unnormalised == physical_moment

    # Exact H^2-D identity for ordered p!=q on a synthetic one-prime Kummer table.
    prime_rows = [
        [1, -1, 1, 1, -1, 1],
        [-1, -1, 1, -1, 1, 1],
        [1, 1, -1, -1, 1, -1],
        [1, -1, -1, 1, 1, -1],
    ]
    P = len(prime_rows)
    states = len(prime_rows[0])

    def kpair(p, q, s):
        return prime_rows[p][s] * prime_rows[q][s]

    # Compare the raw numerators of sqrt(m_j*m_k) G_jk.  This avoids irrational
    # square roots while testing exactly the formula stated in R2.11.
    explicit_raw = [[0 for _ in blocks] for _ in blocks]
    for j, bj in enumerate(blocks):
        for k, bk in enumerate(blocks):
            raw = 0
            for p in range(P):
                for q in range(P):
                    if p == q:
                        continue
                    sj = sum(kpair(p, q, s) for s in bj)
                    sk = sum(kpair(p, q, t) for t in bk)
                    raw += sj * sk
            explicit_raw[j][k] = raw

    hd_raw = [[0 for _ in blocks] for _ in blocks]
    for j, bj in enumerate(blocks):
        for k, bk in enumerate(blocks):
            raw = 0
            for s in bj:
                for t in bk:
                    h = sum(prime_rows[r][s] * prime_rows[r][t] for r in range(P))
                    d = sum((prime_rows[r][s] * prime_rows[r][t]) ** 2 for r in range(P))
                    raw += h * h - d
            hd_raw[j][k] = raw
    assert explicit_raw == hd_raw

    # Geometry-only coherent counterguard: one rectangle of mass m, all K=1.
    P_coh, m = 7, 5
    lhs = P_coh * (P_coh - 1) * m * m
    target = P_coh * P_coh * m
    assert lhs > target
    assert Fraction(lhs, target) == Fraction((P_coh - 1) * m, P_coh)
    a, b = 1, m
    assert (a * a) * (b * b) <= 2 * (a * b) ** 2

    required = [
        "STAGE14_TH17_R2=COMPLETE_MATCHED_RECTANGLE_SIGNED_TTSTAR_DUAL_APPLICABILITY_AUDIT",
        "POLAR_ABSOLUTE_VALUE_USED=false",
        "MATCHED_RECTANGLE_PROJECTION_ISOMETRY_PROVED=true",
        "MATCHED_BLOCK_PROJECTION_BESSEL_ZERO_LOSS=true",
        "ONE_PAIR_BLOCK_BESSEL_ALONE_CLOSES_SECOND_MOMENT=false",
        "PHYSICAL_MASS_VECTOR_RAYLEIGH_IS_EXACT_TARGET=true",
        "PROJECTED_TTSTAR_GRAM_IDENTITY_PROVED=true",
        "MATCHED_GRAM_EXACT_H2_MINUS_DIAGONAL_FORMULA_PROVED=true",
        "MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_PROVED=false",
        "T59_T62_GEOMETRY_ALONE_IMPLIES_PROJECTED_CANCELLATION=false",
        "ABSTRACT_OPERATOR_DUALITY_ALONE_CLOSES_PROJECTED_TARGET=false",
        "AMBIENT_STATE_SPACE_LARGE_SIEVE_REQUIRED=false",
        "PHYSICAL_MASS_VECTOR_KUMMER_RAYLEIGH_BOUND_PROVED=false",
        "E4_COEFFICIENT_ENERGY_USED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=PhysicalMassVectorKummerRayleighBound",
    ]
    for token in required:
        assert token in r2, token

    decision = summary["decision"]
    assert decision["STAGE14_TH17_R2"] == "COMPLETE_MATCHED_RECTANGLE_SIGNED_TTSTAR_DUAL_APPLICABILITY_AUDIT"
    assert decision["POLAR_ABSOLUTE_VALUE_USED"] is False
    assert decision["MATCHED_RECTANGLE_PROJECTION_ISOMETRY_PROVED"] is True
    assert decision["MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_PROVED"] is False
    assert decision["PHYSICAL_MASS_VECTOR_KUMMER_RAYLEIGH_BOUND_PROVED"] is False
    assert decision["E4_COEFFICIENT_ENERGY_USED"] is False

    report = {
        "stage": "14-tH17-R2",
        "block_bessel": {
            "masses": masses,
            "projected_energy": str(projected_energy),
            "source_energy": str(source_energy),
            "verified": True,
        },
        "projected_rayleigh": {
            "physical_moment": physical_moment,
            "unnormalised_block_gram_rayleigh": rayleigh_unnormalised,
            "verified": True,
        },
        "h2_minus_d_gram": {
            "prime_count": P,
            "state_count": states,
            "raw_gram_numerators_verified": True,
        },
        "coherent_single_rectangle_guard": {
            "P": P_coh,
            "mass": m,
            "lhs": lhs,
            "target": target,
            "failure_ratio": str(Fraction(lhs, target)),
            "aspect_balance_valid": True,
        },
        "boundary_locked": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
