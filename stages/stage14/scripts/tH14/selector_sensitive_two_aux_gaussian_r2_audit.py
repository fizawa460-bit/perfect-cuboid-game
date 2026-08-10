#!/usr/bin/env python3
"""Stage14-tH14 R2 deterministic audit.

This audit verifies the post-t51 theorem boundary.  It deliberately does not
claim the missing PhysicalWeightedSquareclassFiberEnergy theorem.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T46 = ROOT / "stages/stage14/data/14-t46/twist_translation_conductor_energy.json"
TH14_OLD = ROOT / "stages/stage14/data/tH14/selector_sensitive_two_aux_gaussian_summary.json"
TH14_R2 = ROOT / "stages/stage14/data/tH14/selector_sensitive_two_aux_gaussian_r2_summary.json"
T51_RESULT = ROOT / "stages/stage14/14-t51/result.md"
R2_RESULT = ROOT / "stages/stage14/14-tH14/r2.md"


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def check_predecessors() -> None:
    t46 = json.loads(T46.read_text())
    old = json.loads(TH14_OLD.read_text())
    t51 = T51_RESULT.read_text()

    assert t46["decision"]["SAFE_BASE_CONDUCTOR_BOUND"] == "2^10*B^4"
    assert old["trigger"]["tH11_reopen_trigger"] == "genuinely multi-modulus post-dispersion packet"
    assert old["proof_boundary"]["selector_sensitive_gaussian_completion_theorem_proved"] is False
    assert "AUXILIARY_PRODUCT_NO_ALIAS_FOR_RHO_GT_ONE_EIGHTH=true" in t51
    assert "TWO_AUXILIARY_RESIDUE_DIAGONAL_NEAR_LINEAR=true" in t51
    assert "OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_PROVED=false" in t51


def check_signed_squareclass_aggregation() -> None:
    # R-signs must be combined before the squareclass energy is measured.
    # The same D receives +3 and -3 from two refinement blocks.
    signed = {5: 3 + (-3), 13: 2 + 1}
    E_signed = sum(v * v for v in signed.values())
    E_abs_first = (abs(3) + abs(-3)) ** 2 + (abs(2) + abs(1)) ** 2
    assert E_signed == 9
    assert E_abs_first == 45
    assert E_signed < E_abs_first


def check_product_row_encoding() -> None:
    primes = [13, 17, 29, 37, 41, 53]
    unordered_products = {p * q for p, q in combinations(primes, 2)}
    ordered = [(p, q) for p, q in permutations(primes, 2)]
    assert len(unordered_products) == len(primes) * (len(primes) - 1) // 2
    assert len(ordered) == 2 * len(unordered_products)
    # Each n=pq has exactly the two orderings (p,q),(q,p).
    hist = {}
    for p, q in ordered:
        hist[p * q] = hist.get(p * q, 0) + 1
    assert set(hist.values()) == {2}


def check_alias_free_equal_squareclass_countermodel() -> dict:
    # Synthetic legal-frame guard: exact labels are pairwise distinct modulo all pq,
    # while their F-values have one common squareclass 3.
    primes = [13, 17, 29, 37, 41, 53]
    r = 7
    labels = list(range(1, r + 1))
    fvals = [3 * (j + 1) ** 2 for j in labels]

    # Coordinate labels are much smaller than every pq, so equality mod pq means exact equality.
    for p, q in combinations(primes, 2):
        m = p * q
        residues = [j % m for j in labels]
        assert len(set(residues)) == r

    # All values have the same quadratic character as 3 at every active prime.
    for p in primes:
        base = legendre(3, p)
        assert base != 0
        for f in fvals:
            assert legendre(f, p) == base

    P = len(primes)
    lhs = 0
    for p, q in permutations(primes, 2):
        trace = sum(legendre(f, p) * legendre(f, q) for f in fvals)
        assert abs(trace) == r
        lhs += trace * trace

    E_A = r
    target_core = P * P * E_A
    exact_formula = P * (P - 1) * r * r
    assert lhs == exact_formula
    assert lhs > target_core

    return {
        "P": P,
        "r": r,
        "lhs": lhs,
        "P2_EA": target_core,
        "ratio": Fraction(lhs, target_core),
    }


def check_exponent_ledger() -> None:
    # loss=(e_sq-e_A)+max(0,d-2rho)
    samples = [
        (Fraction(1, 2), Fraction(1, 2), Fraction(4), Fraction(2)),
        (Fraction(3, 4), Fraction(3, 4), Fraction(4), Fraction(2)),
        (Fraction(1, 2), Fraction(3, 4), Fraction(3), Fraction(3, 2)),
        (Fraction(2, 3), Fraction(5, 6), Fraction(4), Fraction(3, 2)),
    ]
    for e_A, e_sq, d, rho in samples:
        target = e_A + 2 * rho
        qls = e_sq + max(d, 2 * rho)
        loss = qls - target
        formula = (e_sq - e_A) + max(Fraction(0), d - 2 * rho)
        assert loss == formula

    # Safe t46 envelope d=4 at rho=2: only squareclass-energy loss remains.
    d = Fraction(4)
    rho = Fraction(2)
    e_A = Fraction(7, 8)
    e_sq = Fraction(15, 16)
    assert max(Fraction(0), d - 2 * rho) == 0
    assert (e_sq + max(d, 2 * rho)) - (e_A + 2 * rho) == e_sq - e_A

    # t51's rho>1/8 condition is automatically met at the safe d=4 QLS scale.
    assert rho > Fraction(1, 8)


def check_locked_summary() -> None:
    s = json.loads(TH14_R2.read_text())
    assert s["status"] == "COMPLETE_R2_QUADRATIC_FRAME_REDUCTION_AND_MINIMAL_SQUARECLASS_FIBER_BOUNDARY"
    assert s["mandatory_order"]["t32_angular_completion_before_state_pair_collapse"] is True
    assert s["mandatory_order"]["ordered_state_pair_cross_kernel_precollapse_used"] is False
    assert s["mandatory_order"]["E4_coefficient_energy_used"] is False
    assert s["dual_quadratic_large_sieve"]["adapter_proved"] is True
    assert s["minimal_missing_theorem"]["name"] == "PhysicalWeightedSquareclassFiberEnergy"
    assert s["minimal_missing_theorem"]["proved"] is False
    assert s["target"]["proved"] is False
    assert s["boundary"]["original_SSGC_is_minimal_black_box"] is False
    assert s["boundary"]["global_external_two_prime_mean_square_bound_proved"] is False

    text = R2_RESULT.read_text()
    required = [
        "STAGE14_TH14_R2=COMPLETE_R2_QUADRATIC_FRAME_REDUCTION_AND_MINIMAL_SQUARECLASS_FIBER_BOUNDARY",
        "T32_ANGULAR_COMPLETION_BEFORE_STATE_PAIR_COLLAPSE=true",
        "E4_COEFFICIENT_ENERGY_USED=false",
        "DUAL_QUADRATIC_LARGE_SIEVE_PRODUCT_ROW_ADAPTER_PROVED=true",
        "PHYSICAL_WEIGHTED_SQUARECLASS_FIBER_ENERGY_PROVED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=PhysicalWeightedSquareclassFiberEnergy",
        "SELECTOR_SENSITIVE_TWO_AUXILIARY_GAUSSIAN_SECOND_MOMENT_PROVED=false",
    ]
    for token in required:
        assert token in text


def main() -> None:
    check_predecessors()
    check_signed_squareclass_aggregation()
    check_product_row_encoding()
    counter = check_alias_free_equal_squareclass_countermodel()
    check_exponent_ledger()
    check_locked_summary()

    print("Stage14-tH14 R2 quadratic-frame audit: OK")
    print(f"countermodel P={counter['P']} r={counter['r']} lhs={counter['lhs']} P^2E_A={counter['P2_EA']} ratio={counter['ratio']}")


if __name__ == "__main__":
    main()
