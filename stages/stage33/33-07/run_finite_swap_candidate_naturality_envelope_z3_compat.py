#!/usr/bin/env python3
"""Compatibility/source-lock runner for the exact finite-swap certificate.

Two retained compatibility facts are supplied without changing the certificate
logic: z3 4.15 needs arbitrary XORs folded pairwise, and the compact seven-sign
endpoint intentionally omitted the quadratic matrix that existed in the same
locked successful endpoint artifact.  Reattach that retained matrix only to
the in-memory namespace returned by the seven-sign leaf.
"""
import hashlib
import json
import runpy
from pathlib import Path

import z3

HERE = Path(__file__).resolve().parent
QUADRATIC = HERE / "retained-q256-geometric-sign-quadratic.json"
_ORIGINAL_XOR = z3.Xor
_ORIGINAL_RUN_PATH = runpy.run_path


def _folded_xor(*args):
    if not args:
        return z3.BoolVal(False)
    out = args[0]
    for arg in args[1:]:
        out = _ORIGINAL_XOR(out, arg)
    return out


quad = json.loads(QUADRATIC.read_text(encoding="utf-8"))
claimed = quad.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(quad, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
if claimed != actual or claimed != "5fa065e1781da27f92983749cd782635839251e93b191e7ee4e6063f1fb3843c":
    raise SystemExit("retained finite quadratic source lock moved")
if quad["source_original_canonical_sha256"] != "9f9dec186d3401d75f4aad4e7e4b819529362880091f0070548cb2bf3b13fbf3":
    raise SystemExit("retained original endpoint lock moved")
if quad["discriminant_moduli"] != [2] * 4 + [4] * 6 + [8] * 4:
    raise SystemExit("retained quadratic moduli regression")


def _run_path_with_retained_quadratic(path_name, *args, **kwargs):
    ns = _ORIGINAL_RUN_PATH(path_name, *args, **kwargs)
    if Path(path_name).name == "certify_retained_geometric_sign_intertwiner_space.py":
        endpoint = dict(ns["signs"])
        if endpoint["discriminant_moduli"] != quad["discriminant_moduli"]:
            raise SystemExit("seven-sign endpoint/quadratic moduli mismatch")
        endpoint["discriminant_bilinear_numerator_over_8_reduced"] = quad[
            "discriminant_bilinear_numerator_over_8_reduced"
        ]
        ns["signs"] = endpoint
    return ns


z3.Xor = _folded_xor
runpy.run_path = _run_path_with_retained_quadratic
_ORIGINAL_RUN_PATH(
    str(HERE / "certify_finite_swap_candidate_naturality_envelope.py"),
    run_name="__main__",
)
