#!/usr/bin/env python3
"""Verify Goal4AQ: full unit-character orthogonality is endpoint-equivalent."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4aq-unit-character-bm-endpoint-equivalence.json")
SRC = P("stages/stage35-ex/35ex-35/goal4aq-unit-character-bm-endpoint-equivalence-source-lock.md")
AP = P("stages/stage35-ex/35ex-35/goal4ap-algebraic-brauer-unit-character-infinite-layer.json")
AO = P("stages/stage35-ex/35ex-35/goal4ao-source-marked-two-class-bm-nonempty.json")
S31 = P("stages/stage35-ex/35ex-31/primitive-source-marking-endpoint-equivalence.md")
S22 = P("stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "21d865d7a15d6f9b66f87361c0ac49de9eaac89947395d04686ea747d1a7956e"
SRC_BLOB = "c104cd4c7115588a9fdb1fa52a16424833112293"
AP_CANON = "b291b617552e7280cbf0c1eb3f54eb4f69e86888cb21d2d52ba891ad4030779a"
AO_CANON = "e86b7318aa7593b99ab83bed49dbcd2bdbac05e0c828088e7c9917efd97ff858"
S31_BLOB = "01aa855c32289a467fb66759e25dc90f18df9f80"
S22_BLOB = "537ca589cd45112cca4c8f8091f5c8c77264e70d"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)

assert blob(SRC) == SRC_BLOB
assert blob(S31) == S31_BLOB
assert blob(S22) == S22_BLOB

ap = json.loads(AP.read_text())
ao = json.loads(AO.read_text())
assert ap["canonical_sha256"] == AP_CANON
assert ap["result"]["Br_a_U_infinite"] is True
assert ap["result"]["known_A_B_span_exhausts_Br_a_U"] is False
assert ao["canonical_sha256"] == AO_CANON
assert ao["source_population_adapter"]["hostile_audited"] is True

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["brauer_manin_obstruction_obtained"] is False
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

src = SRC.read_text()
for marker in (
    "Milne, *Arithmetic Duality Theorems*, second edition, Appendix A, Theorem A.3",
    "inv_v <a,chi> = chi(Art_v(a))",
    "Remark 5.7(a)",
    "Lemma 5.9",
    "C_Q ~= R_{>0} x product_p Z_p^*",
    "u(P_p)=r_u",
    "(A_src^loc)^(B_unit) != empty",
    "iff U_PC(Q)^src,+ != empty",
    "ENDPOINT_EQUIVALENT",
):
    assert marker in src, marker

# Exact reconstruction identities from one nonzero rational unit value.
def reconstruct(r: Fraction) -> tuple[Fraction, Fraction]:
    rinv = 1 / r
    edge = (r - rinv) / 2
    diag = (r + rinv) / 2
    assert diag + edge == r
    assert diag - edge == rinv
    assert diag * diag - edge * edge == 1
    return edge, diag

for r in (Fraction(2), Fraction(3, 2), Fraction(-5, 3)):
    reconstruct(r)

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4aq_source"]["blob_sha1"] == SRC_BLOB
ul = art["unit_layer"]
assert ul["visible_q_units"] == ["p+x", "q+y", "w+z"]
assert ul["visible_units_need_form_integral_basis"] is False
assert ul["character_unit_classes_available_for_every_global_finite_character"] is True
lp = art["local_pairing"]
assert lp["d2_ambiguity_loses_pairing_information"] is False
gc = art["global_cft"]
assert gc["all_character_pairings_zero_implies_global_artin_trivial"] is True
assert gc["global_artin_kernel"] == "identity connected component C_Q^0"
assert gc["C_Q_identity_component"] == "R_{>0} x {1}"
cr = art["coordinate_reconstruction"]
assert cr["q2_component_equals_reconstructed_rational_tuple"] is True
assert cr["surface_equations_descend_from_Q2_to_Q"] is True
assert cr["source_marking_descends_from_Q2"] is True
rr = art["result"]
assert rr["source_marked_unit_BM_nonempty_iff_positive_source_marked_Q_point_nonempty"] is True
assert rr["positive_source_marked_Q_point_nonempty_iff_stage35_E1_counterexample_population_nonempty"] is True
assert rr["full_unit_character_route"] == "ENDPOINT_EQUIVALENT_BLOCKER"
assert rr["finite_character_truncation_sufficient_claimed"] is False
assert rr["unit_character_BM_set_empty_claimed"] is False
assert rr["unit_character_BM_set_nonempty_claimed"] is False
assert all(v is False for v in art["credit_firewall"].values())

print("STAGE35_EX_GOAL4AQ_UNIT_CHARACTER_ENDPOINT_EQUIVALENCE=PASS")
print("full_unit_character_route=ENDPOINT_EQUIVALENT_BLOCKER")
print("unit_BM_nonempty_iff_source_marked_Q_point_nonempty=true")
print("finite_character_truncation_sufficient_claimed=false")
print("canonical_sha256=" + EXPECTED)
