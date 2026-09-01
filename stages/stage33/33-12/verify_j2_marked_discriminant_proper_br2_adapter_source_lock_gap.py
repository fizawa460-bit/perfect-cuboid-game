#!/usr/bin/env python3
"""Verify the exact Stage33-12 marked-discriminant/proper-Br2 source-lock gap.

This verifier deliberately audits an explicit, hash-locked authority manifest.  It
must not infer absence of an adapter from filenames, source-code substrings, or
fuzzy key-name searches.
"""
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
sb=SRC.read_bytes(); assert blob(sb)=='aaf4cf64cb9bc65aaea1e9c06d3d9c885b4a5299'

# Named semantic orientation and the two marked full-surface A_T[2] vectors are exact.
assert orient['exact_conclusion']['named_CV_J2_fixed_marked_Kc_coordinate_f2']==[1,0]
assert orient['exact_conclusion']['named_CV_J2_semantic_discriminant_label']=='u1'
assert orient['kernel_fingerprint_identification']['unique'] is True
u1v=u1['exact_normalization']['full_surface_A_T_2_coordinates_f2']; u2v=u2['semantic_u2_pullback']['full_surface_A_T_2_coordinates_f2']
assert u1v==cert['locked_facts']['u1_full_surface_A_T_2_coordinates_f2']; assert u2v==cert['locked_facts']['u2_full_surface_A_T_2_coordinates_f2']; assert len(u1v)==len(u2v)==14 and u1v!=u2v

# Explicit authority-manifest audit.  U1 carries the discriminant form itself,
# but its exact artifact explicitly withholds any proper-Br2 coordinate.  The
# 14x14 bilinear numerator therefore cannot silently be reinterpreted as the
# missing marked source->target basis adapter.
u1_locks_expected={
 'picard_discriminant_compact_sha256','prior_six_ct_pullbacks_sha256','retained_q256_endpoint_sha256',
 'stage32_picard_core_sha256','stage33_09_marked_basis_sha256','stoll_commit','stoll_git_blob_sha1',
 'submitted_magma_code_sha256'}
assert set(u1['source_locks'])==u1_locks_expected
assert u1['promotion_firewall']['proper_Br2_14D_coordinate_materialized'] is False
pairing=u1['retained_common_smith_source']['discriminant_bilinear_numerator_over_8_reduced']
assert len(pairing)==14 and all(len(row)==14 for row in pairing)
assert u1['retained_common_smith_source']['discriminant_moduli']==[2,2,2,2,4,4,4,4,4,4,8,8,8,8]

# The proper-Br2 producer is independently hash-locked and explicitly says the
# actual index-512 K3 glue was not identified.  It supplies the abstract dual
# module, not a marked full-surface anti-isometry/basis adapter.
assert proper['actual_index512_k3_glue_identified'] is False
assert proper['A_T_two_torsion_dimension_f2']==14
assert proper['proper_geometric_Br2_dimension_f2']==14
assert proper['equivariant_identification']=='T/2T ~= A_T[2] via x mod 2T -> x/2 mod T'

# Exact source-lock manifest of the historical Picard-adjoint certificate.  By
# checking the complete key set under a canonical hash, aliases cannot evade
# this audit: this is not a substring/name heuristic.
adj_locks_expected={
 'full_surface_picard_base_sha256','kc_discriminant_2torsion_sha256','proper_brauer2_sha256',
 'retained_10D_target_sha256','semantic_picard_basis_sha256','semantic_u1_full_surface_sha256',
 'semantic_u2_full_surface_sha256','stoll_commit','stoll_git_blob_sha1','submitted_magma_code_sha256'}
assert set(adj['source_locks'])==adj_locks_expected
assert adj['source_locks']['proper_brauer2_sha256']==LOCKS[PROPER]
assert adj['source_locks']['semantic_u1_full_surface_sha256']==LOCKS[U1]
assert adj['source_locks']['semantic_u2_full_surface_sha256']==LOCKS[U2]
assert cert['source_locks']['picard_adjoint_materializer_git_blob_sha1']=='aaf4cf64cb9bc65aaea1e9c06d3d9c885b4a5299'
assert cert['source_locks']['proper_brauer2_sha256']==LOCKS[PROPER]
assert cert['source_locks']['semantic_u1_full_surface_sha256']==LOCKS[U1]
assert cert['source_locks']['semantic_u2_full_surface_sha256']==LOCKS[U2]
assert cert['provenance_gap']['existing_semantic_u1_u2_artifacts_materialize_full_14D_marked_discriminant_to_transcendental_basis_adapter'] is False
assert cert['provenance_gap']['proper_brauer2_producer_actual_index512_k3_glue_identified'] is False
assert cert['provenance_gap']['picard_adjoint_materializer_source_locks_marked_full_surface_transcendental_anti_isometry'] is False

# Mathematical downgrade and promotion firewalls remain independently replayed.
assert diag['exact_reopen_trigger']['picard_adjoint_J2_mask_decimal']==6; assert diag['exact_reopen_trigger']['locked_target_reachable_from_mask6'] is False
assert diag['promotion_firewall']['picard_adjoint_named_J2_binding_retained_as_authoritative'] is False
assert compat['locked_named_j2']['locked_75D_target_reachable_from_locked_source'] is False
assert compat['consequence']['old_relation_may_be_used_as_kummer_matrix_relation'] is False
d=diag['two_dimensional_adjoint_image_diagnostic']; assert d['beta2_mask_decimal']==742 and d['beta2_target_compatible'] is True; assert d['beta1_plus_beta2_mask_decimal']==736 and d['beta1_plus_beta2_target_compatible'] is True
assert diag['promotion_firewall']['beta2_promoted_as_J2'] is False; assert diag['promotion_firewall']['beta1_plus_beta2_promoted_as_J2'] is False
assert cert['promotion_firewall']['named_J2_source_coordinate_promoted'] is False
print(json.dumps({'success':True,'status':cert['status'],'authority_manifest_audit':'PASS_EXACT_HASH_LOCKED_NO_NAME_HEURISTICS','u1_discriminant_pairing_present_but_not_promoted_as_adapter':True,'named_Kc_orientation_retained':[1,0],'old_mask6_rejected':True,'candidate_742_736_promotion_forbidden':True,'required_adapter':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
