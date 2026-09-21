#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(RESIDUAL))

from compressed_terminal_indexer import CompressedTerminalIndexer

INDEXER = RESIDUAL / "compressed_terminal_indexer.py"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"
FAMILY = RESIDUAL / "compressed_terminal_family.py"
FAMILY_BLOB = "90ff82ed312dcc0cb32cf207935945f550e29170"

ROW_ID = "g0-d008"
DEGREE = 8
EXCEPTIONAL_MASS = 8
NORMAL_BUDGET = 112
STATIC_ORDER = ("a", "b", "c", "t", "x4", "e", "d")
ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)
L4 = (
    (0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0),
    (0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0),
    (1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1),
    (1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
)


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def base4(x: tuple[int, ...]) -> tuple[int, int, int, int]:
    return tuple(
        sum(int(row[j]) * int(x[j]) for j in range(11))
        for row in L4
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    req(blob(INDEXER) == INDEXER_BLOB, "compressed indexer drift")
    req(blob(FAMILY) == FAMILY_BLOB, "compressed terminal family drift")

    indexer = CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    req(indexer.normal_budget == NORMAL_BUDGET, "normal budget drift")
    exceptional_count = int(indexer.exceptional_count)
    terminal_count = int(indexer.terminal_count)
    req(terminal_count == (NORMAL_BUDGET + 1) * exceptional_count,
        "terminal factorization drift")

    counts: Counter[tuple[int, int, int, int]] = Counter()
    representative_exceptional_rank: dict[tuple[int, int, int, int], int] = {}

    stride = NORMAL_BUDGET + 1
    for exceptional_rank in range(exceptional_count):
        terminal_rank = exceptional_rank * stride
        x = tuple(int(v) for v in indexer.unrank(terminal_rank))
        req(x[4] == 0, "x4 stride regression")
        req(indexer.rank(x) == terminal_rank, "rank/unrank census replay")
        key = base4(x)
        counts[key] += 1
        representative_exceptional_rank.setdefault(key, exceptional_rank)

    req(sum(counts.values()) == exceptional_count, "exceptional population conservation")

    base_keys = sorted(counts)
    static7_key_count = len(base_keys) * stride
    reconstructed_terminal_mass = sum(counts[k] * stride for k in base_keys)
    req(reconstructed_terminal_mass == terminal_count, "static-key mass conservation")

    rows = []
    for k in base_keys:
        rows.append({
            "base4": list(k),
            "exceptional_multiplicity_per_x4": int(counts[k]),
            "representative_exceptional_rank": int(representative_exceptional_rank[k]),
            "representative_terminal_rank_x4_0": int(representative_exceptional_rank[k] * stride),
        })

    mult_hist = Counter(int(v) for v in counts.values())
    payload = {
        "schema": "STAGE32_MAIN_BTVA_STATIC7_KEY_CENSUS_V1",
        "stage": 32,
        "route": "BTVA_COMPRESSED_PICARD_LIFT_RECEIVER_INTERSECTION",
        "status": "EXACT_G0_D008_E8_STATIC7_KEY_CENSUS_ZERO_CREDIT",
        "source_locks": {
            "compressed_terminal_indexer_blob_sha1": INDEXER_BLOB,
            "compressed_terminal_family_blob_sha1": FAMILY_BLOB,
        },
        "target": {
            "row_id": ROW_ID,
            "degree": DEGREE,
            "exceptional_mass": EXCEPTIONAL_MASS,
            "normal_budget": NORMAL_BUDGET,
            "static_order": list(STATIC_ORDER),
            "exceptional_state_count": exceptional_count,
            "x4_value_count": stride,
            "terminal_count": terminal_count,
        },
        "factorization": {
            "x4_is_independent_in_terminal_indexer": True,
            "x4_range_inclusive": [0, NORMAL_BUDGET],
            "enumerated_exceptional_states_only": exceptional_count,
            "full_terminal_materialization_performed": False,
            "static7_key_count": static7_key_count,
            "reconstructed_terminal_mass": reconstructed_terminal_mass,
        },
        "base4_keys": rows,
        "multiplicity_histogram": [
            {"multiplicity": m, "base4_key_count": mult_hist[m]}
            for m in sorted(mult_hist)
        ],
        "firewalls": {
            "main_pruning_credit": False,
            "receiver_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_complete": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
        "next_exact_step":
            "Run the BTVA Picard64 compatibility solver over every exact static7 key or a source-locked partition thereof, using multiplicities here for no-double-charge accounting.",
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("BTVA_STATIC7_KEY_CENSUS_SUMMARY=" + json.dumps({
        "exceptional_states": exceptional_count,
        "base4_keys": len(base_keys),
        "x4_values": stride,
        "static7_keys": static7_key_count,
        "terminal_count": terminal_count,
        "canonical": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
