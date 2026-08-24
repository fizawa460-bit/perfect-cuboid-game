#!/usr/bin/env python3
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
src = json.loads((ROOT / "upic-v4-action-certificate.json").read_text(encoding="utf-8"))

unit_mult = src["unit_v4_rational_character_multiplicities"]
picu_mult = src["pic_u_free_v4_rational_character_multiplicities"]
if unit_mult != {
    "cc+1_ct+1": 14,
    "cc+1_ct-1": 0,
    "cc-1_ct+1": 0,
    "cc-1_ct-1": 0,
}:
    raise SystemExit(f"unit action is not trivial: {unit_mult}")
if picu_mult["cc+1_ct+1"] != 0:
    raise SystemExit(f"Pic(Ubar)_free has unexpected invariant rational line: {picu_mult}")
if src["complex"]["pic_u_torsion"] != [2, 2]:
    raise SystemExit("Pic(Ubar) torsion is not purely 2-primary")

# Exact odd-primary consequence of the truncation triangle for UPic.
# For C=UPic with H^0(C)=U_D and H^1(C)=Pic(Ubar), the long exact sequence has
#
# Pic(Ubar)^G -> H^2(Q,U_D) -> H^2(Q,C) -> H^1(Q,Pic(Ubar)).
#
# Odd-primary analysis:
# * U_D ~= Z^14 with trivial full G_Q action (the action factors through the
#   source-locked V4, and both generators act identically on U_D).
# * Pic(Ubar)_free has no V4-trivial rational summand, hence no nonzero free
#   invariant; its torsion is (Z/2)^2. Thus Pic(Ubar)^G has no odd-primary part.
# * H^1(Q,Pic(Ubar))_odd=0: on the free part inflation-restriction reduces to
#   H^1(V4,-), annihilated by 4; the torsion part is 2-primary.
# Therefore H^2(Q,UPic)_odd ~= H^2(Q,Z^14)_odd.
# Finally 0->Z->Q->Q/Z->0 and H^{>0}(Q,Q)=0 give
# H^2(Q,Z) ~= H^1(Q,Q/Z)=Hom_cont(G_Q,Q/Z).

certificate = {
    "schema": "STAGE33_03_ODD_PRIMARY_UPIC_CLOSURE_V1",
    "source_upic_action_sha256": src["canonical_sha256"],
    "unit_lattice": {
        "rank": 14,
        "full_gq_action_trivial": True,
        "reason": "action factors through pinned V4 and both V4 generators act trivially",
    },
    "pic_u": {
        "free_rank": 6,
        "free_trivial_character_multiplicity": 0,
        "torsion": [2, 2],
        "odd_primary_invariants": 0,
        "h1_odd_primary": 0,
    },
    "long_exact_sequence_odd_primary": {
        "left_source_pic_u_invariants_odd": 0,
        "right_target_h1_pic_u_odd": 0,
        "middle_isomorphism": "H^2(Q,UPic(Ubar))_odd ~= H^2(Q,Z^14)_odd",
    },
    "br_a_u_odd_primary_parametric_description": "Hom_cont(G_Q,Q/Z)_odd^14",
    "odd_primary_br0b_parametrically_complete": True,
    "odd_primary_group_finite": False,
    "odd_primary_classes_enumerated_individually": False,
    "two_primary_part_complete": False,
    "br0b_all_primary_classes_accounted": False,
    "next_exact_leaf": "L33-03-TWO-PRIMARY-UPIC-EXTENSION-AND-TRANSGRESSION",
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "odd-primary-closure.json").write_text(
    json.dumps(certificate, indent=2, sort_keys=True)+"\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "unit_rank_trivial_gq": 14,
    "pic_u_free_trivial_character_multiplicity": 0,
    "br_a_u_odd_primary": certificate["br_a_u_odd_primary_parametric_description"],
    "odd_primary_br0b_parametrically_complete": True,
    "next_exact_leaf": certificate["next_exact_leaf"],
    "certificate_sha256": certificate["canonical_sha256"],
}, indent=2, sort_keys=True))
