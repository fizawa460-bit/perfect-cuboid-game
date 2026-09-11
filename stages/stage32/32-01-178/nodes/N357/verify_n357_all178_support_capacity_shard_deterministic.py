#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANONICAL = HERE / "verify_n357_all178_support_capacity_shard_canonical.py"
EXPECTED_CANONICAL_BLOB = "81bcbab9bb49d4ac1f8be28c038f25ae3a469ab8"
EXPECTED_PREFIX_PRODUCER_BLOB = "2b04166a863383bdd5e6eeccc01998dd173e40d3"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_canonical():
    actual = git_blob_sha1(CANONICAL)
    if actual != EXPECTED_CANONICAL_BLOB:
        raise ValueError(f"N357 canonical shard source-lock regression: {actual}!={EXPECTED_CANONICAL_BLOB}")
    spec = importlib.util.spec_from_file_location("s32_n357_deterministic_canonical", CANONICAL)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {CANONICAL}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--output", type=Path, required=True)
    known, _ = ap.parse_known_args()

    mod = load_canonical()
    mod.EXPECTED_PREFIX_PRODUCER_BLOB = EXPECTED_PREFIX_PRODUCER_BLOB
    mod.main()

    result = json.loads(known.output.read_text())
    if result.get("worker_blob_sha1") != EXPECTED_CANONICAL_BLOB:
        raise ValueError("N357 canonical worker output source-lock regression")
    if result.get("prefix_producer_blob_sha1") != EXPECTED_PREFIX_PRODUCER_BLOB:
        raise ValueError("N357 deterministic prefix producer output regression")
    result["canonical_worker_blob_sha1"] = EXPECTED_CANONICAL_BLOB
    result["worker_blob_sha1"] = git_blob_sha1(Path(__file__))
    known.output.write_text(json.dumps(result, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N357_ALL178_DETERMINISTIC_ENTRYPOINT",
        "worker_blob_sha1": result["worker_blob_sha1"],
        "canonical_worker_blob_sha1": EXPECTED_CANONICAL_BLOB,
        "prefix_producer_blob_sha1": EXPECTED_PREFIX_PRODUCER_BLOB,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
