#!/usr/bin/env python3
"""Current corrected J2 full-surface mu2/HS-d2 boundary contract.

The old zero-defect producer is retired.  This verifier source-locks the new
corrected normalization/full-L pre-Kummer descent cochain and the hostile
post-R5 FAIL certificate.  It intentionally records that the functorial map to
H^2_et(Kc_bar,mu_2), Pic/2 defect, integral Pic lift, and HS d2 are still open.
"""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
S33=HERE.parent
PRE=S33/"33-05"/"j2-corrected-pre-kummer-descent-cochain.json"
FAIL=S33/"33-05"/"j2-post-r5-hs-descent-datum.json"
OUT=HERE/"j2-full-surface-mu2-zero-defect-contract.json"
EXPECTED_PRE="940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106"
EXPECTED_FAIL="a7c08372b9ef012a1446bd3bf4f40541d77d372dadc73e3780f6ce2529fcc6d8"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load_canonical(path,expected):
    obj=json.loads(path.read_text(encoding="utf-8")); b=dict(obj); claimed=b.pop("canonical_sha256",None)
    if claimed!=expected or csha(b)!=expected: raise SystemExit(f"canonical source lock moved: {path}")
    return obj
pre=load_canonical(PRE,EXPECTED_PRE)
fail=load_canonical(FAIL,EXPECTED_FAIL)
assert pre["audit_boundary"]["full_surface_mu2_lift_materialized"] is False
assert pre["audit_boundary"]["HS_d2_2cocycle_materialized"] is False
assert fail["audit_failure"]["HS_d2_2cocycle_materialized"] is False
certificate={
"schema":"STAGE33_12_J2_FULL_SURFACE_MU2_ZERO_DEFECT_CONTRACT_V3_CORRECTED_PRE_KUMMER",
"status":"OPEN_CORRECTED_REPRESENTATIVE_PRE_KUMMER_COCHAIN_MATERIALIZED_SURFACE_MU2_AND_HS_D2_UNPROVEN",
"source_locks":{"corrected_pre_kummer_certificate":"stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json","corrected_pre_kummer_canonical_sha256":EXPECTED_PRE,"post_r5_fail_certificate":"stages/stage33/33-05/j2-post-r5-hs-descent-datum.json","post_r5_fail_canonical_sha256":EXPECTED_FAIL},
"exact_input":{"class":"corrected geometric J2=(f2,1)","named_geometric_representative_certified":True,"marked_brauer_coordinate":[1,0],"normalization_half_divisor":"D=P_r2-P_r4","normalization_half_divisor_descent_cochain_materialized":True,"full_split_pair_representative_witnesses_materialized":True},
"kummer_exact_sequence":{"sequence":"Pic(Kc_bar)/2 -> H^2_et(Kc_bar,mu_2) -> Br(Kc_bar)[2] -> 0","full_surface_mu2_lift_for_corrected_J2_materialized":False,"normalization_to_surface_Kummer_adapter_materialized":False,"reason":"The corrected normalization/full-L descent cochain is exact, but no committed functorial map yet turns it into an H^2_et(Kc_bar,mu_2) lift in the marked Kc surface presentation."},
"defect_state":{"pic_mod2_defect_1cocycle_materialized":False,"integral_Pic_lift_materialized":False,"HS_d2_2cocycle_materialized":False,"HS_d2_zero_proved":False,"finite_V4_zero_credit":False,"absolute_zero_credit":False},
"retired_historical_credit":{"old_Q_defined_ell_J2_may_be_used":False,"historical_delta_Kum_V4_EXACT_ZERO_revoked":True,"historical_named_kummer_glue_producer_tombstoned":True},
"next_exact_leaf":"MATERIALIZE_NORMALIZATION_HALF_DIVISOR_TO_KC_SURFACE_H2_MU2_ADAPTER_THEN_COMPUTE_PIC_MOD2_DEFECT_AND_BOCKSTEIN_HS_D2",
"promotion_firewall":{"Q_defined_descent_credit_restored":False,"arithmetic_hs_d2_computed":False,"stage33_05_reclosed":False,"stage33_12_closed":False,"stage33_13_released":False,"stage33_progress":"5/11","theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
certificate["canonical_sha256"]=csha(certificate)
if OUT.exists():
    recorded=json.loads(OUT.read_text(encoding="utf-8"))
    assert recorded==certificate, "recorded corrected mu2 boundary contract mismatch"
else:
    OUT.write_text(json.dumps(certificate,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(certificate,indent=2,sort_keys=True))
