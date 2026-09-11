#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOCKER = HERE / "verify_n356_dependency_source_locks.py"
ENGINE = HERE.parent / "N356-engine" / "verify_n356_optimistic_exceptional_transport.py"
EXPECTED_LOCKER_BLOB = "45c0c793f8b2edfec29728412f2951ce9639e352"
EXPECTED_ENGINE_BLOB = "ad0f5dcf7eb70cc24a9a54d4d31807226de1d2ad"


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


def validate_dependency_boundary():
    locker = load_locked(LOCKER, EXPECTED_LOCKER_BLOB, "s32_n356_dependency_locks_serial")
    observed = locker.validate_n356_dependency_source_locks()
    engine = load_locked(ENGINE, EXPECTED_ENGINE_BLOB, "s32_n356_locked_serial_engine")
    return observed, engine


_DEPENDENCY_LOCKS, _ENGINE = validate_dependency_boundary()

for _name in dir(_ENGINE):
    if not _name.startswith("__") and _name != "main":
        globals()[_name] = getattr(_ENGINE, _name)


def main() -> None:
    global _DEPENDENCY_LOCKS, _ENGINE
    _DEPENDENCY_LOCKS, _ENGINE = validate_dependency_boundary()
    _ENGINE.main()


if __name__ == "__main__":
    main()
