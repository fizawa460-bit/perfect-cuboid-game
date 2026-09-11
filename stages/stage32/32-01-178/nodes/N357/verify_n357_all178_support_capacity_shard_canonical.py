#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import pickle
import sys
from collections import defaultdict
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "verify_n357_all178_support_capacity_census.py"
BASE_SHARD = HERE / "verify_n357_all178_support_capacity_shard.py"
EXPECTED_TARGET_BLOB = "beb6fb487a41f16d783f8762220a175d46ff2620"
EXPECTED_BASE_SHARD_BLOB = "546335d44c068a565e715973c886e9980cf85587"
EXPECTED_PREFIX_PRODUCER_BLOB = "173ea0c029dbdfc511baecc9138a9613693afa70"

_MOD = None


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _compute(item):
    global _MOD
    (h, threshold), strata = item
    if threshold < -h:
        out = []
        for row_id, g, d, e, required, normal_block in strata:
            out.append({
                "row_id": row_id,
                "g": g,
                "d": d,
                "e": e,
                "h": h,
                "threshold_b_minus_c": 3 * d - e,
                "required_support": required,
                "n356_transport_remaining_terminals": 0,
                "n357_support_capacity_rejected_terminals": 0,
                "n357_support_capacity_remaining_terminals": 0,
            })
        return out
    out = _MOD._compute_group(item)
    for rec in out:
        rec["threshold_b_minus_c"] = 3 * int(rec["d"]) - int(rec["e"])
    return out


