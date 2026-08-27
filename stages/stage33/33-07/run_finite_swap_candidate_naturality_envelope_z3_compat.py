#!/usr/bin/env python3
"""Compatibility runner for the exact finite-swap Boolean certificate.

z3-solver 4.15 exposes Xor with a bounded Python positional signature even
though the Boolean operator is associative.  Fold arbitrary-length XORs
pairwise, then execute the locked certificate unchanged.
"""
import runpy
from pathlib import Path

import z3

_ORIGINAL_XOR = z3.Xor


def _folded_xor(*args):
    if not args:
        return z3.BoolVal(False)
    out = args[0]
    for arg in args[1:]:
        out = _ORIGINAL_XOR(out, arg)
    return out


z3.Xor = _folded_xor
runpy.run_path(
    str(Path(__file__).resolve().parent / "certify_finite_swap_candidate_naturality_envelope.py"),
    run_name="__main__",
)
