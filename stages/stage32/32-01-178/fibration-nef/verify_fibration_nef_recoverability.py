#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[4]
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
ST33 = ROOT / "stages" / "stage33" / "33-07"
SOURCE_BASE = "df3b29d20ef0f7da1e34fa92beada6418ad3a4ea"
LOCKED = [
    "stages/stage32/residual-32-01-production/pairing_prefix_engine.py",
    "stages/stage32/residual-32-01-production/hperp_integral_adapter.py",
    "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648aw_Z_Wpair_support_cells.py",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648az_full_48node_equivariant_bijection.py",
    "stages/stage33/33-07/stage32_picard_marking_retained.py",
    "stages/stage33/33-07/picard_base_rows_retained.py",
]

ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
FIBRATIONS = [
    ("Q_a1_b1_c", ("a1", "b1", "c")),
    ("Q_a2_b2_c", ("a2", "b2", "c")),
    ("Q_a3_b3_c", ("a3", "b3", "c")),
    ("Q_a2_a3_b1", ("a2", "a3", "b1")),
    ("Q_a1_a3_b2", ("a1", "a3", "b2")),
    ("Q_a1_a2_b3", ("a1", "a2", "b3")),
]


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

    bij = run_json(RES / "diagnose_stage32_post1648az_full_48node_equivariant_bijection.py")
    if not bij["explicit_48_node_bijection_obtained"] or bij["source_node_count"] != 48:
        raise ValueError("48-node bijection regression")

    node_rows = []
    block_labels = []
    all_labels = set()
    for name, triple in FIBRATIONS:
        labels = sorted(
            int(r["retained_exceptional_label_1based"])
            for r in bij["records"]
            if set(triple).issubset(set(r["source_zero_coordinates"]))
        )
        if len(labels) != 8:
            raise ValueError(f"{name}: expected 8 base nodes, got {len(labels)}")
        node_rows.append({"name": name, "zero_coordinates": list(triple), "exceptional_labels_1based": labels})
        block_labels.append(labels)
        if all_labels.intersection(labels):
            raise ValueError("rank-3 base loci are not disjoint")
        all_labels.update(labels)
    if all_labels != set(range(93, 141)):
        raise ValueError("six base loci do not partition all 48 exceptional labels")

    targets = []
    for labels in block_labels:
        D = H.copy()
        for lab in labels:
            D -= coords.row(lab - 1)
        targets.append(D)

    base_rows = [H] + [coords.row(lab - 1) for lab in ASSIGNMENT_LABELS]
    Etotal = Matrix([[0] * 64])
    for lab in range(93, 141):
        Etotal += coords.row(lab - 1)

    base_profile = span_profile(base_rows, targets)
    total_profile = span_profile(base_rows + [Etotal], targets)

    if set().union(*(set(x) for x in block_labels)) != set(range(93, 141)):
        raise ValueError("partition regression")
    sum_target = Matrix([[0] * 64])
    for D in targets:
        sum_target += D
    if sum_target != 6 * H - Etotal:
        raise ValueError("sum L_Q identity regression")

    observed_exceptionals = sorted(x for x in ASSIGNMENT_LABELS if x >= 93)
    coverage = []
    for row in node_rows:
        hit = sorted(set(row["exceptional_labels_1based"]) & set(observed_exceptionals))
        coverage.append({
            "name": row["name"],
            "observed_exceptional_labels_1based": hit,
            "observed_count": len(hit),
            "missing_count": 8 - len(hit),
        })

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_RECOVERABILITY_PREFLIGHT_V1",
        "source_base_exact_head": SOURCE_BASE,
        "source_lock": "git diff --quiet SOURCE_BASE over exact Picard64/node/compression inputs",
        "stoll_testa_divisor_identity": "D_Q=2F_Q=H-sum_{P in B_Q}E_P",
        "assignment_labels_1based": ASSIGNMENT_LABELS,
        "observed_exceptional_labels_1based": observed_exceptionals,
        "six_rank3_base_loci": node_rows,
        "six_base_loci_partition_all_48_exceptionals": True,
        "coverage": coverage,
        "base_observables": {
            "semantics": "H pairing (degree) plus the 11 retained assignment pairings",
            "profile": base_profile,
        },
        "base_plus_exact_total_exceptional": {
            "semantics": "base observables plus E_total=sum_{93..140} E_j, ONLY if current stratum e is proven to equal this exact pairing total",
            "identity": "sum_Q L_Q = 6*degree - E_total",
            "profile": total_profile,
        },
        "minimum_additional_arbitrary_linear_observables_over_Q": {
            "without_E_total": base_profile["quotient_target_rank_over_Q"],
            "with_exact_E_total": total_profile["quotient_target_rank_over_Q"],
        },
        "producer_recommendation": (
            "CURRENT_OBSERVABLES_SUFFICE"
            if base_profile["all_targets_recoverable_over_Q"]
            else "DO_NOT_RUN_BOUNDED_VIOLATION_CENSUS_YET__ADD_MINIMAL_TARGET_OBSERVABLES_OR_PROVE_EXACT_E_TOTAL_SEMANTICS"
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
