#!/usr/bin/env python3
"""V31: certify current cc compactification from the global square witness."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
OUT=HERE/'j2-current-cc-global-square-cech-overlap-v31.json'
EXPECTED='a2e74b2344f380c6e908e282309bb8d31dc4cfcb5a70c05365e1120ced6726fb'
LOCKS={'v25':('j2-genuine-h2-mu2-kummer-adapter-v25.json','d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c'),'explicit':('j2-corrected-explicit-cech-mu2-lift.json','6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b'),'branch':('j2-corrected-branch-surface-mu2-adapter.json','edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875'),'semantic':('j2-semantic-kc-picard-basis.json','c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0'),'v30':('j2-current-lambda-d-odd-ramified-cech-overlaps-v30.json','5f911ca53e5e16374250e34e74e557229a9477d4814c910b8db7880dd993d66d')}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def load(k):
 n,h=LOCKS[k]; o=json.loads((HERE/n).read_text()); b=dict(o); got=b.pop('canonical_sha256'); assert got==h==csha(b),(n,got,csha(b)); return o
def main():
 d={k:load(k) for k in LOCKS}; out=json.loads(OUT.read_text()); body=dict(out); got=body.pop('canonical_sha256'); assert got==EXPECTED==csha(body),(got,csha(body))
 assert d['v25']['genuine_h2_mu2_adapter']['kc_lift_class']=='lambda_D=alpha(e_D), represented generically by {f2,g22}'
 cc=d['explicit']['galois_defect_generic_splittings']['cc']; assert cc['formula']=='cc(lambda_D)-lambda_D={f2,g21*g22}={f2,(B1/(2*t))^2}'
 assert d['branch']['double_cover_geometry']['cover_equation']=='B1^2=A2^2+A3^2'
 assert d['branch']['resolution_adapter']['normalized_double_cover_smooth_above_crossings'] is True
 assert len(d['semantic']['j2_branch_carrier']['marked_semantic_picK_coords'])==20
 v30=d['v30']['actual_ct_defect_marked_pic_mod2']; assert v30['nonzero'] is True
 assert out['current_authority']['cc_defect_formula']==cc['formula']; assert out['current_authority']['historical_generic_square_zero_inference_used'] is False
 comp=out['resolved_compactification']; assert comp['determinant']=='det(G_E)=w_cc'; assert comp['global_determinant_cartier_divisor']=='sum_E ord_E(w_cc)*E = div(w_cc)'
 assert comp['resolution_exceptionals_included'] and comp['quotient_A1_exceptionals_included'] and comp['branch_crossing_exceptionals_included']
 p=out['actual_cc_defect_marked_pic_mod2']; assert p['determinant_divisor_is_principal'] and p['integral_picard_class']==[0]*20 and p['coordinates_mod2']==[0]*20 and p['zero']
 f=out['v4_pic_mod2_frontier']; assert f['ct_coordinates_from_v30']==v30['coordinates']; assert f['cc_component_materialized'] and f['ct_component_materialized']; assert f['full_1cocycle_relation_checked_against_action_matrices'] is False
 print(json.dumps({'success':True,'canonical_sha256':EXPECTED,'cc_pic_mod2':[0]*20,'status':out['status']},sort_keys=True))
if __name__=='__main__': main()
