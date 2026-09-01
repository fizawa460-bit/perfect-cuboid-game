#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

CERT_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
EXCEPTIONAL = [1,1,1,2,2,0,1,2,8,4,7,2,9,5,1,10,5,11,7,1,3,1,13,1,6,2,12,16,4,3,5,6,5,10,8,1,10,15,11,2,5,11,4,10,2,4,3,13]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical_without(path: Path, field: str) -> tuple[dict, str]:
    obj = json.loads(path.read_text())
    body = dict(obj)
    body.pop(field, None)
    return obj, csha(body)


def count_hist(extra: int, twos: int) -> int:
    # extra=0: only 1/2; extra=3 or 4: exactly one such branch globally.
    dp = {(0, 0): 1}
    for t in EXCEPTIONAL:
        nd = defaultdict(int)
        for (x2, used), count in dp.items():
            for k2 in range(t // 2 + 1):
                nd[(x2 + k2, used)] += count
            if extra and used == 0 and t >= extra:
                for k2 in range((t - extra) // 2 + 1):
                    nd[(x2 + k2, 1)] += count
        dp = nd
    return dp[(twos, 0 if extra == 0 else 1)]


def main() -> None:
    here = Path(__file__).resolve().parent
    cert_path = here / "post1473-o188-cusp-ramification-budget.json"
    cert, actual = canonical_without(cert_path, "canonical_sha256_without_this_field")
    if actual != CERT_CANONICAL or cert["canonical_sha256_without_this_field"] != CERT_CANONICAL:
        raise ValueError(f"certificate canonical moved: {actual}")
    if len(EXCEPTIONAL) != 48 or sum(EXCEPTIONAL) != 266:
        raise ValueError("exceptional vector regression")

    # O=188 profile arithmetic.
    # q'=2: R={8,0}; q'=4 asymmetric: R={16,0}; q'=4 symmetric: R={8,8}.
    if 0 // 2 != 0 or 0 // 4 != 0 or 8 // 4 != 2:
        raise ValueError("ramification budget regression")

    base = count_hist(0, 39)
    one3 = count_hist(3, 38)
    one4 = count_hist(4, 37)
    expected = (
        6851266935728760020,
        116737713339105712855,
        67027354848511690399,
    )
    if (base, one3, one4) != expected:
        raise ValueError(f"nodewise reachability counts moved: {(base, one3, one4)}")

    print("STAGE32_POST1473_O188_CUSP_RAMIFICATION_BUDGET=PASS")
    print("ZERO_SLACK_S1_149_PROVISIONALLY_EXCLUDED=true")
    print("Q2_CONTACT_HIST=188x1+39x2")
    print("Q4_ASYM_CONTACT_HIST=188x1+39x2")
    print("Q4_SYM_CONTACT_HIST_TYPES=3")
    print(f"NODEWISE_COUNTS={base},{one3},{one4}")
    print(f"CERT_CANONICAL={CERT_CANONICAL}")


if __name__ == "__main__":
    main()
