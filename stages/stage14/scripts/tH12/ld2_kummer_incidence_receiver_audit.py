#!/usr/bin/env python3
"""Stage14-tH12 deterministic audit for LD2 Kummer incidence receivers."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T43_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t43_low_degree_kummer_transversality_audit.py"
T43_DATA = ROOT / "stages/stage14/data/14-t43/low_degree_kummer_transversality.json"
TH10_DATA = ROOT / "stages/stage14/data/tH10/squareclass_fiber_energy_toolbox_summary.json"
SUMMARY = ROOT / "stages/stage14/data/tH12/ld2_kummer_incidence_receiver_summary.json"

HEAVY_THRESHOLD = 20


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def add_counter(dst: Counter, src: Counter) -> None:
    for k, v in src.items():
        dst[k] += v


def frozen_ld2_partition_audit() -> dict:
    frozen43 = json.loads(T43_DATA.read_text())
    th10 = json.loads(TH10_DATA.read_text())
    assert frozen43["decision"]["STAGE14_T43"] == (
        "COMPLETE_LOW_DEGREE_ISOGENY_CERTIFICATE_AND_GENERIC_KUMMER_BARRIER"
    )
    assert frozen43["decision"]["GENERIC_TWISTED_KUMMER_REMAINS_PRIMARY"] is True
    assert th10["status"] == "COMPLETE_SQUARECLASS_FIBER_AND_AUTOCORRELATION_INCIDENCE_TOOLBOX"

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    t43 = runpy.run_path(str(T43_SCRIPT), run_name="stage14_t43_import")

    states = t36["build_frozen_states"]()
    reps = t42["reciprocal_quotient"](states)
    assert len(reps) == 560

    direction_keys = sorted({(s["a"], s["b"]) for s in reps})
    relation, _ = t43["relation_matrix"](direction_keys)
    cross_kernel = t42["cross_kernel"]
    common_key = t42["common_packet_key"]

    total_by_tau = Counter()
    by_core: dict[tuple, Counter] = defaultdict(Counter)
    by_ell: dict[int, Counter] = defaultdict(Counter)
    by_joint: dict[tuple, Counter] = defaultdict(Counter)
    same_core = same_ell = same_both = 0

    generic_pairs = 0
    for x in reps:
        dx = (x["a"], x["b"])
        cx = common_key(x)
        ellx = int(x["ell"])
        for y in reps:
            dy = (y["a"], y["b"])
            if dx == dy or relation[(dx, dy)] != "ld2_transverse":
                continue
            tau = cross_kernel(int(x["kernel"]), int(y["kernel"]))
            generic_pairs += 1
            total_by_tau[tau] += 1
            by_core[cx][tau] += 1
            by_ell[ellx][tau] += 1
            by_joint[(cx, ellx)][tau] += 1

            cy = common_key(y)
            elly = int(y["ell"])
            eqc = cx == cy
            eqe = ellx == elly
            same_core += int(eqc)
            same_ell += int(eqe)
            same_both += int(eqc and eqe)

    assert generic_pairs == 308_846

    rec_core = Counter()
    rec_ell = Counter()
    rec_joint = Counter()
    for c in by_core.values():
        add_counter(rec_core, c)
    for c in by_ell.values():
        add_counter(rec_ell, c)
    for c in by_joint.values():
        add_counter(rec_joint, c)
    assert rec_core == total_by_tau
    assert rec_ell == total_by_tau
    assert rec_joint == total_by_tau

    # Full squareclass convolution is the tH10 heavy/light receiver input.
    conv = Counter()
    for x in reps:
        for y in reps:
            tau = cross_kernel(int(x["kernel"]), int(y["kernel"]))
            conv[tau] += 1
    H = len(reps)
    A1 = conv[1]
    assert (H, A1) == (560, 592)
    R_non = max(v for k, v in conv.items() if k != 1)
    heavy = {k: v for k, v in conv.items() if k != 1 and v > HEAVY_THRESHOLD}
    M_T = sum(heavy.values())
    E4 = sum(v * v for v in conv.values())
    assert R_non == 40
    assert len(heavy) == 72
    assert M_T == 1834
    assert E4 == 1_324_576

    rhs_hl = (
        A1 * A1
        + HEAVY_THRESHOLD * (H * H - A1)
        + (R_non - HEAVY_THRESHOLD) * M_T
    )
    assert E4 <= rhs_hl

    generic_heavy_mass = sum(total_by_tau[tau] for tau in heavy)

    return {
        "states": H,
        "A1": A1,
        "generic_ld2_ordered_pairs": generic_pairs,
        "distinct_common_core_left_cells": len(by_core),
        "distinct_canonical_ell_left_cells": len(by_ell),
        "distinct_joint_left_cells": len(by_joint),
        "same_common_core_generic_pairs": same_core,
        "same_canonical_ell_generic_pairs": same_ell,
        "same_both_generic_pairs": same_both,
        "twists_in_generic_ld2": len(total_by_tau),
        "heavy_kernel_count": len(heavy),
        "heavy_pair_mass_full": M_T,
        "generic_ld2_mass_on_heavy_kernels": generic_heavy_mass,
        "R_non": R_non,
        "E4": E4,
        "heavy_light_rhs_T20": rhs_hl,
        "fubini_core_exact": True,
        "fubini_ell_exact": True,
        "fubini_joint_exact": True,
        "fubini_twistwise_exact": True,
    }


def many_block_countermodel(n: int = 64) -> dict[str, int]:
    # One point per block.  A local O(1) statement does not imply global O(1).
    local = [1] * n
    return {
        "blocks": n,
        "max_local_incidence": max(local),
        "global_incidence": sum(local),
    }


def local_square_false_positive() -> dict[str, int | bool]:
    n = 6
    q = 5
    r = isqrt(n)
    assert r * r != n
    assert legendre(n, q) == 1
    return {
        "integer": n,
        "modulus": q,
        "integer_is_square": False,
        "legendre_symbol": 1,
    }


def square_polynomial_degeneracy() -> dict[str, int]:
    q = 101
    total = sum(legendre(h * h, q) for h in range(q))
    # h^2 is a square polynomial: all nonzero values have character +1.
    assert total == q - 1
    return {"q": q, "complete_sum_chi_h2": total}


def root_vs_residue_audit() -> dict[str, int]:
    q = 101
    roots = sum(1 for h in range(q) if h % q == 0)
    residues_plus = sum(1 for h in range(q) if legendre(h, q) == 1)
    assert roots == 1
    assert residues_plus == (q - 1) // 2
    return {"q": q, "root_classes": roots, "legendre_plus_one_classes": residues_plus}


def polynomial_value(h: int, coeffs: tuple[int, ...], q: int) -> int:
    out = 0
    for a in coeffs:
        out = (out * h + a) % q
    return out


def lattice_root_receiver_audit() -> dict[str, int]:
    # P(h)=h^2-1, degree 2.  Over each odd prime there are at most 2 roots.
    coeffs = (1, 0, -1)
    degree = 2
    H = 1000
    checks = 0
    max_roots = 0
    for q in (5, 7, 11, 13, 17, 19, 23, 29):
        roots = [r for r in range(q) if polynomial_value(r, coeffs, q) == 0]
        assert len(roots) <= degree
        count = sum(1 for h in range(1, H + 1) if polynomial_value(h, coeffs, q) == 0)
        bound = degree * (H // q + 1)
        assert count <= bound
        max_roots = max(max_roots, len(roots))
        checks += 1
    return {"prime_checks": checks, "max_root_classes": max_roots, "degree": degree}


def divisors(n: int) -> list[int]:
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def divisor_receiver_audit() -> dict[str, int]:
    M = (2**5) * (3**3) * (5**2)
    ds = divisors(M)
    assert len(ds) == (5 + 1) * (3 + 1) * (2 + 1) == 72

    # Counterexample to the moving-dividend mistake: h | h for every h.
    moving = sum(1 for h in range(1, 101) if h % h == 0)
    assert moving == 100
    return {"fixed_M": M, "fixed_divisor_count": len(ds), "moving_dividend_survivors_1_to_100": moving}


def adaptive_modulus_counterexample() -> dict[str, int]:
    # Two nonsquares pass local +1 tests after choosing different moduli.
    assert legendre(2, 7) == 1
    assert legendre(3, 13) == 1
    return {"n1": 2, "q1": 7, "n2": 3, "q2": 13}


def summary_contract_audit() -> dict[str, bool]:
    s = json.loads(SUMMARY.read_text())
    assert s["status"] == "COMPLETE_LD2_KUMMER_CANONICAL_PRIME_COMMON_CORE_RECEIVER"
    assert s["requires_t44_result"] is False
    assert s["quantifier_guards"]["single_legendre_plus_one_implies_global_square"] is False
    assert s["quantifier_guards"]["ld2_transverse_implies_all_degree_nonisogenous"] is False
    assert s["proof_boundary"]["generic_kummer_incidence_power_saving_proved"] is False
    assert s["proof_boundary"]["canonical_prime_selector_cancellation_proved"] is False
    return {
        "summary_status_locked": True,
        "t44_independence_locked": True,
        "no_false_power_saving_claim": True,
    }


def main() -> None:
    frozen = frozen_ld2_partition_audit()
    countermodels = {
        "many_blocks": many_block_countermodel(),
        "local_square_false_positive": local_square_false_positive(),
        "square_polynomial": square_polynomial_degeneracy(),
        "root_vs_residue": root_vs_residue_audit(),
        "adaptive_modulus": adaptive_modulus_counterexample(),
        "divisor": divisor_receiver_audit(),
    }
    lattice = lattice_root_receiver_audit()
    contract = summary_contract_audit()

    report = {
        "frozen_ld2": frozen,
        "countermodels": countermodels,
        "lattice_receiver": lattice,
        "contract": contract,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Stage14-tH12 audit: PASS")


if __name__ == "__main__":
    main()
