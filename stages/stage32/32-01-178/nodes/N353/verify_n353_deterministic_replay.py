#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_n353_full178_scalar_hurwitz_census.py"
EXPECTED_BASE_BLOB = "06807bde7ba0e5de745b12f25192934c00539a1c"
EXPECTED_CANONICAL = "4400dac0b9bcb04497f4963e53afc61e472251da0287c4d880f8e9dbaae2c113"
EXPECTED_STREAM = "87b50a7053f544717acb3b8682ffa9e15502e1fdba6668379bc44a39121aae5c"
EXPECTED_CONTRADICTED = 12788
EXPECTED_REMAINING = 47703
EXPECTED_REJECTED_TERMINALS = 264541612417334415376
EXPECTED_REMAINING_TERMINALS = 346053443361304169755481593
EXPECTED_TOTAL = 346053707902916587089896969


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    got_blob = git_blob_sha1(BASE)
    if got_blob != EXPECTED_BASE_BLOB:
        raise ValueError(f"N353 base verifier source-lock regression: {got_blob} != {EXPECTED_BASE_BLOB}")

    with tempfile.TemporaryDirectory() as td:
        raw = Path(td) / "n353.json"
        subprocess.run([sys.executable, str(BASE), "--output", str(raw)], check=True)
        body = json.loads(raw.read_text())

    agg = body["aggregate"]
    checks = {
        "canonical": (body["canonical_sha256_without_this_field"], EXPECTED_CANONICAL),
        "stream": (agg["per_stratum_stream_sha256"], EXPECTED_STREAM),
        "contradicted_strata": (agg["contradicted_strata"], EXPECTED_CONTRADICTED),
        "remaining_strata": (agg["not_contradicted_strata"], EXPECTED_REMAINING),
        "candidate_rejected_terminals": (agg["candidate_rejected_terminals"], EXPECTED_REJECTED_TERMINALS),
        "candidate_remaining_terminals": (agg["candidate_remaining_terminals"], EXPECTED_REMAINING_TERMINALS),
        "post_n220_terminals": (body["population"]["post_n220_terminals"], EXPECTED_TOTAL),
    }
    for name, (got, expected) in checks.items():
        if got != expected:
            raise ValueError(f"N353 deterministic replay regression {name}: {got} != {expected}")
    if EXPECTED_REJECTED_TERMINALS + EXPECTED_REMAINING_TERMINALS != EXPECTED_TOTAL:
        raise ValueError("N353 expected terminal partition constant regression")
    if body["semantics"]["main_pruning_credit"] is not False:
        raise ValueError("N353 firewall regression: main_pruning_credit must remain false")
    if body["semantics"]["full178_complete"] is not False:
        raise ValueError("N353 firewall regression: full178_complete must remain false")

    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N353_DETERMINISTIC_REPLAY",
        "base_verifier_blob": got_blob,
        "canonical": EXPECTED_CANONICAL,
        "aggregate": agg,
        "by_genus": body["by_genus"],
        "frontier": body["frontier"],
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
