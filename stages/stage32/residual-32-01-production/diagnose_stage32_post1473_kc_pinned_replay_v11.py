#!/usr/bin/env python3
"""Reuse the exact all140 adapter that generated the V6 witness pairings."""
from __future__ import annotations

from types import SimpleNamespace

import hperp_integral_adapter
import diagnose_stage32_post1473_kc_pinned_replay_v9 as v9

_original_load_module = v9.v7.v6.base.load_module
_proxy = SimpleNamespace(
    AutEquivariantPairingAdapter=hperp_integral_adapter.HperpIntegralPairingAdapter
)


def _safe_load_module(path, name):
    if path.name == "aut_equivariant_pairing_adapter.py":
        # V9 only consumes .from_retained(...).pairing_matrix/.certificate.
        # Use the exact Hperp adapter used by the V6 reconstruction path rather
        # than introducing the separate Aut-orbit propagation adapter.
        return _proxy
    return _original_load_module(path, name)


if __name__ == "__main__":
    v9.v7.v6.base.load_module = _safe_load_module
    v9.main()
