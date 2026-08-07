#!/usr/bin/env python3
"""Stage13-4a: finite layer ledger for the two near-1 components ac and bc.

This is deliberately a cheap discriminator.  It does not re-enumerate cuboids.
Instead it reads the locked Stage13-3 reports and asks where the finite ac/bc
closeness survives or collapses across already-audited structural layers.

Primary diagnostic:

    epsilon_ac_bc = (X_ac - X_bc) / (X_ac + X_bc)

for any positive two-component weight X.  This is symmetric under overall
rescaling and equals 0 at exact ac=bc symmetry.

The script accepts both the compact committed representation-density report
schema and the nested schema emitted by representation_density.py.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
RAW_PATH = ROOT / "stages/stage13/data/13-3/raw_incidence_report.json"
REP_PATH = ROOT / "stages/stage13/data/13-3/representation_density_report.json"
BOUNDARY_PATH = ROOT / "stages/stage13/data/13-3/boundary_stability_report.json"
OUTPUT = ROOT / "stages/stage13/data/13-4/ac_bc_gap_report.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def eps_from_pair(ac: float, bc: float) -> float:
    return (ac - bc) / (ac + bc)


def eps_from_ratio(r: float) -> float:
    return (r - 1.0) / (r + 1.0)


def ratio_from_pair(ac: float, bc: float) -> float:
    return ac / bc


def rep_ratio(row: dict[str, Any], key: str) -> float:
    # Compact committed report: shell_neutral_ratio_bc / G_neutral_ratio_bc.
    compact = f"{key}_ratio_bc"
    if compact in row:
        return float(row[compact]["ac"])
    # Full script-emitted report: row[key]["ratio_bc"].
    return float(row[key]["ratio_bc"]["ac"])


def parity_block(rep: dict[str, Any]) -> dict[str, Any]:
    if "B100000_detail" in rep:
        return rep["B100000_detail"]["parity_control"]
    top = rep["rows"][-1]
    return top["parity_control"]


def parity_neutral_ratio(block: dict[str, Any]) -> float:
    if "shell_neutral_ratio_bc" in block:
        return float(block["shell_neutral_ratio_bc"]["ac"])
    return float(block["shell_neutral_ratio_bc"]["ac"])


def build_report() -> dict[str, Any]:
    raw = load(RAW_PATH)
    rep = load(REP_PATH)
    boundary = load(BOUNDARY_PATH)

    rep_by_B = {int(row["B"]): row for row in rep["rows"]}
    rows = []

    for row in raw["rows"]:
        B = int(row["B"])
        rr = rep_by_B[B]
        ac = float(row["raw_incidence"]["ac"])
        bc = float(row["raw_incidence"]["bc"])
        eac = float(row["exact_one"]["ac"])
        ebc = float(row["exact_one"]["bc"])
        shell_r = rep_ratio(rr, "shell_neutral")
        g_r = rep_ratio(rr, "G_neutral")
        rows.append(
            {
                "B": B,
                "raw": {
                    "ac": int(ac),
                    "bc": int(bc),
                    "difference": int(ac - bc),
                    "ratio_ac_over_bc": ratio_from_pair(ac, bc),
                    "epsilon": eps_from_pair(ac, bc),
                },
                "exact_one": {
                    "ac": int(eac),
                    "bc": int(ebc),
                    "difference": int(eac - ebc),
                    "ratio_ac_over_bc": ratio_from_pair(eac, ebc),
                    "epsilon": eps_from_pair(eac, ebc),
                },
                "overlap_change_in_ac_minus_bc": int((eac - ebc) - (ac - bc)),
                "shell_neutral": {
                    "ratio_ac_over_bc": shell_r,
                    "epsilon": eps_from_ratio(shell_r),
                },
                "G_neutral": {
                    "ratio_ac_over_bc": g_r,
                    "epsilon": eps_from_ratio(g_r),
                },
            }
        )

    geom_r = float(rep["metadata"]["geometric_reference"]["ratio_bc"]["ac"])
    top = rows[-1]
    pctl = parity_block(rep)

    parity = {}
    for kind in ("OE", "EE"):
        block = pctl[kind]
        raw_r = float(block["raw_ratio_bc"]["ac"])
        neutral_r = float(block["shell_neutral_ratio_bc"]["ac"])
        parity[kind] = {
            "raw_ratio_ac_over_bc": raw_r,
            "raw_epsilon": eps_from_ratio(raw_r),
            "shell_neutral_ratio_ac_over_bc": neutral_r,
            "shell_neutral_epsilon": eps_from_ratio(neutral_r),
            "neutralization_delta_ratio": neutral_r - raw_r,
        }

    outer_r = float(
        boundary["largest_cutoff_boundary_test"]["outer_half_ratio_bc"]["ac"]
    )

    largest = {
        "B": 100000,
        "archimedean_geometry": {
            "ratio_ac_over_bc": geom_r,
            "epsilon": eps_from_ratio(geom_r),
        },
        "raw": top["raw"],
        "exact_one": top["exact_one"],
        "shell_neutral": top["shell_neutral"],
        "G_neutral": top["G_neutral"],
        "outer_half_50000_100000": {
            "ratio_ac_over_bc": outer_r,
            "epsilon": eps_from_ratio(outer_r),
        },
        "parity_control": parity,
    }

    return {
        "metadata": {
            "stage": "13-4a",
            "title": "Finite ac/bc gap ledger across established Stage13-3 layers",
            "metric": "epsilon=(X_ac-X_bc)/(X_ac+X_bc)",
            "scope": "finite structural discriminator; no ac/bc asymptotic equality claim",
            "sources": [str(RAW_PATH.relative_to(ROOT)), str(REP_PATH.relative_to(ROOT)), str(BOUNDARY_PATH.relative_to(ROOT))],
        },
        "rows": rows,
        "largest_bound_ledger": largest,
        "conclusion": {
            "exact_one_overlap_explains_ac_bc_closeness": False,
            "largest_boundary_explains_ac_bc_closeness": False,
            "supported_shell_richness_explains_aggregate_ac_bc_gap": False,
            "pure_G_deweighting_nearly_equalizes_ac_bc_at_B100000": True,
            "parity_strata_respond_same_way_to_shell_neutralization": False,
            "single_exact_ac_bc_symmetry_established": False,
            "working_interpretation": (
                "The finite ac/bc closeness survives the exact-one sieve and the largest outer-boundary test. "
                "Unlike the leading-ab effect, supported shell-richness neutralization barely changes the aggregate ac/bc ratio at B=100000. "
                "Pure G(p) deweighting, however, moves ac/bc to about 1.002, while OE and EE shell-neutral responses have opposite signs. "
                "This points toward an arithmetic/parity coupling or cancellation rather than one already-proved universal ac<->bc symmetry."
            ),
            "next": (
                "Stage13-4b: split pure G(p) richness and primitive-support correction inside OE/EE and geometric subregions, "
                "and test for an involution/common factor that could explain the near equality."
            ),
        },
    }


def main() -> None:
    report = build_report()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["largest_bound_ledger"], indent=2))
    print(json.dumps(report["conclusion"], indent=2))


if __name__ == "__main__":
    main()
