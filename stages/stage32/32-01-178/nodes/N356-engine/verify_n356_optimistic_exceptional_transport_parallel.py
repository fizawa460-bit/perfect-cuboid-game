#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import os
from multiprocessing import get_context
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "verify_n356_optimistic_exceptional_transport.py"
EXPECTED_TARGET_BLOB = "ad0f5dcf7eb70cc24a9a54d4d31807226de1d2ad"

_REF_BUILD = None
_BC_PREF = None
_LEX_PREF = None
_FULLMOD = None


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_target():
    actual = git_blob_sha1(TARGET)
    if actual != EXPECTED_TARGET_BLOB:
        raise ValueError(f"N356 reference verifier source-lock regression: {actual}!={EXPECTED_TARGET_BLOB}")
    spec = importlib.util.spec_from_file_location("s32_n356_reference_parallel", TARGET)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {TARGET}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _compute_key(key):
    h, threshold = key
    return key, _REF_BUILD(h, threshold, _BC_PREF, _LEX_PREF, _FULLMOD)


def main() -> None:
    global _REF_BUILD, _BC_PREF, _LEX_PREF, _FULLMOD

    mod = load_target()
    reference_load = mod.load_module
    fullmod = reference_load(mod.N355_FULL, "s32_n356_parallel_n355_full")
    pre = reference_load(mod.N355_PREFLIGHT, "s32_n356_parallel_n355_preflight")

    manifest = fullmod.base.load_canonical(mod.MANIFEST, fullmod.base.EXPECTED_MANIFEST_CANONICAL)
    rows = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    parsed = [fullmod.base.parse_row_id(row_id) for row_id in rows]
    H = max(d // 2 for _, d in parsed)

    original_bc = fullmod.build_bc_prefix
    original_lex = fullmod.build_lex_prefix
    original_capped = fullmod.build_capped_exact
    bc_pref = original_bc(H)
    lex_pref = original_lex(H)

    capped_cache = {}

    def cached_capped(h: int, bc, lex):
        h = int(h)
        if h not in capped_cache:
            capped_cache[h] = original_capped(h, bc, lex)
        return capped_cache[h]

    def cached_bc(hmax: int):
        if int(hmax) == H:
            return bc_pref
        return original_bc(hmax)

    def cached_lex(hmax: int):
        if int(hmax) == H:
            return lex_pref
        return original_lex(hmax)

    fullmod.build_bc_prefix = cached_bc
    fullmod.build_lex_prefix = cached_lex
    fullmod.build_capped_exact = cached_capped

    keys = set()
    for row_id in rows:
        g, d = fullmod.base.parse_row_id(row_id)
        h = d // 2
        legacy_emin = 8 if g == 0 else 4
        K = fullmod.ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, K)
        emax = (19 * d) // 5
        for e in range(effective_emin, emax + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * fullmod.ceil_div(e, 6):
                continue
            threshold = 4 * h + d - e
            if threshold < h:
                keys.add((h, threshold))

    reference_build = mod.build_transport_exact
    precomputed = {}
    ordered_keys = sorted(keys)

    _REF_BUILD = reference_build
    _BC_PREF = bc_pref
    _LEX_PREF = lex_pref
    _FULLMOD = fullmod

    workers = min(4, max(1, os.cpu_count() or 1), max(1, len(ordered_keys)))
    if ordered_keys:
        if workers == 1:
            items = [_compute_key(key) for key in ordered_keys]
        else:
            ctx = get_context("fork")
            chunksize = max(1, len(ordered_keys) // (workers * 8))
            with ctx.Pool(processes=workers) as pool:
                items = pool.map(_compute_key, ordered_keys, chunksize=chunksize)
        precomputed.update(items)

    identity_cache = {}

    def accelerated_build(h: int, threshold: int, bc, lex, fm):
        h = int(h)
        threshold = int(threshold)
        if threshold >= h:
            if h not in identity_cache:
                identity_cache[h] = cached_capped(h, bc, lex)
            return identity_cache[h]
        key = (h, threshold)
        if key in precomputed:
            return precomputed[key]
        return reference_build(h, threshold, bc, lex, fm)

    def accelerated_load(path: Path, name: str):
        if path == mod.N355_FULL:
            return fullmod
        if path == mod.N355_PREFLIGHT:
            return pre
        return reference_load(path, name)

    mod.build_transport_exact = accelerated_build
    mod.load_module = accelerated_load

    print(
        f"N356_PARALLEL_PRECOMPUTE keys={len(ordered_keys)} workers={workers} "
        f"identity_h_cache={len(identity_cache)}"
    )
    mod.main()


if __name__ == "__main__":
    main()
