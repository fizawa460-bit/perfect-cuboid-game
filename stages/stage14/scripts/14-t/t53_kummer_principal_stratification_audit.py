#!/usr/bin/env python3
"""Stage14-t53: stratify post-residue generic LD2 Kummer principal incidences."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T52 = ROOT / "stages/stage14/data/14-t52/ssgc_principal_resonance_frozen.json"
OUT = ROOT / "stages/stage14/data/14-t53/kummer_principal_stratification.json"


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    return (s["eps"], s["delta"], h, s["branch"])


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def exact_unit_pair_key(s):
    return (common_packet_key(s), gaussian_unit_key(s["U"]), gaussian_unit_key(s["V"]))


def cover_key(s):
    return (min(s["p"], s["q"]), max(s["p"], s["q"]))


def block_flags(x, y):
    kx = x["n"] // x["delta"]
    ky = y["n"] // y["delta"]
    hx = x["eps"] * x["m"] // kx
    hy = y["eps"] * y["m"] // ky
    return {
        "same_U_unit": gaussian_unit_key(x["U"]) == gaussian_unit_key(y["U"]),
        "same_V_unit": gaussian_unit_key(x["V"]) == gaussian_unit_key(y["V"]),
        "same_branch": x["branch"] == y["branch"],
        "same_common_packet": common_packet_key(x) == common_packet_key(y),
        "same_cover": cover_key(x) == cover_key(y),
        "same_ell": x["ell"] == y["ell"],
        "same_eps": x["eps"] == y["eps"],
        "same_delta": x["delta"] == y["delta"],
        "same_h": hx == hy,
        "same_m": x["m"] == y["m"],
        "same_n": x["n"] == y["n"],
        "same_exact_unit_pair": exact_unit_pair_key(x) == exact_unit_pair_key(y),
    }


def main():
    t52 = json.loads(T52.read_text())
    assert t52["boundary"] == "COMPLETE_SSGC_PRINCIPAL_RESONANCE_AUDIT_AND_KUMMER_REIDENTIFICATION"
    assert t52["FROZEN_POST_RESIDUE_PRINCIPAL_BLOCKS"] == 14
    assert t52["FROZEN_POST_RESIDUE_DISTINCT_ELL_CROSS_GOOD_BLOCKS"] == 12
    assert t52["FROZEN_POST_RESIDUE_SAME_ELL_BLOCKS"] == 2

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)

    all_blocks = []
    post = []
    for kernel, members in sorted(by_kernel.items()):
        if len(members) != 2:
            continue
        x, y = members
        flags = block_flags(x, y)
        row = {
            "kernel": kernel,
            "x": {k: x[k] for k in ("a","b","p","q","ell","m","n","delta","eps","branch")},
            "y": {k: y[k] for k in ("a","b","p","q","ell","m","n","delta","eps","branch")},
            **flags,
        }
        all_blocks.append(row)
        if not flags["same_exact_unit_pair"]:
            post.append(row)

    assert len(all_blocks) == 16
    assert len(post) == 14

    flag_names = [
        "same_U_unit","same_V_unit","same_branch","same_common_packet","same_cover",
        "same_ell","same_eps","same_delta","same_h","same_m","same_n",
    ]
    counts = {name: sum(int(r[name]) for r in post) for name in flag_names}
    type_counter = Counter((r["same_U_unit"], r["same_V_unit"], r["same_ell"]) for r in post)

    distinct = [r for r in post if not r["same_ell"]]
    sameell = [r for r in post if r["same_ell"]]
    assert len(distinct) == 12
    assert len(sameell) == 2

    distinct_counts = {name: sum(int(r[name]) for r in distinct) for name in flag_names}
    sameell_counts = {name: sum(int(r[name]) for r in sameell) for name in flag_names}

    shared_u = [r for r in distinct if r["same_U_unit"]]
    shared_v = [r for r in distinct if r["same_V_unit"]]
    transverse = [r for r in distinct if not r["same_U_unit"] and not r["same_V_unit"]]

    # Every post-residue block has distinct exact Gaussian-pair labels by construction.
    assert all(not r["same_exact_unit_pair"] for r in post)
    # t52/t44 identify every distinct-ell post-residue block as cross-good LD2.
    # We retain that merged classification; this stage only refines its arithmetic fibers.

    report = {
        "stage": "14-t53",
        "input": {
            "post_residue_principal_blocks": len(post),
            "distinct_ell_cross_good_ld2_blocks": len(distinct),
            "same_ell_ld2_blocks": len(sameell),
        },
        "post_residue_flag_counts": counts,
        "distinct_ell_flag_counts": distinct_counts,
        "same_ell_flag_counts": sameell_counts,
        "distinct_ell_strata": {
            "shared_U_blocks": len(shared_u),
            "shared_V_blocks": len(shared_v),
            "shared_U_or_V_union_blocks": len([r for r in distinct if r["same_U_unit"] or r["same_V_unit"]]),
            "genuinely_UV_transverse_blocks": len(transverse),
            "type_counts": {str(k): v for k, v in sorted(type_counter.items(), key=lambda kv: str(kv[0]))},
        },
        "shared_U_blocks": shared_u,
        "shared_V_blocks": shared_v,
        "UV_transverse_blocks": transverse,
        "same_ell_blocks": sameell,
        "decision": {
            "STAGE14_T53_EXPLORATORY": "POST_RESIDUE_KUMMER_PRINCIPAL_STRATIFICATION",
            "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "TH15_NEEDED": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
