#!/usr/bin/env python3
"""Verify the exact Stage33-12 marked-discriminant/proper-Br2 source-lock gap."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; LEGACY=HERE.parent/'33-07'
CERT=HERE/'j2-marked-discriminant-proper-br2-adapter-source-lock-gap.json'
DIAG=HERE/'j2-picard-adjoint-reopen-diagnostic.json'; ORIENT=HERE/'j2-cv-d2-semantic-orientation.json'
U1=HERE/'j2-semantic-u1-full-surface-smith-source.json'; U2=HERE/'j2-semantic-u2-full-surface-at2.json'
PROPER=LEGACY/'proper-brauer2-from-discriminant.json'; ADJ=HERE/'j2-picard-adjoint-proper-br2.json'
SRC=HERE/'materialize_j2_picard_adjoint_proper_br2.py'; COMPAT=HERE/'j2-kummer-source-target-module-compatibility-audit.json'
LOCKS={CERT:'e27da962e6bd4330bd2e3ede77424bedb5ad40a684d81fadba632ac2fdef8b58',DIAG:'1a20e001fd23b292881f9652818e52d5afc7f0bd43657809d5e52075ae6d1737',ORIENT:'0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e',U1:'ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec',U2:'60b6d058459f7745f6fa3f9b6d3b44f1610e12ff46c42e3133ec574f71613039',PROPER:'c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf',ADJ:'066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8',COMPAT:'463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229'}
def locked(p):
 x=json.loads(p.read_text()); b=dict(x); h=b.pop('canonical_sha256'); got=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert h==got==LOCKS[p],p; return x
def blob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
cert=locked(CERT); diag=locked(DIAG); orient=locked(ORIENT); u1=locked(U1); u2=locked(U2); proper=locked(PROPER); adj=locked(ADJ); compat=locked(COMPAT)
sb=SRC.read_bytes(); assert blob(sb)=='aaf4cf64cb9bc65aaea1e9c06d3d9c885b4a5299'; src=sb.decode()
assert orient['exact_conclusion']['named_CV_J2_fixed_marked_Kc_coordinate_f2']==[1,0]
assert orient['exact_conclusion']['named_CV_J2_semantic_discriminant_label']=='u1'
assert orient['kernel_fingerprint_identification']['unique'] is True
u1v=u1['exact_normalization']['full_surface_A_T_2_coordinates_f2']; u2v=u2['semantic_u2_pullback']['full_surface_A_T_2_coordinates_f2']
assert u1v==cert['locked_facts']['u1_full_surface_A_T_2_coordinates_f2']; assert u2v==cert['locked_facts']['u2_full_surface_A_T_2_coordinates_f2']; assert len(u1v)==len(u2v)==14 and u1v!=u2v
assert proper['actual_index512_k3_glue_identified'] is False; assert proper['proper_geometric_Br2_dimension_f2']==14
assert 'K3 discriminant anti-isometries' in src
keys=set(adj['source_locks']); assert not any(('anti' in k.lower() and 'isometr' in k.lower()) or ('transcendental' in k.lower() and 'mark' in k.lower()) for k in keys)
assert diag['exact_reopen_trigger']['picard_adjoint_J2_mask_decimal']==6; assert diag['exact_reopen_trigger']['locked_target_reachable_from_mask6'] is False
assert diag['promotion_firewall']['picard_adjoint_named_J2_binding_retained_as_authoritative'] is False
assert compat['locked_named_j2']['locked_75D_target_reachable_from_locked_source'] is False
assert compat['consequence']['old_relation_may_be_used_as_kummer_matrix_relation'] is False
d=diag['two_dimensional_adjoint_image_diagnostic']; assert d['beta2_mask_decimal']==742 and d['beta2_target_compatible'] is True; assert d['beta1_plus_beta2_mask_decimal']==736 and d['beta1_plus_beta2_target_compatible'] is True
assert diag['promotion_firewall']['beta2_promoted_as_J2'] is False; assert diag['promotion_firewall']['beta1_plus_beta2_promoted_as_J2'] is False
assert cert['provenance_gap']['picard_adjoint_materializer_source_locks_marked_full_surface_transcendental_anti_isometry'] is False
assert cert['promotion_firewall']['named_J2_source_coordinate_promoted'] is False
print(json.dumps({'success':True,'status':cert['status'],'named_Kc_orientation_retained':[1,0],'old_mask6_rejected':True,'candidate_742_736_promotion_forbidden':True,'required_adapter':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
