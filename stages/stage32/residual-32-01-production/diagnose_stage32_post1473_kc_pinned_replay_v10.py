#!/usr/bin/env python3
"""Loader-only fix for the V9 exact exceptional-ordering replay."""
from __future__ import annotations

import importlib

import diagnose_stage32_post1473_kc_pinned_replay_v9 as v9

_original_load_module = v9.v7.v6.base.load_module


def _safe_load_module(path, name):
    if path.name == "aut_equivariant_pairing_adapter.py":
        return importlib.import_module("aut_equivariant_pairing_adapter")
    return _original_load_module(path, name)


if __name__ == "__main__":
    v9.v7.v6.base.load_module = _safe_load_module
    v9.main()
