#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

# Reuse the exact Stage32 post1473 Hperp adapter that already reconstructed the
# source-locked full 140x140 intersection form for PR #1474.
import sys

FIXED_ROWS = [17, 21, 24, 25, 26, 28, 30, 31]
FULL_INTERSECTION_SHA256 = "3e967406344d7b13027a25bafa832701f76f028a77f4a1dfa7bd0ebc0cdf1f4e"
V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
V6_ALL140_SHA256 = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
EXPECTED_HISTOGRAM = {0: 14, 1: 22, 2: 10, 3: 2}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module_payload(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load module {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--witness", type=Path, required=True)
    ap.add_argument("--adapter-dir", type=Path, required=True)
    args = ap.parse_args()

    sys.path.insert(0, str(args.adapter_dir))
    from hperp_integral_adapter import _parse_hperp, _recover_full_intersection, matrix_list

    # Loading the retained modules executes their own nonexpiring source-lock checks.
    load_module_payload(args.retained, "stage32ex6_projection_retained")
    marking = load_module_payload(args.marking, "stage32ex6_projection_marking")
    hperp_text = marking.get("hperp_text")
    if not isinstance(hperp_text, str):
        raise ValueError("retained marking missing hperp_text")
    q, degree, linear, _caps, hmeta = _parse_hperp(hperp_text)
    full = _recover_full_intersection(q, degree, linear)
    if full.rows != 140 or full.cols != 140 or full != full.T:
        raise ValueError(f"unexpected full intersection shape/symmetry: {full.shape}")
    full_sha = csha(matrix_list(full))
    if full_sha != FULL_INTERSECTION_SHA256:
        raise ValueError(f"full intersection hash moved: {full_sha}")

    witness = json.loads(args.witness.read_text())
    if witness.get("canonical_sha256_without_this_field") != V6_CANONICAL:
        raise ValueError("V6 witness canonical hash moved")
    all140 = [int(x) for x in witness["witness"]["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != V6_ALL140_SHA256:
        raise ValueError("V6 all140 pairings moved")

    f_pairings = [sum(int(full[r - 1, j]) for r in FIXED_ROWS) for j in range(140)]
    f_exc = f_pairings[92:]
    hist = {m: f_exc.count(m) for m in sorted(set(f_exc))}
    if sum(f_exc) != 48 or hist != EXPECTED_HISTOGRAM:
        raise ValueError(f"eight-conic exceptional incidence regression: sum={sum(f_exc)} hist={hist}")

    k_pairings = [2] * 32 + [4] * 60 + [0] * 48
    d1 = [all140[j] - k_pairings[j] - f_pairings[j] for j in range(140)]
    d1_exc = d1[92:]
    negative_all = [j + 1 for j, x in enumerate(d1) if x < 0]
    zero_all = [j + 1 for j, x in enumerate(d1) if x == 0]
    negative_exc = [93 + j for j, x in enumerate(d1_exc) if x < 0]
    zero_exc = [93 + j for j, x in enumerate(d1_exc) if x == 0]

    out = {
        "schema": "STAGE32EX6_SCRATCH_V6_EIGHT_CONIC_EXCEPTIONAL_ORDER_PROJECTION_V1",
        "status": "PASS",
        "source_locks": {
            "full_intersection_sha256": full_sha,
            "hperp_text_sha256": hmeta.get("hperp_text_sha256"),
            "upstream_git_blob_sha1": hmeta.get("upstream_git_blob_sha1"),
            "v6_canonical_sha256": V6_CANONICAL,
            "v6_all140_pairings_sha256": V6_ALL140_SHA256,
        },
        "fixed_conic_rows": FIXED_ROWS,
        "F_exceptional_pairings_stage32_order": f_exc,
        "F_exceptional_pairing_histogram": {str(k): v for k, v in sorted(hist.items())},
        "D1_exceptional_pairings_stage32_order": d1_exc,
        "D1_negative_exceptional_rows": negative_exc,
        "D1_zero_exceptional_rows": zero_exc,
        "D1_negative_classical140_rows": negative_all,
        "D1_zero_classical140_rows": zero_all,
        "D1_classical140_all_nonnegative": len(negative_all) == 0,
        "previous_unlabeled_exceptional_gap_resolved": True,
        "global_nefness_claimed": False,
        "O266_endpoint_excluded": False,
        "O264_descent_authorized": False,
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
