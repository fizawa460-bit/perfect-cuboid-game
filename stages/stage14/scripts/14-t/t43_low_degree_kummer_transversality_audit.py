#!/usr/bin/env python3
"""Stage14-t43: tH10 receiver reuse + low-degree Kummer transversality audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T42_DATA = ROOT / "stages/stage14/data/14-t42/kummer_transversality.json"
TH10_DATA = ROOT / "stages/stage14/data/tH10/squareclass_fiber_energy_toolbox_summary.json"
OUT = ROOT / "stages/stage14/data/14-t43/low_degree_kummer_transversality.json"

HEAVY_THRESHOLD = 20


def direction_u(a: int, b: int) -> Fraction:
    return Fraction(a * a, b * b)


def direction_j(a: int, b: int) -> Fraction:
    u = direction_u(a, b)
    A = u**4 + 14 * u**2 + 1
    return 16 * A**3 / (u**2 * (1 - u**2) ** 4)


def phi2(X: Fraction, Y: Fraction) -> Fraction:
    return (
        X**3 + Y**3 - X**2 * Y**2
        + 1488 * X * Y * (X + Y)
        - 162000 * (X**2 + Y**2)
        + 40773375 * X * Y
        + 8748000000 * (X + Y)
        - 157464000000000
    )


def relation_matrix(direction_keys):
    js = {d: direction_j(*d) for d in direction_keys}
    out = {}
    counts = Counter()
    for d1 in direction_keys:
        for d2 in direction_keys:
            same = js[d1] == js[d2]
            isog2 = phi2(js[d1], js[d2]) == 0
            if same:
                label = "degree1_same_j"
            elif isog2:
                label = "degree2_isogenous"
            else:
                label = "ld2_transverse"
            out[(d1, d2)] = label
            counts[label] += 1
    return out, counts


def audit_principal_blocks(reps, relation):
    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)
    counts = Counter()
    same_ell = 0
    same_common = 0
    for members in by_kernel.values():
        if len(members) != 2:
            continue
        x, y = members
        d1 = (x["a"], x["b"])
        d2 = (y["a"], y["b"])
        assert d1 != d2
        counts[relation[(d1, d2)]] += 1
        same_ell += x["ell"] == y["ell"]
    assert sum(counts.values()) == 16
    return counts, same_ell


def audit_autocorrelation(reps, relation, cross_kernel):
    c = Counter()
    c_offdir = Counter()
    c_offdir_low = Counter()
    relation_pair_mass = Counter()
    for x in reps:
        dx = (x["a"], x["b"])
        for y in reps:
            dy = (y["a"], y["b"])
            tau = cross_kernel(x["kernel"], y["kernel"])
            c[tau] += 1
            if dx != dy:
                c_offdir[tau] += 1
                lab = relation[(dx, dy)]
                relation_pair_mass[lab] += 1
                if lab != "ld2_transverse":
                    c_offdir_low[tau] += 1

    H = len(reps)
    A1 = c[1]
    assert H == 560 and A1 == 592
    heavy = {tau: mult for tau, mult in c.items() if tau != 1 and mult > HEAVY_THRESHOLD}
    top20 = sorted(((tau, mult) for tau, mult in c.items() if tau != 1), key=lambda kv: (-kv[1], kv[0]))[:20]
    return {
        "H": H,
        "A1": A1,
        "max_nonprincipal_multiplicity": max(mult for tau, mult in c.items() if tau != 1),
        "heavy_threshold": HEAVY_THRESHOLD,
        "heavy_kernel_count": len(heavy),
        "heavy_pair_mass": sum(heavy.values()),
        "heavy_off_direction_low_degree_exception_mass": sum(c_offdir_low[tau] for tau in heavy),
        "top20_all_low_degree_exception_mass_zero": all(c_offdir_low[tau] == 0 for tau, _ in top20),
        "off_direction_degree1_same_j_pair_mass": relation_pair_mass["degree1_same_j"],
        "off_direction_degree2_isogenous_pair_mass": relation_pair_mass["degree2_isogenous"],
        "off_direction_ld2_transverse_pair_mass": relation_pair_mass["ld2_transverse"],
    }


def main():
    t42 = json.loads(T42_DATA.read_text())
    th10 = json.loads(TH10_DATA.read_text())
    assert t42["decision"]["STAGE14_T42"] == "COMPLETE_RECIPROCAL_QUOTIENT_AND_TWISTED_KUMMER_ENERGY_REDUCTION"
    assert th10["status"] == "COMPLETE_SQUARECLASS_FIBER_AND_AUTOCORRELATION_INCIDENCE_TOOLBOX"
    assert th10["fourth_energy_receivers"]["uniform_nonprincipal"] == "E4<=A1^2+R_non*(H^2-A1)"
    assert th10["fourth_energy_receivers"]["heavy_light"] == "E4<=A1^2+T*(H^2-A1)+(R_non-T)*M_T"

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42mod = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    states = t36["build_frozen_states"]()
    reps = t42mod["reciprocal_quotient"](states)
    direction_keys = sorted({(s["a"], s["b"]) for s in reps})
    assert len(direction_keys) == 137
    relation, rc = relation_matrix(direction_keys)
    pc, same_ell = audit_principal_blocks(reps, relation)
    ac = audit_autocorrelation(reps, relation, t42mod["cross_kernel"])

    assert rc["degree1_same_j"] == 193
    assert rc["degree2_isogenous"] == 0
    assert rc["ld2_transverse"] == 18576
    assert pc == Counter({"ld2_transverse": 16})
    assert ac["heavy_kernel_count"] == 72
    assert ac["heavy_pair_mass"] == 1834
    assert ac["heavy_off_direction_low_degree_exception_mass"] == 4
    assert ac["top20_all_low_degree_exception_mass_zero"] is True

    report = {
        "stage": "14-t43",
        "th_reuse": {
            "tH9_squareclass_autocorrelation_atlas_reused": True,
            "tH10_generic_exceptional_principal_receiver_reused": True,
            "tH10_uniform_nonprincipal_receiver_reused": True,
            "tH10_heavy_light_receiver_reused": True,
            "assessment": "tH roadwork is directly useful; t43 does not rebuild the energy bookkeeping",
        },
        "direction_family": {
            "direction_count": len(direction_keys),
            "u": "(a/b)^2",
            "legendre_lambda": "((1-u)/(1+u))^2",
            "j": "16*(u^4+14*u^2+1)^3/(u^2*(1-u^2)^4)",
            "degree1_certificate": "j(u)=j(v)",
            "degree2_certificate": "Phi_2(j(u),j(v))=0",
            "ordered_degree1_same_j_pairs": rc["degree1_same_j"],
            "ordered_offdiagonal_degree1_same_j_pairs": rc["degree1_same_j"] - len(direction_keys),
            "ordered_degree2_isogenous_pairs": rc["degree2_isogenous"],
            "ordered_ld2_transverse_pairs": rc["ld2_transverse"],
        },
        "principal_collision_audit": {
            "reciprocal_quotient_blocks": 16,
            "ld2_transverse_blocks": pc["ld2_transverse"],
            "degree1_same_j_blocks": pc["degree1_same_j"],
            "degree2_isogenous_blocks": pc["degree2_isogenous"],
            "same_canonical_ell_blocks": same_ell,
        },
        "nonprincipal_heavy_audit": ac,
        "receiver": {
            "principal": "A1=L_P+I_gen+I_exc (tH10)",
            "uniform_fourth": "E4<=A1^2+R_non*(H^2-A1) (tH10/t42)",
            "heavy_light_fourth": "E4<=A1^2+T*(H^2-A1)+(R_non-T)*M_T (tH10)",
            "t43_split": "exceptional=degree1 same-j or degree2 isogenous; generic=LD2-transverse; higher-degree isogeny remains unclassified",
        },
        "decision": {
            "STAGE14_T43": "COMPLETE_LOW_DEGREE_ISOGENY_CERTIFICATE_AND_GENERIC_KUMMER_BARRIER",
            "TH9_AUTOCORRELATION_ATLAS_REUSED": True,
            "TH10_ENERGY_RECEIVERS_REUSED": True,
            "DIRECTION_J_INVARIANT_EXACT": True,
            "DEGREE2_MODULAR_POLYNOMIAL_CERTIFICATE_EXACT": True,
            "FROZEN_PRINCIPAL_BLOCKS_ALL_LD2_TRANSVERSE": True,
            "FROZEN_DEGREE2_ISOGENOUS_DIRECTION_PAIRS": 0,
            "FROZEN_TOP20_HEAVY_KERNELS_LOW_DEGREE_EXCEPTION_FREE": True,
            "LOW_DEGREE_ISOGENY_EXPLAINS_FROZEN_HEAVY_ENERGY": False,
            "GENERIC_TWISTED_KUMMER_REMAINS_PRIMARY": True,
            "HIGHER_DEGREE_ISOGENY_EXCEPTION_CLASSIFIED": False,
            "GENERIC_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "OFF_DIRECTION_PRINCIPAL_AGGREGATE_BOUND_PROVED": False,
            "NONPRINCIPAL_TWIST_MULTIPLICITY_SUBPOLY_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t44 attack the genuinely generic LD2-transverse twisted-Kummer incidence using canonical Gaussian-prime/common-core arithmetic; use the tH10 heavy-light receiver so higher-isogeny exceptions need only be isolated when they create heavy mass",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
