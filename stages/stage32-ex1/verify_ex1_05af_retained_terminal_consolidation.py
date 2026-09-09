#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"ex1-05af-retained-terminal-consolidation.json"

def git_blob_sha1(path: Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

d=json.loads(ART.read_text(encoding="utf-8"))
claimed=d.pop("canonical_sha256_without_this_field")
raw=json.dumps(d,sort_keys=True,separators=(",",":")).encode()
assert hashlib.sha256(raw).hexdigest()==claimed

d["canonical_sha256_without_this_field"]=claimed
EXPECTED_BLOBS={
"ex1-05o-common-v4-branch-cycle-monodromy-lift-preflight.json":"db22f3fdf75be3371d2bf46a516067c0d2e0f4b8",
"ex1-05w-simultaneous-nielsen-common-v4-torsor-matching-preflight.json":"97833e1533c48f3c6da6712db19ba235809789a3",
"ex1-05x-character-prym-lift-common-v4-correspondence-preflight.json":"1ad7c18a374b1e9b4a060a96528f660abd7a3a46",
"ex1-05y-prym-elliptic-endomorphism-norm-character-line-alignment-preflight.json":"76ecc594505261086b371e74b875223ffe1ce927",
"ex1-05z-integral-h-equivariant-jacobian-glue-congruence-preflight.json":"4a900fed80366dbc7553693943be89571fe9adf9",
"ex1-05aa-q602-mod4-isotropic-glue-kernel-action-preflight.json":"8e453f889951191ded2f4e784850754257001f8e",
"ex1-05ab-fixed-x8-prym-selected-2torsion-cm-orbit-preflight.json":"410c89e86a61de381d622c82f9dd821e4043a0b9",
"ex1-05ac-fixed-x8-polarization-kernel-antiisometry-transvection-alignment-preflight.json":"74a9d76faf652b5f40eb6b5b1b3244071a0d24b5",
"ex1-05ad-global-jx8-h-equivariant-endomorphism-descent-assembly-preflight.json":"f360242d2fec69002d8e14135c834060c6f3408f",
"ex1-05ae-h-linearized-correspondence-class-descent-to-s0-preflight.json":"37853cb07845ced93a22b5351dbddbbe891a9e88",
"ex1-05af-s0-integral-ns-pullback-saturation-preflight.json":"bf52be685e2a07d23b6f4ed836968687c610bb64",
"ex1-05af-cellular-h2-domain-certificate.json":"ee14798ce1f92aae0b8519ceec3f883d9106788f",
"ex1-05af-cellular-pullback-smith-certificate.json":"8f238ff7bdea3516ab4e1246a0202954b2d1bc3f"}
for name,sha in EXPECTED_BLOBS.items():
    p=HERE/name
    assert p.exists(),p
    got=git_blob_sha1(p)
    assert got==sha,(name,got,sha)

RUNS=[
("verify_ex1_05o_common_v4_branch_cycle_monodromy_lift.py","PASS_EX1_05O_UNIFORM_TRANSVECTION_28_TO_3"),
("verify_ex1_05x_character_prym_lift_common_v4_correspondence.py","PASS_EX1_05X_CHARACTER_PRYM_FOURIER_SPLIT"),
("verify_ex1_05y_prym_elliptic_endomorphism_norm_character_alignment.py","PASS_EX1_05Y_GAUSSIAN_PRYM_NORMS_REALIZABLE"),
("verify_ex1_05aa_q602_mod4_isotropic_glue_kernel_action.py","PASS_EX1_05AA_ACTUAL_RING_MOD4_COLLAPSES_TO_TRANSVECTIONS"),
("verify_ex1_05ab_fixed_x8_prym_selected_2torsion_cm_orbit.py","PASS_EX1_05AB_ALL_SELECTED_PRYM_POINTS_CM_FIXED"),
("verify_ex1_05ac_fixed_x8_polarization_kernel_antiisometry_transvection_alignment.py","PASS_EX1_05AC_FIXED_GLUE_ALIGNS_ALL_THREE_TRANSVECTIONS"),
("verify_ex1_05ad_global_jx8_h_equivariant_endomorphism_descent_assembly.py","PASS_EX1_05AD_GLOBAL_JX8_ASSEMBLY_ALL_RESIDUES"),
("verify_ex1_05ae_h_linearized_correspondence_class_descent_to_s0.py","PASS_EX1_05AE_RATIONAL_DESCENT_NUMERICS_EXACT_INTEGRAL_SATURATION_OPEN"),
("verify_ex1_05af_s0_integral_ns_pullback_saturation.py","PASS_EX1_05AF_ALL_6144_ASSEMBLIES_HAVE_ORDER2_NS_DESCENT_OBSTRUCTION"),
("verify_ex1_05af_full_cellular_smith_certificate.py","PASS_EX1_05AF_FULL_CELLULAR_SMITH_CERTIFICATE")]
for script,token in RUNS:
    cp=subprocess.run([sys.executable,str(HERE/script)],cwd=HERE,text=True,capture_output=True)
    if cp.returncode:
        print(cp.stdout)
        print(cp.stderr,file=sys.stderr)
        raise SystemExit(cp.returncode)
    assert token in cp.stdout,(script,token,cp.stdout)
    print(token)

dec=d["decision"]
assert dec["status"]=="PROVISIONAL_AUDIT_READY_TERMINAL_CANDIDATE"
assert dec["candidate_terminal_outcome"]=="ALL_V6_GENUS1_CARRIERS_EXCLUDED"
assert dec["h4_states_excluded_candidate"]==29
assert dec["h4_survivors_candidate"]==[]
assert dec["q602_residues_excluded_candidate"]==[73,97,235]
for key in ("authority_credit_granted","hostile_audit_credit_granted","stage32_main_credit_granted","ex_to_main_promotion_performed"):
    assert dec[key] is False,key
print("PASS_EX1_05AF_RETAINED_TERMINAL_CONSOLIDATION")
