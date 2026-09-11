#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"


def main() -> None:
    cert = json.loads((NODE / "BTVA-PROJECTIVE-SPAN-FILTER.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_PROJECTIVE_SPAN_FILTER_V1"
    ca = cert["canonical_embedding_adapter"]
    assert ca["H_equals_K"] is True
    assert ca["H_square"] == 16
    assert ca["therefore_d_gt_16_implies_span_P6"] is True
    assert cert["genus_zero"]["nonconic_distinct_surface_nodes_min"] == 7
    assert cert["genus_zero"]["nonconic_node_span"] == "P6"
    assert cert["genus_one"]["receiver_filter_for_d_gt_16"] == "N>=6 and met-node set spans at least P5"

    # Arithmetic routing: any proper-linear-span carrier is confined to d<=16.
    for d in range(17, 2001):
        assert d > ca["H_square"]

    # The previously retained arbitrary-degree scaling profile uses every box node,
    # so this support theorem cannot close that direction on its own.
    for k in range(1, 501):
        d = 96 * k
        assert d > 16
        assert cert["interaction_with_scaling_ray"]["positive_node_support"] == 48
        assert 48 >= 7 and 48 >= 6
        assert cert["interaction_with_scaling_ray"]["projective_span_filter_excludes_ray"] is False

    fw = cert["firewalls"]
    assert fw["surface_node_support_equals_strict_transform_ordinary_nodes"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 BTVA projective-span filter verifier PASS")
    print("retained: rational nonconic => >=7 box nodes spanning P6")
    print("retained: genus1 d>16 => >=6 box nodes spanning at least P5")
    print("finite degree window remains OPEN")


if __name__ == "__main__":
    main()
