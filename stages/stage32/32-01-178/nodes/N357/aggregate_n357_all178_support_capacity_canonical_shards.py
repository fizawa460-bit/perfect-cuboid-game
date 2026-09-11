#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "aggregate_n357_all178_support_capacity_shards.py"
EXPECTED_BASE_BLOB = "f9bbfc2739629c302d00a4d8d3974be3a30b52b7"
EXPECTED_CANONICAL_WORKER_BLOB = "81bcbab9bb49d4ac1f8be28c038f25ae3a469ab8"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def main() -> None:
    actual = git_blob_sha1(BASE)
    if actual != EXPECTED_BASE_BLOB:
        raise ValueError(f"N357 aggregate base source-lock regression: {actual}!={EXPECTED_BASE_BLOB}")
    spec = importlib.util.spec_from_file_location("s32_n357_canonical_aggregate_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {BASE}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    mod.EXPECTED_WORKER_BLOB = EXPECTED_CANONICAL_WORKER_BLOB
    mod.main()


if __name__ == "__main__":
    main()
