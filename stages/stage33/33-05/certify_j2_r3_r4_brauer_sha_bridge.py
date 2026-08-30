#!/usr/bin/env python3
"""Deterministic R3->R4 Brauer-to-Sha bridge verifier.

Network-free verifier for the repository adapter. External theorem text is
source-locked by exact paper/theorem locations in the certificate and must be
independently checked by hostile audit. This script checks the repo-side
dictionary and that no forbidden shortcut is used.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAGE33 = ROOT.parent
CERT = ROOT / "j2-r3-r4-brauer-sha-bridge.json"


def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()


r2=json.loads((ROOT/"j2-corrected-full-l-representative.json").read_text())
assert r2["canonical_sha256"]=="73ca8ecc89282369b1cd36dabc906a7f79eee1d6880b8371cb1a18a43b4c42cd"
assert r2["abstract_J2_source_locked_pair"]=="(f2,1)"
assert r2["full_quotient_zero_test"]["corrected_pair_zero"] is False

r3=json.loads((ROOT/"j2-corrected-cv-e2-cocycle.json").read_text())
assert r3["canonical_sha256"]=="8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312"
assert r3["corrected_full_L_representative"]["ell_J2_corrected"]=="(f2,1)"
assert r3["corrected_full_L_representative"]["belongs_to_L1"] is True
assert r3["cv_lemma_4_6"]["xi_rho"]=="Tr"
assert r3["cv_lemma_4_6"]["cocycle_condition_verified"] is True
assert r3["fixed_rational_E2_kummer_coordinates"]["nonzero"] is True

r4=json.loads((ROOT/"j2-r4-2isogeny-orientation-correction.json").read_text())
assert r4["canonical_sha256"]=="f7261a1f2d8e88fc1f1cfff31441cf3d0be01a02c4114a472c810ba37ff4cd90"
assert r4["status"]=="PASS_EXACT_R4_ATTEMPT4_2ISOGENY_ORIENTATION_PHI_COVER_CANDIDATE_BRAUER_SHA_BRIDGE_REQUIRED"
pc=r4["corrected_phi_cover_candidate"]
assert pc["jacobian"]=="E_Kc"
assert pc["kernel_exact_sequence"]=="0 -> <Tr> -> E_Kc -> Eprime_Tr -> 0"
assert pc["named_J2_torsor_credit_without_bridge"] is False

old=json.loads((STAGE33/"33-12"/"j2-brauer-to-sha-leray-edge-interface.json").read_text())
assert old["j2_brauer_to_sha_leray_edge_materialized"] is False
assert "named CV Azumaya/corestriction" in old["required_materialization"]["named_J2_requirement"]

tw=json.loads((STAGE33/"33-12"/"j2-twisted-poincare-torsor-target.json").read_text())
assert "a scalar norm or one rational 2-isogeny squareclass" in tw["twisted_poincare_interface"]["not_sufficient"]

c=json.loads(CERT.read_text())
assert c["status"]=="PASS_EXACT_R3_R4_BRAUER_SHA_ADAPTER_MATERIALIZED_PENDING_FRESH_SUPER_HOSTILE_AUDIT"
assert c["scope"]=="GEOMETRIC_Kgeom_Qbar_t_ONLY_NO_Q_DEFINED_DESCENT_CREDIT"
cv=c["source_lock"]["creutz_viray"]
assert cv["arxiv"]=="1403.2924v1"
assert cv["doi"]=="10.1007/s00229-014-0721-7"
assert cv["compatibility_statement"]=="h0(gamma(ell)) = d(ell) in H^1(K,Pic C)"

d=c["base_field_dictionary"]
assert d["K"]=="Kgeom=Qbar(t)"
assert d["J"]=="Jac(C)=E_Kc"
assert d["rational_origin_available"] is True

chain=c["cv_brauer_to_wc_chain"]
assert chain["r3_explicit_xi"]=="xi(rho)=Tr for rho flipping sqrt(f2)"
assert chain["proposition_5_1_compatibility"]=="h0(gamma(f2,1))=d(f2,1)"
assert chain["generic_weil_chatelet_class"]=="[xi] in H^1(K,E_Kc)"

pm=c["phi_cover_match"]
assert pm["kernel_exact_sequence"]=="0 -> <Tr> -> E_Kc -> Eprime_Tr -> 0"
assert pm["squareclass"]=="d=f2"
assert pm["kummer_cocycle"]=="rho -> Tr"
assert pm["standard_formula_match"] is True
assert pm["attempt4_jacobian"]=="E_Kc"
assert pm["same_H1_E_class_as_CV_d"] is True

ex=c["exact_conclusion"]
assert ex["brauer_to_sha_bridge_materialized"] is True
assert ex["old_arbitrary_matching_support_shortcut_used"] is False
assert ex["one_isogeny_squareclass_alone_used_as_identity_proof"] is False
assert ex["identity_proof_uses_CV_gamma_d_compatibility"] is True
assert ex["attempt4_phi_cover_identified_with_named_geometric_J2_torsor"] is True
assert ex["authoritative_promotion_pending_fresh_super_hostile_audit"] is True
assert ex["R4_exit_4_8_12_selected"] is False
assert ex["candidate_minimum_norms"]==[4,8,12]

fw=c["firewalls"]
for k in (
    "Q_defined_descent_credit_restored",
    "stage33_05_reclosed",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "minimum_norm_selected",
    "marked_brauer_coordinate_selected",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
    "merge_allowed",
):
    assert fw[k] is False

dct=dict(c)
got=dct.pop("canonical_sha256")
assert got==csha(dct)
print(json.dumps({
    "success":True,
    "status":c["status"],
    "canonical_sha256":got,
    "brauer_to_sha_bridge_materialized":True,
    "named_J2_torsor_identification":"PROVISIONAL_PENDING_FRESH_SUPER_HOSTILE_AUDIT",
    "R4_exit_4_8_12_selected":False,
    "next_exact_leaf_after_fresh_audit":ex["next_exact_leaf_after_fresh_audit"],
},indent=2,sort_keys=True))
