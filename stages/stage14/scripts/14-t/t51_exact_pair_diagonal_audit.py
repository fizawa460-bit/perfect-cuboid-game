#!/usr/bin/env python3
"""Stage14-t51: exact-pair diagonal / off-diagonal selector boundary audit."""

from __future__ import annotations

from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T50 = ROOT / "stages/stage14/data/14-t50/selector_sensitive_two_modulus_frozen.json"
TH5 = ROOT / "stages/stage14/data/tH5/gaussian_pair_collision_energy_summary.json"
OUT = ROOT / "stages/stage14/data/14-t51/exact_pair_diagonal.json"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def split_primes(start: int, count: int):
    out = []
    n = max(5, start | 1)
    while len(out) < count:
        if n % 4 == 1 and is_prime(n):
            out.append(n)
        n += 2
    return out


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def exact_pair_key(s):
    # Keep the full common-refinement packet and oriented Gaussian pair.
    # This is a refinement of any coarser exact-pair label, so its collision
    # energy cannot exceed a proved coarser exact-pair collision energy.
    return (common_packet_key(s), tuple(s["U"]), tuple(s["V"]))


def residue_pair_key(s, M: int):
    U = tuple(x % M for x in s["U"])
    V = tuple(x % M for x in s["V"])
    return (common_packet_key(s), U, V)


def collision_energy(keys) -> int:
    c = Counter(keys)
    return sum(v * v for v in c.values())