def main() -> None:
    global _MOD
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard-index", type=int, required=True)
    ap.add_argument("--shard-count", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--prefix-cache", type=Path, required=True)
    ap.add_argument("--prefix-meta", type=Path, required=True)
    ap.add_argument("--workers", type=int, default=0)
    args = ap.parse_args()
    if args.shard_count <= 0 or not 0 <= args.shard_index < args.shard_count:
        raise ValueError("invalid shard index/count")

    if git_blob_sha1(TARGET) != EXPECTED_TARGET_BLOB:
        raise ValueError("N357 target source-lock regression")
    if git_blob_sha1(BASE_SHARD) != EXPECTED_BASE_SHARD_BLOB:
        raise ValueError("N357 base-shard source-lock regression")

    mod = load_module(TARGET, f"s32_n357_canonical_target_{args.shard_index}")
    for path, expected in [
        (mod.N355_FULL, mod.EXPECTED_N355_FULL_BLOB),
        (mod.N357_ENGINE, mod.EXPECTED_N357_ENGINE_BLOB),
        (mod.N356_RECEIPT, mod.EXPECTED_N356_RECEIPT_BLOB),
        (mod.MANIFEST, mod.EXPECTED_MANIFEST_BLOB),
    ]:
        if mod.git_blob_sha1(path) != expected:
            raise ValueError(f"source-lock regression {path}")

    receipt = json.loads(mod.N356_RECEIPT.read_text())
    if receipt.get("status") != "PASS" or receipt.get("review_id") != mod.EXPECTED_N356_REVIEW:
        raise ValueError("N356 hostile-audit PASS regression")
    if receipt.get("audited_exact_head") != mod.EXPECTED_N356_HEAD:
        raise ValueError("N356 hostile-audit exact-head regression")
    counts = receipt.get("consumed_counts", {})
    if counts.get("remaining_strata") != mod.EXPECTED_N356_STRATA or counts.get("remaining_terminals") != mod.EXPECTED_N356_TERMINALS:
        raise ValueError("N356 authoritative residual regression")

    fullmod = mod.load_module(mod.N355_FULL, f"s32_n357_canonical_n355_{args.shard_index}")
    engine = mod.load_module(mod.N357_ENGINE, f"s32_n357_canonical_engine_{args.shard_index}")
    if args.shard_index == 0:
        engine.validate_flow_formulas()
        engine.validate_strict_witness()
    manifest = fullmod.base.load_canonical(mod.MANIFEST, fullmod.base.EXPECTED_MANIFEST_CANONICAL)

    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")
    parsed = [fullmod.base.parse_row_id(row_id) for row_id in rows]
    if not all((d & 1) == 0 for _, d in parsed):
        raise ValueError("N357 canonical shard requires verified even FULL178 degrees")
    H = max(d // 2 for _, d in parsed)

    meta = json.loads(args.prefix_meta.read_text())
    if meta.get("schema") != "STAGE32_32_01_178_N357_PREFIX_CACHE_META_V1":
        raise ValueError("N357 prefix metadata schema regression")
    if meta.get("producer_blob_sha1") != EXPECTED_PREFIX_PRODUCER_BLOB:
        raise ValueError("N357 prefix producer source-lock regression")
    if meta.get("target_blob_sha1") != EXPECTED_TARGET_BLOB:
        raise ValueError("N357 prefix target source-lock regression")
    if meta.get("cache_sha256") != sha256_file(args.prefix_cache):
        raise ValueError("N357 prefix cache digest regression")
    if int(meta.get("H", -1)) != H or int(meta.get("full178_rows", -1)) != len(rows):
        raise ValueError("N357 prefix domain regression")
    if meta.get("main_pruning_credit") is not False:
        raise ValueError("N357 prefix cache must not self-promote MAIN credit")

    with gzip.open(args.prefix_cache, "rb") as fh:
        payload = pickle.load(fh)
    if payload.get("schema") != "STAGE32_32_01_178_N357_PREFIX_CACHE_V1" or int(payload.get("H", -1)) != H:
        raise ValueError("N357 prefix cache payload regression")
    bc_pref = payload["bc_pref"]
    lex_pref = payload["lex_pref"]
    fullmod.build_bc_prefix = lambda _h: bc_pref
    fullmod.build_lex_prefix = lambda _h: lex_pref

    groups = defaultdict(list)
    structural_records = 0
    raw_group_keys = set()
    for row_id in rows:
        g, d = fullmod.base.parse_row_id(row_id)
        h = d // 2
        legacy_emin = 8 if g == 0 else 4
        required = fullmod.ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, required)
        emax = (19 * d) // 5
        for e in range(effective_emin, emax + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * fullmod.ceil_div(e, 6):
                continue
            threshold = 4 * h + d - e
            normal_block = 19 * d - 5 * e + 1
            if normal_block <= 0:
                raise ValueError(f"nonpositive normal block {(g,d,e)}")
            raw_group_keys.add((h, threshold))
            canonical_threshold = h if threshold >= h else threshold
            groups[(h, canonical_threshold)].append((row_id, g, d, e, required, normal_block))
            structural_records += 1

    ordered = sorted(groups.items())
    selected = ordered[args.shard_index::args.shard_count]
    mod._ENGINE = engine
    mod._FULLMOD = fullmod
    _MOD = mod

    workers = args.workers or min(4, max(1, os.cpu_count() or 1), max(1, len(selected)))
    if workers == 1:
        batches = [_compute(item) for item in selected]
    else:
        ctx = get_context("fork")
        chunksize = max(1, len(selected) // (workers * 8))
        with ctx.Pool(processes=workers) as pool:
            batches = pool.map(_compute, selected, chunksize=chunksize)
    records = [rec for batch in batches for rec in batch]

    worker_blob = git_blob_sha1(Path(__file__))
    stream = hashlib.sha256()
    for rec in sorted(records, key=lambda r: (r["g"], r["d"], r["e"], r["row_id"])):
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    result = {
        "schema": "STAGE32_32_01_178_N357_ALL178_SHARD_V1",
        "node_id": "N357",
        "status": "RESEARCH_SHARD_NO_MAIN_CREDIT",
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "workers": workers,
        "worker_blob_sha1": worker_blob,
        "target_blob_sha1": EXPECTED_TARGET_BLOB,
        "prefix_producer_blob_sha1": EXPECTED_PREFIX_PRODUCER_BLOB,
        "prefix_cache_sha256": meta["cache_sha256"],
        "raw_structural_group_count_total": len(raw_group_keys),
        "structural_group_count_total": len(ordered),
        "structural_record_count_total": structural_records,
        "shard_group_count": len(selected),
        "shard_record_count": len(records),
        "partial_source_terminals": sum(r["n356_transport_remaining_terminals"] for r in records),
        "partial_rejected_terminals": sum(r["n357_support_capacity_rejected_terminals"] for r in records),
        "partial_remaining_terminals": sum(r["n357_support_capacity_remaining_terminals"] for r in records),
        "partial_stream_sha256": stream.hexdigest(),
        "canonicalization": "threshold>=h -> h; threshold<-h -> exact zero",
        "records": records,
        "main_pruning_credit": False,
    }
    args.output.write_text(json.dumps(result, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N357_ALL178_CANONICAL_SHARD",
        "shard_index": args.shard_index,
        "shard_count": args.shard_count,
        "workers": workers,
        "raw_groups": len(raw_group_keys),
        "canonical_groups": len(ordered),
        "shard_groups": len(selected),
        "records": len(records),
        "partial_source_terminals": result["partial_source_terminals"],
        "partial_rejected_terminals": result["partial_rejected_terminals"],
        "partial_remaining_terminals": result["partial_remaining_terminals"],
        "stream": result["partial_stream_sha256"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
