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
    """j of y^2=(b^2 x^2-a^2)(b^2-a^2 x^2), via Legendre lambda."""
    u = direction_u(a, b)
    A = u**4 + 14 * u**2 + 1
    return 16 * A**3 / (u**2 * (1 - u**2) ** 4)


def phi2(X: Fraction, Y: Fraction) -> Fraction:
    """Classical modular polynomial Phi_2(X,Y)."""
    return (
        X**3
        + Y**3
        - X**2 * Y**2
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
    return out, dict(counts)


def audit_principal_blocks(t42, relation):
    blocks = t42["off_direction_principal"]["collision_blocks"]
    counts = Counter()
    rows = []
    for block in blocks:
        d1 = tuple(block["directions"][0])
        d2 = tuple(block["directions"][1])
        label = relation[(d1, d2)]
        counts[label] += 1
        rows.append({
            "kernel": block["kernel"],
            "directions": [list(d1), list(d2)],
            "relation": label,
            "same_ell": block["same_ell"],
            "same_common_packet": block["same_common_packet"],
        })
    assert len(blocks) == 16
    return dict(counts), rows


def audit_autocorrelation(reps, relation, cross_kernel):
    c = Counter()
    c_offdir = Counter()
    c_offdir_ld2 = Counter()
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
                    c_offdir_ld2[tau] += 1

    A1 = c[1]
    H = len(reps)
    assert H == 560 and A1 == 592
    heavy = {tau: mult for tau, mult in c.items() if tau != 1 and mult > HEAVY_THRESHOLD}
    heavy_mass = sum(heavy.values())
    heavy_low_degree_mass = sum(c_offdir_ld2[tau] for tau in heavy)
    max_non = max(mult for tau, mult in c.items() if tau != 1)

    top = sorted(((tau, mult) for tau, mult in c.items() if tau != 1), key=lambda kv: (-kv[1], kv[0]))[:20]
    top_rows = []
    for tau, mult in top:
        top_rows.append({
            "tau": tau,
            "multiplicity": mult,
            "off_direction_mass": c_offdir[tau],
            "off_direction_low_degree_exception_mass": c_offdir_ld2[tau],
        })

    return {
        "H": H,
        "A1": A1,
        "max_nonprincipal_multiplicity": max_non,
        "heavy_threshold": HEAVY_THRESHOLD,
        "heavy_kernel_count": len(heavy),
        "heavy_pair_mass": heavy_mass,
        "heavy_off_direction_low_degree_exception_mass": heavy_low_degree_mass,
        "relation_pair_mass_off_direction": dict(relation_pair_mass),
        "top_nonprincipal": top_rows,
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
    relation, relation_counts = relation_matrix(direction_keys)
    principal_counts, principal_rows = audit_principal_blocks(t42, relation)
    autocorr = audit_autocorrelation(reps, relation, t42mod["cross_kernel"])

    report = {
        "stage": "14-t43-probe",
        "th_reuse": {
            "tH9_role": "squareclass autocorrelation / cross-ratio atlas",
            "tH10_role": "generic-exceptional principal receiver plus uniform and heavy-light E4 receivers",
            "tH10_used_directly": True,
        },
        "direction_family": {
            "u": "(a/b)^2",
            "legendre_lambda": "((1-u)/(1+u))^2",
            "j": "16*(u^4+14*u^2+1)^3/(u^2*(1-u^2)^4)",
            "degree2_exception_certificate": "Phi_2(j(u),j(v))=0",
            "relation_counts_on_direction_grid": relation_counts,
        },
        "principal_16_blocks": {
            "relation_counts": principal_counts,
            "blocks": principal_rows,
        },
        "autocorrelation_low_degree_audit": autocorr,
        "boundary_probe": {
            "LOW_DEGREE_2_ISOGENY_EXCEPTION_CERTIFICATE_EXACT": True,
            "TH10_GENERIC_EXCEPTIONAL_RECEIVER_REUSED": True,
            "GENERIC_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "HIGHER_DEGREE_ISOGENY_EXCEPTION_CLASSIFIED": False,
            "OFF_DIRECTION_PRINCIPAL_AGGREGATE_BOUND_PROVED": False,
            "NONPRINCIPAL_TWIST_MULTIPLICITY_SUBPOLY_PROVED": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
