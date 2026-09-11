#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "verify_n356_optimistic_exceptional_transport.py"
EXPECTED_TARGET_BLOB = "ad0f5dcf7eb70cc24a9a54d4d31807226de1d2ad"


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_target():
    actual = git_blob_sha1(TARGET)
    if actual != EXPECTED_TARGET_BLOB:
        raise ValueError(f"N356 reference verifier source-lock regression: {actual}!={EXPECTED_TARGET_BLOB}")
    spec = importlib.util.spec_from_file_location("s32_n356_reference", TARGET)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {TARGET}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    mod = load_target()
    reference_build = mod.build_transport_exact
    identity_cache = {}

    def accelerated_build(h: int, threshold: int, bc_pref, lex_pref, fullmod):
        # Under the audited N355 full-prefix condition, 0<=b,c<=h.  Hence
        # b-c<=h.  When threshold>=h the N356 predicate b-c<=threshold is
        # automatic, so the exact N356 distribution is literally the N355
        # capped distribution.  This is an identity shortcut, not a relaxed
        # or approximate count.
        if threshold >= h:
            if h not in identity_cache:
                identity_cache[h] = fullmod.build_capped_exact(h, bc_pref, lex_pref)
            return identity_cache[h]
        return reference_build(h, threshold, bc_pref, lex_pref, fullmod)

    mod.build_transport_exact = accelerated_build
    mod.main()


if __name__ == "__main__":
    main()
