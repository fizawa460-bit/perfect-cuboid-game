#!/usr/bin/env python3
from __future__ import annotations
import json,hashlib,runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
S35=ROOT/'stages/stage35-ex'
ART=S35/'35ex-35/goal4ad-c5-pair-marked-picard-adapter-preflight.json'
LOCK=S35/'35ex-35/goal4ad-c5-pair-marked-picard-adapter-preflight-source-lock.md'
STATE=S35/'MAIN-STATE.json'
SNAP=S35/'snapshots/MAIN-STATE-V66-62bef97cbbac.json'
G4AC=S35/'35ex-35/goal4ac-c5-individual-quadratic-residual.json'
G4ACV=S35/'verify_stage35_ex_35_goal4ac.py'
S33=ROOT/'stages/stage33'
S33U=S33/'33-12/e3-v91c1u-a2-02-known140-locator-preflight.json'
S33UV=S33/'33-12/verify_e3_v91c1u_a2_02_known140_locator_preflight.py'
REC=S33/'33-07/certify_two_coordinate_swap_picard_rows.py'

def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

a=json.loads(ART.read_text())
assert a['schema']=='STAGE35_EX_35_GOAL4AD_C5_PAIR_MARKED_PICARD_ADAPTER_PREFLIGHT_V1'
assert a['parent']['schema']=='STAGE35_EX_PESCH_E1_STATE_V66_GOAL4AC_C5_STRICT_RESIDUAL_EXHAUSTED_MARKED_PAIR_PICARD_PENDING_AUDIT'
assert a['parent']['source_head_sha']=='62bef97cbbac1ca6b12aa52abc6299f2a63587fa'
assert blob(LOCK)==a['source_locks']['goal4ad_source_lock']['blob_sha']=='5e32c67c087853a741d9c9026b998672187d2954'
assert blob(G4AC)==a['source_locks']['goal4ac']['blob_sha']=='ef451544bce4aaafc14d24081e22ce997977a861'
assert blob(G4ACV)==a['source_locks']['goal4ac_verifier']['blob_sha']=='a635727e2ae48288afb29977fa7464821fc2347d'
assert blob(S33U)==a['source_locks']['stage33_known140_preflight']['blob_sha']=='b799de4a575401f1540739b8093867ef4399619e'
assert a['source_locks']['upstream_stoll']['commit']=='51233ed5ef2bf228fac9416c66db9adc0ebcaadd'
assert a['source_locks']['upstream_stoll']['git_blob_sha1']=='0422b69847f2afb97cb7b3ed02ebef91279f61b1'

# Replay Goal4AC exactly against immutable V66 state.
snaptext=SNAP.read_text(); snap=json.loads(snaptext)
assert blob(SNAP)=='b45e56114b7823330cd3132188ac71e5dce219a6'
assert snap['schema']=='STAGE35_EX_PESCH_E1_STATE_V66_GOAL4AC_C5_STRICT_RESIDUAL_EXHAUSTED_MARKED_PAIR_PICARD_PENDING_AUDIT'
orig=Path.read_text; sr=STATE.resolve()
def patched(self:Path,*args,**kwargs):
    if self.resolve()==sr:return snaptext
    return orig(self,*args,**kwargs)
Path.read_text=patched
try:
    runpy.run_path(str(G4ACV),run_name='__main__')
finally:
    Path.read_text=orig

# Stage33's compact verifier proves that the retained 140-class packet is
# exactly recoverable in the primitive INDLIST64 marking while refusing to
# invent a geometric locator.  This runs the denylisted retained payload only
# runner-side through its compact reconstruction script.
runpy.run_path(str(S33UV),run_name='__main__')
u=json.loads(S33U.read_text())
assert u['materialized_capabilities']['known_surface_class_count']==140
assert u['materialized_capabilities']['known_surface_classes_recoverable_in_primitive_indlist_picard64'] is True
assert u['locator_audit']['implicit_ordering_promoted_to_source_bound_locator'] is False
assert u['exact_consequence']['picard64_lattice_reconstruction_is_not_the_current_blocker'] is True

