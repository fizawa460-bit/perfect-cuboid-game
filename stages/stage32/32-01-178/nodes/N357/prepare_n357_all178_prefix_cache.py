#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import pickle
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "verify_n357_all178_support_capacity_census.py"
EXPECTED_TARGET_BLOB = "beb6fb487a41f16d783f8762220a175d46ff2620"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_target():
    actual = git_blob_sha1(TARGET)
    if actual != EXPECTED_TARGET_BLOB:
        raise ValueError(f"N357 all178 target source-lock regression: {actual}!={EXPECTED_TARGET_BLOB}")
    spec = importlib.util.spec_from_file_location("s32_n357_prefix_target", TARGET)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {TARGET}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=Path, required=True)
    ap.add_argument("--meta", type=Path, required=True)
    args = ap.parse_args()

    mod = load_target()
    for path, expected in [
        (mod.N355_FULL, mod.EXPECTED_N355_FULL_BLOB),
        (mod.MANIFEST, mod.EXPECTED_MANIFEST_BLOB),
    ]:
        actual = mod.git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual}!={expected}")

    fullmod = mod.load_module(mod.N355_FULL, "s32_n357_prefix_n355_full")
    manifest = fullmod.base.load_canonical(mod.MANIFEST, fullmod.base.EXPECTED_MANIFEST_CANONICAL)
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")
    parsed = [fullmod.base.parse_row_id(row_id) for row_id in rows]
    if not all((d & 1) == 0 for _, d in parsed):
        raise ValueError("N357 prefix cache requires verified even FULL178 degrees")
    H = max(d // 2 for _, d in parsed)

    bc_pref = fullmod.build_bc_prefix(H)
    lex_pref = fullmod.build_lex_prefix(H)
    payload = {
        "schema": "STAGE32_32_01_178_N357_PREFIX_CACHE_V1",
        "H": H,
        "bc_pref": bc_pref,
        "lex_pref": lex_pref,
    }
    args.cache.parent.mkdir(parents=True, exist_ok=True)
    # Deterministic gzip envelope: a wall-clock mtime would make the cache digest
    # (and therefore the retained census canonical) drift across exact replays.
    with args.cache.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", compresslevel=6, fileobj=raw, mtime=0) as fh:
            pickle.dump(payload, fh, protocol=pickle.HIGHEST_PROTOCOL)

    producer_blob = git_blob_sha1(Path(__file__))
    meta = {
        "schema": "STAGE32_32_01_178_N357_PREFIX_CACHE_META_V1",
        "H": H,
        "full178_rows": len(rows),
        "producer_blob_sha1": producer_blob,
        "target_blob_sha1": EXPECTED_TARGET_BLOB,
        "n355_full_blob_sha1": mod.EXPECTED_N355_FULL_BLOB,
        "manifest_blob_sha1": mod.EXPECTED_MANIFEST_BLOB,
        "cache_sha256": sha256_file(args.cache),
        "main_pruning_credit": False,
    }
    args.meta.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N357_PREFIX_CACHE",
        "H": H,
        "cache_sha256": meta["cache_sha256"],
        "producer_blob_sha1": producer_blob,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
