#!/usr/bin/env python3
"""Stage14-t55: fixed-U invisible projective complete-trace / centered-selector reduction."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T54 = ROOT / "stages/stage14/data/14-t54/shared_u_canonical_prime_frozen.json"
OUT = ROOT / "stages/stage14/data/14-t55/shared_u_projective_trace.json"

SPLIT_PRIMES = (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97)
INERT_PRIMES = (7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79)


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def p1_points(p: int):
    return [(x, 1) for x in range(p)] + [(1, 0)]


def projective_kernel(A, P, p: int) -> int:
    a, b = A
    x, y = P
    f = (b*b*x*x - a*a*y*y) * (b*b*y*y - a*a*x*x)
    return legendre(f, p)


def complete_projective_trace_bruteforce(p: int) -> int:
    pts = p1_points(p)
    return sum(projective_kernel(A, P, p) for A in pts for P in pts)


def elliptic_character_sum(p: int) -> int:
    # Sum_x chi(x^3-x) = -a_p for E: y^2=x^3-x.
    return sum(legendre(x*x*x - x, p) for x in range(p))


def complete_projective_trace_formula(p: int) -> int:
    ap_neg = elliptic_character_sum(p)
    if p % 4 == 1:
        return 4 * p + ap_neg * ap_neg
    return 0


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    return (s["eps"], s["delta"], h, s["branch"])


def exact_unit_pair_key(s):
    return (common_packet_key(s), gaussian_unit_key(s["U"]), gaussian_unit_key(s["V"]))


def mul_gaussian_projective(U, Z, p: int):
    u, v = U
    r, s = Z
    return ((u*r - v*s) % p, (v*r + u*s) % p)


def normalize_p1(Z, p: int):
    a, b = Z[0] % p, Z[1] % p
    assert a or b
    if b:
        inv = pow(b, p - 2, p)
        return (a * inv % p, 1)
    return (1, 0)


def transformed_first_coordinate_trace(U, p: int) -> int:
    # If p does not divide N(U), multiplication by U is a PGL2 bijection.
    u, v = U
    assert (u*u + v*v) % p != 0
    pts = p1_points(p)
    total = 0
    seen = set()
    for Z in pts:
        A = normalize_p1(mul_gaussian_projective(U, Z, p), p)
        seen.add(A)
        for P in pts:
            total += projective_kernel(A, P, p)
    assert len(seen) == p + 1
    return total


def main():
    t54 = json.loads(T54.read_text())
    assert t54["boundary"] == "COMPLETE_SHARED_U_DIVISOR_FAN_AND_BIPARTITE_ENERGY_REDUCTION"
    assert t54["TH15_NEEDED"] is True
    assert t54["SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED"] is False

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    # Exact quartic -> rational cross-ratio squareclass identity on every state.
    cross_ratio_checks = 0
    for s in reps:
        a, b, x, y = s["a"], s["b"], s["p"], s["q"]
        A = b*b*x*x - a*a*y*y
        B = b*b*y*y - a*a*x*x
        assert A and B
        F = A * B
        assert F == s["F"]
        R = Fraction(A, B)
        # F / R = B^2 is a rational square, hence [F]=[R].
        assert Fraction(F, 1) / R == B * B
        T = Fraction(a*a, b*b)
        X = Fraction(x*x, y*y)
        assert R == (X - T) / (1 - T * X)
        cross_ratio_checks += 1

    # Rebuild post-residue shared-U principal blocks and split branch types.
    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)

    shared_u = []
    for kernel, members in sorted(by_kernel.items()):
        if len(members) != 2:
            continue
        x, y = members
        if exact_unit_pair_key(x) == exact_unit_pair_key(y):
            continue
        if x["ell"] == y["ell"]:
            continue
        if gaussian_unit_key(x["U"]) != gaussian_unit_key(y["U"]):
            continue
        shared_u.append((kernel, x, y))

    assert len(shared_u) == 6
    branch_types = Counter(tuple(sorted((x["branch"], y["branch"]))) for _, x, y in shared_u)
    assert branch_types[("invisible", "invisible")] == 5
    assert branch_types[("invisible", "visible")] == 1

    # Exact complete P1xP1 trace. For split primes this is 4p+a_p^2,
    # where |a_p|<=2sqrt(p) by Hasse, hence <=8p.
    split_rows = []
    for p in SPLIT_PRIMES:
        brute = complete_projective_trace_bruteforce(p)
        formula = complete_projective_trace_formula(p)
        e_sum = elliptic_character_sum(p)
        assert p % 4 == 1
        assert brute == formula
        assert formula == 4*p + e_sum*e_sum
        assert e_sum*e_sum <= 4*p
        assert 0 <= formula <= 8*p
        split_rows.append({
            "p": p,
            "elliptic_character_sum": e_sum,
            "projective_trace": formula,
            "trace_over_p": formula / p,
        })

    inert_rows = []
    for p in INERT_PRIMES:
        brute = complete_projective_trace_bruteforce(p)
        formula = complete_projective_trace_formula(p)
        assert p % 4 == 3
        assert brute == formula == 0
        inert_rows.append({"p": p, "projective_trace": 0})

    # Fixed-U multiplication only reparametrizes the first projective coordinate
    # for good auxiliary primes p not dividing N(U).
    ukeys = sorted({gaussian_unit_key(s["U"]) for s in reps})
    pgl_checks = 0
    for U in ukeys:
        for p in SPLIT_PRIMES[:6]:
            if (U[0]*U[0] + U[1]*U[1]) % p == 0:
                continue
            assert transformed_first_coordinate_trace(U, p) == complete_projective_trace_formula(p)
            pgl_checks += 1

    # Two distinct split primes factor by CRT. Record the exact safe constant.
    pair_rows = []
    for i, p in enumerate(SPLIT_PRIMES):
        for q in SPLIT_PRIMES[i+1:]:
            tr = complete_projective_trace_formula(p) * complete_projective_trace_formula(q)
            assert tr <= 64 * p * q
            pair_rows.append({"p": p, "q": q, "projective_trace_product": tr, "safe_bound": 64*p*q})

    # Centered-selector decomposition on the complete projective residue box.
    # For m=lambda*mu, |Omega_m|=(lambda+1)^2(mu+1)^2 and
    # |Sigma_m|<=64 lambda mu. Thus the constant-density term is
    # <=64 R_U/(lambda*mu). In a dyadic lambda,mu~L amplifier, its
    # total square over P^2 pairs is <= B^o * R_U^2 P^2/L^4.
    # Since t38 gives R_U<=B^(1/2+o(1)), rho>1/8 makes this o(R_U P^2).
    mean_ledger = {
        "projective_box_size": "(lambda+1)^2*(mu+1)^2",
        "complete_trace_bound": "|Sigma_{lambda,mu}|<=64*lambda*mu",
        "constant_density_term_per_pair": "<=64*R_U/(lambda*mu)",
        "dyadic_mean_square": "<=B^o(1)*R_U^2*P^2/L^4",
        "critical_census_input": "R_U<=B^(1/2+o(1)) from the t38 global critical-family bound",
        "rho_threshold": "rho>1/8 implies R_U/L^4=B^(1/2-4rho+o(1))=o(1)",
        "constant_density_part_closed": True,
    }

    report = {
        "stage": "14-t55",
        "input": {
            "reciprocal_states": len(reps),
            "shared_U_principal_blocks": len(shared_u),
            "shared_U_invisible_invisible_blocks": branch_types[("invisible", "invisible")],
            "shared_U_mixed_branch_blocks": branch_types[("invisible", "visible")],
        },
        "quartic_cross_ratio_squareclass": {
            "checks": cross_ratio_checks,
            "identity": "[F]=[(x^2-t^2)/(1-t^2*x^2)] with t=a/b, x=p/q",
            "integer_identity": "F/(A/B)=B^2 for A=b^2 p^2-a^2 q^2, B=b^2 q^2-a^2 p^2",
            "proved": True,
        },
        "complete_projective_trace": {
            "kernel": "chi_p((b^2 x^2-a^2 y^2)(b^2 y^2-a^2 x^2)) on P1xP1",
            "split_formula": "Sigma_p=4p+a_p^2, a_p=-trace(E_p), E:y^2=x^3-x",
            "split_hasse_bound": "0<=Sigma_p<=8p",
            "inert_formula": "Sigma_p=0 for p=3 mod 4",
            "split_rows": split_rows,
            "inert_rows": inert_rows,
            "fixed_U_PGL2_checks": pgl_checks,
            "two_split_prime_CRT_bound": "|Sigma_{lambda,mu}|<=64*lambda*mu",
            "pair_checks": len(pair_rows),
            "proved": True,
        },
        "centered_selector_reduction": {
            **mean_ledger,
            "remaining_object": "SharedUInvisibleCenteredProjectiveSelectorDispersion",
            "target": "sum_{lambda!=mu}|<b_{U,lambda*mu},K_{lambda*mu}>|^2 <= R_U*P^2*B^o(1)",
            "selector_definition": "nu_{U,m}=physical fixed-U invisible state counts on (P1(Z/m))^2; b=nu-(R_U/|Omega_m|)1",
            "state_pair_cross_kernel_precollapse_forbidden": True,
            "proved": False,
        },
        "mixed_branch_exception": {
            "frozen_blocks": 1,
            "status": "separate; not absorbed into the rectangular invisible/invisible selector theorem",
        },
        "tH_decision": {
            "TH15_STILL_NEEDED": True,
            "reason": "t55 proves the optimal-size complete two-dimensional projective trace and closes the constant-density term, but the physical fixed-U divisor-fan selector can still correlate with the character kernel; the remaining theorem is now a centered selector discrepancy/dispersion statement",
            "requested_object": "SharedUInvisibleCenteredProjectiveSelectorDispersion",
        },
        "decision": {
            "STAGE14_T55": "COMPLETE_SHARED_U_PROJECTIVE_TRACE_AND_CENTERED_SELECTOR_REDUCTION",
            "SHARED_U_INVISIBLE_COMPLETE_PROJECTIVE_TRACE_PROVED": True,
            "SHARED_U_CONSTANT_DENSITY_MEAN_CLOSED": True,
            "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_REQUIRED": True,
            "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED": False,
            "UV_TRANSVERSE_CROSS_GOOD_LD2_KUMMER_INCIDENCE_PROVED": False,
            "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH15_NEEDED": True,
            "NEXT": "Stage14-t56 attack SharedUInvisibleCenteredProjectiveSelectorDispersion; consume tH15 if available, keep the one mixed-branch block separate, and exploit the exact P1xP1 complete trace before any cross-kernel collapse",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
