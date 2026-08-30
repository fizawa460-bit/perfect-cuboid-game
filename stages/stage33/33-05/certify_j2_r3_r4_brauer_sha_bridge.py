#!/usr/bin/env python3
"""Deterministic verifier for the fresh-super-hostile-passed R3->R4 bridge."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAGE33 = ROOT.parent
CERT = ROOT / "j2-r3-r4-brauer-sha-bridge.json"
EXPECTED="3dff502b69bbee725abfe7e1f5580837410f1a8552a7b4cae31dd85c9b34bb28"

def csha(o):
    return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

r1=json.loads((ROOT/"j2-abstract-nonzero-reaudit.json").read_text())
assert r1["status"]=="PASS_ABSTRACT_J2_NONZERO_CONFIRMED_IN_GEOMETRIC_BRAUER_QUOTIENT"
assert r1["exact_conclusion"]["J2_nonzero_in_LcE_mod_im_xalpha_for_all_undetermined_b_d"] is True

r2=json.loads((ROOT/"j2-corrected-full-l-representative.json").read_text())
assert r2["canonical_sha256"]=="73ca8ecc89282369b1cd36dabc906a7f79eee1d6880b8371cb1a18a43b4c42cd"
assert r2["abstract_J2_source_locked_pair"]=="(f2,1)"
assert r2["full_quotient_zero_test"]["corrected_pair_zero"] is False

r3=json.loads((ROOT/"j2-corrected-cv-e2-cocycle.json").read_text())
assert r3["canonical_sha256"]=="8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312"
assert r3["corrected_full_L_representative"]["ell_J2_corrected"]=="(f2,1)"
assert r3["cv_lemma_4_6"]["xi_rho"]=="Tr"
assert r3["cv_lemma_4_6"]["cocycle_condition_verified"] is True

r4=json.loads((ROOT/"j2-r4-2isogeny-orientation-correction.json").read_text())
assert r4["canonical_sha256"]=="f7261a1f2d8e88fc1f1cfff31441cf3d0be01a02c4114a472c810ba37ff4cd90"
assert r4["status"]=="PASS_EXACT_R4_ATTEMPT4_2ISOGENY_ORIENTATION_PHI_COVER_CANDIDATE_BRAUER_SHA_BRIDGE_REQUIRED"
pc=r4["corrected_phi_cover_candidate"]
assert pc["jacobian"]=="E_Kc"
assert pc["kernel_exact_sequence"]=="0 -> <Tr> -> E_Kc -> Eprime_Tr -> 0"
assert pc["named_J2_torsor_credit_without_bridge"] is False

c=json.loads(CERT.read_text())
assert c["schema"]=="STAGE33_05_J2_R3_R4_BRAUER_SHA_BRIDGE_V2_FRESH_SUPER_HOSTILE_HARDENED"
assert c["status"]=="PASS_FRESH_SUPER_HOSTILE_R3_R4_BRAUER_SHA_BRIDGE_AUTHORITATIVE_NAMED_J2_TORSOR"
assert c["scope"]=="GEOMETRIC_Kgeom_Qbar_t_ONLY_NO_Q_DEFINED_DESCENT_CREDIT"
assert c["fresh_super_hostile_audit"]["verdict"]=="PASS_FRESH_SUPER_HOSTILE_MATHEMATICALLY"
assert c["fresh_super_hostile_audit"]["audited_head"]=="b569159aced79d4038399e11fde2924d0a69c52e"
assert c["fresh_super_hostile_audit"]["pre_authoritative_hardening_completed"] is True

sl=c["source_lock"]
assert sl["r1_blob_sha1"]=="792bd4d4c9c0b452e59dbcba0b3305e1195e40bf"
cv=sl["creutz_viray_curve"]
assert cv["arxiv"]=="1403.2924v1" and cv["doi"]=="10.1007/s00229-014-0721-7"
assert cv["compatibility_statement"]=="h0(gamma(ell)) = d(ell) in H^1(K,Pic C)"
surf=sl["creutz_viray_surface"]
assert surf["arxiv"]=="1306.3251" and surf["doi"]=="10.1007/s00208-014-1153-0"
assert "Br X subset Br C" in surf["surface_to_generic_location"]
assert "Theorem 2.5" in surf["generic_gamma_location"]
assert "Corollary 5.4" in surf["surface_gamma_presentation_location"]
os=sl["ogg_shafarevich"]
assert os["doi"]=="10.1093/imrn/rnae061" and "equation (4.1)" in os["location"]
assert "Tate-Shafarevich" in os["statement"]
phi=sl["standard_phi_descent"]
assert phi["cover_formula"]=="d*N^2=d^2*U^4-2*a*d*U^2*V^2+(a^2-4*b)*V^4"
assert "section 37.8" in phi["reference"]

chain=c["cv_brauer_to_wc_chain"]
assert chain["gamma_corrected_pair_nonzero_mod_constants"] is True
assert chain["h0_injective_on_BrC_mod_Br0"] is True
assert chain["proposition_5_1_compatibility"]=="h0(gamma(f2,1))=d(f2,1)"
assert chain["r3_explicit_xi"]=="xi(rho)=Tr for rho flipping sqrt(f2)"
assert chain["generic_weil_chatelet_class"]=="[xi] in H^1(K,E_Kc)"
assert chain["generic_weil_chatelet_class_nonzero"] is True
assert chain["surface_restriction_preserves_named_class"] is True

pm=c["phi_cover_match"]
assert pm["kernel_exact_sequence"]=="0 -> <Tr> -> E_Kc -> Eprime_Tr -> 0"
assert pm["squareclass"]=="d=f2" and pm["kummer_cocycle"]=="rho -> Tr"
assert pm["standard_formula_match"] is True and pm["attempt4_jacobian"]=="E_Kc"
assert pm["same_H1_E_class_as_CV_d"] is True

ex=c["exact_conclusion"]
assert ex["brauer_to_sha_bridge_materialized"] is True
assert ex["fresh_super_hostile_audit_passed"] is True
assert ex["authoritative_promotion_pending_fresh_super_hostile_audit"] is False
assert ex["generic_weil_chatelet_class_nonzero"] is True
assert ex["attempt4_phi_cover_identified_with_named_geometric_J2_torsor"] is True
assert ex["named_J2_torsor_authoritative_credit"] is True
assert ex["old_arbitrary_matching_support_shortcut_used"] is False
assert ex["one_isogeny_squareclass_alone_used_as_identity_proof"] is False
assert ex["R4_exit_4_8_12_selected"] is False and ex["candidate_minimum_norms"]==[4,8,12]

edge=json.loads((STAGE33/"33-12"/"j2-brauer-to-sha-leray-edge-interface.json").read_text())
assert edge["status"]=="RESOLVED_FRESH_SUPER_HOSTILE_PASS_NAMED_J2_TORSOR_AUTHORITATIVE"
assert edge["current_credit"]["named_J2_torsor_authoritative_credit"] is True
assert edge["current_credit"]["generic_weil_chatelet_class_nonzero"] is True

tw=json.loads((STAGE33/"33-12"/"j2-twisted-poincare-torsor-target.json").read_text())
assert tw["status"]=="SUPERSEDED_FOR_NAMED_J2_IDENTITY_BY_FRESH_SUPER_HOSTILE_PASSED_CV_BRAUER_SHA_BRIDGE"
assert tw["historical_v1"]["load_bearing_warning"]=="one rational 2-isogeny squareclass alone is not sufficient to identify the named J2 torsor"
assert tw["current_target"]["named_identity_authoritative_after_fresh_super_hostile"] is True

for k,v in c["firewalls"].items():
    if k in {"Q_defined_descent_credit_restored","endpoint_credit","marked_brauer_coordinate_selected","merge_allowed","minimum_norm_selected","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","stage33_05_reclosed","stage33_12_closed_exact","stage33_13_released","theorem_credit"}:
        assert v is False

dct=dict(c); got=dct.pop("canonical_sha256")
assert got==EXPECTED and got==csha(dct)
print(json.dumps({
    "success":True,
    "status":c["status"],
    "canonical_sha256":got,
    "generic_weil_chatelet_class_nonzero":True,
    "named_J2_torsor_authoritative_credit":True,
    "R4_exit_4_8_12_selected":False,
    "next_exact_leaf":ex["next_exact_leaf"],
},indent=2,sort_keys=True))
