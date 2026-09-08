#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART_PATH = ROOT / "stages/stage32-ex4/ex4-r6-brezhnev-burnside-explicit-uniformization-marking-preflight-scratch.json"
R5_PATH = ROOT / "stages/stage32-ex4/ex4-r5-kuusalo-figure9-10-branch-to-h1-label-recovery-scratch.json"

art = json.loads(ART_PATH.read_text())
r5 = json.loads(R5_PATH.read_text())

raw = dict(art)
expected = raw.pop("canonical_sha256_without_this_field")
canon = json.dumps(raw, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
assert hashlib.sha256(canon).hexdigest() == expected == "007c80db16b644bbffc999bdeb3b4f264edfe0f7b1288face4195ae04d4a86fd"

assert art["source_locks"]["r5"]["canonical_sha256"] == r5["canonical_sha256_without_this_field"]
assert art["source_locks"]["r5"]["canonical_sha256"] == "816f9c0574302ea99473384dd9dd9c047d48db3712fcd48f1630eb553f517ecc"
assert art["prior_r5"]["residual_phase_count"] == 4
assert art["typed_adapter_test"]["algebraic_branch_labels_to_brezhnev_modular_polygon"]["provided"] is True
assert art["typed_adapter_test"]["brezhnev_polygon_to_kuusalo_figure9_side_numbering"]["provided"] is False
assert art["typed_adapter_test"]["brezhnev_triangulation_to_kuusalo_figure10_chosen_triangle_P"]["provided"] is False
assert art["typed_adapter_test"]["explicit_named_canonical_h1_cycle_assignment"]["provided"] is False
assert art["typed_adapter_test"]["kuusalo_f2_algebraic_mobius_formula"]["provided"] is False
assert art["source_nonuniqueness_and_gauge"]["Px_boundary_uniqueness"] is False
assert art["r4_phase_replay"]["candidate_k_before_r6"] == [0, 1, 2, 3]
assert art["r4_phase_replay"]["candidate_k_after_r6"] == [0, 1, 2, 3]
assert art["r4_phase_replay"]["residual_phase_count"] == 4
assert art["r4_phase_replay"]["brezhnev_independently_selects_one_k"] is False
assert art["r4_phase_replay"]["literal_B8_k0_source_selected"] is False
assert art["decision"]["source_lane_classification"] == "REQUIRES_ADAPTER_EXACT_NONPRUNING"
assert art["decision"]["r4_fourfold_phase_reduced"] is False
assert art["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert art["decision"]["absolute_Q602_residue_identified"] is False
assert art["decision"]["conditional_residue97_only"] is True
assert art["decision"]["next_exact_route"] == "EX4-R7_TRIANGLE_GROUP_REGULAR_OCTAGON_MARKING_PREFLIGHT"
for key, value in art["firewalls"].items():
    assert value is False, key

print("Stage32EX4 R6 Brezhnev explicit-uniformization marking boundary: PASS")
print("Brezhnev branch labels -> own modular polygon/triangulation: exact retained partial adapter")
print("Brezhnev polygon -> Kuusalo Figure9/10 phase: missing; four R4 k values survive")
print("residue97 remains conditional; no Q602/O210/Stage32 MAIN credit")
