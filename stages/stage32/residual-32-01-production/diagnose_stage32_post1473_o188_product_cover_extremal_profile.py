#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

D = 186
E = 266
O = 188
CERT_CANONICAL = "45775c816f7e3ba46c9c0ab81ff0646d41cbc7d5d5e9a623f8f43c04ccd36923"
AUDIT_REVIEW = 5078184271
AUDITED_HEAD = "300140d4ff519965571ade06f29595f9011e3f67"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical_without(path: Path, field: str) -> tuple[dict, str]:
    obj = json.loads(path.read_text())
    body = dict(obj)
    body.pop(field, None)
    return obj, csha(body)


def profiles(qprime: int) -> list[tuple[int, int, int, int]]:
    total = qprime * D // 4
    out = []
    for n1 in range(total + 1):
        n2 = total - n1
        r1 = qprime * O - 8 * n1
        r2 = qprime * O - 8 * n2
        if r1 >= 0 and r2 >= 0:
            out.append((n1, n2, r1, r2))
    return out


def main() -> None:
    here = Path(__file__).resolve().parent
    cert_path = here / "post1473-o188-product-cover-extremal-profile.json"
    cert, actual = canonical_without(cert_path, "canonical_sha256_without_this_field")
    if actual != CERT_CANONICAL or cert.get("canonical_sha256_without_this_field") != CERT_CANONICAL:
        raise ValueError(f"certificate canonical moved: {actual}")

    promotion = cert["audit_promotion"]
    if promotion["review_id"] != AUDIT_REVIEW or promotion["audited_head"] != AUDITED_HEAD:
        raise ValueError("audit authority moved")
    if promotion["promoted_consequence"] != {"universal_O_min":188,"universal_S1_min":149,"O186_eliminated":True}:
        raise ValueError("audited promotion payload mismatch")

    q2 = profiles(2)
    if q2 != [(46,47,8,0),(47,46,0,8)]:
        raise ValueError(f"qprime=2 profile regression: {q2}")
    q4 = profiles(4)
    if q4 != [(92,94,16,0),(93,93,8,8),(94,92,0,16)]:
        raise ValueError(f"qprime=4 profile regression: {q4}")

    s1 = 149
    non_single_odd = O - s1
    minimal_mass = s1 + 3 * non_single_odd
    if (non_single_odd, minimal_mass) != (39, E):
        raise ValueError("extremal branch-mass profile regression")

    branch = cert["O188_branch_mass_profile"]["extremal_S1_149"]
    if branch["B"] != 188 or branch["multiplicity_histogram"] != {"m1":149,"m3":39,"all_other_multiplicities":0}:
        raise ValueError("certificate branch histogram mismatch")

    print("STAGE32_POST1473_O188_PRODUCT_COVER_EXTREMAL_PROFILE=PASS")
    print("AUDITED_UNIVERSAL_WALL=O>=188,S1>=149")
    print("QPRIME2_PROFILES=(46,47;8,0)|(47,46;0,8)")
    print("QPRIME4_PROFILES=(92,94;16,0)|(93,93;8,8)|(94,92;0,16)")
    print("S1_149_BRANCH_HISTOGRAM=149x1+39x3")
    print(f"CERT_CANONICAL={CERT_CANONICAL}")


if __name__ == "__main__":
    main()
