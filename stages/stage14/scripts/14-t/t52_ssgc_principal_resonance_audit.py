#!/usr/bin/env python3
"""Stage14-t52: expose the principal squareclass subproblem inside SSGC."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T51 = ROOT / "stages/stage14/data/14-t51/exact_pair_diagonal_frozen.json"
TH14 = ROOT / "stages/stage14/data/tH14/selector_sensitive_two_aux_gaussian_summary.json"
T43 = ROOT / "stages/stage14/data/14-t43/low_degree_kummer_transversality.json"
T44 = ROOT / "stages/stage14/data/14-t44/canonical_prime_twist_support.json"
OUT = ROOT / "stages/stage14/data/14-t52/ssgc_principal_resonance.json"


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def exact_unit_pair_key(s):
    return (common_packet_key(s), gaussian_unit_key(s["U"]), gaussian_unit_key(s["V"]))


def exact_oriented_pair_key(s):
    return (common_packet_key(s), tuple(s["U"]), tuple(s["V"]))


def principal_pair_audit(reps):
    by_kernel = defaultdict(list)
    for i, s in enumerate(reps):
        by_kernel[s["kernel"]].append((i, s))

    H = len(reps)
    A1 = sum(len(v) ** 2 for v in by_kernel.values())
    unordered_off = 0
    ordered_off = 0
    exact_oriented_ordered_off = 0
    exact_unit_ordered_off = 0
    same_common_ordered_off = 0
    same_ell_ordered_off = 0
    distinct_ell_ordered_off = 0
    block_rows = []

    for kernel, members in sorted(by_kernel.items()):
        if len(members) < 2:
            continue
        for a in range(len(members)):
            for b in range(a + 1, len(members)):
                _, x = members[a]
                _, y = members[b]
                unordered_off += 1
                ordered_off += 2
                same_common = common_packet_key(x) == common_packet_key(y)
                same_oriented = exact_oriented_pair_key(x) == exact_oriented_pair_key(y)
                same_unit = exact_unit_pair_key(x) == exact_unit_pair_key(y)
                same_ell = x["ell"] == y["ell"]
                same_common_ordered_off += 2 * int(same_common)
                exact_oriented_ordered_off += 2 * int(same_oriented)
                exact_unit_ordered_off += 2 * int(same_unit)
                same_ell_ordered_off += 2 * int(same_ell)
                distinct_ell_ordered_off += 2 * int(not same_ell)
                block_rows.append(
                    {
                        "kernel": kernel,
                        "x": [x["a"], x["b"], x["p"], x["q"], x["ell"]],
                        "y": [y["a"], y["b"], y["p"], y["q"], y["ell"]],
                        "same_common_packet": same_common,
                        "same_exact_oriented_pair": same_oriented,
                        "same_exact_unit_pair": same_unit,
                        "same_ell": same_ell,
                    }
                )

    assert A1 - H == ordered_off
    return {
        "H": H,
        "A1": A1,
        "principal_self_mass": H,
        "principal_offdiagonal_ordered_mass": ordered_off,
        "principal_offdiagonal_unordered_blocks": unordered_off,
        "same_common_packet_ordered_mass": same_common_ordered_off,
        "same_exact_oriented_pair_ordered_mass": exact_oriented_ordered_off,
        "same_exact_unit_pair_ordered_mass": exact_unit_ordered_off,
        "same_ell_ordered_mass": same_ell_ordered_off,
        "distinct_ell_ordered_mass": distinct_ell_ordered_off,
        "residue_offdiagonal_principal_ordered_mass": ordered_off - exact_unit_ordered_off,
        "blocks": block_rows,
    }


def synthetic_guard(P=16, N=32):
    # Logical countermodel: exact labels and residue labels are all distinct,
    # but every F-value is a nonzero rational square. Hence all quadratic
    # trace columns are identical although residue collision energy is diagonal.
    exact_pair_energy = N
    residue_collision_energy = N
    second_moment = P * (P - 1) * N * N
    target = P * (P - 1) * N
    assert second_moment == N * target
    return {
        "states": N,
        "auxiliary_primes": P,
        "exact_pair_energy": exact_pair_energy,
        "residue_collision_energy": residue_collision_energy,
        "all_squareclass_equal": True,
        "two_auxiliary_offdiagonal_second_moment": second_moment,
        "near_linear_target": target,
        "failure_factor": N,
        "conclusion": "exact/residue collision control plus complete-trace input cannot imply SSGC without a global squareclass-transversality hypothesis",
    }


def main():
    t51 = json.loads(T51.read_text())
    th14 = json.loads(TH14.read_text())
    t43 = json.loads(T43.read_text())
    t44 = json.loads(T44.read_text())

    assert t51["boundary"] == "COMPLETE_ALIAS_FREE_EXACT_PAIR_DIAGONAL_AND_OFFDIAGONAL_RESIDUE_REDUCTION"
    assert t51["TH14_STILL_NEEDED"] is True
    assert th14["status"] == "COMPLETE_TWO_AUXILIARY_SELECTOR_RECEIVER_AND_RESIDUE_COLLISION_CLOSURE"
    assert th14["proof_boundary"]["aggregate_same_modulus_residue_collision_energy_proved"] is True
    assert th14["proof_boundary"]["selector_sensitive_gaussian_completion_theorem_proved"] is False
    assert th14["residue_collision"]["global_equal_squareclass_resonance_absorbed_by_tH5"] is False
    assert t43["decision"]["FROZEN_PRINCIPAL_BLOCKS_ALL_LD2_TRANSVERSE"] is True
    assert t43["principal_collision_audit"]["ld2_transverse_blocks"] == 16
    assert t44["principal"]["distinct_ell"] == 14
    assert t44["principal"]["distinct_ell_cross_good"] == 14
    assert t44["principal"]["same_ell"] == 2

    t36mod = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42mod = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42mod["reciprocal_quotient"](t36mod["build_frozen_states"]())
    assert len(reps) == 560

    principal = principal_pair_audit(reps)
    assert principal["H"] == 560
    assert principal["A1"] == 592
    assert principal["principal_offdiagonal_unordered_blocks"] == 16
    assert principal["principal_offdiagonal_ordered_mass"] == 32
    assert principal["same_ell_ordered_mass"] == 4
    assert principal["distinct_ell_ordered_mass"] == 28

    guard = synthetic_guard()

    report = {
        "stage": "14-t52",
        "inputs": {
            "t51_alias_free_diagonal_closed": True,
            "tH14_residue_collision_closed": True,
            "tH14_SSGC_open": True,
            "tH14_global_squareclass_resonance_not_absorbed": True,
        },
        "principal_resonance_identity": {
            "statement": "if [Ftilde(z)]=[Ftilde(z')], then chi_p(Ftilde(z))=chi_p(Ftilde(z')) for every good auxiliary p; this coherence is independent of whether z,z' share a local U/V residue class",
            "consequence": "any target-scale SSGC theorem on the physical unit-weight family implies the t49 near-linear principal collision bound A1<=H*B^o(1)",
            "converse": "A1 near-linear alone does not prove SSGC because nonprincipal trace correlations remain; SSGC is stronger but necessarily contains the principal theorem",
        },
        "frozen_principal_audit": principal,
        "synthetic_quantifier_guard": guard,
        "old_barrier_reidentification": {
            "t43_all_frozen_principal_blocks_LD2_transverse": True,
            "t43_principal_blocks": 16,
            "t44_distinct_ell_principal_blocks": 14,
            "t44_distinct_ell_cross_good_principal_blocks": 14,
            "t44_same_ell_principal_blocks": 2,
            "primary_live_object": "GenericCrossGoodLD2KummerPrincipalIncidence",
            "same_ell_slice": "separate exceptional slice",
            "interpretation": "after t51/tH14 local residue cleanup, the principal part of SSGC returns exactly to the generic LD2-transverse cross-good Kummer incidence isolated at t43/t44",
        },
        "corrected_ssgc_contract": {
            "local_residue_component": "closed at P^2*E_A*B^o(1) by tH14 and strengthened by t51 in rho>1/8 alias-free regime",
            "principal_global_component": "requires A1/off-residue equal-squareclass incidence control; cannot be supplied by local completion alone",
            "nonprincipal_component": "still requires signed two-auxiliary trace dispersion after common-refinement retention",
            "forbidden_claim": "t32 complete angular cancellation + tH5 exact-pair energy + tH14 residue collision closure => SSGC",
            "noncircular_route": "prove/bound GenericCrossGoodLD2KummerPrincipalIncidence separately, then combine with a genuinely nonprincipal selector-dispersion estimate",
        },
        "tH_decision": {
            "tH14_consumed": True,
            "additional_tH15_needed": False,
            "reason": "the newly exposed obstruction is live principal Kummer incidence already represented by t42-t44, not missing infrastructure",
        },
        "decision": {
            "STAGE14_T52": "COMPLETE_SSGC_PRINCIPAL_RESONANCE_AUDIT_AND_KUMMER_REIDENTIFICATION",
            "TH14_CONSUMED": True,
            "AGGREGATE_RESIDUE_COLLISION_CLOSED": True,
            "SSGC_CONTAINS_GLOBAL_PRINCIPAL_COLLISION_SUBPROBLEM": True,
            "RESIDUE_COLLISION_CONTROL_ALONE_IMPLIES_SSGC": False,
            "SYNTHETIC_SQUARECLASS_COHERENCE_COUNTERMODEL": True,
            "FROZEN_PRINCIPAL_BLOCKS_ALL_LD2_TRANSVERSE": True,
            "FROZEN_DISTINCT_ELL_PRINCIPAL_BLOCKS_ALL_CROSS_GOOD": True,
            "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_REQUIRED": True,
            "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED": False,
            "NONPRINCIPAL_SELECTOR_DISPERSION_PROVED": False,
            "SELECTOR_SENSITIVE_GAUSSIAN_COMPLETION_THEOREM_PROVED": False,
            "GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "TH15_NEEDED": False,
            "NEXT": "Stage14-t53 attack GenericCrossGoodLD2KummerPrincipalIncidence directly, with the 14 distinct-ell cross-good principal blocks as the generic model and the 2 same-ell blocks separated; do not treat SSGC as an independent black-box completion theorem",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
