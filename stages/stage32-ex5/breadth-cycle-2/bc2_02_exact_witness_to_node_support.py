#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sympy import I, Matrix, sympify

ROOT = Path(__file__).resolve().parents[3]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained

EXPECTED_ANTI_RANK = 59
EXPECTED_PICARD_RANK = 64
EXPECTED_PAIRINGS = 140
EXPECTED_EXCEPTIONAL = 48
SCHEMA = "STAGE32EX5_BC2_02_EXACT_WITNESS_TO_NODE_SUPPORT_V1"


def sha256_json(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def vector_list(v: Matrix) -> list[int]:
    if v.cols != 1:
        raise ValueError("expected column vector")
    return [int(v[i, 0]) for i in range(v.rows)]


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_evidence(path: Path) -> tuple[dict, str | None]:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    if claimed is not None:
        body = dict(raw)
        body.pop("canonical_sha256_without_this_field", None)
        if csha(body) != claimed:
            raise ValueError("input evidence canonical hash regression")
    result = raw.get("result", {})
    if result.get("status") != "SAT" and result.get("original_z3_replay_status") != "sat":
        raise ValueError("input evidence does not contain an exact SAT witness")
    witness = result.get("witness_r_reduced")
    if not isinstance(witness, list) or len(witness) != EXPECTED_ANTI_RANK:
        raise ValueError("reduced witness must have length 59")
    target = raw.get("target", {})
    if not isinstance(target.get("z"), list) or len(target["z"]) != 5:
        raise ValueError("target z must have length 5")
    for key in ("row_id", "e", "a"):
        if key not in target:
            raise ValueError(f"target missing {key}")
    return raw, claimed


def parse_qi(value: object):
    if isinstance(value, int):
        return value
    text = str(value).strip()
    return sympify(text, locals={"i": I})


def load_node_bridge(path: Path) -> tuple[list[dict], str | None]:
    raw = json.loads(path.read_text())
    rows = raw.get("rows")
    if not isinstance(rows, list) or len(rows) != EXPECTED_EXCEPTIONAL:
        raise ValueError("BC2-01B bridge must contain 48 rows")
    rows = sorted(rows, key=lambda row: int(row["retained_exceptional_index_0based"]))
    for k, row in enumerate(rows):
        if int(row["retained_exceptional_index_0based"]) != k:
            raise ValueError("exceptional index coverage regression")
        if int(row["all140_index_0based"]) != 92 + k:
            raise ValueError("all140 exceptional-slot binding regression")
        coords = row.get("canonical_stoll_coordinates")
        if not isinstance(coords, list) or len(coords) != 7:
            raise ValueError("node coordinate row must have length 7")
    return rows, raw.get("canonical_sha256_without_this_field")


def reconstruct(evidence: dict, bundle: dict, marking: dict, bridge_rows: list[dict]) -> dict:
    data = reconstruct_translation_data(marking, bundle)
    target = evidence["target"]
    genus, degree = parse_row_id(str(target["row_id"]))
    e = int(target["e"])
    a = int(target["a"])
    z = Matrix([int(v) for v in target["z"]])
    r_values = [int(v) for v in evidence["result"]["witness_r_reduced"]]
    r = Matrix(r_values)

    M = data["M"]
    pivots = tuple(int(v) for v in data["pivot_rows"])
    selected_M = M.extract(list(pivots), list(range(EXPECTED_ANTI_RANK)))
    reduced_rows, Trow = selected_M.T.lll_transform()
    if reduced_rows != Trow * selected_M.T:
        raise ValueError("LLL transform reconstruction regression")
    U = Trow.T
    if abs(int(U.det())) != 1:
        raise ValueError("reduced-coordinate transform is not unimodular")
    Mred = M * U

    x0 = data["x0_map"] * z
    q = data["K"] * U * r
    x = x0 + q
    if x.shape != (EXPECTED_PICARD_RANK, 1):
        raise ValueError("Picard reconstruction rank regression")

    adapter = data["adapter"]
    slice_bridge = data["bridge"]
    pairings = adapter.pairing_matrix * x
    if pairings.shape != (EXPECTED_PAIRINGS, 1):
        raise ValueError("all140 pairing count regression")
    pairing_values = vector_list(pairings)

    y0 = data["pairing_x0_map"] * z
    pairings_from_reduced = y0 + Mred * r
    fixed_projection_exact = data["C"] * x == z
    affine_kernel_exact = data["C"] * q == Matrix.zeros(5, 1)
    pairing_model_replay_exact = pairings == pairings_from_reduced

    phi = Matrix([
        list(slice_bridge.degree_functional),
        list(slice_bridge.exceptional_mass_functional),
        list(slice_bridge.first_normal_half_functional),
    ])
    slice_values = vector_list(phi * x)
    slice_exact = slice_values == [degree, e, a]

    last48 = pairing_values[92:140]
    if len(last48) != EXPECTED_EXCEPTIONAL:
        raise ValueError("last48 extraction regression")
    exceptional_mass_exact = sum(last48) == e
    all140_nonnegative = min(pairing_values) >= 0
    exceptional_nonnegative = min(last48) >= 0
    support = [k for k, value in enumerate(last48) if value > 0]
    zeros = [k for k, value in enumerate(last48) if value == 0]

    support_rows = [bridge_rows[k] for k in support]
    coord_matrix = Matrix([
        [parse_qi(v) for v in row["canonical_stoll_coordinates"]]
        for row in support_rows
    ]) if support_rows else Matrix.zeros(0, 7)
    vector_rank = int(coord_matrix.rank()) if support_rows else 0
    projective_span_dimension = vector_rank - 1 if vector_rank else -1
    spans_p6 = vector_rank == 7

    checks = {
        "fixed_projection_exact": fixed_projection_exact,
        "affine_kernel_exact": affine_kernel_exact,
        "pairing_model_replay_exact": pairing_model_replay_exact,
        "slice_exact": slice_exact,
        "exceptional_mass_exact": exceptional_mass_exact,
        "bridge_48_rows_exact": len(bridge_rows) == 48,
    }
    status = (
        "PASS_EXACT_WITNESS_TO_NODE_SUPPORT"
        if all(checks.values())
        else "FAIL_EXACT_WITNESS_TO_NODE_SUPPORT"
    )

    return {
        "schema": SCHEMA,
        "stage": "32EX5",
        "target": "BC2-02_FULL178_SUPPORT_RECONSTRUCTION",
        "status": status,
        "candidate": {
            "row_id": target["row_id"],
            "genus": genus,
            "degree": degree,
            "e": e,
            "a": a,
            "z": vector_list(z),
            "witness_r_reduced_count": len(r_values),
            "witness_r_reduced_sha256": sha256_json(r_values),
        },
        "reconstruction": {
            "picard_rank": EXPECTED_PICARD_RANK,
            "anti_fixed_rank": EXPECTED_ANTI_RANK,
            "reduced_transform_unimodular": True,
            "picard_coordinates_sha256": sha256_json(vector_list(x)),
            "pairing_count": len(pairing_values),
            "all140_pairings_sha256": sha256_json(pairing_values),
            "all140_nonnegative": all140_nonnegative,
            "checks": checks,
        },
        "exceptional_support": {
            "all140_indices_0based": [92, 139],
            "pairings_last48": last48,
            "pairings_last48_sha256": sha256_json(last48),
            "sum": sum(last48),
            "nonnegative": exceptional_nonnegative,
            "support_indices_0based": support,
            "zero_indices_0based": zeros,
            "support_count": len(support),
            "canonical_node_vector_rank": vector_rank,
            "projective_span_dimension": projective_span_dimension,
            "spans_p6": spans_p6,
            "support_nodes": [
                {
                    "retained_exceptional_index_0based": int(row["retained_exceptional_index_0based"]),
                    "all140_index_0based": int(row["all140_index_0based"]),
                    "source_label": row.get("source_label"),
                    "canonical_stoll_coordinates": row["canonical_stoll_coordinates"],
                }
                for row in support_rows
            ],
        },
        "semantics": {
            "support_rule": "for an effective nonexceptional curve with nonnegative exceptional pairings, support={k: C.E_k>0}",
            "exact_witness_is_required": True,
            "scalar_exceptional_mass_is_not_substituted_for_labelled_support": True,
            "this_adapter_consumes_a_materialized_59d_witness_but_does_not_find_one": True,
            "continuous_kkt_survivor_is_not_an_integral_picard_class": True,
            "picard_numerical_class_is_not_effective_curve_existence": True,
            "genus1_span_alone_is_not_exclusion_credit": True,
        },
        "firewalls": {
            "FULL178_complete": False,
            "receiver_credit": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--node-bridge", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    evidence, evidence_canonical = load_evidence(args.evidence)
    bridge_rows, bridge_canonical = load_node_bridge(args.node_bridge)
    bundle = load_retained(args.retained, "s32ex5_bc2_02_picard")
    marking = load_retained(args.marking, "s32ex5_bc2_02_marking")
    payload = reconstruct(evidence, bundle, marking, bridge_rows)
    payload["source"] = {
        "evidence": str(args.evidence),
        "evidence_canonical_sha256": evidence_canonical,
        "node_bridge": str(args.node_bridge),
        "node_bridge_canonical_sha256": bridge_canonical,
        "retained_bundle_sha256": bundle.get("canonical_sha256"),
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "row_id": payload["candidate"]["row_id"],
        "support_count": payload["exceptional_support"]["support_count"],
        "span_dimension": payload["exceptional_support"]["projective_span_dimension"],
        "spans_p6": payload["exceptional_support"]["spans_p6"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))
    if payload["status"].startswith("FAIL"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
