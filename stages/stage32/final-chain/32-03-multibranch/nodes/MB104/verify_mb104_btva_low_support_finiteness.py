#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"


def main() -> None:
    cert = json.loads((NODE / "BTVA-LOW-SUPPORT-FINITENESS.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_LOW_SUPPORT_FINITENESS_V1"
    c = cert["contract"]
    assert c["surface_node_count"] == 48
    assert c["removed_exceptional_count_r"] == 35
    assert c["node_support_threshold"] == 13
    assert 48 - 13 == 35
    assert c["geometric_genera"] == [0, 1]
    assert c["curves_with_N_le_13_finite"] is True
    assert c["applies_to_multibranch_receiver"] is True
    assert c["abstract_absolute_degree_max_exists"] is True
    assert c["explicit_degree_max_computed"] is False
    assert c["unbounded_distinct_low_genus_sequence_eventually_requires_N_ge_14"] is True

    d = cert["decision"]
    assert d["low_support_subpopulation_abstractly_finite"] is True
    assert d["finite_picard_enumeration_released_for_low_support"] is False
    assert d["remaining_unbounded_route_must_lie_in_N_ge_14"] is True
    assert d["finite_degree_window_proved_population_wide"] is False

    fw = cert["firewalls"]
    assert fw["surface_node_support_equals_ordinary_self_nodes"] is False
    assert fw["abstract_finiteness_equals_effective_degree_cutoff"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 BTVA low-support finiteness verifier PASS")
    print("retained: genus 0/1 curves with N<=13 form a finite set")
    print("non-effective: no numerical D_13; unbounded route must lie in N>=14")


if __name__ == "__main__":
    main()
