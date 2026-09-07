#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-05b-inertia-parity-stabilizer.json"


def canonical_sha256_without_field(data):
    body = dict(data)
    expected = body.pop("canonical_sha256_without_this_field")
    payload = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    got = hashlib.sha256(payload).hexdigest()
    assert got == expected, (got, expected)


def main():
    d = json.loads(ART.read_text())
    canonical_sha256_without_field(d)

    m = d["target"]["exceptional_pairings"]
    assert len(m) == 48
    assert sum(m) == 266
    assert sum(x > 0 for x in m) == 47

    odd_labels = [i + 1 for i, x in enumerate(m) if x % 2 == 1]
    even_pos_labels = [i + 1 for i, x in enumerate(m) if x > 0 and x % 2 == 0]
    gp = d["global_parity_consequences"]
    assert odd_labels == gp["odd_pairing_labels_1based"]
    assert even_pos_labels == gp["even_positive_pairing_labels_1based"]
    assert len(odd_labels) == 26
    assert sum(m[i - 1] for i in odd_labels) == 140
    assert len(even_pos_labels) == 21
    assert sum(m[i - 1] for i in even_pos_labels) == 126

    # Q >= 186 and the odd-contact nodes can contribute at most 140.
    even_needed = 186 - 140
    assert even_needed == 46
    even_caps = sorted((x for x in m if x > 0 and x % 2 == 0), reverse=True)
    assert sum(even_caps[:3]) == 38 < even_needed
    assert sum(even_caps[:4]) == 48 >= even_needed
    assert gp["even_pairing_ramified_node_count_lower_bound"] == 4
    assert gp["ramified_surface_node_count_lower_bound"] == 30

    # Baseline q_i=m_i mod 2 has total 26. Extra odd-contact capacity at a
    # nonunit node is m_i-(m_i mod 2).
    extra_needed = 186 - 26
    assert extra_needed == 160
    extra_caps = sorted((x - (x % 2) for x in m if x >= 2), reverse=True)
    assert sum(extra_caps[:14]) == 152 < extra_needed
    assert sum(extra_caps[:15]) == 160 >= extra_needed
    assert gp["multibranch_node_count_lower_bound"] == 15

    # Slack replay: Q=186+2s, contact half-excess=40-s.
    for s in range(41):
        Q = 186 + 2 * s
        H = (266 - Q) // 2
        assert Q % 2 == 0
        assert 186 <= Q <= 266
        assert H == 40 - s
        assert Q - H == 146 + 3 * s

    # Stabilizer parity and the h=2/h=4 extremal arithmetic.
    # 8(alpha+beta)=372h => 2(alpha+beta)=93h, hence h even.
    admissible_h = []
    for h in (1, 2, 4):
        rhs = 93 * h
        if rhs % 2 == 0:
            admissible_h.append(h)
    assert admissible_h == [2, 4]

    # h=2: alpha+beta=93, so max>=47 and Q>=4*47=188.
    assert (93 + 1) // 2 == 47
    assert 4 * 47 == 188
    # h=4: alpha+beta=186, so max>=93 and Q>=2*93=186.
    assert (186 + 1) // 2 == 93
    assert 2 * 93 == 186

    # Three single-sign inertia types, 16 nodes each.
    gi = d["G0_inertia_structure"]
    assert gi["single_sign_fixed_points_each"] == 8
    assert gi["nodes_per_inertia_type"] == 16
    assert len(gi["node_inertia_types"]) == 3
    assert 3 * 16 == 48

    assert d["exit"]["all_residual_configurations_disposed"] is False
    assert d["exit"]["full_target_closure"] is False
    assert d["firewalls"]["h2_excluded_without_EXC_inertia_adapter"] is False
    print("PASS EX1-05B inertia parity/stabilizer replay")


if __name__ == "__main__":
    main()
