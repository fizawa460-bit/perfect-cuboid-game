#!/usr/bin/env python3
"""Exact finite reduction of the Stage33-07 two-primary transcendental glue wall."""
from __future__ import annotations
import hashlib, json, math
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[2]
kb=json.loads((HERE/'kb-picard-lattice.json').read_text())
kc=json.loads((HERE/'kc-picard-lattice.json').read_text())
ep=json.loads((HERE/'endpoint-picard-discriminant-retained.json').read_text())
adapter=(REPO/'stages'/'stage29'/'29-02e'/'global-k3-eigenspace-adapter.md').read_text()

if kb['canonical_sha256']!='3ec9b28393199eca93ca4b4de37af8eca8133afdff52f1873f411fc1dc220635': raise SystemExit('Kb lock regression')
if kc['canonical_sha256']!='eab9420431ed60960d39b4a76269aacd0fe4b5f600615dd1e7106a7af74dde56': raise SystemExit('Kc lock regression')
if kb['picard_rank']!=20 or kc['picard_rank']!=20: raise SystemExit('K3 Picard rank regression')
if kb['picard_smith_diagonal'][-2:]!=[4,4] or abs(kb['picard_determinant'])!=16: raise SystemExit('Kb discriminant regression')
if kc['picard_smith_diagonal'][-2:]!=[4,8] or abs(kc['picard_determinant'])!=32: raise SystemExit('Kc discriminant regression')
if not kb['full_picard_lattice_certified'] or not kc['full_picard_lattice_certified']: raise SystemExit('K3 lattice not certified full')
for s in ('T(K_c) = V_h32','T(K_a) = V_h8','T(K_b) = V_h16','K_a ~= K_c'):
    if s not in adapter: raise SystemExit(f'Stage29 adapter regression: {s}')

def smith2(G):
    d=0
    for row in G:
        for x in row: d=math.gcd(d,abs(x))
    det=abs(G[0][0]*G[1][1]-G[0][1]*G[1][0])
    return [d,det//d]

def reduced_even_forms(det):
    out=[]
    for a in range(1,det+1):
        for c in range(a,det+1):
            for b in range(-a,a+1):
                if 4*a*c-b*b==det:
                    G=[[2*a,b],[b,2*c]]
                    out.append({'gram':G,'smith':smith2(G)})
    return out

kb_forms=reduced_even_forms(16); kc_forms=reduced_even_forms(32)
kb_match=[x for x in kb_forms if x['smith']==[4,4]]
kc_match=[x for x in kc_forms if x['smith']==[4,8]]
if len(kb_match)!=1 or kb_match[0]['gram']!=[[4,0],[0,4]]: raise SystemExit(f'Kb rank-two isometry ambiguity {kb_match}')
if len(kc_match)!=1 or kc_match[0]['gram']!=[[4,0],[0,8]]: raise SystemExit(f'Kc rank-two isometry ambiguity {kc_match}')

# Testa--Stoll Ka~=Kc over Q(i), so their geometric integral T-lattices agree.
# Degree-two quotient pullback scales the intersection form by 2.
L0_diag=sorted([8,8]*3+[8,16]+[8,16]*3)
if L0_diag!=[8]*10+[16]*4: raise SystemExit('seven-piece diagonal regression')
det_L0=math.prod(L0_diag)
if det_L0!=2**46: raise SystemExit('L0 determinant regression')
if ep['picard_rank']!=64 or abs(ep['picard_determinant'])!=2**28: raise SystemExit('endpoint Picard determinant regression')
endpoint_nontrivial=[d for d in ep['picard_smith_diagonal'] if d>1]
if endpoint_nontrivial!=[2]*4+[4]*6+[8]*4: raise SystemExit('endpoint discriminant regression')

# H^2 is unimodular and NS is primitive, hence |disc T(S)|=|disc Pic(Sbar)|.
det_T=abs(ep['picard_determinant']); ratio=det_L0//det_T; idx=math.isqrt(ratio)
if idx*idx!=ratio or idx!=512: raise SystemExit(f'glue index regression {ratio=} {idx=}')

cert={
 'schema':'STAGE33_07_COORDINATE_K3_TRANSCENDENTAL_GLUE_INDEX_V1',
 'source_locks':{
  'kb_certificate_sha256':kb['canonical_sha256'],
  'kc_certificate_sha256':kc['canonical_sha256'],
  'endpoint_picard_source_certificate_sha256':ep['source_certificate_canonical_sha256'],
  'endpoint_picard_source_artifact_zip_sha256':ep['source_artifact_zip_sha256'],
  'stage29_coordinate_k3_adapter':'stages/stage29/29-02e/global-k3-eigenspace-adapter.md',
  'testa_stoll_upstream_git_blob_sha1':kb['upstream_git_blob_sha1'],
 },
 'rank_two_reduced_form_census':{'Kb_det16':kb_forms,'Kc_det32':kc_forms},
 'coordinate_transcendental_lattices':{'T_Kb':'diag(4,4)','T_Kc':'diag(4,8)','T_Ka_geometric':'diag(4,8)'},
 'degree_two_pullback_scaled_lattices':{'Kb_each':'diag(8,8)','Kc':'diag(8,16)','Ka_each':'diag(8,16)','multiplicities':'3*Kb + 1*Kc + 3*Ka'},
 'seven_piece_integral_pullback_sublattice':{
  'rank':14,'diagonal_gram':L0_diag,'isometry_type':'<8>^10 direct_sum <16>^4',
  'discriminant_group':'(Z/8)^10 direct_sum (Z/16)^4','determinant':det_L0,'determinant_v2':46,
 },
 'endpoint_transcendental_target':{
  'rank':14,'determinant_abs':det_T,'determinant_v2':28,
  'discriminant_group_invariant_factors':endpoint_nontrivial,
  'discriminant_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4',
 },
 'integral_glue':{
  'index_T_over_L0':idx,'index_v2':9,'glue_subgroup_order':idx,
  'ambient_discriminant_module':'A_L0=(Z/8)^10 direct_sum (Z/16)^4',
  'required_condition':'identify the actual isotropic order-2^9 subgroup H in A_L0, stable under arithmetic Galois and coordinate-sign actions, with H_perp/H equal to the endpoint discriminant module',
  'actual_glue_subgroup_identified':False,'no_elementary_or_invariant_factor_type_assumed':True,
 },
 'repair_scope':'TWO_PRIMARY_ONLY','odd_primary_repair_already_closed':True,
 'global_q_defined_boundary_lifts_complete':False,'localization_lift_torsor_computed':False,
 'hs_d2_computed_on_remaining_26_generators':False,'unit_status':'RUNNING_REPAIR','unit_closed':False,
 'stage33_progress':'6/11','stage33_08_released':False,
 'new_residual_kernel':'R33-BR2A-INDEX512-TWO-ADIC-K3-GLUE-AND-GALOIS-DESCENT',
 'next_exact_leaf':'L33-07-IDENTIFY-ACTUAL-ORDER512-ISOTROPIC-K3-GLUE-THEN-COMPUTE-BR4-GALOIS-MODULE-AND-DELTA_LOC',
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'coordinate-k3-transcendental-glue-index.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'T_Kb':'diag(4,4)','T_Kc':'diag(4,8)','L0':'<8>^10+<16>^4','det_L0_v2':46,'det_T_v2':28,'glue_index':idx,'glue_index_v2':9,'remaining_kernel':cert['new_residual_kernel'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
