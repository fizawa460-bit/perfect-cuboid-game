#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED_CANONICAL = "29afae4e789522162374baeaca89c860a1c6dac21ce77059e7fe06988e43bfcf"
EXPECTED_ADAPTER = "919f8bed23fc07a8bd39907c1d348f7e3b7535cee0dd64642aa600ab793f633b"
EXPECTED_DECK = "cdc186f8da6eff760a79f98b50106de19d565ebf806dc58b00cc105e4d983af2"


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path) -> tuple[dict, str]:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if csha(raw) != claimed:
        raise SystemExit(f"canonical mismatch: {path}")
    return raw, claimed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, required=True)
    args = ap.parse_args()

    adapter, ac = load(HERE / "post1490-o210-q4-bolza-x-local-multiplicity-adapter.json")
    if ac != EXPECTED_ADAPTER:
        raise SystemExit("local multiplicity adapter moved")
    deck, dc = load(HERE / "post1490-o210-q4-bolza-v4-deck-translate-defect-decomposition.json")
    if dc != EXPECTED_DECK:
        raise SystemExit("deck defect certificate moved")

    mult = [int(x) for x in adapter["exact_multiplicity_vector"]["values"]]
    intrinsic = sum(m * (m - 1) // 2 for m in mult)
    if intrinsic != 1046:
        raise SystemExit(f"marked intrinsic delta lower bound moved: {intrinsic}")
    cb = {k:int(v) for k,v in adapter["deck_local_intersection"]["c_t_lower_bounds"].items()}
    if cb != {"u":680,"v":898,"uv":726}:
        raise SystemExit(f"marked deck lower bounds moved: {cb}")
    deck_sum = sum(cb.values())
    combined = intrinsic + deck_sum
    if deck_sum != 2304 or combined != 3350 or 8586-combined != 5236:
        raise SystemExit("marked multiplicity-only budget arithmetic moved")

    cert, cc = load(args.check)
    if cc != EXPECTED_CANONICAL:
        raise SystemExit("multiplicity-only boundary canonical moved")
    if cert["marked_intrinsic_delta_lower_bound"] != intrinsic:
        raise SystemExit("intrinsic delta lower bound differs from replay")
    if cert["marked_deck_collision_c_lower_bounds"] != cb:
        raise SystemExit("deck lower bounds differ from replay")
    if cert["combined_marked_budget_lower_bound"] != combined or cert["unforced_budget_after_marked_multiplicity_only"] != 5236:
        raise SystemExit("boundary totals differ from replay")
    if cert["verdict"]["O210_excluded"] or cert["verdict"]["marked_multiplicity_only_sufficient"]:
        raise SystemExit("nonexclusion boundary overpromoted")

    print(json.dumps({
        "verdict":"PASS_EXACT_MARKED_MULTIPLICITY_ONLY_NONEXCLUSION_BOUNDARY",
        "canonical_sha256":cc,
        "marked_intrinsic_delta_lower_bound":intrinsic,
        "marked_deck_collision_sum_lower_bound":deck_sum,
        "combined_marked_budget_lower_bound":combined,
        "unforced_budget":5236,
        "O210_excluded":False,
        "next_exact_leaf":cert["verdict"]["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
