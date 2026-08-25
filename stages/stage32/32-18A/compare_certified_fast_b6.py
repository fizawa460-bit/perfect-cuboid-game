#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib
M=140
EXPECTED_STABLE='7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3'

def records(path:pathlib.Path):
    raw=path.read_bytes()
    if raw[:8]!=b'S32D16C1': raise RuntimeError(f'bad dump magic {path}')
    body=raw[8:]; size=M+1
    if len(body)%size: raise RuntimeError('truncated dump')
    return [(body[o],bytes(body[o+1:o+size])) for o in range(0,len(body),size)]

def file_sha(p:pathlib.Path): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    for name in ('exact_json','exact_dump','fast_json','fast_dump','fast_verify','provenance','output'):
        ap.add_argument('--'+name.replace('_','-'),dest=name,type=pathlib.Path,required=True)
    a=ap.parse_args(); e=json.loads(a.exact_json.read_text()); f=json.loads(a.fast_json.read_text()); v=json.loads(a.fast_verify.read_text()); p=json.loads(a.provenance.read_text())
    er=records(a.exact_dump); fr=records(a.fast_dump)
    if len(er)!=len(set(er)) or len(fr)!=len(set(fr)): raise RuntimeError('duplicate canonical record')
    if set(er)!=set(fr): raise RuntimeError(f'exact/fast canonical sets differ exact={len(er)} fast={len(fr)}')
    expected_hist={'0':1,'2':1,'4':7,'6':28}
    checks=[
        e.get('schema')=='STAGE32_18A_D16_EXACT_B6_TRAVERSAL_CERT_V1', e.get('status')=='COMPLETE', e.get('bound')==6,
        e.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is True, e.get('floating_arithmetic_used_for_traversal_pruning') is False,
        e.get('exact_ldl_reconstructs_integer_gram') is True, e.get('cap_survivors_before_symmetry')==17833,
        e.get('precanonical_survivors')==232, e.get('canonical_rejects')==195, e.get('canonical_survivors_including_zero')==37,
        e.get('canonical_nonzero_survivors')==36, e.get('canonical_norm_histogram')==expected_hist,
        f.get('status')=='COMPLETE', f.get('precanonical_survivors')==232, f.get('canonical_rejects')==195,
        f.get('canonical_survivors_including_zero')==37, f.get('canonical_nonzero_survivors')==36,
        v.get('every_emitted_pairing_is_full_group_score_then_lex_minimum') is True,
        v.get('canonical_pairings_unique') is True, p.get('stable_aut_content_sha256')==EXPECTED_STABLE,
        e.get('stable_aut_content_sha256')==EXPECTED_STABLE, f.get('aut_canonical_sha256')==EXPECTED_STABLE,
        len(er)==37,
    ]
    if not all(checks): raise RuntimeError('certification regression mismatch')
    out={'schema':'STAGE32_18A_D16_TRAVERSAL_AND_PROVENANCE_CERTIFICATE_V1','verdict':'PASS_EXACT_B6_TRAVERSAL_CERTIFICATE_AND_STABLE_AUT_PROVENANCE','exact_norm_ball_cap_survivors':17833,'symmetry_breaker_survivors':232,'full_aut_canonical_survivors_including_zero':37,'canonical_nonzero_survivors':36,'exact_and_fast_canonical_sets_identical':True,'stable_aut_content_sha256':EXPECTED_STABLE,'exact_dump_sha256':file_sha(a.exact_dump),'fast_dump_sha256':file_sha(a.fast_dump),'d16_b6_numerical_credit_basis_certified':True,'scope':'B6_TRAVERSAL_CERTIFICATION_GATE_ONLY__NOT_FULL_D16_ROW','AUDIT_STATUS':'PENDING','THEOREM_CREDIT':False,'RECEIVER_CREDIT':False,'FULL_D16_G0_ROW_COMPLETE':False,'FULL_D176_D192_NUMERICAL_ORBIT_CENSUS':False,'R29_LG2_NUMERICAL_COMPONENT_COMPLETE':False,'R29_LG2':'NOT_DISCHARGED','G10_LOWGENUS_PICARD':'AMBER','next_item_after_hostile_audit_pass':'32-18B-D16-AUT-CANONICAL-BOUNDED-PRODUCTION'}
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,sort_keys=True))
if __name__=='__main__': main()
