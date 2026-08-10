#!/usr/bin/env python3
"""Stage14-t54: shared-U canonical-prime/divisor-fan principal incidence audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T53 = ROOT / "stages/stage14/data/14-t53/kummer_principal_stratification_frozen.json"
OUT = ROOT / "stages/stage14/data/14-t54/shared_u_canonical_prime.json"


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def exact_unit_pair_key(s):
    return (common_packet_key(s), gaussian_unit_key(s["U"]), gaussian_unit_key(s["V"]))


def state_row(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    return {
        "a": s["a"], "b": s["b"], "p": s["p"], "q": s["q"],
        "ell": s["ell"], "eps": s["eps"], "m": s["m"], "n": s["n"],
        "delta": s["delta"], "k": k, "h": h, "branch": s["branch"],
        "U": list(s["U"]), "V": list(s["V"]), "kernel": s["kernel"],
    }


def latin_square_guard(N=32):
    # N x N states, color c=i+j mod N.  Every row and every column contains
    # each color once, but every color occurs N times globally.
    H = N * N
    row_color_max = 1
    col_color_max = 1
    global_energy = N * N * N
    near_linear_target = H
    assert global_energy == N * near_linear_target
    return {
        "N": N,
        "states": H,
        "row_color_max_multiplicity": row_color_max,
        "column_color_max_multiplicity": col_color_max,
        "global_squareclass_energy": global_energy,
        "near_linear_target": near_linear_target,
        "failure_factor": N,
        "conclusion": "uniform one-variable multiplicity bounds in both coordinates do not imply near-linear global squareclass energy",
    }


def main():
    t53 = json.loads(T53.read_text())
    assert t53["boundary"] == "COMPLETE_POST_RESIDUE_KUMMER_PRINCIPAL_STRATIFICATION"
    assert t53["shared_U_blocks"] == 6
    assert t53["TH15_NEEDED"] is False

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)

    shared_u_blocks = []
    post_blocks = 0
    for kernel, members in sorted(by_kernel.items()):
        if len(members) != 2:
            continue
        x, y = members
        if exact_unit_pair_key(x) == exact_unit_pair_key(y):
            continue
        post_blocks += 1
        if x["ell"] == y["ell"]:
            continue
        if gaussian_unit_key(x["U"]) != gaussian_unit_key(y["U"]):
            continue
        assert x["m"] == y["m"]
        kx = x["n"] // x["delta"]
        ky = y["n"] // y["delta"]
        assert x["eps"] * x["m"] % kx == 0
        assert y["eps"] * y["m"] % ky == 0
        shared_u_blocks.append({
            "kernel": kernel,
            "x": state_row(x),
            "y": state_row(y),
            "same_eps": x["eps"] == y["eps"],
            "same_branch": x["branch"] == y["branch"],
            "same_k": kx == ky,
            "same_h": x["eps"] * x["m"] // kx == y["eps"] * y["m"] // ky,
            "same_delta": x["delta"] == y["delta"],
            "same_V_unit": gaussian_unit_key(x["V"]) == gaussian_unit_key(y["V"]),
        })

    assert post_blocks == 14
    assert len(shared_u_blocks) == 6

    shared_counts = {
        "same_eps": sum(b["same_eps"] for b in shared_u_blocks),
        "same_branch": sum(b["same_branch"] for b in shared_u_blocks),
        "same_k": sum(b["same_k"] for b in shared_u_blocks),
        "same_h": sum(b["same_h"] for b in shared_u_blocks),
        "same_delta": sum(b["same_delta"] for b in shared_u_blocks),
        "same_V_unit": sum(b["same_V_unit"] for b in shared_u_blocks),
    }

    # Full reciprocal-quotient U fibers: measure how much remains after U is fixed.
    by_u = defaultdict(list)
    for s in reps:
        by_u[gaussian_unit_key(s["U"])].append(s)

    fiber_rows = []
    for ukey, states in by_u.items():
        eps_values = {s["eps"] for s in states}
        branches = {s["branch"] for s in states}
        ells = {s["ell"] for s in states}
        deltas = {s["delta"] for s in states}
        ks = {s["n"] // s["delta"] for s in states}
        vkeys = {gaussian_unit_key(s["V"]) for s in states}
        kernels = Counter(s["kernel"] for s in states)
        energy = sum(c * c for c in kernels.values())
        fiber_rows.append({
            "U": list(ukey),
            "states": len(states),
            "eps_values": len(eps_values),
            "branches": len(branches),
            "distinct_ell": len(ells),
            "distinct_delta": len(deltas),
            "distinct_k": len(ks),
            "distinct_V_unit": len(vkeys),
            "squareclass_energy": energy,
            "principal_excess": energy - len(states),
        })

    max_states = max(r["states"] for r in fiber_rows)
    max_v = max(r["distinct_V_unit"] for r in fiber_rows)
    max_delta = max(r["distinct_delta"] for r in fiber_rows)
    max_energy_excess = max(r["principal_excess"] for r in fiber_rows)
    collision_u_fibers = sum(r["principal_excess"] > 0 for r in fiber_rows)

    # Exact divisor-fan identities.  These are the theorem-level algebraic facts
    # used by the next receiver, not finite-only observations.
    divisor_checks = 0
    for s in reps:
        k = s["n"] // s["delta"]
        assert s["n"] == k * s["delta"]
        assert (s["eps"] * s["m"]) % k == 0
        h = s["eps"] * s["m"] // k
        assert h * k == s["eps"] * s["m"]
        divisor_checks += 1

    report = {
        "stage": "14-t54",
        "input": {
            "reciprocal_states": len(reps),
            "post_residue_principal_blocks": post_blocks,
            "shared_U_principal_blocks": len(shared_u_blocks),
        },
        "exact_fixed_U_divisor_fan": {
            "identity_n_equals_k_delta": True,
            "identity_k_divides_eps_m": True,
            "identity_hk_equals_eps_m": True,
            "checks": divisor_checks,
            "fixed_U_consequence": "m=N(U) is fixed; after the finite eps split, k ranges only over divisors of eps*m, so k/h contribute B^o(1) divisor-fan choices; V still moves with N(V)=k*delta",
            "critical_strip_consequence": "fixed U does not fix V or the common-refinement packet; delta and primitive Gaussian representations V remain live",
        },
        "frozen_shared_U_blocks": shared_u_blocks,
        "frozen_shared_U_pair_counts": shared_counts,
        "full_U_fiber_diagnostics": {
            "distinct_U_unit_fibers": len(fiber_rows),
            "max_states_per_U_fiber": max_states,
            "max_distinct_V_per_U_fiber": max_v,
            "max_distinct_delta_per_U_fiber": max_delta,
            "U_fibers_with_principal_excess": collision_u_fibers,
            "max_principal_excess_in_U_fiber": max_energy_excess,
        },
        "one_variable_receivers": {
            "fixed_pi_direction_side": "t36 controls squareclass energy/multiplicity along the cover variable for one fixed direction pi*U",
            "fixed_V_canonical_side": "t38 moving-prime genus-one quartic controls one fixed descended (U,V,branch) packet; the same twist mechanism applies to a fixed represented squareclass",
            "globalization": False,
            "reason": "the physical shared-U family is a two-coordinate incidence array (pi,V); row/column fiber control does not bound the global color/squareclass energy",
        },
        "latin_square_quantifier_guard": latin_square_guard(),
        "required_receiver": {
            "name": "SharedUBipartiteSquareclassEnergy",
            "state_space": "fixed primitive U and eps, divisor-fan k|eps*N(U), moving canonical Gaussian prime pi, moving primitive V with N(V)=k*delta, branch/reconstruction masks retained",
            "target": "E_U=sum_kappa r_U(kappa)^2 <= R_U*B^o(1), uniformly after B^o divisor/branch splits",
            "equivalent_incidence_view": "near-linear equal-squareclass incidence between the moving-pi and moving-V coordinates inside a fixed-U divisor fan",
            "existing_t36_alone_sufficient": False,
            "existing_t38_alone_sufficient": False,
            "existing_tH12_fixed_core_receiver_sufficient": False,
            "reason_tH12_fails": "fixed U is not fixed common core; V and delta remain live, so the residual family is genuinely two-dimensional before further dispersion",
        },
        "tH_decision": {
            "TH15_NEEDED": True,
            "reason": "t54 exposes a concrete two-dimensional fixed-U/moving-(pi,V) principal-incidence receiver not supplied by t36, t38, or tH12/tH13/tH14; one-dimensional fiber bounds provably do not globalize",
            "requested_object": "a noncircular fixed-U divisor-fan bipartite squareclass-energy/dispersion theorem or a precise impossibility boundary",
        },
        "decision": {
            "STAGE14_T54": "COMPLETE_SHARED_U_DIVISOR_FAN_AND_BIPARTITE_ENERGY_REDUCTION",
            "FIXED_U_DIVISOR_FAN_PROVED": True,
            "FIXED_U_REDUCES_TO_ONE_DIMENSIONAL_CANONICAL_PRIME_SUM": False,
            "ONE_VARIABLE_FIBER_BOUNDS_GLOBALIZE": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_REQUIRED": True,
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
            "NEXT": "Stage14-t55 attack SharedUBipartiteSquareclassEnergy directly; consume tH15 if available, and preserve the fixed-U divisor fan instead of collapsing to cross-kernel energy",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
