#!/usr/bin/env python3
"""Compatibility runner for the Stage33-11 pinned retained-Smith transport."""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
TARGET = HERE / "materialize_stage33_11_pinned_retained_smith_transport.py"
PINNED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

sys.path.insert(0, str(LEGACY))
import stoll_cuboid_source as stoll


def locked_source(blob: str) -> str:
    if blob != PINNED_BLOB:
        raise SystemExit(f"unexpected requested pinned blob: {blob}")
    _, core, got, attempt = stoll.load_pinned_source()
    if got != PINNED_BLOB:
        raise SystemExit(f"pinned Testa--Stoll source lock moved: {got}")
    print(f"STAGE33_11_PINNED_SOURCE=PASS attempt={attempt} blob={got}")
    return core

stoll.locked_source = locked_source
runpy.run_path(str(TARGET), run_name="__main__")
