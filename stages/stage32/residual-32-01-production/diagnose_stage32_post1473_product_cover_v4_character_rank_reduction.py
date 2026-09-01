#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

CERT_CANONICAL = "509635ab9964de7e7eecb41277b892589a7bb418676d8e76bd99b20607dac9dd"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def mm(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(2)) % 8 for j in range(2)] for i in range(2)]


def main() -> None:
    path = Path(__file__).with_name("post1473-product-cover-v4-character-rank-reduction.json")
    cert = json.loads(path.read_text())
    body = dict(cert)
    pinned = body.pop("canonical_sha256_without_this_field")
    actual = csha(body)
    if pinned != CERT_CANONICAL or actual != CERT_CANONICAL:
        raise ValueError(f"certificate canonical moved: pinned={pinned} actual={actual}")

    reps = cert["deck_group_model"]["nonidentity_mod8_representatives"]
    g1, g2, g3 = reps["g1"], reps["g2"], reps["g1_plus_g2"]
    identity = [[1, 0], [0, 1]]
    if mm(g1, g1) != identity or mm(g2, g2) != identity:
        raise ValueError("chosen mod-8 generators are not involutions")
    if mm(g1, g2) != g3 or mm(g2, g1) != g3:
        raise ValueError("chosen generators do not realize V4")

    chars = cert["deck_group_model"]["chosen_character_basis"]
    if chars["chi1"] != {"g1": 1, "g2": 0} or chars["chi2"] != {"g1": 0, "g2": 1}:
        raise ValueError("character basis moved")

    cases = cert["carrier_pullback_reduction"]["cases"]
    if cases != [{"rank": 0, "qprime": 1}, {"rank": 1, "qprime": 2}, {"rank": 2, "qprime": 4}]:
        raise ValueError("rank/qprime table moved")
    if cert["carrier_pullback_reduction"]["rational_function_representatives_required_for_the_rank_statement"] is not False:
        raise ValueError("rank reduction unexpectedly requires rational representatives")
    if cert["remaining_exact_gap"]["carrier_pullback_classes_alpha_beta_evaluated"] is not False:
        raise ValueError("unknown carrier pullback was promoted")
    if cert["verdict"]["carrier_full_V4_decided"] is not False:
        raise ValueError("dependency reduction was promoted to monodromy decision")

    print("STAGE32_POST1473_PRODUCT_COVER_V4_CHARACTER_RANK_REDUCTION=PASS")
    print("V4_GENERATORS_MOD8=PASS")
    print("QPRIME_BY_PULLBACK_CHARACTER_RANK=0:1,1:2,2:4")
    print("O186_REQUIRES_PULLBACK_CHARACTER_RANK=2")
    print(f"CERT_CANONICAL={CERT_CANONICAL}")


if __name__ == "__main__":
    main()
