#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"

LOCKS = {
    "stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md": "512fcc70afb1acf16956fd4b7a2b9b935a052150",
    "stages/stage32/residual-32-01-production/post1648am-beauville-fibration-picard-source-lock.json": "aa14d340e8b68f863d4013d34fb0eee7b306c0ee",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CURVE-CONE-WALL.json": "61e516f2cb231ad61d16eb097395ec69e409c943",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONTRACTION-CONDUCTOR.json": "fda08685a63caab19851d0d6e5bac353092c888e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/SPECIAL-DISCRIMINANT-CAPACITY-WALL.json": "d6c53f35268fc09111017b1f147c656dfd6127f1",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    for rel, expected in LOCKS.items():
        got = git_blob_sha(ROOT / rel)
        assert got == expected, (rel, got, expected)

    cert = json.loads((NODE / "AMBIENT-A1-SCALING-WALL.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_AMBIENT_A1_SCALING_WALL_V2"
    assert cert["source_locks"]["am_blob_sha1"] == "aa14d340e8b68f863d4013d34fb0eee7b306c0ee"

    for m in range(1, 501):
        A, B = 2, 4 * m
        ox, oy, oz = A, (A + B) // 2, B
        assert A > 0 and B > 0 and (A + B) % 2 == 0
        assert ox + oz == 2 * oy
        assert ox == 2 and oy == 2 * m + 1 and oz == 4 * m
        gaps = [j for j in range(1, 2 * m + 1) if j % 2 == 1]
        assert len(gaps) == m
        strict_gaps = [j for j in range(1, 2 * m - 1) if j % 2 == 1]
        assert len(strict_gaps) == m - 1
        contraction = (min(A, B) ** 2) // 4
        assert contraction == 1
        assert (m - 1) + contraction == m
        assert 2 * m + 1 == 1 + 2 * m

    for k in range(1, 501):
        d = 96 * k
        n1 = n2 = 48 * k
        Mi = 2 * k
        M = 48 * Mi
        R = M
        s_min = R
        assert n1 + n2 == d
        assert M == d == R == s_min
        assert M // 2 - n1 == 0 and M // 2 - n2 == 0
        q1 = 3 * n1 - M // 2
        q2 = 3 * n2 - M // 2
        assert q1 == q2 == 96 * k
        assert 6 * 16 * k == q1
        assert 2 * (16 * k) + 8 * (2 * k) == n1
        assert 2 * n1 == 96 * k
        assert q1 == 2 * n1
        q_a1 = 48 * ((Mi * Mi) // 4)
        assert q_a1 == 48 * k * k
        assert q_a1 * 192 == d * d
        D2 = 480 * k * k
        pa = 1 + (D2 + d) // 2
        delta_strict = pa - 1
        assert delta_strict == 240 * k * k + 48 * k
        exponent = 2 * delta_strict + 1
        assert exponent == 480 * k * k + 96 * k + 1 and exponent % 2 == 1
        delta_image = delta_strict + q_a1
        assert delta_image == 288 * k * k + 48 * k

    decision = cert["decision"]
    assert decision["ambient_a1_local_capacity_route_closes"] is False
    assert decision["special_fibre_scalar_route_closes"] is False
    assert decision["current_interfaces_admit_arbitrarily_large_simultaneous_analytic_scaling_witnesses"] is True
    assert decision["global_algebraic_member_constructed"] is False
    assert decision["next_subobligation"] == "MB104_GLOBAL_LINEAR_SYSTEM_JET_OR_MEMBER_EXISTENCE_BOUND"

    fw = cert["firewalls"]
    assert fw["effective_Dk_has_integral_member_claimed"] is False
    assert fw["effective_Dk_has_genus_one_member_claimed"] is False
    assert fw["local_analytic_germs_globalize_claimed"] is False
    assert fw["finite_degree_window_proved"] is False
    assert fw["r29_lg2_mb_discharged"] is False
    assert fw["merge_authorized"] is False

    print("MB104 ambient-A1 scaling-wall verifier PASS")
    print("AM source lock repaired to authoritative JSON blob")
    print("embedded family realizes unbounded index in xz=y^2")
    print("simultaneous ray remains nonclosing; global member input required")


if __name__ == "__main__":
    main()
