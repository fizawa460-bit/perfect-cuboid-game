#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMPL_PATH = HERE / "verify_stage32_claim_dag_impl.py"
HISTORICAL_ROUTING_DIR = HERE / "historical-routing-blobs"

_spec = importlib.util.spec_from_file_location("stage32_claim_dag_impl", IMPL_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError("cannot load Stage32 claim-DAG implementation")
_impl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_impl)
_ORIGINAL_VALIDATE_SOURCE_LOCKS = _impl.validate_source_locks

# Re-export the existing verifier API so verify_stage32_active_frontier.py keeps
# importing the same public names from this path.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

_HISTORICAL_ROUTING_STATUSES = {"DECLARED_GOAL", "SUPERSEDED", "REVOKED"}


def _is_mutable_routing_state(lock: dict) -> bool:
    path = lock.get("path")
    return isinstance(path, str) and (
        path.endswith("/MAIN-STATE.json")
        or path == "stages/stage32/proof/ACTIVE-FRONTIER.json"
    )


def _historical_blob_bytes(expected_sha1: str) -> bytes:
    # Shallow exact-head CI is not guaranteed to retain old git blobs. Prefer a
    # retained immutable snapshot whose filename is the registered blob SHA.
    snapshot = HISTORICAL_ROUTING_DIR / f"{expected_sha1}.json"
    if snapshot.is_file():
        data = snapshot.read_bytes()
        if git_blob_sha1(data) != expected_sha1:
            raise CheckError(
                f"historical routing snapshot digest mismatch: {snapshot.relative_to(ROOT)}"
            )
        return data

    # Local/full clones may still contain the historical object; keep this as a
    # secondary provenance path for older locks that have not needed a retained
    # snapshot yet.
    probe = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "-e", expected_sha1],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if probe.returncode != 0:
        raise CheckError(
            "historical routing snapshot unavailable in retained snapshots or git object store: "
            + expected_sha1
        )
    data = subprocess.check_output(
        ["git", "-C", str(ROOT), "cat-file", "blob", expected_sha1]
    )
    if git_blob_sha1(data) != expected_sha1:
        raise CheckError(f"historical routing snapshot blob digest mismatch: {expected_sha1}")
    return data


def _check_locked_bytes(cid: str, lock: dict, data: bytes) -> None:
    if "canonical_sha256" not in lock:
        return
    expected = lock["canonical_sha256"]
    if not isinstance(expected, str) or not HEX64_RE.fullmatch(expected):
        raise CheckError(f"{cid}: malformed canonical_sha256 for {lock['path']}")
    try:
        obj = json.loads(data)
    except Exception as exc:
        raise CheckError(f"{cid}: canonical lock requires JSON: {lock['path']}") from exc
    stored = obj.get("canonical_sha256_without_this_field")
    if stored != expected:
        raise CheckError(
            f"{cid}: stored canonical digest mismatch for {lock['path']}: {stored} != {expected}"
        )
    stripped = dict(obj)
    stripped.pop("canonical_sha256_without_this_field", None)
    actual = csha(stripped)
    if actual != expected:
        raise CheckError(
            f"{cid}: recomputed canonical digest mismatch for {lock['path']}: {actual} != {expected}"
        )


def validate_source_locks(by_id: dict[str, dict]) -> int:
    """Verify stable evidence live; preserve non-credit mutable routing locks historically.

    A mutable routing-state lock attached to DECLARED_GOAL/SUPERSEDED/REVOKED records is
    a registration-time routing snapshot, not mathematical evidence. If the live
    routing file has advanced, the exact locked bytes must be recoverable from a
    retained hash-named snapshot (preferred for shallow CI) or the git object
    store. AUDITED/PROVISIONAL/SCRATCH locks retain strict working-tree equality,
    as do all non-routing source locks.
    """
    stable: dict[str, dict] = {}
    historical: list[tuple[str, dict]] = []

    for cid, claim in by_id.items():
        clone = dict(claim)
        clone["source_locks"] = []
        for lock in claim["source_locks"]:
            if (
                claim["authority_status"] in _HISTORICAL_ROUTING_STATUSES
                and _is_mutable_routing_state(lock)
            ):
                historical.append((cid, lock))
            else:
                clone["source_locks"].append(lock)
        stable[cid] = clone

    checked = _ORIGINAL_VALIDATE_SOURCE_LOCKS(stable)

    for cid, lock in historical:
        if not isinstance(lock, dict) or not isinstance(lock.get("path"), str):
            raise CheckError(f"{cid}: malformed source lock")
        path = ROOT / lock["path"]
        if not path.exists() or not path.is_file():
            raise CheckError(f"{cid}: missing routing state path {lock['path']}")

        live_data = path.read_bytes()
        locked_data = live_data
        if "blob_sha1" in lock:
            expected = lock["blob_sha1"]
            if not isinstance(expected, str) or not HEX40_RE.fullmatch(expected):
                raise CheckError(f"{cid}: malformed blob_sha1 for {lock['path']}")
            live_sha1 = git_blob_sha1(live_data)
            if live_sha1 != expected:
                locked_data = _historical_blob_bytes(expected)
        _check_locked_bytes(cid, lock, locked_data)
        checked += 1

    return checked


# The implementation's main() resolves validate_source_locks from its own module
# globals, so install the narrowed routing-snapshot policy there as well.
_impl.validate_source_locks = validate_source_locks


def main() -> int:
    _impl.validate_source_locks = validate_source_locks
    return _impl.main()


if __name__ == "__main__":
    sys.exit(main())
