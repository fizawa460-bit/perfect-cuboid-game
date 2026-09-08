#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART_PATH = ROOT / "stages/stage32-ex4/ex4-r5-kuusalo-figure9-10-branch-to-h1-label-recovery-scratch.json"
R4_PATH = ROOT / "stages/stage32-ex4/ex4-r4-kuusalo-f2-branch-action-to-cecotti-b8-algebraic-binding-preflight-scratch.json"

art = json.loads(ART_PATH.read_text())
r4 = json.loads(R4_PATH.read_text())
raw = dict(art)
expected = raw.pop("canonical_sha256_without_this_field")
canon = json.dumps(raw, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
assert hashlib.sha256(canon).hexdigest() == expected == "816f9c0574302ea99473384dd9dd9c047d48db3712fcd48f1630eb553f517ecc"
assert art["source_locks"]["r4"]["canonical_sha256"] == r4["canonical_sha256_without_this_field"]
assert art["prior_r4"]["residual_f2_branch_actions"] == 4
assert art["missing_absolute_phase"]["residual_phase_count"] == 4
assert art["missing_absolute_phase"]["literal_B8_k0_source_selected"] is False
assert art["source_exact_textual_geometry"]["labelled_walk_around_infinity"] == ["infinity", "+1", "0", "-i", "0", "-1", "0", "+i", "0", "+1", "infinity"]
assert art["canonical_h1_side_number_data"]["figure9_relations"]["1"] == "b2"
assert art["canonical_h1_side_number_data"]["figure9_relations"]["3"] == "a2"
assert len(art["missing_absolute_phase"]["text_does_not_state"]) == 3
assert art["decision"]["r4_fourfold_phase_reduced"] is False
assert art["decision"]["literal_Kuusalo_f2_equals_Cecotti_B8_proved"] is False
assert art["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert art["decision"]["absolute_Q602_residue_identified"] is False
assert art["decision"]["conditional_residue97_only"] is True
assert art["decision"]["next_exact_route"] == "EX4-R6_BREZHNEV_BURNSIDE_EXPLICIT_UNIFORMIZATION_MARKING_PREFLIGHT"
for key, value in art["firewalls"].items():
    assert value is False, key
print("Stage32EX4 R5 Kuusalo figure-label recovery boundary: PASS")
print("source geometry fixes branch strata and [infinity,+1] ray orientation")
print("Figure9 side-number absolute phase / Figure10 triangle P label remain unbound")
print("R4 four B8 conjugates survive; residue97 remains conditional")
