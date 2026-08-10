#!/usr/bin/env python3
"""Stage14-t45: two-canonical-prime local character and many-conductor audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import gcd
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T43_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t43_low_degree_kummer_transversality_audit.py"
T44_DATA = ROOT / "stages/stage14/data/14-t44/canonical_prime_twist_support.json"
TH12_DATA = ROOT / "stages/stage14/data/tH12/ld2_kummer_incidence_receiver_summary.json"
OUT = ROOT / "stages/stage14/data/14-t45/two_canonical_character.json"

HEAVY_THRESHOLD = 20
TOP_TARGET_COUNT = 8


def vp(n: int, p: int) -> int:
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def squarefree_product(a: int, b: int) -> int:
    g = gcd(a, b)
    return (a // g) * (b // g)


def fundamental_discriminant_from_squarefree(d: int) -> int:
    assert d > 0
    return d if d % 4 == 1 else 4 * d


def common_core_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def common_t(s):
    C = common_core_key(s)
    eps, _delta, h, _branch = C
    g = gcd(eps, h)
    B0 = h // g
    assert s["m"] % B0 == 0
    return s["m"] // B0


def own_normalized_F(s):
    v = vp(s["F"], s["ell"])
    assert v in (0, 2)
    return s["F"] // (s["ell"] ** v), v


def main():
    frozen44 = json.loads(T44_DATA.read_text())
    th12 = json.loads(TH12_DATA.read_text())
    assert frozen44["boundary"]["GENERIC_CROSS_GOOD_KUMMER_REMAINS_PRIMARY"] is True
    assert frozen44["boundary"]["FROZEN_HEAVY_CROSS_BAD_MASS"] == 0
    assert th12["boundary"]["STAGE14_TH12"] == "COMPLETE_LD2_KUMMER_CANONICAL_PRIME_COMMON_CORE_RECEIVER"
    assert th12["boundary"]["ONE_DIMENSIONAL_PRIME_CHARACTER_CERTIFICATE_DEFINED"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    t43 = runpy.run_path(str(T43_SCRIPT), run_name="stage14_t43_import")

    states = t36["build_frozen_states"]()
    reps = t42["reciprocal_quotient"](states)
    cross_kernel = t42["cross_kernel"]
    assert len(reps) == 560

    direction_keys = sorted({(s["a"], s["b"]) for s in reps})
    relation, _relation_counts = t43["relation_matrix"](direction_keys)

    # Frozen evidence for the tH12 quantifier warning: fixed common core is not scalar.
    by_core = defaultdict(list)
    by_ell = defaultdict(list)
    by_joint = defaultdict(list)
    by_descended_packet = defaultdict(list)
    self_signs = Counter()
    for s in reps:
        C = common_core_key(s)
        t = common_t(s)
        by_core[C].append(s)
        by_ell[s["ell"]].append(s)
        by_joint[(C, s["ell"])].append(s)
        packet = (C, t, tuple(s["U"]), tuple(s["V"]))
        by_descended_packet[packet].append(s)
        Fsharp, v = own_normalized_F(s)
        sg = legendre(Fsharp, s["ell"])
        assert sg in (-1, 1)
        self_signs[(s["branch"], s["ell"] % 8, sg, v)] += 1

    core_t_counts = [len({common_t(s) for s in members}) for members in by_core.values()]
    core_ell_counts = [len({s["ell"] for s in members}) for members in by_core.values()]
    ell_core_counts = [len({common_core_key(s) for s in members}) for members in by_ell.values()]

    # Full convolution gives target twists and heavy set.
    conv = Counter()
    for x in reps:
        for y in reps:
            conv[cross_kernel(x["kernel"], y["kernel"])] += 1
    assert conv[1] == 592
    heavy = [(tau, mult) for tau, mult in conv.items() if tau != 1 and mult > HEAVY_THRESHOLD]
    heavy.sort(key=lambda kv: (-kv[1], kv[0]))
    assert len(heavy) == 72
    targets = [tau for tau, _mult in heavy[:TOP_TARGET_COUNT]]

    # Materialize the genuinely generic distinct-ell cross-good pair family once.
    generic_pairs = []
    for ix, x in enumerate(reps):
        dx = (x["a"], x["b"])
        for iy, y in enumerate(reps):
            dy = (y["a"], y["b"])
            if dx == dy or relation[(dx, dy)] != "ld2_transverse":
                continue
            if x["ell"] == y["ell"]:
                continue
            if vp(y["F"], x["ell"]) or vp(x["F"], y["ell"]):
                continue
            generic_pairs.append((ix, iy))

    # Exact fixed-partner character identity and two endogenous local filters.
    # For a true tau-pair, tau*F_x^#*F_y and tau*F_x*F_y^# are rational squares,
    # hence both own-prime Legendre symbols are +1. For arbitrary candidates these
    # are only two local necessary tests.
    target_rows = []
    prime_character_identity_checks = 0
    actual_subset_checks = 0
    for tau in targets:
        left_pass = 0
        right_pass = 0
        both_pass = 0
        good_candidates = 0
        actual = 0
        conductor_set = set()
        partner_conductor_hist = Counter()

        for ix, iy in generic_pairs:
            x, y = reps[ix], reps[iy]
            # If tau itself contains an endogenous modulus, this local test is bad and is
            # routed away exactly as required by t44/tH12 bad-prime accounting.
            if tau % x["ell"] == 0 or tau % y["ell"] == 0:
                continue
            good_candidates += 1

            Fxsharp, _vx = own_normalized_F(x)
            Fysharp, _vy = own_normalized_F(y)
            L = legendre(tau * Fxsharp * y["F"], x["ell"])
            R = legendre(tau * x["F"] * Fysharp, y["ell"])
            assert L in (-1, 1) and R in (-1, 1)
            left_pass += int(L == 1)
            right_pass += int(R == 1)
            both_pass += int(L == 1 and R == 1)

            # Fixed y: chi_{ell_x}(tau F_y) is exactly the primitive quadratic
            # Dirichlet character attached to the fundamental discriminant of the
            # squarefree part of tau F_y, evaluated at ell_x.
            d_y = squarefree_product(tau, y["kernel"])
            D_y = fundamental_discriminant_from_squarefree(d_y)
            conductor_set.add(D_y)
            partner_conductor_hist[D_y] += 1
            assert legendre(tau * y["F"], x["ell"]) == legendre(D_y, x["ell"])
            prime_character_identity_checks += 1

            if cross_kernel(x["kernel"], y["kernel"]) == tau:
                actual += 1
                assert L == 1 and R == 1
                actual_subset_checks += 1

        target_rows.append({
            "tau": tau,
            "global_multiplicity": conv[tau],
            "generic_good_candidate_pairs": good_candidates,
            "left_local_pass": left_pass,
            "right_local_pass": right_pass,
            "two_local_pass": both_pass,
            "actual_generic_cross_good_pairs": actual,
            "two_local_pass_to_candidate_ratio": both_pass / good_candidates,
            "actual_to_two_local_pass_ratio": actual / both_pass,
            "distinct_fixed_partner_conductors": len(conductor_set),
            "max_pairs_sharing_one_partner_conductor": max(partner_conductor_hist.values()),
        })

    # The endogenous two-prime positivity detector has a fixed constant term 1/4.
    # This is an exact algebraic barrier: without cancellation in the three nonconstant
    # character terms it cannot change an exponent.
    detector_expansion = (
        "1_square(N) <= ((1+chi_ellx(N))/2)*((1+chi_elly(N))/2) "
        "= (1+chi_ellx(N)+chi_elly(N)+chi_ellx(N)chi_elly(N))/4"
    )

    report = {
        "stage": "14-t45-probe",
        "th12_reuse": {
            "receiver_imported": True,
            "fixed_partner_prime_character_identity_proved": True,
            "fixed_common_core_alone_one_dimensional": False,
            "reason": "common core leaves t/orientation/cofactor data moving unless further refined",
        },
        "partition_census": {
            "states": len(reps),
            "common_core_blocks": len(by_core),
            "canonical_prime_blocks": len(by_ell),
            "joint_core_prime_blocks": len(by_joint),
            "descended_packet_blocks": len(by_descended_packet),
            "max_states_per_common_core": max(map(len, by_core.values())),
            "max_distinct_t_per_common_core": max(core_t_counts),
            "max_distinct_ell_per_common_core": max(core_ell_counts),
            "max_distinct_common_cores_per_ell": max(ell_core_counts),
        },
        "own_prime_self_signs": {
            f"{branch}_ellmod8_{mod8}_sign_{sg}_v{v}": count
            for (branch, mod8, sg, v), count in sorted(self_signs.items())
        },
        "generic_cross_good": {
            "ordered_pair_count": len(generic_pairs),
            "top_heavy_targets": target_rows,
            "prime_character_identity_checks": prime_character_identity_checks,
            "actual_pair_local_subset_checks": actual_subset_checks,
        },
        "two_endogenous_prime_detector": {
            "exact_expansion": detector_expansion,
            "constant_term": "1/4",
            "bounded_number_of_local_tests_changes_exponent": False,
            "cancellation_or_growing_modulus_family_required": True,
        },
        "many_conductor_boundary": {
            "fixed_partner_phase": "D_{tau,y}=funddisc(sqf(tau*F_y))",
            "prime_character": "chi_{D_{tau,y}}(ell_x)",
            "partner_moves_so_conductor_moves": True,
            "blockwise_1d_character_implies_global_saving": False,
            "aggregate_multi_conductor_large_sieve_or_dispersion_required": True,
        },
        "boundary": {
            "STAGE14_T45": "PROBE_TWO_CANONICAL_LOCAL_FILTER_AND_MANY_CONDUCTOR_BOUNDARY",
            "TH12_PRIME_CHARACTER_SPECIALIZATION_FOUND": True,
            "TWO_ENDOGENOUS_CANONICAL_LOCAL_FILTERS_EXACT": True,
            "TWO_ENDOGENOUS_CANONICAL_LOCAL_FILTERS_POWER_SAVING": False,
            "MANY_CONDUCTOR_AGGREGATION_REQUIRED": True,
            "GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
