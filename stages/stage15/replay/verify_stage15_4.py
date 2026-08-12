#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stage15_4_normal_form import (  # noqa: E402
    normal_form,
    norm_factors,
    prime_factors,
    recover_toric_params,
    toric_raw,
)


def test_survivors() -> None:
    cases = [
        ((104, 153, 672, 185, 680), (13, 4, 13, 1), 17, 697),
        ((117, 520, 756, 533, 765), (9, 1, 13, 1), 10, 925),
        ((840, 448, 495, 952, 975), (5, 3, 7, 4), 1, 1073),
        ((448, 264, 975, 520, 1073), (7, 4, 32, 7), 65, 1105),
        ((495, 264, 952, 561, 1073), (5, 3, 45, 11), 34, 1105),
    ]
    for physical, params, expected_k, expected_d in cases:
        assert recover_toric_params(*physical) == params
        rec = normal_form(*params)
        assert tuple(rec["physical"]) == physical
        assert rec["space_integral"] is True
        assert rec["AB_square"] is True
        assert rec["sf_A"] == rec["sf_B"] == expected_k
        assert rec["k"] == expected_k
        assert rec["physical_d"] == expected_d
        for p in prime_factors(expected_k):
            assert p == 2 or p % 4 == 1


def test_nonsurvivors() -> None:
    cases = [
        ((12, 5, 9, 13, 15), (3, 2, 2, 1), 10, 1),
        ((12, 5, 16, 13, 20), (3, 2, 3, 1), 85, 5),
        ((12, 5, 35, 13, 37), (3, 2, 6, 1), 82, 17),
    ]
    for physical, params, sf_a, sf_b in cases:
        assert recover_toric_params(*physical) == params
        rec = normal_form(*params)
        assert tuple(rec["physical"]) == physical
        assert rec["space_integral"] is False
        assert rec["AB_square"] is False
        assert (rec["sf_A"], rec["sf_B"]) == (sf_a, sf_b)
        assert rec["k"] is None


def test_exact_algebra() -> None:
    samples = [(3, 2, 2, 1), (13, 4, 13, 1), (7, 4, 32, 7), (5, 3, 45, 11)]
    for m, n, r, s in samples:
        e, x, y, _, _ = toric_raw(m, n, r, s)
        a, b = norm_factors(m, n, r, s)
        assert e * e + x * x + y * y == 4 * a * b
        assert a + b == (m * m + n * n) * (r * r + s * s)
        assert a - b == (m * m - n * n) * (r * r - s * s)


def test_frozen_readiness() -> None:
    evidence = json.loads((ROOT / "evidence" / "stage15_4_normal_form.json").read_text(encoding="utf-8"))
    readiness = evidence["readiness"]
    assert readiness["STAGE15_4_NORMAL_FORM_FIXED"] is True
    assert readiness["STAGE15_5_READY_WITH_ARSENAL"] is True
    assert readiness["STAGE15_5_DIRECT_SAVING_WEAPON_IDENTIFIED"] is False
    assert readiness["STAGE15_5_SURVIVAL_PROOF_STARTED"] is False
    assert readiness["STAGE15_4_AUTOCONTINUE_TO_5"] is False
    arsenal = evidence["arsenal_trigger_map"]
    assert arsenal["AR-017"] == "TRIGGERED_ADAPTER_REQUIRED"
    assert arsenal["AR-009"] == "TRIGGERED_ADAPTER_REQUIRED"
    assert arsenal["AR-012"] == "NOT_TRIGGERED"
    assert arsenal["AR-014"] == "WATCH_AFTER_CORE_DECOMPOSITION"


def main() -> None:
    test_survivors()
    test_nonsurvivors()
    test_exact_algebra()
    test_frozen_readiness()
    print("STAGE15_4_VERIFY=PASS")
    print("MINIMAL_NORMAL_FORM=sf(N(mr+i*ns))=sf(N(ms+i*nr))")
    print("PRIMARY_ARSENAL_CANDIDATES=AR-017,AR-009,AR-018")
    print("STAGE15_5_READY_WITH_ARSENAL=true")
    print("STAGE15_5_SURVIVAL_PROOF_STARTED=false")


if __name__ == "__main__":
    main()
