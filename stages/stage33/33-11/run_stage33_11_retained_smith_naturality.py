#!/usr/bin/env python3
"""Run the retained-Smith naturality verifier with the retained Br2 key spelling.

The certificate key is lower-case `v4`; the proof source used the older
upper-case spelling.  Patch exactly that one lookup and execute fail-closed.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "certify_stage33_11_retained_smith_naturality.py"
src = TARGET.read_text(encoding="utf-8")
old = 'br2["proper_Br2_joint_V4_fixed_dimension_f2"]'
new = 'br2["proper_Br2_joint_v4_fixed_dimension_f2"]'
if src.count(old) != 1:
    raise SystemExit("Stage33-11 retained Br2 key patch anchor moved")
src = src.replace(old, new)
g = {"__name__": "__main__", "__file__": str(TARGET)}
exec(compile(src, str(TARGET), "exec"), g, g)
