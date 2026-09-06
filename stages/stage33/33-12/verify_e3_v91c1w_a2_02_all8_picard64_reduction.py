#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
CERT=HERE/'e3-v91c1w-a2-02-all8-picard64-reduction.json'
V=HERE/'e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json'
PROV=HERE/'diagnose_e3_v91c1w_all8_strict_scheme_provenance.py'
DIAG=HERE/'diagnose_e3_v91c1w_all8_picard64_reduction_v2.py'
CERT_SHA='e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7'
V_SHA='60f41e8e324e5fb29d1b109adb860b947308b521f677e49c4965e337a0c2d2d2'
PROV_BLOB='363ee4618143050fdc73ecdd8f08a8a1e6d53202'
DIAG_BLOB='7b0ba747021f55860615a3a054864afff6ef537b'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def blob_sha(p):
 b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 ca=load(CERT,CERT_SHA); load(V,V_SHA)
 assert blob_sha(PROV)==PROV_BLOB and blob_sha(DIAG)==DIAG_BLOB
 e=ca['entry_authority']
 assert e['pr']==1667 and e['exact_audited_head']=='56ac6b79a4a8e13205a497af1a2cdd6d1e23aee4'
 assert e['hostile_reaudit_review']==5126709022 and e['merge_commit']=='bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177'
 ns=runpy.run_path(str(DIAG)); r=ns['result']; x=ca['exact_result']
 assert r['success'] is True and r['credit'] is False
 assert r['strict_scheme_count']==8 and r['strict_scheme_picard64_classes_materialized'] is True
 assert r['multi_match_exact_decomposition_count']==6 and r['zero_match_direct_relation_count']==2
 assert r['all_eight_exact_decomposition_or_source_bound_relation'] is True
 assert len(r['direct_decompositions'])==6
 assert all(z['exact_ideal_intersection_equals_target'] and z['decomposition_exhaustive'] and z['decomposition_reduced'] for z in r['direct_decompositions'].values())
 assert all(z['component_multiplicities']==[1]*z['component_count'] for z in r['direct_decompositions'].values())
 assert len(r['zero_match_relations'])==2
 retained=r['zero_match_relations']['e5235f980a52e408098a096dfeb1c428babf7af9bf61d7b737d5b38a297a81d2']
 acted=r['zero_match_relations']['8353da8852818df4bc17a94369d69e658aa8b2897cf073dfb18f2e6c26318bdc']
 assert retained['source_carrier_id']==x['zero_match_retained_parent_carrier_id']
 assert retained['single_strict_component'] is True and retained['component_multiplicity']==1
 assert acted['agrees_with_exact_swap23_picard_action'] is True
 assert csha(r['strict_package_picard64_row'])==x['strict_package_picard64_row_sha256']
 assert csha(r['exceptional_package_picard64_row'])==x['exceptional_package_picard64_row_sha256']
 assert csha(r['complete_swap23_difference_picard64_row'])==x['complete_swap23_difference_picard64_row_sha256']
 assert r['complete_swap23_difference_mod2_support_one_based']==[]
 assert r['complete_swap23_difference_zero_mod2'] is True and r['pic2_cech_difference_class_computed'] is True
 assert r['a2_02_swap23_seed_fixed_mod_pic2_promoted'] is False
 assert r['a2_02_marked_brauer_image_excluded_from_mask20'] is False
 assert ca['exact_consequence']['a2_02_swap23_seed_fixed_mod_pic2_promoted'] is False
 assert ca['credit_firewall']['merge_allowed'] is False and ca['credit_firewall']['stage33_progress']=='6/11'
 print(json.dumps({'success':True,'marker':'V91C1W_ALL8_PICARD64_COMPLETE_SWAP23_PIC2_ZERO','certificate_sha256':CERT_SHA,'all8_picard64':True,'complete_difference_zero_mod2':True,'seed_fixedness_promoted':False,'next_exact_leaf':ca['next_exact_leaf']},sort_keys=True))
if __name__=='__main__': main()
