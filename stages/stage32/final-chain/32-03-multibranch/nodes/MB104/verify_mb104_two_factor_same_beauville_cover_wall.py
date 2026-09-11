#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
LOCKS = {
    "stages/stage32/residual-32-01-production/post1648al-beauville-cover-projection-genus-bound.json": "dbe2bea1b2cae1e69ad6c27e5828f81494532fa4",
    "stages/stage32/residual-32-01-production/post1648am-beauville-fibration-picard-source-lock.json": "aa14d340e8b68f863d4013d34fb0eee7b306c0ee",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    for rel, expected in LOCKS.items():
        assert git_blob_sha(ROOT / rel) == expected
    cert = json.loads((NODE / "TWO-FACTOR-SAME-BEAUVILLE-COVER-WALL.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_TWO_FACTOR_SAME_BEAUVILLE_COVER_WALL_V1"
    cc = cert["cover_contract"]
    assert cc["single_resolved_cover"] is True
    assert cc["factor_directions"] == 2
    assert cert["hurwitz_replay"]["independent_r1_r2_available"] is False
    assert cert["hurwitz_replay"]["summing_two_independent_ramification_ledgers_allowed"] is False

    for g in (0, 1):
        for d in range(2, 1001):
            for n1 in range(1, d):
                n2 = d - n1
                bound = 2 * max(n1, n2) - 4 * g + 4
                assert bound >= d - 4 * g + 4

    assert cert["relation_to_retained_mb104"]["two_factor_same_cover_adds_stronger_asymptotic_slope"] is False
    assert cert["decision"]["finite_degree_window_proved"] is False
    assert cert["firewalls"]["ramification_count_duplicated"] is False
    assert cert["firewalls"]["merge_authorized"] is False
    print("MB104 two-factor same-Beauville-cover wall verifier PASS")
    print("two factor projections share one ramification count r")
    print("combined Hurwitz returns r>=d-4g+4; no independent r1+r2 gain")


if __name__ == "__main__":
    main()
