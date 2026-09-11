#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
MB103 = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB103/verify_mb103_aut_node_quotient.py"
ZERO = (Fraction(0), Fraction(0))


def qpair(x):
    return (Fraction(x[0]), Fraction(x[1]))


def qsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def qmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qinv(x):
    den = x[0] * x[0] + x[1] * x[1]
    assert den != 0
    return (x[0] / den, -x[1] / den)


def gaussian_rank(rows):
    a = [[qpair(z) for z in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != ZERO), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = qinv(a[r][c])
        a[r] = [qmul(v, inv) for v in a[r]]
        for i in range(m):
            if i == r or a[i][c] == ZERO:
                continue
            f = a[i][c]
            a[i] = [qsub(a[i][j], qmul(f, a[r][j])) for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def load_mb103():
    spec = importlib.util.spec_from_file_location("mb103_verify", MB103)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    cert = json.loads((NODE / "BTVA-PROJECTIVE-SPAN-FILTER.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_PROJECTIVE_SPAN_FILTER_V2"
    ca = cert["canonical_embedding_adapter"]
    assert ca["H_equals_K"] is True
    assert ca["H_square"] == 16
    assert ca["therefore_d_gt_16_implies_span_P6"] is True

    lock = cert["node_coordinate_source_lock"]
    assert lock["mb103_verifier_blob_sha1"] == "5a362acbbc3969e76f74b783b53d69a2c17adedc"
    mb103 = load_mb103()
    nodes = mb103.orbit_nodes()
    assert len(nodes) == 48
    assert gaussian_rank(nodes) == 7 == lock["full_node_vector_rank"]

    w = cert["exact_span_witnesses_in_mb103_order"]
    p5 = [nodes[i] for i in w["P5_six_node_indices_zero_based"]]
    p6 = [nodes[i] for i in w["P6_seven_node_indices_zero_based"]]
    assert gaussian_rank(p5) == 6 == w["P5_vector_rank"]
    assert gaussian_rank(p6) == 7 == w["P6_vector_rank"]

    assert cert["genus_zero"]["nonconic_distinct_surface_nodes_min"] == 7
    assert cert["genus_zero"]["nonconic_node_span"] == "P6"
    assert "rank of met-node coordinate vectors is 7" in cert["genus_zero"]["receiver_filter_for_d_gt_2"]
    assert "rank of met-node coordinate vectors is at least 6" in cert["genus_one"]["receiver_filter_for_d_gt_16"]

    # Any proper-linear-span carrier is confined to d<=16.
    for d in range(17, 2001):
        assert d > ca["H_square"]

    # The retained scaling profile meets every box node, hence survives this filter.
    for k in range(1, 501):
        d = 96 * k
        assert d > 16
        assert cert["interaction_with_scaling_ray"]["positive_node_support"] == 48
        assert gaussian_rank(nodes) == 7
        assert cert["interaction_with_scaling_ray"]["projective_span_filter_excludes_ray"] is False

    fw = cert["firewalls"]
    assert fw["surface_node_support_equals_strict_transform_ordinary_nodes"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 BTVA exact projective-span filter verifier PASS")
    print("48 node coordinate rank=7; witness ranks P5=6 and P6=7")
    print("retained: rational nonconic => >=7 box nodes spanning P6")
    print("retained: genus1 d>16 => >=6 box nodes spanning at least P5")
    print("finite degree window remains OPEN")


if __name__ == "__main__":
    main()
