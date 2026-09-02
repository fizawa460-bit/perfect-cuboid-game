#!/usr/bin/env python3
"""Narrow exact extractor for Stage33 named-J2 order-4 BigK rows 20 and 67.

This script reuses the source-lock/Magma transport helper from Stage33-07, but
constructs a deliberately small source slice: the already-certified full-surface
setup before the automorphism-group block, followed by the pinned K-quotient
setup only through construction of ``preimages``/``MatBigKtoBig``.  It emits no
qPic/S3 candidate search and persists only the two requested sparse rows.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import re
import sys
import traceback
from pathlib import Path

EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
EXPECTED_RAW_SHA256 = "5dc3ae961d872ff96420385880edf0f4225a12d3f906c614e1ccd2220399ce89"
EXPECTED_REQUEST_SHA256 = "d0b7b6605b2e8fde9c0b42d2456abf6ab888f4b7888daf1c2875ff9cb858bbd0"
ROWS = (20, 67)
QUOTIENT_MARKER = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
END_MARKER = "preimsinPic :="
OUTPUT_BUDGET = 16_384


def canonical_sha256(body: dict) -> str:
    data = dict(body)
    data.pop("canonical_sha256", None)
    raw = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def load_helper():
    helper_path = Path(__file__).resolve().parents[1] / "33-07" / "stoll_cuboid_source.py"
    spec = importlib.util.spec_from_file_location("stage33_stoll_source", helper_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import helper {helper_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def grab(stdout: str, name: str):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.MULTILINE)
    if not m:
        raise RuntimeError(f"missing Magma marker {name}")
    return ast.literal_eval(m.group(1))


def normalize_sparse(row_number: int, value) -> list[list[int]]:
    if not isinstance(value, list) or not value:
        raise RuntimeError(f"row {row_number}: empty/non-list sparse payload")
    out: list[list[int]] = []
    seen = set()
    for item in value:
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise RuntimeError(f"row {row_number}: malformed sparse pair {item!r}")
        idx, mult = int(item[0]), int(item[1])
        if idx <= 0 or idx > 10_000:
            raise RuntimeError(f"row {row_number}: invalid full-surface index {idx}")
        if mult == 0:
            raise RuntimeError(f"row {row_number}: zero multiplicity persisted")
        if idx in seen:
            raise RuntimeError(f"row {row_number}: duplicate index {idx}")
        seen.add(idx)
        out.append([idx, mult])
    out.sort()
    return out


def build_slice(text: str, helper) -> str:
    # Reproduce the established Stage33-07 prefix exactly: skip the unused
    # genus-3 degree-8 block and stop before the full automorphism/Galois block.
    a = text.index(helper.SKIP_START)
    b = text.index(helper.SKIP_END, a)
    c = text.index(helper.STOP_MARKER, b)
    prefix = text[:a] + "\n// Stage33-12 v16 skips unused degree-8 curves.\n" + text[b:c]

    q0 = text.index(QUOTIENT_MARKER, c)
    q1 = text.index(END_MARKER, q0)
    quotient = text[q0:q1]
    if "preimages :=" not in quotient or "MatBigKtoBig" not in quotient:
        raise RuntimeError("source slice lost preimages/MatBigKtoBig construction")
    if "signc :=" in quotient or "ImtrcE" in quotient:
        raise RuntimeError("source slice crossed downstream trace/descent boundary")

    emit = r'''
function Stage33SparseRow(M, r)
  return [[j, Integers()!M[r,j]] : j in [1..Ncols(M)] | M[r,j] ne 0];
end function;
printf "STAGE33_ROW20=%o\n", Stage33SparseRow(MatBigKtoBig, 20);
printf "STAGE33_ROW67=%o\n", Stage33SparseRow(MatBigKtoBig, 67);
printf "STAGE33_BDIM=%o\n", bdim;
printf "STAGE33_BDIMK=%o\n", bdimK;
printf "STAGE33_ORDER4_TWO_ROW_DONE\n";
'''
    return prefix + "\n// Stage33-12 v16 skips the unrelated full-surface automorphism/Galois block.\n" + quotient + emit


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()
    out_path = Path(args.out)
    body = {
        "schema": "STAGE33_12_J2_ORDER4_ROW20_ROW67_NARROW_EXECUTION_RESULT_V16",
        "status": "FAILED_BEFORE_EXACT_EXTRACTION",
        "request_canonical_sha256": EXPECTED_REQUEST_SHA256,
        "pinned_source": {
            "repository": "MichaelStollBayreuth/Verification",
            "commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
            "path": "Cuboids/cuboids.magma",
            "git_blob_sha1": EXPECTED_BLOB,
            "raw_sha256": EXPECTED_RAW_SHA256,
        },
        "requested_rows_1based": list(ROWS),
    }
    try:
        helper = load_helper()
        text, _old_core, blob, source_attempt = helper.load_pinned_source()
        raw_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
        if blob != EXPECTED_BLOB:
            raise RuntimeError(f"pinned blob mismatch {blob}")
        if raw_sha != EXPECTED_RAW_SHA256:
            raise RuntimeError(f"pinned raw sha mismatch {raw_sha}")
        code = build_slice(text, helper)
        code_sha = hashlib.sha256(code.encode()).hexdigest()
        stdout, magma_attempt = helper.run_magma(
            code,
            args.timeout,
            "Stage33-12 v16 BigK rows20/67",
            user_agent="perfect-cuboid-stage33-order4-v16/1.0",
        )
        if "STAGE33_ORDER4_TWO_ROW_DONE" not in stdout:
            tail = stdout[-6000:].replace("\r", "")
            raise RuntimeError("Magma did not reach completion marker; tail:\n" + tail)
        row20 = normalize_sparse(20, grab(stdout, "STAGE33_ROW20"))
        row67 = normalize_sparse(67, grab(stdout, "STAGE33_ROW67"))
        bdim = int(grab(stdout, "STAGE33_BDIM"))
        bdimk = int(grab(stdout, "STAGE33_BDIMK"))
        if bdim <= 0 or bdimk < 67:
            raise RuntimeError(f"dimension regression bdim={bdim} bdimK={bdimk}")
        if any(idx > bdim for row in (row20, row67) for idx, _ in row):
            raise RuntimeError("sparse preimage index exceeds bdim")
        body.update({
            "status": "EXACT_ROWS_EXTRACTED",
            "source_download_attempt": source_attempt,
            "magma_submission_attempt": magma_attempt,
            "magma_source_slice_sha256": code_sha,
            "bdim_full_surface": bdim,
            "bdimK": bdimk,
            "rows": {
                "20": {"sparse_full_surface_preimage_pairs_1based": row20},
                "67": {"sparse_full_surface_preimage_pairs_1based": row67},
            },
            "firewalls": {
                "qpic_smith_s3_reopened": False,
                "target_compatibility_inference_used": False,
                "claim_promotion_performed": False,
            },
        })
        rc = 0
    except Exception as exc:  # Persist a bounded diagnostic even on failure.
        body["error_type"] = type(exc).__name__
        body["error"] = str(exc)[-6000:]
        body["traceback_tail"] = traceback.format_exc()[-6000:]
        rc = 1

    body["canonical_sha256"] = canonical_sha256(body)
    encoded = (json.dumps(body, indent=2, sort_keys=True) + "\n").encode()
    if len(encoded) > OUTPUT_BUDGET:
        # Preserve the fail-closed semantics without ever violating the artifact budget.
        body = {
            "schema": "STAGE33_12_J2_ORDER4_ROW20_ROW67_NARROW_EXECUTION_RESULT_V16",
            "status": "FAILED_OUTPUT_BUDGET",
            "request_canonical_sha256": EXPECTED_REQUEST_SHA256,
            "size_before_compaction": len(encoded),
        }
        body["canonical_sha256"] = canonical_sha256(body)
        encoded = (json.dumps(body, indent=2, sort_keys=True) + "\n").encode()
        rc = 1
    out_path.write_bytes(encoded)
    print(encoded.decode(), end="")
    return rc


if __name__ == "__main__":
    sys.exit(main())
