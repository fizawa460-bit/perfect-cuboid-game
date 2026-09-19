#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ARCHIVE_HEAD = "ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"
BASE = "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
ARCHIVE_LOCKS = {
    f"{BASE}/R8-BOUND-ROUTE-LEDGER.md": "548cbf714900cbab3b775ce2bfa2a362b7107960",
    f"{BASE}/BEAUVILLE-ODD-BRANCH-COVER-WALL.md": "1afa8398a337b58256fa05af8f3013688d7d7cae",
    f"{BASE}/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md": "a20547082b1ea2f786b1272d1b76af3527508e9b",
    f"{BASE}/GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY.md": "cb05a7a187c9dd7495ee1f4af3b92fb776900422",
}
CURRENT_P6D = f"{BASE}/MB104-P6D-FULL-DECK-EQUALITY-PASSPORT-20260919.md"
CURRENT_P6D_BLOB = "efd3334a22603a971d72ab2d858be4e5d25f4b99"

def req(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit("FAIL: " + msg)

def blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive-root", required=True)
    args = ap.parse_args()
    archive = Path(args.archive_root)
    head = subprocess.check_output(["git","-C",str(archive),"rev-parse","HEAD"], text=True).strip()
    req(head == ARCHIVE_HEAD, "archive HEAD mismatch")
    for rel, expected in ARCHIVE_LOCKS.items():
        p = archive / rel
        req(p.is_file(), "missing archive source " + rel)
        req(blob_sha1(p) == expected, "archive blob mismatch " + rel)

    root = Path(__file__).resolve().parents[6]
    p6d = root / CURRENT_P6D
    req(p6d.is_file(), "current P6D missing")
    req(blob_sha1(p6d) == CURRENT_P6D_BLOB, "current P6D blob mismatch")

    cert_path = Path(__file__).with_name("MB104-P6D2-AUTOMATIC-ODD-EQUALITY-CERTIFICATE.json")
    c = json.loads(cert_path.read_text())
    req(c["per_l"]["d"] == 112, "d coefficient")
    req(c["per_l"]["M"] == c["per_l"]["d"], "M=d")
    req(c["support_node_count"] * c["per_l"]["Mi_each"] == c["per_l"]["M"], "sum Mi=M")
    req(c["per_l"]["R8_lower_from_fsm"] == c["per_l"]["d"] // 4, "FSM lower bound")
    req(c["per_l"]["R8_lower_from_fsm"] > 0, "R8 positive")
    req(sum(c["node_type_counts"].values()) == c["support_node_count"], "node type count")
    req(all(v > 0 for v in c["node_type_counts"].values()), "all three node types occur")
    req(c["full_deck"]["e"] == 4, "full deck e")
    u = c["six_value_passport"]["unramified_pair_totals_l"]
    r = c["six_value_passport"]["ramified_pair_totals_l"]
    req(u == [48,16,48], "unramified pair totals")
    req(r == [32,48,32], "ramified pair totals")
    req(sum(u) == c["per_l"]["d"], "unramified total equals d")
    req(sum(r) == c["per_l"]["d"], "ramification total")
    req(c["deductions"]["R8_equals_d"] is False, "must not overclaim R8=d")
    req(all(v is False for v in c["firewalls"].values()), "credit firewall")
    print("PASS: P6D2 automatic odd-contact equality")
    print("d=M=r_odd=R = 112*l; every exceptional branch has m=1")
    print("R8 is only bounded below by 28*l; R8=d is NOT claimed")
    print("full deck e=4; six-value pair totals=(48,16,48)*l")

if __name__ == "__main__":
    main()
