#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[4]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
ST33 = ROOT / "stages" / "stage33" / "33-07"
N220_STATE = ROOT / "stages" / "stage32" / "32-01-178" / "nodes" / "N220" / "STATE.json"
N220_AUDITED = ROOT / "stages" / "stage32" / "32-01-178" / "nodes" / "N220" / "STATE-AUDITED.json"
SOURCE_BASE = "df3b29d20ef0f7da1e34fa92beada6418ad3a4ea"
LOCKED = [
    "stages/stage32/residual-32-01-production/pairing_prefix_engine.py",
    "stages/stage32/residual-32-01-production/hperp_integral_adapter.py",
    "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648aw_Z_Wpair_support_cells.py",
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
    "stages/stage32/32-01-178/nodes/N220/STATE.json",
    "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json",
    "stages/stage33/33-07/stage32_picard_marking_retained.py",
    "stages/stage33/33-07/picard_base_rows_retained.py",
]

ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def run_json(path: Path) -> dict:
    p = subprocess.run(
        [sys.executable, "-B", str(path)],
        cwd=ROOT, capture_output=True, text=True,
    )
    if p.returncode != 0:
        raise RuntimeError(
            f"dependency failed: {path.name}; rc={p.returncode}; "
            f"stdout={p.stdout[-4000:]!r}; stderr={p.stderr[-8000:]!r}"
        )
    return json.loads(p.stdout)


def lock_sources() -> None:
    subprocess.run(["git", "cat-file", "-e", f"{SOURCE_BASE}^{{commit}}"], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "diff", "--quiet", SOURCE_BASE, "--", *LOCKED],
        cwd=ROOT, check=True,
    )


def audited_total_exceptional_semantics() -> dict:
    raw = json.loads(N220_STATE.read_text())
    payload = json.loads(N220_AUDITED.read_text())
    if raw.get("node_id") != "N220":
        raise ValueError("N220 raw-state identity regression")
    definitions = raw.get("retained_result", {}).get("definitions", {})
    if definitions.get("remaining_exceptional_slot_count") != 38 or definitions.get("remaining_exceptional_mass") != "e-M10":
        raise ValueError("N220 raw exact remaining-exceptional-mass semantics regression")
    if payload.get("node_id") != "N220" or payload.get("status") != "DONE_AUDITED_EXACT_NECESSARY_PREFIX_PRUNING":
        raise ValueError("N220 audited-state identity/status regression")
    hostile = payload.get("hostile_audit", {})
    predicate = payload.get("audited_predicate", {})
    if hostile.get("result") != "PASS" or hostile.get("corrected_review_id") != 5159411821:
        raise ValueError("N220 hostile-audit authority regression")
    expected = "S10 + min(38, e-M10) >= ceil((d-16g+16)/4)"
    if predicate.get("necessary_form") != expected or not predicate.get("zero_loss_necessary_pruning"):
        raise ValueError("N220 exact remaining-exceptional-mass semantics regression")
    return {
        "authority": "AUDITED_N220_EXACT_REMAINING_EXCEPTIONAL_MASS",
        "hostile_audit_review_id": 5159411821,
        "raw_remaining_exceptional_slot_count": 38,
        "raw_remaining_exceptional_mass": "e-M10",
        "necessary_form": expected,
        "deduction": "the ten assigned exceptional coordinates have mass M10 and the remaining 38 have exact mass e-M10; hence sum_{j=93..140}<D,E_j>=e",
        "E_total_pairing_value_in_each_stratum": "e",
    }


