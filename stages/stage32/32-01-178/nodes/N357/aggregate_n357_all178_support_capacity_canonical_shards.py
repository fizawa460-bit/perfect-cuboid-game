#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "aggregate_n357_all178_support_capacity_shards.py"
EXPECTED_BASE_BLOB = "f9bbfc2739629c302d00a4d8d3974be3a30b52b7"
EXPECTED_DETERMINISTIC_WORKER_BLOB = "cf6cf60d557f05268ea063f6d8bc7bc24fad1f8c"
EXPECTED_CANONICAL_WORKER_BLOB = "81bcbab9bb49d4ac1f8be28c038f25ae3a469ab8"
EXPECTED_PREFIX_PRODUCER_BLOB = "2b04166a863383bdd5e6eeccc01998dd173e40d3"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main() -> None:
    actual = git_blob_sha1(BASE)
    if actual != EXPECTED_BASE_BLOB:
        raise ValueError(f"N357 aggregate base source-lock regression: {actual}!={EXPECTED_BASE_BLOB}")

    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--shard-dir", type=Path, required=True)
    known, _ = ap.parse_known_args()
    shard_paths = sorted(known.shard_dir.glob("n357-shard-*.json"))
    if len(shard_paths) != 16:
        raise ValueError(f"expected 16 deterministic shard artifacts, got {len(shard_paths)}")
    for path in shard_paths:
        shard = json.loads(path.read_text())
        if shard.get("worker_blob_sha1") != EXPECTED_DETERMINISTIC_WORKER_BLOB:
            raise ValueError(f"deterministic worker source-lock regression in {path.name}")
        if shard.get("canonical_worker_blob_sha1") != EXPECTED_CANONICAL_WORKER_BLOB:
            raise ValueError(f"canonical worker transitive source-lock regression in {path.name}")
        if shard.get("prefix_producer_blob_sha1") != EXPECTED_PREFIX_PRODUCER_BLOB:
            raise ValueError(f"deterministic prefix producer source-lock regression in {path.name}")

    spec = importlib.util.spec_from_file_location("s32_n357_canonical_aggregate_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {BASE}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    mod.EXPECTED_WORKER_BLOB = EXPECTED_DETERMINISTIC_WORKER_BLOB
    mod.EXPECTED_PREFIX_PRODUCER_BLOB = EXPECTED_PREFIX_PRODUCER_BLOB
    mod.main()


if __name__ == "__main__":
    main()
