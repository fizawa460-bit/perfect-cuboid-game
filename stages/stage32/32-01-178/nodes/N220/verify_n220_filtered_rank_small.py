#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_indexer import CompressedTerminalIndexer

EXPECTED_INDEXER_RAW_SHA256 = None  # filled from --indexer after raw hash check is reported
EXPECTED_INDEXER_BLOB_SHA = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"


def ceil_div(a: int, b: int) -> int:
    return -((-int(a)) // int(b))


def accept_n220(x: tuple[int, ...], *, g: int, d: int, e: int) -> bool:
    m10 = sum(x[i] for i in range(11) if i != 4)
    s10 = sum(1 for i in range(11) if i != 4 and x[i] > 0)
    k = ceil_div(d - 16 * g + 16, 4)
    return s10 + min(38, e - m10) >= k


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay_case(*, g: int, d: int, e: int, max_old_ranks: int) -> dict:
    idx = CompressedTerminalIndexer(e, d)
    if idx.terminal_count > max_old_ranks:
        raise ValueError(
            f"bounded replay gate: {idx.terminal_count}>{max_old_ranks} for g={g},d={d},e={e}"
        )
    block = idx.normal_budget + 1
    cert = idx.certificate()
    if cert["canonical_index_order"] != "EXCEPTIONAL_UNEQUAL_THEN_EQUAL__NORMAL_X4_INNERMOST":
        raise ValueError("canonical index order regression")
    if idx.terminal_count != idx.exceptional_count * block:
        raise ValueError("old terminal factorization regression")

    accepted_exceptional: list[int] = []
    rejected_exceptional: list[int] = []
    for erank in range(idx.exceptional_count):
        old0 = erank * block
        x0 = tuple(int(v) for v in idx.unrank(old0))
        if x0[4] != 0 or idx.rank(x0) != old0:
            raise ValueError("old exceptional-rank representative replay regression")
        a0 = accept_n220(x0, g=g, d=d, e=e)
        # N220 is independent of x4; verify this against every x4 in this bounded case.
        for x4 in range(block):
            old_rank = erank * block + x4
            x = tuple(int(v) for v in idx.unrank(old_rank))
            if idx.rank(x) != old_rank:
                raise ValueError("old rank/unrank regression")
            if x[4] != x4:
                raise ValueError("x4 inner-coordinate regression")
            if accept_n220(x, g=g, d=d, e=e) != a0:
                raise ValueError("N220 unexpectedly depends on x4")
        (accepted_exceptional if a0 else rejected_exceptional).append(erank)

    inverse = {old_erank: new_erank for new_erank, old_erank in enumerate(accepted_exceptional)}
    survivor_count = len(accepted_exceptional) * block
    rejected_count = len(rejected_exceptional) * block
    if survivor_count + rejected_count != idx.terminal_count:
        raise ValueError("filtered partition count regression")

    # Exhaustively replay secondary filtered rank/unrank in the bounded case.
    for old_erank, new_erank in inverse.items():
        for x4 in range(block):
            old_rank = old_erank * block + x4
            filtered_rank = new_erank * block + x4
            q_new_erank, q_x4 = divmod(filtered_rank, block)
            replay_old_erank = accepted_exceptional[q_new_erank]
            replay_old_rank = replay_old_erank * block + q_x4
            if replay_old_rank != old_rank:
                raise ValueError("filtered rank/unrank old-rank replay regression")
            x = tuple(int(v) for v in idx.unrank(replay_old_rank))
            if not accept_n220(x, g=g, d=d, e=e):
                raise ValueError("filtered unrank returned N220 rejection")

    return {
        "g": g,
        "d": d,
        "e": e,
        "normal_block": block,
        "old_terminal_count": idx.terminal_count,
        "old_exceptional_count": idx.exceptional_count,
        "accepted_exceptional_count": len(accepted_exceptional),
        "rejected_exceptional_count": len(rejected_exceptional),
        "filtered_survivor_terminal_count": survivor_count,
        "n220_rejected_terminal_count": rejected_count,
        "partition_exact": True,
        "rank_unrank_replay_exact": True,
        "x4_block_preserved_exactly": True,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--indexer",
        type=Path,
        default=RESIDUAL / "compressed_terminal_indexer.py",
    )
    ap.add_argument("--max-old-ranks", type=int, default=250000)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    if args.max_old_ranks <= 0:
        raise ValueError("max-old-ranks must be positive")

    # The Git blob SHA is source-locked in this file. Raw SHA256 is emitted so a
    # hostile replay can additionally pin bytes without silently confusing Git SHA1
    # with raw SHA256.
    cases = [
        replay_case(g=1, d=8, e=4, max_old_ranks=args.max_old_ranks),
        replay_case(g=1, d=8, e=5, max_old_ranks=args.max_old_ranks),
    ]
    payload = {
        "schema": "STAGE32_32_01_178_N220_FILTERED_RANK_SMALL_REPLAY_V1",
        "status": "PASS_BOUNDED_FILTERED_RANK_ARCHITECTURE_REPLAY_NO_N220_AUDIT_CREDIT",
        "indexer": {
            "path": str(args.indexer),
            "git_blob_sha": EXPECTED_INDEXER_BLOB_SHA,
            "raw_sha256": sha256(args.indexer),
            "canonical_order": "EXCEPTIONAL_UNEQUAL_THEN_EQUAL__NORMAL_X4_INNERMOST",
        },
        "cases": cases,
        "semantics": {
            "old_canonical_rank_remains_authority": True,
            "secondary_filtered_rank_only": True,
            "filtered_rank_formula": "accepted_exceptional_rank*(normal_budget+1)+x4",
            "x4_block_is_not_reordered": True,
            "n220_predicate_is_x4_independent": True,
        },
        "firewalls": {
            "n220_hostile_audit_pass_granted": False,
            "production_pruning_authorized": False,
            "full178_complete": False,
            "heavy_compute_authorized": False,
            "theorem_credit": False,
            "merge_authorized": False,
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
