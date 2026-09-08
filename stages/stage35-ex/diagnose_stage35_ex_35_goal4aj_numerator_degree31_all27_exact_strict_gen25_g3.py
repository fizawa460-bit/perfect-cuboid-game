#!/usr/bin/env python3
"""Goal4AJ gen25-g3: transport-fixed wrapper for all-27 exact strict replay.

Reuses gen25's exact Singular membership checks and shard/aggregate logic, but
loads the permanent gen24 Q-candidate by the two invariants that matter:
(1) exact repo blob SHA1 for the transport text, and
(2) exact decompressed Q-candidate byte length + SHA256.

The failed gen25 generation-2 run stopped before any mathematical condition
because an intermediate compressed-payload metadata assertion disagreed with
the repo transport. This wrapper does not reinterpret that as math credit.
"""
from __future__ import annotations

import argparse
import base64
import bz2
import hashlib
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
BASE = HERE / "diagnose_stage35_ex_35_goal4aj_numerator_degree31_all27_exact_strict_gen25.py"
BASE_BLOB = "5920842a35877245bcb01a457882674d2b891340"
Q_SHA = "358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb"
Q_BYTES = 208802
CANDIDATE_BLOB = "9d8b934961f03a423cf940bc95efdffe8e28e0fd"
LOCK_BLOB = "1bc208ed5010ec2d3f50d90b70db3698f860a134"
LOCK_CANONICAL = "b341897f941e7237f2769e0a94bc906b959f346bde753dcd4d15cbc5e3985e5f"
GEN24_CANONICAL = "9463e3ca0431fbb8310c139481873ddf98122136f360cdac58ecf35eaa325e26"


def git_blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def main() -> None:
    assert git_blob(BASE) == BASE_BLOB
    ns = runpy.run_path(str(BASE))
    candidate = ns["CANDIDATE"]
    lock_path = ns["LOCK"]
    assert git_blob(candidate) == CANDIDATE_BLOB
    assert git_blob(lock_path) == LOCK_BLOB
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    assert lock["schema"] == "STAGE35_EX_GOAL4AJ_GEN24_PARALLEL_FOUR_PRIME_MATERIALIZATION_REPO_LOCK_V2"
    assert lock["repo_lock_canonical_sha256"] == LOCK_CANONICAL
    assert lock["gen24_canonical_sha256"] == GEN24_CANONICAL
    assert lock["q_candidate_sha256"] == Q_SHA
    assert lock["q_candidate_text_bytes"] == Q_BYTES

    def fixed_load_q_candidate() -> str:
        payload = base64.b64decode("".join(candidate.read_text(encoding="utf-8").split()))
        raw = bz2.decompress(payload)
        actual = {
            "repo_blob_sha1": git_blob(candidate),
            "base64_chars": len("".join(candidate.read_text(encoding="utf-8").split())),
            "compressed_bytes": len(payload),
            "compressed_sha256": hashlib.sha256(payload).hexdigest(),
            "raw_bytes": len(raw),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
        }
        print("GOAL4AJ_GEN25_G3_TRANSPORT_ACTUAL=" + json.dumps(actual, sort_keys=True, separators=(",", ":")), flush=True)
        assert actual["repo_blob_sha1"] == CANDIDATE_BLOB
        assert actual["raw_bytes"] == Q_BYTES and actual["raw_sha256"] == Q_SHA
        return raw.decode("utf-8")

    # run_path's returned mapping is not guaranteed to be the live globals dict
    # retained by imported function objects. Patch the function globals directly.
    ns["shard_mode"].__globals__["load_q_candidate"] = fixed_load_q_candidate

    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="mode", required=True)
    s = sub.add_parser("shard"); s.add_argument("--shard", type=int, required=True); s.add_argument("--output-dir", type=Path, required=True)
    a = sub.add_parser("aggregate"); a.add_argument("--input-dir", type=Path, required=True); a.add_argument("--output-dir", type=Path, required=True)
    args = ap.parse_args()
    if args.mode == "shard":
        ns["shard_mode"](args.shard, args.output_dir)
    else:
        ns["aggregate_mode"](args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
