#!/usr/bin/env python3
"""Idempotently write the Stage33-12 MAIN checkpoint after J2 marked-PicK extraction."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
CERT=HERE/"j2-stoll-marked-picard-input.json"; RESULT=HERE/"result.md"; CONTROLLER=S33/"controller.json"
def csha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()
cert=json.loads(CERT.read_text(encoding="utf-8")); body=dict(cert); claimed=body.pop("canonical_sha256",None)
if claimed != csha(body): raise SystemExit("J2 marked-PicK certificate canonical hash mismatch")
if cert["schema"] != "STAGE33_12_J2_STOLL_MARKED_PICARD_INPUT_V2": raise SystemExit("J2 marked-PicK certificate schema mismatch")
scope=cert["exact_scope"]; exc=cert["named_J2_infinity_exceptional"]
if not scope["J2_carrier_marked_PicK_class_materialized"] or not scope["infinity_exceptional_marked_PicK_class_materialized"]: raise SystemExit("marked PicK input incomplete")
if not scope["infinity_exceptional_identity_order_independent"] or exc["semantic_identification"] != "UNIQUE_CSK_INCIDENCE_VECTOR_MATCH" or exc["unique_match_count"] != 1 or exc["ptsK_order_used_as_semantic_identity"]: raise SystemExit("exceptional identity is not order-independent")
if scope["J2_kc_discriminant_coordinate_materialized"]: raise SystemExit("unexpected J2 Br coordinate promotion")
text=RESULT.read_text(encoding="utf-8")
for old in ("Status: `MAIN_IN_PROGRESS_J2_RULED_TO_STOLL_KC_SUPPORT_COORDINATES_MATERIALIZED`","Status: `MAIN_IN_PROGRESS_J2_STOLL_MARKED_PICARD_INPUT_MATERIALIZED`"):
 if old in text: text=text.replace(old,"Status: `MAIN_IN_PROGRESS_J2_STOLL_MARKED_PICARD_INPUT_ORDER_INDEPENDENT`",1); break
if "Status: `MAIN_IN_PROGRESS_J2_STOLL_MARKED_PICARD_INPUT_ORDER_INDEPENDENT`" not in text: raise SystemExit("unexpected Stage33-12 result status")
marker="## New exact progress: order-independent J2 exceptional marking in PicK"
if marker not in text:
 c=cert["named_J2_carrier"]; e=exc
 section=f'''\n\n{marker}\n\nFresh source-locked Magma evaluation of the pinned Stoll Kc quotient now fixes the two actual divisor classes needed at the current support-resolution interface. The infinity exceptional is **not** identified by the position of `ptsK`: its exact 62-entry incidence vector against all `CsK` curves is computed from `[1:0:0:0:-1:-1]`, matched against `MatCPK`, and required to have exactly one match. The resulting internal `ptsK` position `{e["derived_internal_ptsK_index_1based"]}` is only a transport index.\n\n* named J2 carrier: `CsK[22] = {{B1=0, i*A2-A3=0}}`;\n* semantic exceptional identity: `UNIQUE_CSK_INCIDENCE_VECTOR_MATCH`;\n* unique-match count: `{e["unique_match_count"]}` across `{e["incidence_signature_length"]}` marked curves;\n* the corresponding exceptional `(-2)`-curve is internal `BigK.{e["BigK_exceptional_index_1based"]}`;\n* the J2 carrier meets the infinity singularity with exact multiplicity `{c["multiplicity_at_infinity_singularity"]}`;\n* `indlistK` is a unimodular rank-20 marked PicK basis in this extraction.\n\nCarrier marked coordinates: `{c["marked_indlistK_coordinates"]}`.\n\nInfinity exceptional marked coordinates: `{e["marked_indlistK_coordinates"]}`.\n\nCertificate: `j2-stoll-marked-picard-input.json`, canonical SHA256 `{claimed}`.\n\nThe branch-Jacobian 2-torsion / Picard-transcendental Kummer glue remains the missing map; therefore no `75 x 10` Kummer-defect column is promoted at this checkpoint.\n\nNext exact leaf: `{cert["next_exact_leaf"]}`.\n'''
 text=text.rstrip()+section
footer="## Latest order-independent marked-PicK checkpoint firewalls"
if footer not in text:
 text += '''\n\n## Latest order-independent marked-PicK checkpoint firewalls\n\n```text\nJ2_CARRIER_MARKED_PICK_CLASS_MATERIALIZED=true\nJ2_INFINITY_EXCEPTIONAL_MARKED_PICK_CLASS_MATERIALIZED=true\nJ2_INFINITY_EXCEPTIONAL_IDENTITY_ORDER_INDEPENDENT=true\nPTSK_ORDER_USED_AS_SEMANTIC_IDENTITY=false\nJ2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false\nJ2_Q1_KC_ADAPTER_UNIQUE=false\nFINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0\nARITHMETIC_HS_D2_COMPUTED=false\nGLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false\nSTAGE33_07_HOSTILE_REAUDIT=NOT_RUN\nSTAGE33_12_CLOSED=false\nSTAGE33_08_RELEASE=false\nTHEOREM_CREDIT=false\nENDPOINT_CREDIT=false\nRECEIVER_CREDIT=false\nPERFECT_CUBOID_EXISTENCE_CLAIM=false\nPERFECT_CUBOID_NONEXISTENCE_CLAIM=false\n```\n'''
RESULT.write_text(text,encoding="utf-8")
ctrl=json.loads(CONTROLLER.read_text(encoding="utf-8")); s07=ctrl["stage33_07"]
s07["stage33_12_j2_stoll_marked_picard_input_sha256"]=claimed; s07["stage33_12_j2_carrier_marked_picard_class_materialized"]=True; s07["stage33_12_j2_infinity_exceptional_marked_picard_class_materialized"]=True; s07["stage33_12_j2_infinity_exceptional_identity_order_independent"]=True; s07["stage33_12_ptsK_order_used_as_semantic_identity"]=False
s07["stage33_12_j2_infinity_internal_ptsK_index_1based"]=exc["derived_internal_ptsK_index_1based"]; s07["stage33_12_j2_infinity_exceptional_BigK_index_1based"]=exc["BigK_exceptional_index_1based"]; s07["stage33_12_j2_kc_discriminant_coordinate_materialized"]=False
child=next(x for x in ctrl["repair_children"] if x["id"]=="33-12")
child["j2_stoll_marked_picard_input"]="stages/stage33/33-12/j2-stoll-marked-picard-input.json"; child["j2_stoll_marked_picard_input_sha256"]=claimed; child["j2_carrier_marked_picard_class_materialized"]=True; child["j2_infinity_exceptional_marked_picard_class_materialized"]=True; child["j2_infinity_exceptional_identity_order_independent"]=True; child["ptsK_order_used_as_semantic_identity"]=False
child["j2_infinity_internal_ptsK_index_1based"]=exc["derived_internal_ptsK_index_1based"]; child["j2_infinity_exceptional_BigK_index_1based"]=exc["BigK_exceptional_index_1based"]; child["j2_kc_discriminant_coordinate_materialized"]=False; child["next_exact_leaf"]=cert["next_exact_leaf"]
ctrl["next_item"]="Stage33-12_APPLY_NAMED_BRANCH_JACOBIAN_2TORSION_TO_KC_PICARD_TRANSCENDENTAL_KUMMER_GLUE_AND_FIX_J2_KERNEL_LINE"
cp=ctrl["controller_writeback_checkpoint"]; cp["stage33_12_j2_stoll_marked_picard_input_sha256"]=claimed; cp["stage33_12_j2_carrier_marked_picard_class_materialized"]=True; cp["stage33_12_j2_infinity_exceptional_marked_picard_class_materialized"]=True; cp["stage33_12_j2_infinity_exceptional_identity_order_independent"]=True; cp["stage33_12_ptsK_order_used_as_semantic_identity"]=False; cp["stage33_12_j2_infinity_internal_ptsK_index_1based"]=exc["derived_internal_ptsK_index_1based"]; cp["stage33_12_j2_infinity_exceptional_BigK_index_1based"]=exc["BigK_exceptional_index_1based"]; cp["stage33_12_j2_kc_discriminant_coordinate_materialized"]=False
ctrl["theorem_credit"]=False; ctrl["endpoint_credit"]=False; ctrl["stage33_08_released"]=False; ctrl["stage33_08_release_allowed"]=False; ctrl["perfect_cuboid_existence_claim"]=False; ctrl["perfect_cuboid_nonexistence_claim"]=False
child["arithmetic_hs_d2_computed"]=False; child["global_q_br0g_residue_lifts_complete"]=False; child["stage33_07_hostile_reaudit"]="NOT_RUN"; child["heavy_actions_authorized"]=False
CONTROLLER.write_text(json.dumps(ctrl,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("STAGE33_12_J2_MARKED_PICK_CONTROLLER_WRITEBACK=PASS_ORDER_INDEPENDENT"); print("CERTIFICATE_SHA256="+claimed)