def recover_unordered_fibration_blocks() -> tuple[list[list[int]], dict]:
    """Recover the six 8-node base loci without choosing individual node names.

    Source support has Z=(b1,b2,b3) and W=(a1,a2,a3,c).  The six
    fibration base loci are exactly the cells where one Z and one of the six
    unordered W-pairs vanish.  Their three Z-rows are the three perfect
    matchings of K4.  AW verifies this support design directly on retained
    exceptional labels, so no 48-node semantic bijection is required.
    """
    av = run_json(RES / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py")
    zd = run_json(RES / "diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py")
    aw = run_json(RES / "diagnose_stage32_post1648aw_Z_Wpair_support_cells.py")

    covers = av["coordinate_W1_W2_W3_C_recovery"]["global_four_hyperplane_exact_covers"]
    zparts = zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"]
    survivors = aw["support_design_survivors"]
    if len(covers) != 25 or len(zparts) != 1:
        raise ValueError("AV/AW exact-cover or Z-partition count regression")
    if aw.get("input_WC_exact_cover_count") != 25 or aw.get("support_design_survivor_count") != 1 or len(survivors) != 1:
        raise ValueError("AW support-design uniqueness regression")

    survivor = survivors[0]
    wanted = tuple(survivor["candidate_indices_zero_based"])
    selected = [c for c in covers if tuple(c["candidate_indices_zero_based"]) == wanted]
    if len(selected) != 1:
        raise ValueError("unique AW support-design cover lookup regression")

    zblocks = [set(b["exceptional_labels_1based"]) for b in zparts[0]["blocks"]]
    wblocks = [set(g["exceptional_labels_1based"]) for g in selected[0]["groups"]]
    if len(zblocks) != 3 or len(wblocks) != 4:
        raise ValueError("Z/W block count regression")
    if any(len(z) != 16 for z in zblocks) or any(len(w) != 24 for w in wblocks):
        raise ValueError("Z/W block size regression")

    wpairs = list(itertools.combinations(range(4), 2))
    blocks: list[list[int]] = []
    cells = []
    used_pairs = []
    per_z_counts = []
    for z_index, z in enumerate(zblocks):
        row_counts = []
        row_hits = 0
        for i, j in wpairs:
            labels = sorted(z & wblocks[i] & wblocks[j])
            row_counts.append(len(labels))
            if len(labels) == 8:
                row_hits += 1
                used_pairs.append((i, j))
                blocks.append(labels)
                cells.append({
                    "unordered_Z_block_index": z_index,
                    "unordered_W_pair_indices": [i, j],
                    "exceptional_labels_1based": labels,
                })
            elif labels:
                raise ValueError("surviving AW support cell has nonzero non-eight size")
        if row_hits != 2 or sorted(row_counts) != [0, 0, 0, 0, 8, 8]:
            raise ValueError("AW per-Z perfect-matching support regression")
        per_z_counts.append(row_counts)

    canonical_blocks = sorted(tuple(x) for x in blocks)
    if len(canonical_blocks) != 6 or sorted(used_pairs) != wpairs:
        raise ValueError("AW six-pair support regression")
    flat = [x for block in canonical_blocks for x in block]
    if len(flat) != 48 or len(set(flat)) != 48 or set(flat) != set(range(93, 141)):
        raise ValueError("AW fibration cells do not partition all 48 exceptionals")

    return [list(x) for x in canonical_blocks], {
        "producer_chain": [
            "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py",
            "diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py",
            "diagnose_stage32_post1648aw_Z_Wpair_support_cells.py",
        ],
        "individual_48node_semantic_bijection_required": False,
        "ordered_coordinate_names_required": False,
        "source_support_dictionary": "Z=(b1,b2,b3), W=(a1,a2,a3,c); six base loci are one Z plus one W-pair, with the three Z rows equal to the three perfect matchings of K4",
        "input_WC_exact_cover_count": len(covers),
        "unordered_Z_partition_count": len(zparts),
        "support_design_survivor_count": len(survivors),
        "selected_W_cover_candidate_indices_zero_based": list(wanted),
        "selected_W_cover_exceptional_mass_sums": selected[0]["exceptional_mass_sums"],
        "per_Z_Wpair_cell_sizes": per_z_counts,
        "used_Wpairs_exactly_once": [list(x) for x in used_pairs],
        "unordered_six_base_locus_cells": cells,
    }


def span_profile(rows: list[Matrix], targets: list[Matrix]) -> dict:
    base = Matrix.vstack(*rows)
    tmat = Matrix.vstack(*targets)
    base_rank = int(base.rank())
    joined_rank = int(Matrix.vstack(base, tmat).rank())
    per_target = []
    for i, target in enumerate(targets):
        rank_with = int(Matrix.vstack(base, target).rank())
        recoverable = rank_with == base_rank
        entry = {"target_index": i, "recoverable_over_Q": recoverable}
        if recoverable:
            sol, params = base.T.gauss_jordan_solve(target.T)
            if params.rows:
                sol = sol.xreplace({x: 0 for x in params})
            coeffs = [Fraction(x) for x in sol]
            entry["one_exact_coefficient_vector"] = [
                {"num": x.numerator, "den": x.denominator} for x in coeffs
            ]
            entry["coefficient_denominator_lcm"] = __import__("math").lcm(
                *[x.denominator for x in coeffs]
            )
        per_target.append(entry)
    return {
        "observable_count": len(rows),
        "observable_rank_over_Q": base_rank,
        "target_rank_over_Q": int(tmat.rank()),
        "joined_rank_over_Q": joined_rank,
        "quotient_target_rank_over_Q": joined_rank - base_rank,
        "all_targets_recoverable_over_Q": joined_rank == base_rank,
        "per_target": per_target,
    }


def main() -> None:
    lock_sources()
    total_exceptional_semantics = audited_total_exceptional_semantics()
    block_labels, block_adapter = recover_unordered_fibration_blocks()

    sys.path.insert(0, str(RES))
    from hperp_integral_adapter import (  # noqa: E402
        HperpIntegralPairingAdapter, RETAINED_BASIS_KNOWN_LABELS_1BASED, _parse_hperp,
    )

    marking = load_retained(ST33 / "stage32_picard_marking_retained.py", "nef_marking")
    bundle = load_retained(ST33 / "picard_base_rows_retained.py", "nef_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    if coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("Picard64 shape regression")

    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]
    retained_labels = list(RETAINED_BASIS_KNOWN_LABELS_1BASED)
    retained_idx = [x - 1 for x in retained_labels]
    Kq = Matrix([[degrees[i] for i in retained_idx]]) * gram.inv()
    if any(getattr(x, "q", 1) != 1 for x in Kq):
        raise ValueError("hyperplane/canonical class not integral")
    H = Matrix([[int(x) for x in Kq]])
    if int((H * gram * H.T)[0, 0]) != 16:
        raise ValueError("H=K square regression")

    targets = []
    node_rows = []
    for i, labels in enumerate(block_labels):
        D = H.copy()
        for lab in labels:
            D -= coords.row(lab - 1)
        targets.append(D)
        node_rows.append({
            "unordered_block_index": i,
            "exceptional_labels_1based": labels,
        })

    base_rows = [H] + [coords.row(lab - 1) for lab in ASSIGNMENT_LABELS]
    Etotal = Matrix([[0] * 64])
    for lab in range(93, 141):
        Etotal += coords.row(lab - 1)

    base_profile = span_profile(base_rows, targets)
    exact_profile = span_profile(base_rows + [Etotal], targets)

    if set().union(*(set(x) for x in block_labels)) != set(range(93, 141)):
        raise ValueError("partition regression")
    sum_target = Matrix([[0] * 64])
    for D in targets:
        sum_target += D
    if sum_target != 6 * H - Etotal:
        raise ValueError("sum L_Q identity regression")

    observed_exceptionals = sorted(x for x in ASSIGNMENT_LABELS if x >= 93)
    coverage = []
    for i, labels in enumerate(block_labels):
        hit = sorted(set(labels) & set(observed_exceptionals))
        coverage.append({
            "unordered_block_index": i,
            "observed_exceptional_labels_1based": hit,
            "observed_count": len(hit),
            "missing_count": 8 - len(hit),
        })

    # Construct an explicit minimum-size observable basis.  E_total already
    # supplies one relation among the six block sums, so the quotient-rank
    # lower bound is five.  Reuse every individually observed exceptional and
    # request only the residual mass of the first five canonical blocks.  The
    # sixth block mass is then E_total minus the first five complete masses.
    observed_set = set(observed_exceptionals)
    residual_supports = [
        sorted(set(labels) - observed_set) for labels in block_labels[:5]
    ]
    expected_residual_supports = [
        [100],
        [104, 105, 106, 107, 108],
        [109, 110, 111, 112, 113, 114, 115, 116],
        [117, 118, 119, 120, 121, 122, 123, 124],
        [125, 126, 127, 128, 129, 130, 131, 132],
    ]
    if residual_supports != expected_residual_supports:
        raise ValueError("canonical residual fibration-block support regression")

    residual_rows = []
    residual_specs = []
    for i, support in enumerate(residual_supports):
        row = Matrix([[0] * 64])
        for lab in support:
            row += coords.row(lab - 1)
        residual_rows.append(row)
        residual_specs.append({
            "observable_index": i,
            "semantics": "sum of pairings on residual exceptional support",
            "support_exceptional_labels_1based": support,
            "support_size": len(support),
            "completes_canonical_fibration_block_index": i,
            "already_individually_observed_in_block": coverage[i]["observed_exceptional_labels_1based"],
        })

    constructive_profile = span_profile(
        base_rows + [Etotal] + residual_rows,
        targets,
    )
    deficiency = exact_profile["quotient_target_rank_over_Q"]
    rank_gain = (
        constructive_profile["observable_rank_over_Q"]
        - exact_profile["observable_rank_over_Q"]
    )
    if deficiency != 5:
        raise ValueError("exact fibration quotient-rank deficiency regression")
    if len(residual_rows) != deficiency or rank_gain != deficiency:
        raise ValueError("five residual observables are not independent modulo current audited observables")
    if not constructive_profile["all_targets_recoverable_over_Q"] or constructive_profile["quotient_target_rank_over_Q"] != 0:
        raise ValueError("five residual observables do not recover all six fibration divisors")

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_RECOVERABILITY_PREFLIGHT_V4",
        "source_base_exact_head": SOURCE_BASE,
        "source_lock": "git diff --quiet SOURCE_BASE over exact Picard64/AV/AW/compression/N220 raw+audited inputs",
        "fibration_block_adapter": block_adapter,
        "stoll_testa_divisor_identity": "D_Q=2F_Q=H-sum_{P in B_Q}E_P",
        "assignment_labels_1based": ASSIGNMENT_LABELS,
        "observed_exceptional_labels_1based": observed_exceptionals,
        "six_rank3_base_loci_unordered": node_rows,
        "six_base_loci_partition_all_48_exceptionals": True,
        "coverage": coverage,
        "base_observables": {
            "semantics": "H pairing (degree) plus the 11 retained assignment pairings",
            "profile": base_profile,
        },
        "audited_exact_total_exceptional_observable": {
            "semantics": total_exceptional_semantics,
            "identity": "E_total=sum_{j=93..140} E_j and <D,E_total>=e",
            "fibration_sum_identity": "sum_Q L_Q = 6*degree - e",
            "profile": exact_profile,
        },
        "minimum_additional_arbitrary_linear_observables_over_Q": {
            "without_audited_E_total": base_profile["quotient_target_rank_over_Q"],
            "with_audited_E_total": deficiency,
        },
        "constructive_minimal_five_observable_certificate": {
            "lower_bound_from_exact_quotient_rank": deficiency,
            "observable_count": len(residual_specs),
            "observable_support_sizes": [x["support_size"] for x in residual_specs],
            "observables": residual_specs,
            "reconstruction": {
                "blocks_0_through_4": "complete each block mass by adding its already observed singleton pairings to the listed residual observable",
                "block_5": "B5 = E_total - (B0+B1+B2+B3+B4)",
                "fibration_divisors": "L_i = H - B_i for i=0..5",
            },
            "rank_gain_over_current_audited_observables": rank_gain,
            "profile_after_adding_five": constructive_profile,
            "minimal_over_Q": True,
        },
        "producer_recommendation": (
            "CURRENT_AUDITED_OBSERVABLES_SUFFICE"
            if exact_profile["all_targets_recoverable_over_Q"]
            else "DO_NOT_RUN_BOUNDED_VIOLATION_CENSUS_YET__EXPOSE_THE_CERTIFIED_FIVE_RESIDUAL_BLOCK_SUMS"
        ),
        "bounded_violation_census_run": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "td02_additive_credit_claimed": False,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