def main():
    t50 = json.loads(T50.read_text())
    th5 = json.loads(TH5.read_text())
    assert t50["boundary"] == "COMPLETE_BAD_AUXILIARY_BOUND_AND_SELECTOR_SENSITIVE_TWO_MODULUS_BOUNDARY"
    assert t50["TH14_NEEDED"] is True
    assert t50["bad_auxiliary"]["aggregate_bound_proved"] is True
    assert th5["proof_boundary"]["full_exact_gaussian_pair_coefficient_collision_energy_proved"] is True
    assert th5["proof_boundary"]["same_modulus_residue_collision_energy_proved"] is False

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    # Exact critical-strip norm inequalities already present in the live variables:
    # k=n/delta <= eps*m, hence n<=eps*m*delta.
    # t37/t50 critical super-sqrt branch gives eps*m*delta <= 2B/ell = O(B^(1/2)).
    algebra_checks = 0
    for s in reps:
        k = s["n"] // s["delta"]
        assert k == gcd(s["n"], s["eps"] * s["m"])
        assert k <= s["eps"] * s["m"]
        assert s["n"] <= s["eps"] * s["m"] * s["delta"]
        assert s["U"][0] ** 2 + s["U"][1] ** 2 == s["m"]
        assert s["V"][0] ** 2 + s["V"][1] ** 2 == s["n"]
        algebra_checks += 1

    max_abs_coord = max(abs(z) for s in reps for pair in (s["U"], s["V"]) for z in pair)
    exact_keys = [exact_pair_key(s) for s in reps]
    exact_energy = collision_energy(exact_keys)
    exact_max_mult = max(Counter(exact_keys).values())

    # Frozen amplifier primes are deliberately much larger than the finite Gaussian
    # coordinates.  The asymptotic theorem uses p,q~B^rho, rho>1/8, because
    # pq~B^(2rho) dominates the O(B^(1/4)) coordinate diameter.
    primes = split_primes(2000, 16)
    min_modulus = primes[0] * primes[1]
    assert min_modulus > 2 * max_abs_coord

    residue_energies = []
    alias_failures = 0
    pair_checks = 0
    for i, p in enumerate(primes):
        for q in primes[i + 1 :]:
            M = p * q
            residue_keys = [residue_pair_key(s, M) for s in reps]
            re = collision_energy(residue_keys)
            residue_energies.append(re)
            if re != exact_energy:
                alias_failures += 1
            pair_checks += 1
    assert alias_failures == 0
    assert len(set(residue_energies)) == 1
    assert residue_energies[0] == exact_energy

    # Quantitative no-alias ledger.  In the critical strip ell >= c*sqrt(B),
    # m,n << B^(1/2), hence every Gaussian coordinate is << B^(1/4).
    # If rho>1/8 then pq~B^(2rho) dominates every coordinate difference.
    # Consequently residue equality mod pq inside one fixed common-refinement
    # packet implies exact oriented-pair equality.  tH5 then supplies near-linear
    # exact-pair coefficient energy, and the residue diagonal contributes
    # P^2 * H * B^o(1), exactly the t49 target scale.

    report = {
        "stage": "14-t51",
        "predecessor": {
            "t50_bad_auxiliary_closed": True,
            "t50_selector_sensitive_second_moment_open": True,
            "tH5_exact_pair_energy_proved": True,
            "tH5_same_modulus_residue_energy_previously_open": True,
        },
        "critical_strip_no_alias": {
            "identities": [
                "k=n/delta=gcd(n,eps*m)<=eps*m",
                "n<=eps*m*delta",
                "critical super-sqrt branch: eps*m*delta<=2B/ell=O(B^(1/2))",
                "N(U)=m and N(V)=n imply |U_i|,|V_i|=O(B^(1/4))",
            ],
            "auxiliary_scale": "p,q~L=B^rho with fixed rho>1/8",
            "product_modulus": "pq~B^(2rho) >> B^(1/4)",
            "conclusion": "within a fixed common-refinement packet, equality of oriented (U,V) modulo pq implies exact equality of oriented (U,V)",
            "algebra_checks": algebra_checks,
        },
        "frozen_alias_audit": {
            "states": len(reps),
            "external_split_primes": len(primes),
            "prime_pair_checks": pair_checks,
            "min_prime": min(primes),
            "max_prime": max(primes),
            "min_product_modulus": min_modulus,
            "max_abs_gaussian_coordinate": max_abs_coord,
            "exact_pair_collision_energy": exact_energy,
            "exact_pair_max_multiplicity": exact_max_mult,
            "residue_pair_collision_energy": residue_energies[0],
            "alias_failures": alias_failures,
        },
        "diagonal_receiver": {
            "exact_pair_refinement": "(common-refinement packet, oriented U, oriented V)",
            "energy": "E_exact <= H*B^o(1) by tH5; retaining extra common-refinement fields can only reduce collisions",
            "two_auxiliary_residue_diagonal": "E_res(pq)=E_exact for rho>1/8 on the critical strip",
            "frobenius_diagonal_contribution": "R_diag <= P^2*H*B^o(1)",
            "target_scale_met": True,
        },
        "remaining_offdiagonal": {
            "name": "OffDiagonalTwoAuxiliaryGaussianResidueDispersion",
            "object": "after t32 angular completion and common-refinement retention, sum the nonzero residue/frequency pairs across distinct p,q without Cauchy over blocks",
            "required_bound": "R_off,res <= P^2*(sum_R ||w_R||_2^2)*B^o(1)",
            "physical_specialization": "R_off,res <= H*P^2*B^o(1)",
            "must_preserve": [
                "signed common-refinement aggregation",
                "shared U/V modulus group",
                "two distinct split auxiliaries p,q",
                "divisor-coupled hyperbola selector",
                "canonical/branch/reconstruction masks",
            ],
            "pair_collapse_before_cancellation_forbidden": True,
            "proved": False,
        },
        "tH_decision": {
            "tH14_still_needed": True,
            "additional_tH15_needed": False,
            "reason": "t51 closes the exact/residue diagonal using the rho>1/8 no-alias regime plus tH5; the remaining object is precisely the off-diagonal part of the already-requested tH14 two-auxiliary second moment",
        },
        "decision": {
            "STAGE14_T51": "COMPLETE_ALIAS_FREE_EXACT_PAIR_DIAGONAL_AND_OFFDIAGONAL_RESIDUE_REDUCTION",
            "CRITICAL_STRIP_GAUSSIAN_COORDINATE_BOUND_B_QUARTER": True,
            "AUXILIARY_PRODUCT_NO_ALIAS_FOR_RHO_GT_ONE_EIGHTH": True,
            "TWO_AUXILIARY_RESIDUE_DIAGONAL_NEAR_LINEAR": True,
            "TH5_EXACT_PAIR_ENERGY_USED": True,
            "OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_REQUIRED": True,
            "OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_PROVED": False,
            "GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH14_STILL_NEEDED": True,
            "TH15_NEEDED": False,
            "NEXT": "Stage14-t52 attack OffDiagonalTwoAuxiliaryGaussianResidueDispersion; consume tH14 if available and keep the rho>1/8 alias-free diagonal separated",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
