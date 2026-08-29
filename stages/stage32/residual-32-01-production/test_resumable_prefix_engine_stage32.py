#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))

from aut_equivariant_pairing_adapter import (
    AutEquivariantPrefixCanonicalAugmentation,
    EquivariantPrefixMembershipOracle,
)
from hperp_integral_adapter import HperpIntegralPairingAdapter
from resumable_prefix_engine import run_resumable_dfs
from run_full178_prefix_work_unit import (
    KNOWN_LABEL_ORDER,
    load_module_payload,
    next_upper,
    run_partition,
)


def stream_digest(terminals: list[tuple[int, ...]]) -> str:
    h = hashlib.sha256()
    for terminal in terminals:
        h.update(json.dumps(list(terminal), separators=(",", ":")).encode() + b"\n")
    return h.hexdigest()


def main() -> None:
    retained = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
    marking_path = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
    bundle = load_module_payload(retained, "stage32_picard_retained_resume_test")
    marking = load_module_payload(marking_path, "stage32_marking_retained_resume_test")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    oracle = EquivariantPrefixMembershipOracle(adapter, KNOWN_LABEL_ORDER)
    aut = AutEquivariantPrefixCanonicalAugmentation(
        marking["aut_action"]["permutations_1based"],
        KNOWN_LABEL_ORDER,
        marking["aut_action"]["canonical_sha256_without_this_field"],
    )

    # Actual Stage32 coordinates, small bounded regression only.
    e = 8
    d = 8
    baseline = run_partition(
        oracle,
        aut,
        KNOWN_LABEL_ORDER,
        e=e,
        d=d,
        node_limit=50_000,
        prefix=[],
        next_min=0,
        next_max=e,
    )
    assert baseline["nodes"] == 50_000
    assert baseline["complete"] is False

    continuation = None
    terminals: list[tuple[int, ...]] = []
    nodes = membership = symmetry = terminal_count = 0
    for budget in (17_000, 17_000, 16_000):
        out = run_resumable_dfs(
            labels=KNOWN_LABEL_ORDER,
            fixed_prefix=[],
            root_lo=0,
            root_hi=e,
            node_limit=budget,
            upper_for_prefix=lambda p: next_upper(KNOWN_LABEL_ORDER, p, e, d),
            feasible=oracle.feasible,
            canonical=aut.canonical,
            continuation=continuation,
            capture_terminals=True,
        )
        nodes += out.nodes
        membership += out.membership_prunes
        symmetry += out.symmetry_prunes
        terminal_count += out.terminal_count
        terminals.extend(out.terminals)
        continuation = out.continuation

    assert nodes == baseline["nodes"] == 50_000
    assert membership == baseline["membership_prunes"]
    assert symmetry == baseline["symmetry_prunes"]
    assert terminal_count == baseline["terminal_count"]
    assert stream_digest(terminals) == baseline["terminal_stream_sha256"]
    assert continuation is not None
    print(json.dumps({
        "verdict": "PASS_REAL_STAGE32_RESUME_EQUIVALENCE",
        "nodes": nodes,
        "membership_prunes": membership,
        "symmetry_prunes": symmetry,
        "terminal_count": terminal_count,
        "continuation_children": 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
