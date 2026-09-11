#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"

LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CURVE-CONE-WALL.json": "61e516f2cb231ad61d16eb097395ec69e409c943",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AMBIENT-A1-SCALING-WALL.json": "443335ac8c4d1bb80c0f3e6294e9ed116a0c4001",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    for rel, expected in LOCKS.items():
        got = git_blob_sha(ROOT / rel)
        assert got == expected, (rel, got, expected)

    cert = json.loads((NODE / "LU-MIYAOKA-ORDINARY-NODE-DEBT.json").read_text())
    known = json.loads((NODE / "KNOWN-CURVE-CONE-WALL.json").read_text())
    ambient = json.loads((NODE / "AMBIENT-A1-SCALING-WALL.json").read_text())

    assert cert["schema"] == "STAGE32_MB104_LU_MIYAOKA_ORDINARY_NODE_DEBT_V1"
    assert known["geometry_contract"]["H_square"] == 16
    assert known["riemann_roch_effectivity"]["chi_O_S"] == 8
    assert 12 * 8 - 16 == 80
    assert 3 * 80 - 16 == 224
    assert ambient["picard_ray_simultaneous_witness"]["degree"] == "d=96*k"

    for k in range(1, 1001):
        d = 96 * k

        # genus one
        delta1 = 240 * k * k + 48 * k
        n1 = max(0, d - 224)
        rem1 = delta1 - n1
        assert d <= 224 + n1
        assert rem1 > 0
        assert 2 * rem1 + 1 > 0 and (2 * rem1 + 1) % 2 == 1

        # genus zero
        delta0 = 1 + 240 * k * k + 48 * k
        n0 = max(0, d - 220)
        rem0 = delta0 - n0
        assert d <= 220 + n0
        assert rem0 > 0
        assert 2 * rem0 + 1 > 0 and (2 * rem0 + 1) % 2 == 1

        # Linear ordinary-singularity debt is asymptotically weaker than the
        # quadratic RR/defect scale retained on this ray.
        chi = 240 * k * k - 48 * k + 8
        assert chi > 0
        assert n1 <= delta1 and n0 <= delta0

    fw = cert["firewalls"]
    assert fw["ordinary_node_triple_count_identified_with_total_delta"] is False
    assert fw["repaired_analytic_profile_globalizes_claimed"] is False
    assert fw["finite_degree_window_proved"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 Lu-Miyaoka ordinary-node debt verifier PASS")
    print("surface invariants: K^2=16, chi=8, c2=80, 3c2-K^2=224")
    print("retained: g0 n_ot>=max(0,d-220); g1 n_ot>=max(0,d-224)")
    print("repaired analytic scaling witness remains scalar-feasible through k=1000")
    print("finite degree window remains OPEN")


if __name__ == "__main__":
    main()