# Fail-close the source-packet boundary.  The retained reconstruction itself
# pins 92 source curves followed by 48 exceptional classes; the upstream source
# lock pins CsK=C1sK cat C2sK cat C3sK and constructs C5 separately later.
rectext=REC.read_text()
assert 'KNOWN_COUNT = 140' in rectext
assert 'CURVE_COUNT = 92' in rectext
locktext=LOCK.read_text()
for needle in [
    'CsK := C1sK cat C2sK cat C3sK;',
    'C5Kp := imageinPicK(C5K);',
    'until #C5sK eq 8;',
    'PicKtoPicS := hom<PicK -> Pic | ... >;',
    'C5K / its orbit -> imageinPicK -> PicKtoPicS -> historical Pic(S) -> INDLIST64 marking',
]:
    assert needle in locktext,needle

k=a['known140_boundary']
assert k['known_surface_class_count']==140
assert k['retained_curve_class_count']==92 and k['exceptional_class_count']==48
assert k['source_curve_packet']=='C1sK_CAT_C2sK_CAT_C3sK'
assert k['C5_in_source_known140_packet'] is False
assert k['historical_INDLIST_rank']==64
assert k['known140_to_INDLIST64_recovery_materialized'] is True
assert k['known140_index_route_is_primary_C5_adapter'] is False

d=a['direct_c5_source_route']
assert d['C5K_constructed'] is True
assert d['C5Kp_computed_by_imageinPicK'] is True
assert d['C5K_orbit_size']==8
assert d['PicKtoPicS_homomorphism_constructed'] is True
assert d['numeric_C5Kp_orbit_coordinates_retained_here'] is False
assert d['numeric_PicKtoPicS_C5_images_retained_here'] is False
assert d['C5_pair_to_INDLIST64_coordinates_materialized'] is False
ad=a['adapter_architecture']
assert ad['selected_route']=='C5K_ORBIT_TO_IMAGEINPICK_TO_PICKTOPICS_TO_HISTORICAL_PICS_TO_INDLIST64'
assert ad['known140_locator_bypass_required'] is True
assert ad['source_bound_numeric_extraction_required'] is True
assert ad['target_span_test_legal_now'] is False
ex=a['exact_consequence']
assert ex['goal4ad_executed'] is True
assert ex['marked_picard_adapter_architecture_resolved'] is True
assert ex['four_c5_pair_marked_picard64_classes_computed'] is False
assert ex['four_c5_pair_total_transform_corrections_computed'] is False
assert ex['target_span_after_adjoining_c5_pair_classes_computed'] is False
assert ex['current_blocker']=='SOURCE_BOUND_NUMERIC_C5Kp_ORBIT_AND_PicKtoPicS_IMAGES_IN_HISTORICAL_INDLIST64'
for key,val in a['semantic_firewall'].items():
    assert val is False,key
assert a['route_result']['general_qi_principal_function_problem']=='OPEN'
assert a['route_result']['next']=='35EX-35_GOAL4AE_SECOND_CLASS_QI_CYCLIC_C5_DIRECT_PicK_TO_PicS_INDLIST64_EXTRACTION_PREFLIGHT'

state=json.loads(STATE.read_text())
assert state['schema']=='STAGE35_EX_PESCH_E1_STATE_V67_GOAL4AD_C5_MARKED_PICARD_ROUTE_RESOLVED_DIRECT_EXTRACTION_PENDING_AUDIT'
assert state['current']['unit']==a['unit']
assert state['claims']['goal4ad_executed'] is True
assert state['claims']['open_receiver_second_class_C5_marked_picard_route_resolved'] is True
assert state['claims']['open_receiver_second_class_C5_pair_marked_picard_adapter_computed'] is False
assert state['claims']['open_receiver_second_class_target_span_with_C5_pairs_computed'] is False
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['brauer_manin_obstruction_obtained'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False
print('PASS Stage35-EX Goal4AD: known140 is not the C5 locator; direct C5 PicK -> Pic(S) -> INDLIST64 extraction is the exact next adapter route')
