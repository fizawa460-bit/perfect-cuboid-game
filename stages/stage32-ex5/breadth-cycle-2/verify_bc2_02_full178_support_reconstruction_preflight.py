#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ART = HERE / "bc2-02-full178-support-reconstruction-preflight.json"
ADAPTER = ROOT / "stages" / "stage32" / "residual-32-01-production" / "adapt_stage32_post21bl_picard_witness.py"
CENSUS = ROOT / "stages" / "stage32" / "residual-32-01-production" / "build_stage32_post21bl_full178_node_mass_census.py"
BRIDGE = HERE / "bc2-01b-runtime-node-coordinate-bridge.json"


def main() -> None:
    art = json.loads(ART.read_text(encoding="utf-8"))
    adapter = ADAPTER.read_text(encoding="utf-8")
    census = CENSUS.read_text(encoding="utf-8")
    bridge = json.loads(BRIDGE.read_text(encoding="utf-8"))

    assert art["schema"] == "STAGE32EX5_BC2_02_FULL178_SUPPORT_RECONSTRUCTION_PREFLIGHT_V1"
    assert art["status"] == "BLOCKED_RETAINED_INTERFACE_MISSING_EXACT_48_SUPPORT_WITNESS"
    assert art["exact_inputs"]["exact_picard_witness_adapter"]["required_reduced_witness_rank"] == 59
    assert art["exact_inputs"]["full178_census_builder"]["full_population_row_count"] == 178

    # Exact reconstruction interface: a 59-entry reduced Picard witness is load-bearing.
    assert "EXPECTED_ANTI_RANK = 59" in adapter
    assert 'witness_r_reduced' in adapter
    assert 'len(witness) != EXPECTED_ANTI_RANK' in adapter
    assert 'Mred = M * U' in adapter
    assert 'pairings_from_reduced = y0 + Mred * r' in adapter
    assert 'EXPECTED_PAIRINGS = 140' in adapter

    # FULL178 census is a 178-row numerical census and does not retain that full witness.
    assert 'if len(all_rows) != 178 or len(set(all_rows)) != 178:' in census
    assert 'f"{row_id}|{e}|{a}|{witness[0]}|{witness[1]}|"' in census
    assert '"strong_48bit_node_support_not_inferred_from_exceptional_mass": True' in census
    assert 'witness_r_reduced' not in census

    # BC2-01B has already fixed the 48 exceptional identities; the missing object is
    # therefore the candidate-specific support/pairing witness, not node identity.
    assert bridge["counts"]["historical_exceptional_indices"] == 48
    assert bridge["counts"]["canonical_nodes"] == 48
    assert bridge["mainbatch_independent_validation"]["observed_map_rows"] == 48

    boundary = art["scope_boundary"]
    assert boundary["claim_is_repository_wide_absence_theorem"] is False
    assert boundary["affine_fiber_support_nonuniqueness_proved_here"] is False
    assert art["firewalls"]["full178_projective_span_replay_complete"] is False
    assert art["firewalls"]["merge_authorized"] is False

    print("PASS BC2-02 retained-interface blocker")
    print("full178_rows=178 reduced_picard_witness_required=59 exceptional_nodes=48")
    print("status=BLOCKED_RETAINED_INTERFACE_MISSING_EXACT_48_SUPPORT_WITNESS")


if __name__ == "__main__":
    main()
