#!/usr/bin/env python3
"""CUT103 runner with the historical BC2-18 non-replayable canonical-field contract.

BC2-24 itself loads BC2-18 with replay=False: the Git blob and embedded canonical
field are source locks, while the JSON canonical is not recomputed.  All other
CUT103 lineage checkpoints retain strict canonical replay.
"""
from __future__ import annotations

import json
from pathlib import Path

import cut103_scope_preimage_fresh_replay as base

STRICT_CHECKED = base.checked
BC2_18_NAME = "bc2-18-n354-survivor-selected-exceptional-mod8-checkpoint.json"


def checked_compat(path: Path, blob: str, canonical: str) -> dict:
    if path.name != BC2_18_NAME:
        return STRICT_CHECKED(path, blob, canonical)
    if base.git_blob_sha(path) != blob:
        raise ValueError(f"BC2-18 blob lock moved: {path}")
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != canonical:
        raise ValueError(f"BC2-18 canonical field moved: {path}")
    return obj


base.checked = checked_compat

if __name__ == "__main__":
    base.main()
