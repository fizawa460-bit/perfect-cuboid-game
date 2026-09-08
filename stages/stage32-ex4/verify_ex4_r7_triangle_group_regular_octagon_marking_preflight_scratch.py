#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ART_PATH=ROOT/"stages/stage32-ex4/ex4-r7-triangle-group-regular-octagon-marking-preflight-scratch.json"
R6_PATH=ROOT/"stages/stage32-ex4/ex4-r6-brezhnev-burnside-explicit-uniformization-marking-preflight-scratch.json"

art=json.loads(ART_PATH.read_text())
r6=json.loads(R6_PATH.read_text())

raw=dict(art)
expected=raw.pop("canonical_sha256_without_this_field")
canon=json.dumps(raw,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
assert hashlib.sha256(canon).hexdigest()==expected=="89a8f229461877f8030577962e61218610c62afdde99c3912fabfd779f058f96"
assert art["source_locks"]["r6"]["canonical_sha256"]==r6["canonical_sha256_without_this_field"]
assert art["prior_r6"]["residual_phase_count"]==4
assert art["source_exact_data"]["curve"]=="w^2=z^5-z"
assert art["source_exact_data"]["triangle_group_choice"]["conjugate_subgroup_count"]==3
assert art["source_exact_data"]["triangle_group_choice"]["relations"]==["U^2=I","T^4=I","S^8=I","STU=I"]
assert art["source_exact_data"]["genus2_surface_group_diagonal_pairing_words"]=={
    "f1":"S^4*T^2","f2":"S*T^2*S^3","f3":"S^-2*T^2*S^6","f4":"S^3*T^2*S"
}
assert art["typed_adapter_test"]["triangle_group_to_regular_octagon_geometry"]["provided"] is True
for key in [
    "triangle_group_S_fixed_point_to_algebraic_branch_label",
    "triangle_group_T_fixed_point_to_algebraic_branch_label",
    "surface_group_f1_f4_to_kuusalo_canonical_h1",
    "triangle_group_to_kuusalo_figure9_side_numbering",
    "triangle_group_order3_center_to_kuusalo_figure10_P",
]:
    assert art["typed_adapter_test"][key]["provided"] is False,key
assert art["r4_phase_replay"]["candidate_k_before_r7"]==[0,1,2,3]
assert art["r4_phase_replay"]["candidate_k_after_r7"]==[0,1,2,3]
assert art["r4_phase_replay"]["residual_phase_count"]==4
assert art["r4_phase_replay"]["hknr_independently_selects_one_k"] is False
assert art["decision"]["r4_fourfold_phase_reduced"] is False
assert art["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert art["decision"]["absolute_Q602_residue_identified"] is False
assert art["decision"]["conditional_residue97_only"] is True
assert art["decision"]["next_exact_route"]=="EX4-R8_COOK_JENNI_BRANCH_LABELLED_OCTAGON_TO_ORDER3_TRIANGLE_MARKING_PREFLIGHT"
for key,value in art["firewalls"].items():
    assert value is False,key

print("Stage32EX4 R7 triangle-group regular-octagon marking boundary: PASS")
print("exact (2,4,8)/(2,3,8) group geometry and surface-group words retained")
print("algebraic Weierstrass labels / Kuusalo Figure9-10 phase remain unbound")
print("four R4 conjugates survive; residue97 remains conditional")
