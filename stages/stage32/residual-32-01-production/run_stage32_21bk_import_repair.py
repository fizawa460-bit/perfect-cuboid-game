#!/usr/bin/env python3
"""21bk import-plumbing repair launcher.

The original 21bk source imported load_21bh_lock/r54_lo_from_table from the
21bh module, while those helpers live in the audited 21bi module. Patch only
those module attributes in-memory, then execute the unchanged 21bk source.
"""
from __future__ import annotations

import runpy

import certify_stage32_21bh_r54_per_triple_projection as bh
from certify_stage32_21bi_r57_per_triple_projection import load_21bh_lock, r54_lo_from_table

if hasattr(bh, "load_21bh_lock") or hasattr(bh, "r54_lo_from_table"):
    raise RuntimeError("21bk repair launcher is obsolete: 21bh already exports repaired helpers")

bh.load_21bh_lock = load_21bh_lock
bh.r54_lo_from_table = r54_lo_from_table
runpy.run_module("certify_stage32_21bk_r20_final_single_coordinate", run_name="__main__")
