#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

import sympy
from sympy import Matrix

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_to_picard64_completion.py"
BASE_BLOB = "6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633"
PAIRING_BRIDGE = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-01a-exceptional-pairing-bridge.json"
PAIRING_BRIDGE_BLOB = "0a4b6b748bd4f4f94ae70e16cf38a0a2174c55d4"
FINITE_CONTRACT = ROOT / "stages/stage29/29-02c-LG2/finite-search-contract.md"
FINITE_CONTRACT_BLOB = "2c1a4813a77b517482b6fef497f9a517c9d12fe6"

TARGET_DEGREE = 8
NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
ALL140_COUNT = 140
PICARD_RANK = 64


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def int_col(v: Matrix) -> list[int]:
    req(v.cols == 1, "expected column vector")
    out = []
    for q in v:
        req(sympy.denom(q) == 1, "nonintegral reconstructed known-curve coordinate")
        out.append(int(q))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    req(blob(BASE) == BASE_BLOB, "base Picard completion source drift")
    req(blob(PAIRING_BRIDGE) == PAIRING_BRIDGE_BLOB, "pairing bridge drift")
    req(blob(FINITE_CONTRACT) == FINITE_CONTRACT_BLOB, "finite-search contract drift")

    finite_text = FINITE_CONTRACT.read_text(encoding="utf-8")
    required_clause = "nonnegative intersection with every known irreducible curve not equal to the candidate"
    req(required_clause in finite_text, "Stage29 known-curve nonnegativity clause drift")

    pairing_bridge = json.loads(PAIRING_BRIDGE.read_text(encoding="utf-8"))
    est = pairing_bridge["established"]
    req(est["all140_count"] == ALL140_COUNT, "all140 count drift")
    req(est["normal_indices_0based"] == [0, 91], "normal row range drift")
    req(est["exceptional_indices_0based"] == [92, 139], "exceptional row range drift")
    ordering = " ".join(est["ordering_evidence"])
    req("known non-exceptional curve classes" in ordering, "known-curve ordering semantics drift")
    req("48 exceptional classes" in ordering, "exceptional ordering semantics drift")

    base = load_module(BASE, "stage32_main_btva_all140_receiver_base")
    bundle = base.load_retained(args.retained, "stage32_main_btva_all140_receiver_picard")
    marking = base.load_retained(args.marking, "stage32_main_btva_all140_receiver_marking")
    data = base.reconstruct_translation_data(marking, bundle)
    P = data["adapter"].pairing_matrix
    bridge = data["bridge"]
    G = Matrix(bundle["picard_gram_64x64"])

    req(P.shape == (ALL140_COUNT, PICARD_RANK), "pairing matrix shape drift")
    req(G.shape == (PICARD_RANK, PICARD_RANK), "Picard Gram shape drift")
    req(G == G.T and G.det() != 0, "Picard Gram degeneracy/asymmetry")
    degree = Matrix([int(v) for v in bridge.degree_functional])
    req(degree.shape == (PICARD_RANK, 1), "degree functional shape drift")

    Ginv = G.inv()
    rows = []
    degree_hist = Counter()
    normal_degree_hist = Counter()
    exceptional_degree_hist = Counter()
    degree8 = []

    for i in range(ALL140_COUNT):
        functional = Matrix(P.row(i)).T
        coords_q = Ginv * functional
        coords = int_col(coords_q)
        c = Matrix(coords)
        req((c.T * G) == Matrix(P.row(i)), f"pairing functional reconstruction drift row {i}")
        d_q = (degree.T * c)[0, 0]
        req(sympy.denom(d_q) == 1, f"known-curve degree nonintegral row {i}")
        d = int(d_q)
        self_q = (c.T * G * c)[0, 0]
        req(sympy.denom(self_q) == 1, f"known-curve self-intersection nonintegral row {i}")
        self_int = int(self_q)
        kind = "KNOWN_NONEXCEPTIONAL" if i < NORMAL_COUNT else "EXCEPTIONAL"
        rows.append({
            "all140_index_0based": i,
            "kind": kind,
            "hyperplane_degree": d,
            "self_intersection": self_int,
            "picard_coordinate_sha256": csha(coords),
        })
        degree_hist[d] += 1
        if i < NORMAL_COUNT:
            normal_degree_hist[d] += 1
        else:
            exceptional_degree_hist[d] += 1
        if d == TARGET_DEGREE:
            degree8.append(i)

    no_equal_known_curve_by_degree = len(degree8) == 0
    payload = {
        "schema": "STAGE32_MAIN_BTVA_ALL140_RECEIVER_NONNEGATIVITY_DIAGNOSTIC_V1",
        "stage": 32,
        "status": (
            "PASS_ALL140_KNOWN_CURVES_DEGREE_DISTINCT_FROM_D8_ZERO_CREDIT"
            if no_equal_known_curve_by_degree
            else "BLOCKED_D8_EQUAL_DEGREE_KNOWN_CURVE_ROWS_PRESENT"
        ),
        "target": {
            "row_id": "g0-d008",
            "degree": TARGET_DEGREE,
            "population": "R29-LG2 numerical unibranch genus-0 FULL178 d=8 slice",
        },
        "source_locks": {
            "base_picard_completion_blob_sha1": BASE_BLOB,
            "pairing_bridge_blob_sha1": PAIRING_BRIDGE_BLOB,
            "finite_search_contract_blob_sha1": FINITE_CONTRACT_BLOB,
            "retained_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_marking_canonical_sha256": marking.get("canonical_sha256"),
        },
        "reconstruction": {
            "all140_count": ALL140_COUNT,
            "normal_known_nonexceptional_count": NORMAL_COUNT,
            "exceptional_count": EXCEPTIONAL_COUNT,
            "every_pairing_row_reconstructed_from_integral_picard_class": True,
            "degree_histogram": {str(k): degree_hist[k] for k in sorted(degree_hist)},
            "normal_degree_histogram": {str(k): normal_degree_hist[k] for k in sorted(normal_degree_hist)},
            "exceptional_degree_histogram": {str(k): exceptional_degree_hist[k] for k in sorted(exceptional_degree_hist)},
            "target_degree_equal_rows_0based": degree8,
            "target_degree_equal_row_count": len(degree8),
            "rows_sha256": csha(rows),
        },
        "receiver_semantics": {
            "stage29_required_clause": required_clause,
            "all140_rows_are_known_curve_or_exceptional_pairing_rows": True,
            "d8_candidate_distinct_from_every_all140_known_curve_by_hyperplane_degree": no_equal_known_curve_by_degree,
            "all140_nonnegativity_is_necessary_for_d8_integral_curve_receiver": no_equal_known_curve_by_degree,
            "reason": (
                "Stage29 requires nonnegative intersection with every known irreducible curve distinct from the candidate. "
                "The retained all140 ordering is the 92 known nonexceptional curve classes followed by 48 exceptional classes. "
                "Exact Picard reconstruction shows no retained all140 class has hyperplane degree 8."
            ),
        },
        "rows": rows,
        "firewalls": {
            "diagnostic_only": True,
            "main_pruning_credit": False,
            "receiver_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": payload["status"],
        "degree_histogram": payload["reconstruction"]["degree_histogram"],
        "normal_degree_histogram": payload["reconstruction"]["normal_degree_histogram"],
        "exceptional_degree_histogram": payload["reconstruction"]["exceptional_degree_histogram"],
        "degree8_rows": degree8,
        "canonical": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
