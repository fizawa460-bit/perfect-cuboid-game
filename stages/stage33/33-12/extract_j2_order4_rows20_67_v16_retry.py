#!/usr/bin/env python3
"""Retry wrapper for the v16 two-row extractor with multiline Magma literals.

The first authorized run reached the exact Magma completion marker, but Magma's
pretty-printer wrapped a sparse row across lines.  This wrapper changes only the
stdout literal parser; the pinned source, source slice, requested rows, storage
budget, and mathematical scope are unchanged.
"""
from __future__ import annotations

import ast
import importlib.util
import re
import sys
from pathlib import Path

BASE = Path(__file__).with_name("extract_j2_order4_rows20_67_v16.py")
spec = importlib.util.spec_from_file_location("stage33_v16_base", BASE)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot import {BASE}")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def grab_multiline(stdout: str, name: str):
    m = re.search(rf"^{re.escape(name)}=(.*)$", stdout, re.MULTILINE)
    if not m:
        raise RuntimeError(f"missing Magma marker {name}")
    first = m.group(1).strip()
    if not first:
        raise RuntimeError(f"empty Magma marker {name}")
    if first[0] not in "[({":
        return ast.literal_eval(first)

    opening = {"[": "]", "(": ")", "{": "}"}
    stack: list[str] = []
    start = m.start(1)
    text = stdout[start:]
    end = None
    in_string = False
    quote = ""
    escape = False
    for i, ch in enumerate(text):
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == quote:
                in_string = False
            continue
        if ch in "'\"":
            in_string = True
            quote = ch
            continue
        if ch in opening:
            stack.append(opening[ch])
        elif ch in "])}":
            if not stack or ch != stack[-1]:
                raise RuntimeError(f"unbalanced Magma literal for {name}")
            stack.pop()
            if not stack:
                end = i + 1
                break
    if end is None:
        raise RuntimeError(f"unterminated Magma literal for {name}")
    literal = text[:end].replace("\r", "")
    return ast.literal_eval(literal)


base.grab = grab_multiline
raise SystemExit(base.main())
