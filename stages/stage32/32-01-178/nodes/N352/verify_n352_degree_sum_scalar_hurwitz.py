#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N345_PATH = HERE.parent / "N345/verify_n345_kernel14_integral_self_square.py"
AO_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1648ao-special-fibre-hurwitz-budget-source-note.md"
CONTRACT = HERE / "DEGREE_SUM_SCALAR_HURWITZ_CONTRACT.md"

EXPECTED_AO_BLOB = "242088adab5c86292154a6de9bc3563ba73b4f43"
EXPECTED_CONTRACT_BLOB = "60295a86297330d83370cf32016c75a8244a2aa4"
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
BOUNDARY_PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
TARGETS = [
    {"row_id": "g0-d174", "genus": 0, "degree": 174, "e": 48, "current_terminal_count": 3067},
    {"row_id": "g0-d176", "genus": 0, "degree": 176, "e": 48, "current_terminal_count": 3105},
    {"row_id": "g1-d190", "genus": 1, "degree": 190, "e": 48, "current_terminal_count": 3371},
    {"row_id": "g1-d192", "genus": 1, "degree": 192, "e": 48, "current_terminal_count": 3409},
]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def row_sum(coords: Matrix, labels) -> Matrix:
    out = Matrix.zeros(1, coords.cols)
    for label in labels:
        out += coords.row(label - 1)
    return out


def vector_json(row: Matrix):
    return [str(v) for v in list(row)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    if git_blob_sha1(AO_NOTE) != EXPECTED_AO_BLOB:
        raise ValueError("AO source-note blob regression")
    if git_blob_sha1(CONTRACT) != EXPECTED_CONTRACT_BLOB:
        raise ValueError("N352 contract blob regression")

    n345 = load_module(N345_PATH, "s32_n352_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n352_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n352_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("retained bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("retained marking canonical regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    fibre_classes = []
    fibre_checks = []
    for pack in BOUNDARY_PACKS:
        rows = []
        seen = []
        incidences = []
        for label in pack:
            inc = [j for j in range(93, 141) if int(full[label - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"boundary incidence regression label={label}")
            seen.extend(inc)
            incidences.append(inc)
            F = 2 * coords.row(label - 1) + row_sum(coords, inc)
            rows.append(F)
        if sorted(seen) != list(range(93, 141)):
            raise ValueError("six-fibre exceptional partition regression")
        if any(F != rows[0] for F in rows[1:]):
            raise ValueError("six special fibres are not linearly equivalent")
        fibre_classes.append(rows[0])
        fibre_checks.append({
            "pack": pack,
            "incidence_sizes": [len(x) for x in incidences],
            "partition_all48": True,
            "common_fibre_class_sha256": csha(vector_json(rows[0])),
        })

    normal_class_sum = row_sum(coords, range(1, 93))
    exceptional_class_sum = row_sum(coords, range(93, 141))
    lhs_class = 19 * (fibre_classes[0] + fibre_classes[1])
    rhs_class = normal_class_sum + 5 * exceptional_class_sum
    if lhs_class != rhs_class:
        raise ValueError("degree-sum class identity regression")

    # Redundant functional check against the exact nondegenerate retained Gram form.
    lhs_functional = lhs_class * gram
    rhs_functional = rhs_class * gram
    if lhs_functional != rhs_functional:
        raise ValueError("degree-sum functional identity regression")

    rows = []
    contradicted = 0
    for t in TARGETS:
        scalar_cap = t["e"] + 4 * t["genus"] - 4
        contradiction = t["degree"] > scalar_cap
        if contradiction:
            contradicted += 1
        rows.append({
            **t,
            "scalar_degree_cap": scalar_cap,
            "contradiction": contradiction,
            "verdict": "SCALAR_HURWITZ_CONTRADICTION" if contradiction else "NOT_CONTRADICTED_ZERO_CREDIT",
        })

    body = {
        "schema": "STAGE32_32_01_178_N352_DEGREE_SUM_SCALAR_HURWITZ_V1",
        "node_id": "N352",
        "status": "AUDIT_CANDIDATE_NO_MAIN_CREDIT",
        "source_locks": {
            "ao_source_note_blob_sha1": EXPECTED_AO_BLOB,
            "contract_blob_sha1": EXPECTED_CONTRACT_BLOB,
            "retained_bundle_canonical": EXPECTED_BUNDLE,
            "retained_marking_canonical": EXPECTED_MARKING,
        },
        "fibre_geometry_checks": fibre_checks,
        "exact_picard_identity": {
            "class_identity": "19*(F1+F2)=sum(normal labels1..92)+5*sum(exceptional labels93..140)",
            "class_identity_verified": True,
            "functional_identity_verified": True,
            "consequence_with_normal_and_exceptional_totals": "n1+n2=d",
            "lhs_class_sha256": csha(vector_json(lhs_class)),
            "rhs_class_sha256": csha(vector_json(rhs_class)),
        },
        "n351_hurwitz_input": {
            "per_factor_cap": "ni <= e/2+2g-2",
            "source_audit_still_required": True,
        },
        "scalar_contraction": {
            "necessary_condition": "d <= e+4g-4",
            "uses_smt": False,
            "uses_n260_allones": False,
            "uses_n349_local44": False,
            "uses_x4": False,
            "uses_self_square": False,
        },
        "aggregate": {
            "row_count": len(TARGETS),
            "contradicted_row_count": contradicted,
            "not_contradicted_row_count": len(TARGETS) - contradicted,
            "candidate_current_terminal_count": sum(t["current_terminal_count"] for t in TARGETS),
        },
        "rows": rows,
        "semantics": {
            "n351_geometric_source_hostile_audit_required": True,
            "n352_hostile_audit_required": True,
            "main_pruning_credit": False,
            "production_leaf_credit": False,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N352_SCALAR_HURWITZ_CONTRACTION",
        "contradicted_rows": contradicted,
        "canonical": body["canonical_sha256_without_this_field"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
