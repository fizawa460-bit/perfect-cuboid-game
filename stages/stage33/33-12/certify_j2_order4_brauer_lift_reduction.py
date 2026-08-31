#!/usr/bin/env python3
"""Reduce the corrected J2 proper-Br2 adapter to the transported order-4 lift.

The previous exact source transported only the doubled order-2 class u1=t1/2.
The marked J2 functional is beta1=t1/8 mod T*, so its lift-sensitive datum is
the order-4 discriminant generator t1/4.  This producer derives its semantic
BigK support, proves why four half-coefficient rows disappeared after doubling,
and fixes the next numeric replay and parity gate without guessing a proper-Br2
coordinate.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
ORIENTATION = HERE / "j2-cv-d2-semantic-orientation.json"
SEMANTIC = HERE / "j2-semantic-kc-picard-basis.json"
U1_SOURCE = HERE / "j2-semantic-u1-full-surface-smith-source.json"
BLOCKER = HERE / "j2-semantic-u1-at2-to-proper-br2-dual-adapter-blocker.json"
PROPER = S33 / "33-07" / "proper-brauer2-from-discriminant.json"
OUT = HERE / "j2-order4-brauer-lift-reduction.json"

LOCKS = {
    ORIENTATION: "0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e",
    SEMANTIC: "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0",
    U1_SOURCE: "ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec",
    BLOCKER: "f5d1336e21dd5563ec6466811b5e1c3cacc6def17e4dbe4968023d9bd3756399",
    PROPER: "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
}


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == LOCKS[path] == csha(body), path
    return obj


orientation = locked(ORIENTATION)
semantic = locked(SEMANTIC)
u1_source = locked(U1_SOURCE)
blocker = locked(BLOCKER)
proper = locked(PROPER)

adapter = orientation["explicit_marked_adapter"]
assert adapter["brauer_functional_f2"] == [1, 0]
assert adapter["T_mod_2T_coordinate_f2"] == [1, 0]
assert adapter["A_T_2torsion_representative"] == "t1/2 mod T"
assert orientation["kernel_fingerprint_identification"]["T_Kc_gram"] == [[4, 0], [0, 8]]
assert orientation["kernel_fingerprint_identification"]["marked_brauer_basis"][0] == "beta1=t1/8"
assert orientation["anti_isometry_check"]["generator"] == "t1/4"
assert orientation["anti_isometry_check"]["doubled_generator"] == "t1/2"
assert proper["equivariant_identification"] == "T/2T ~= A_T[2] via x mod 2T -> x/2 mod T"
assert blocker["exact_shortcut_rejection"]["finite_discriminant_pairing_covector_on_semantic_u1_f2"] == [0] * 14

# On Kc, beta1=t1/8 evaluates with bit 2*(beta1,y)=(t1,y)/4 mod 2.
gram = orientation["kernel_fingerprint_identification"]["T_Kc_gram"]
kc_beta1_evaluations = [(gram[0][j] // 4) & 1 for j in range(2)]
assert kc_beta1_evaluations == [1, 0]

frac_coords = orientation["anti_isometry_check"]["generator_image_semantic_fractional_coordinates"]
assert len(frac_coords) == 20
coeff4 = [int(Fraction(x) * 4) for x in frac_coords]
assert coeff4 == [1,3,0,0,3,1,2,0,0,2,2,0,0,3,3,0,0,0,2,0]

indlist = semantic["upstream_source_lock"]["indlistK_1based"]
assert len(indlist) == 20
order4_terms = [[indlist[i], coeff4[i]] for i in range(20) if coeff4[i] % 4]
order4_rows = [x[0] for x in order4_terms]
assert order4_rows == [2,4,9,10,20,35,39,47,49,67]

# Doubling c/4 modulo Z keeps exactly the odd c coefficients.  These are the
# six rows used by the previous u1=t1/2 replay; the four c=2 rows are exactly
# the information destroyed by doubling.
doubled_rows = [indlist[i] for i,c in enumerate(coeff4) if c & 1]
assert doubled_rows == [2,4,9,10,47,49]
assert doubled_rows == u1_source["semantic_u1_pullback"]["BigK_support_1based"]
extra_rows = [r for r in order4_rows if r not in doubled_rows]
assert extra_rows == [20,35,39,67]

out = {
    "schema": "STAGE33_12_J2_ORDER4_BRAUER_LIFT_REDUCTION_V1",
    "stage": "33-12",
    "status": "PASS_EXACT_ORDER4_LIFT_ROUTE_REDUCED_TO_FOUR_ADDITIONAL_ROWS",
    "source_locks": {
        "semantic_orientation_sha256": LOCKS[ORIENTATION],
        "semantic_picard_basis_sha256": LOCKS[SEMANTIC],
        "semantic_u1_full_surface_smith_source_sha256": LOCKS[U1_SOURCE],
        "proper_dual_adapter_blocker_sha256": LOCKS[BLOCKER],
        "proper_brauer2_sha256": LOCKS[PROPER],
    },
    "marked_kc_normalization": {
        "T_Kc_gram": gram,
        "named_functional": "beta1=t1/8 mod T*",
        "named_functional_coordinate_f2": [1, 0],
        "binary_evaluation_formula": "beta1(y) = (t1,y)/4 mod 2",
        "binary_evaluations_on_marked_T_basis_f2": kc_beta1_evaluations,
        "order4_dual_generator": "t1/4",
        "doubled_order2_generator": "t1/2",
    },
    "semantic_order4_generator": {
        "fractional_coordinates": frac_coords,
        "fourfold_integer_coefficients": coeff4,
        "BigK_terms_row_and_coefficient_mod4": order4_terms,
        "required_BigK_rows_1based": order4_rows,
        "doubling_retains_only_BigK_rows_1based": doubled_rows,
        "additional_rows_invisible_in_u1_order2_replay_1based": extra_rows,
        "exact_explanation": "The four additional rows have coefficient 2/4=1/2 in t1/4, hence double to an integer and disappear modulo PicK when passing to t1/2.",
    },
    "candidate_full_surface_brauer_lift_normalization": {
        "integer_order4_numerator": "n4 = sum(c_j * MatKtoS[BigK_j]) for the ten listed (row,c_j) terms",
        "dual_pairing_vector": "z4 = (n4 * pmPic) / 4; require z4 integral",
        "smith_pairing_vector": "y4 = z4 * V in the retained Magma Smith convention",
        "candidate_proper_Br2_14D_coordinate": "reduce the 14 nontrivial Smith entries of y4 modulo 2",
        "reason_for_parity_gate": "If w is the transported dual-lattice lift represented by t1/4, then J2=w/2 mod T* and its bit on a T-basis vector tau is 2*(w/2,tau)=(w,tau) mod 2.",
        "mandatory_acceptance_checks": [
            "doubling/order2 reduction reproduces the locked full-surface u1 A_T[2] coordinate",
            "candidate proper14 vector is fixed by both current proper-Br2 cc and ct actions",
            "candidate proper14 vector lies in the locked retained 10D invariant domain",
            "no proper14 coordinate is promoted if any lift/integrality/invariance check fails",
        ],
    },
    "next_numeric_leaf": {
        "materialize_additional_BigK_pullback_rows_1based": extra_rows,
        "reuse_already_materialized_BigK_rows_1based": doubled_rows,
        "required_compact_output": [
            "four additional fullPic64 pullback rows",
            "integral z4",
            "14 nontrivial y4 entries modulo 8",
            "candidate proper-Br2 parity vector and cc/ct invariance result",
        ],
        "full_sign_action_search_required": False,
        "repo_wide_source_search_required": False,
    },
    "promotion_firewall": {
        "proper_Br2_14D_coordinate_materialized": False,
        "retained_10D_coordinate_materialized": False,
        "first_75D_matrix_column_materialized": False,
        "finite_v4_kummer_columns_materialized": 0,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "Q_defined_descent_credit_restored": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    },
}
out["canonical_sha256"] = csha(out)
OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "additional_rows": extra_rows,
    "required_order4_rows": order4_rows,
    "canonical_sha256": out["canonical_sha256"],
}, sort_keys=True))
