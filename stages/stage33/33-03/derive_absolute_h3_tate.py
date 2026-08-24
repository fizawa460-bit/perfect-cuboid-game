#!/usr/bin/env python3
"""Kill the absolute d2_11 target by Tate/Milne odd-degree vanishing.

For the source-locked splitting field L=Q(i,sqrt(2)), the absolute Galois
action on U_D factors through V4=Gal(L/Q).  Stage33-03 has already certified
that both V4 generators act identically on U_D, hence U_D is the trivial
absolute G_Q-lattice Z^14.

Milne, Arithmetic Duality Theorems, Chapter I, Section 4, Corollary 4.17:
for every number field K, H^r(G_K,Z)=0 for odd r.  Taking K=Q and r=3 gives
H^3(G_Q,U_D)=H^3(G_Q,Z)^14=0.  Therefore the absolute hypercohomology edge
transgression d2_11 has zero target and is identically zero.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
upic = json.loads((ROOT / "upic-v4-action-certificate.json").read_text())
picu = json.loads((ROOT / "picu-integral-action.json").read_text())
finite = json.loads((ROOT / "finite-transgression-ranks.json").read_text())
d201 = json.loads((ROOT / "d2-01-image.json").read_text())
nsplit = json.loads((ROOT / "absolute-n-restriction-split.json").read_text())

if upic["complex"]["unit_lattice_rank"] != 14:
    raise SystemExit("unit rank regression")
if upic["unit_v4_rational_character_multiplicities"] != {
    "cc+1_ct+1": 14,
    "cc+1_ct-1": 0,
    "cc-1_ct+1": 0,
    "cc-1_ct-1": 0,
}:
    raise SystemExit("unit V4 character regression")
if upic["unit_cc_matrix"] != [[1 if i == j else 0 for j in range(14)] for i in range(14)]:
    raise SystemExit("cc is not identity on U_D")
if upic["unit_ct_matrix"] != [[1 if i == j else 0 for j in range(14)] for i in range(14)]:
    raise SystemExit("ct is not identity on U_D")
if finite["rank_d2_01"] != 2 or finite["rank_d2_11"] != 2:
    raise SystemExit("finite V4 rank regression")
if not d201["finite_d2_01_image_exact"] or d201["image_f2_rank"] != 2:
    raise SystemExit("finite d2_01 image not exact")
if not nsplit["absolute_d2_11_image_restricts_to_zero_on_N"]:
    raise SystemExit("N-restriction reduction missing")
if picu["pic_u_group"] != {"free_rank": 6, "torsion": [2, 2]}:
    raise SystemExit("Pic(Ubar) shape regression")

milne = {
    "author": "J. S. Milne",
    "title": "Arithmetic Duality Theorems",
    "url": "https://jmilne.org/math/Books/ADTnot.pdf",
    "locator": "Chapter I, Section 4, Corollary 4.17",
    "statement_used": "For any number field K, H^r(G_K,Z)=0 for r odd; apply K=Q, r=3.",
}

# Because the entire geometric action factors through Gal(L/Q)=V4 and the
# certified V4 action on U_D is identity, this is an absolute, not merely
# finite-quotient, triviality statement.
cert = {
    "schema": "STAGE33_03_ABSOLUTE_H3_TATE_VANISHING_V1",
    "source_locks": {
        "upic_v4_action_sha256": upic["canonical_sha256"],
        "picu_integral_action_sha256": picu["canonical_sha256"],
        "finite_transgression_ranks_sha256": finite["canonical_sha256"],
        "d2_01_exact_image_sha256": d201["canonical_sha256"],
        "absolute_n_restriction_split_sha256": nsplit["canonical_sha256"],
        "tate_milne": milne,
    },
    "splitting_field": "Q(i,sqrt(2))",
    "absolute_unit_action_factors_through_V4": True,
    "absolute_unit_lattice": "Z^14 with trivial G_Q action",
    "H3_GQ_Z": 0,
    "H3_GQ_unit_lattice": 0,
    "absolute_d2_11_target": 0,
    "absolute_d2_11_zero": True,
    "finite_d2_11_rank_two_inflates_to_zero_absolutely": True,
    "absolute_right_filtration": "H^1(G_Q,Pic(Ubar))",
    "absolute_left_filtration": (
        "Hom_cont(G_Q,Q/Z)^14 / <the two exact visible-V4 quadratic d2_01 image classes>"
    ),
    "odd_primary_left_filtration": "Hom_cont(G_Q,Q/Z)_odd^14",
    "two_primary_left_filtration": (
        "Hom_cont(G_Q,Q/Z)[2^infinity]^14 / <kappa_a,kappa_b>, with kappa_a,kappa_b from d2-01-image.json"
    ),
    "finite_V4_right_transgression_wall_closed": True,
    "absolute_right_transgression_wall_closed": True,
    "remaining_wall": "R33-BR0B-ABSOLUTE-H1-PICU-COMPLETE-CHARACTER-INVENTORY",
    "next_exact_leaf": "L33-03-ABSOLUTE-H1-PICU-COMPLETE-CHARACTER-INVENTORY",
    "br0b_all_primary_classes_accounted": False,
    "unit_closed": False,
    "new_theorem_required": False,
    "theorem_credit": True,
    "theorem_credit_scope": "absolute H^3(G_Q,U_D)=0 and hence absolute d2_11=0 only",
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "absolute-h3-tate-vanishing.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "H3_GQ_unit_lattice": 0,
    "absolute_d2_11_zero": True,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
