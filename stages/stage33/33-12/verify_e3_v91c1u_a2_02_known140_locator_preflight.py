#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
OUT=HERE/'e3-v91c1u-a2-02-known140-locator-preflight.json'
T=HERE/'e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json'
C09=S33/'33-09'/'stage33-09-closure.json'
B09=S33/'33-09'/'marked-picard-basis-bridge-certified.json'
E11=S33/'33-11e'/'stage33-11e-prime-galois-transport-certificate.json'
NODES=S33/'33-07'/'exceptional-p1-tangent-coordinates.json'
REC=S33/'33-07'/'certify_two_coordinate_swap_picard_rows.py'
SHA={OUT:'7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34',T:'6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa',C09:'6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7',B09:'039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92',E11:'1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426',NODES:'beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636'}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==SHA[p]==csha(b),p; return o
def main():
 out,t,c09,b09,e11,nodes=map(load,[OUT,T,C09,B09,E11,NODES])
 assert t['exact_consequence']['literal_swap23_full_codim1_difference_materialized'] is True
 assert t['exact_consequence']['literal_swap23_full_codim1_difference_nonzero'] is True
 assert t['exact_consequence']['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert c09['historical_q256_basis_marking_exact'] is True
 assert c09['exit_condition']['HISTORICAL_RETAINED_PICARD_MARKING_BRIDGE_CERTIFIED'] is True
 assert c09['source_locks']['marked_picard_bridge_certificate_sha256']==SHA[B09]
 assert c09['source_locks']['current_stage32_marking_bundle_sha256']=='e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c'
 assert b09['schema']=='STAGE33_07_MARKED_PICARD_BASIS_BRIDGE_CERTIFIED_V1'
 B=b09['basis_bridge']['matrix_64x64']; assert len(B)==64 and all(len(r)==64 for r in B)
 sys.path.insert(0,str(S33/'33-07'))
 rec=runpy.run_path(str(REC))
 known=rec['known']; indlist=rec['INDLIST']
 assert rec['KNOWN_COUNT']==140 and len(known)==140 and len(indlist)==64
 assert all(len(r)==64 and all(type(x) is int for x in r) for r in known)
 for k,j in enumerate(indlist):
  e=[0]*64; e[k]=1; assert known[j-1]==e
 records=e11['prime_inventory']['records']; assert e11['prime_inventory']['distinct_prime_ids']==len(records)
 assert len(records)>0
 forbidden={'known_class_index_1based','known140_class_index_1based','fullPic64_historical_Magma_coordinates','fullPic64_INDLIST_coordinates','picard64_coordinates'}
 assert all(not (forbidden & set(r)) for r in records)
 models=nodes['exceptional_models']; assert len(models)==48
 assert all('exceptional_id' in r and 'node_point_ambient_P6_L_basis' in r for r in models)
 assert all(not (forbidden & set(r)) for r in models)
 assert out['materialized_capabilities']['known_surface_class_count']==140
 assert out['materialized_capabilities']['known_surface_classes_recoverable_in_primitive_indlist_picard64'] is True
 assert out['locator_audit']['strict_actual_prime_to_known140_class_index_materialized'] is False
 assert out['locator_audit']['exceptional_id_to_known140_class_index_materialized'] is False
 assert out['exact_consequence']['picard64_lattice_reconstruction_is_not_the_current_blocker'] is True
 assert out['exact_consequence']['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert out['exact_consequence']['pic2_cech_difference_class_computed'] is False
 assert out['credit_firewall']['stage33_progress']=='6/11' and out['credit_firewall']['merge_allowed'] is False
 print(json.dumps({'success':True,'marker':'V91C1U_KNOWN140_LOCATOR_PREFLIGHT','certificate_sha256':SHA[OUT],'known140_picard64_recovery':True,'actual_prime_locator_materialized':False,'next_exact_leaf':out['next_exact_leaf']},sort_keys=True))
if __name__=='__main__': main()
