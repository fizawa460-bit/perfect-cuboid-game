#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCKER = HERE / "verify_n356_dependency_source_locks.py"
ENGINE = HERE.parent / "N356-engine" / "verify_n356_optimistic_exceptional_transport_fast.py"
EXPECTED_LOCKER_BLOB = "cbc07540f664fa830262b43e63a4f17327f366e2"
EXPECTED_ENGINE_BLOB = "ec2bba109f4a42816f366dbf605afeea7c16f0a2"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_locked(path: Path, expected: str, name: str):
    actual = git_blob_sha1(path)
    if actual != expected:
        raise ValueError(f"N356 locked-entry source regression {path}: {actual}!={expected}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    locker = load_locked(LOCKER, EXPECTED_LOCKER_BLOB, "s32_n356_dependency_locks_fast")
    locker.validate_n356_dependency_source_locks()
    engine = load_locked(ENGINE, EXPECTED_ENGINE_BLOB, "s32_n356_locked_fast_engine")
    engine.main()


if __name__ == "__main__":
    main()
