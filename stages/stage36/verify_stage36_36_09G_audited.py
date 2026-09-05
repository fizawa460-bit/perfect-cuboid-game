#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
G=ROOT/'stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json'
BLIND=ROOT/'stages/stage36/36-09G/blind-rediscovery-only.json'
BASE='9309801b9caffa857adc5599ad5dd686d84d47d8'
AUDITED_HEAD='400237172efffe75232d485d0ce96e4643002a72'
AUDIT_REVIEW=5120849260
CI_RUN=33960137385
CI_JOB=101290482391
BLIND_COMMIT='30c37a19053638cdf806e88fa726f8d099146306'
COMPARISON_COMMIT='0ea755a7c48b472fdb377b6a044596135de58b66'
CERT_BLOB='bae34622d8ab7f94fafab4a290e770a3830e47fc'
BLIND_BLOB='3f00245edc26394d43a16a699d99634eed831909'
MERGE_PARENT='c8a876838882c91c078c85da5c88d131b151ac40'
MERGED_MAIN='605ef83aae1ba2804537eb6dc36695ca80ade412'
MERGED_V26_BLOB='d50e7ce0e67984bb8598fa1b67d1e86b245ac492'
EXACT_TRANSFER_PATHS=[
 'stages/stage36/36-09G/blind-rediscovery-only.json',
 'stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json',
 'stages/stage36/verify_stage36_36_09G.py',
 'stages/stage36/MAIN-STATE.json',
 '.github/workflows/stage36-bootstrap-audit.yml',
]

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def git(*args:str,check=True)->subprocess.CompletedProcess:
    return subprocess.run(['git',*args],cwd=ROOT,check=check,capture_output=True,text=True)
def out(*args:str)->str:
    return git(*args).stdout.strip()
def show_bytes(spec:str)->bytes:
    return subprocess.check_output(['git','show',spec],cwd=ROOT)
def blob_bytes(b:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def blob(p:Path)->str:
    return blob_bytes(p.read_bytes())
def rank_f2(rows):
    a=[list(map(int,r)) for r in rows]; m=len(a); n=len(a[0]); rank=0
    for col in range(n):
        p=next((i for i in range(rank,m) if a[i][col]),None)
        if p is None: continue
        a[rank],a[p]=a[p],a[rank]
        for i in range(m):
            if i!=rank and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank
def walk(obj):
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield str(k); yield from walk(v)
    elif isinstance(obj,list):
        for v in obj: yield from walk(v)
    elif isinstance(obj,str): yield obj

def main()->None:
    # Original pre-squash chronology is inspected by immutable git objects.
    req(out('show','-s','--format=%P',BLIND_COMMIT)==BASE,'blind snapshot parent moved')
    req(out('show','-s','--format=%P',COMPARISON_COMMIT)==BLIND_COMMIT,'comparison is not direct child of blind snapshot')
    blind_bytes=show_bytes(f'{BLIND_COMMIT}:stages/stage36/36-09G/blind-rediscovery-only.json')
    req(blob_bytes(blind_bytes)==BLIND_BLOB,'immutable blind blob moved')
    req(git('cat-file','-e',f'{BLIND_COMMIT}:stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json',check=False).returncode!=0,'comparison certificate existed at blind snapshot')
    comparison_bytes=show_bytes(f'{COMPARISON_COMMIT}:stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json')
    req(blob_bytes(comparison_bytes)==CERT_BLOB,'comparison certificate blob moved')
    b=json.loads(blind_bytes.decode())
    cc=b['chronology_contract']
    req(cc['contains_route_ledger_mapping'] is False and cc['contains_reusable_method_comparison'] is False and cc['contains_selected_route'] is False,'blind chronology flags moved')
    tokens=list(walk(b))
    forbidden={'mapped_ledger','selected_route','refreshed_candidate_ledger','arsenal_comparison_after_blind_snapshot','route_ledger_mapping_after_blind_snapshot'}
    req(not any(x in forbidden for x in tokens),'blind snapshot contains post-blind ledger/comparison key')
    req(not any('S34-W' in x or re.match(r'^B(?:[1-9]|1[01])_',x) for x in tokens),'blind snapshot contains Arsenal or historical route identifier')

    # Squash merge provenance: exact audited content, not false ancestor semantics.
    req(out('show','-s','--format=%P',MERGED_MAIN)==MERGE_PARENT,'36-09G merge parent moved')
    req(git('merge-base','--is-ancestor',BASE,MERGE_PARENT,check=False).returncode==0,'audit base not ancestor of merge parent')
    changed=[x for x in out('diff','--name-only',BASE,MERGE_PARENT).splitlines() if x]
    req(changed,'expected nonempty audit-to-merge freshness gap')
    allowed=lambda p: p.startswith('stages/stage35-ex/') or p.startswith('.github/workflows/stage35')
    req(all(allowed(p) for p in changed),f'36-09G freshness gap touched protected scope: {[p for p in changed if not allowed(p)]}')
    for p in EXACT_TRANSFER_PATHS:
        req(out('rev-parse',f'{AUDITED_HEAD}:{p}')==out('rev-parse',f'{MERGED_MAIN}:{p}'),f'squash merge did not preserve audited blob: {p}')
    req(out('rev-parse',f'{MERGED_MAIN}:stages/stage36/MAIN-STATE.json')==MERGED_V26_BLOB,'merged V26 blob moved')
    req(out('rev-parse',f'{AUDITED_HEAD}:stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json')==CERT_BLOB,'audited certificate blob moved')
    req(out('rev-parse',f'{AUDITED_HEAD}:stages/stage36/36-09G/blind-rediscovery-only.json')==BLIND_BLOB,'audited blind blob moved')
    req(blob(G)==CERT_BLOB and blob(BLIND)==BLIND_BLOB,'working 36-09G artifact drift')

    # Cheap independent mathematics replay.
    c=json.loads(G.read_text())
    r=c['common_jminus_exact_reduction']
    M=r['common_pair_matrix_F2']
    req(M==[[1,1,1],[1,1,0]] and rank_f2(M)==2,'common J-minus rank moved')
    req(r['kernel_dimension']==1 and r['kernel_generator']==[1,1,0],'common J-minus kernel moved')
    req(r['reduced_receiver']==['D=s+t+1 is a rational square','B*C=(s+1)*(s+t) is a rational square'],'common J-minus reduced receiver moved')
    req(r['strict_rational_properness_witness_obtained'] is False,'rational strictness falsely promoted')
    sr=c['single_representative_full_character_check']
    rows=sr['row_dictionary_in_BCD_after_A_square']
    for name,data in sr['representatives'].items():
        req(rank_f2([rows[x] for x in data['rows']])==3 and data['rank_F2']==3,f'{name}: full three-character rank moved')
    req(c['route_selection']['selected_route']=='B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER','B10 selection moved')
    req(c['route_selection']['S34_W01_TRIGGERED'] is False and c['route_selection']['S34_W01_PREFLIGHT_REQUIRED'] is True,'S34-W01 boundary moved')
    req(all(v is False for v in c['claims'].values()),'36-09G certificate higher credit leaked')

    s=json.loads(STATE.read_text())
    req(s['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V27_THIN_36_09G_AUDITED','V27 schema moved')
    req(s['status']=='ACTIVE' and s['base_main_sha']==MERGED_MAIN,'V27 authority/base moved')
    a=s['authority_frontier']['36-09G']
    req(a['status']=='AUDITED_FRESH_BREADTH_COMMON_JMINUS_SUBRECEIVER','36-09G audited status moved')
    req(a['pr']==1602 and a['hostile_reaudit_review']==AUDIT_REVIEW and a['audited_head']==AUDITED_HEAD,'36-09G audit identity moved')
    req(a['exact_head_ci']==f'{CI_RUN}/{CI_JOB}' and a['certificate_blob_sha']==CERT_BLOB and a['blind_snapshot_blob_sha']==BLIND_BLOB,'36-09G audit evidence moved')
    req(a['merged_main_sha']==MERGED_MAIN and a['promotion_status']=='HOSTILE_REAUDIT_PASS','36-09G promotion status moved')
    req(a['BLIND_PROVENANCE_FAIL_CLOSED'] is True and a['B10_STATUS']=='LIVE_COMMON_TWO_JMINUS_SUBRECEIVER','audited B10/provenance moved')
    req(a['S34_W01_STATUS']=='APPLICABILITY_CANDIDATE_PREFLIGHT_REQUIRED' and a['S34_W01_TRIGGERED'] is False,'S34-W01 audited boundary moved')
    req(a['COMMON_SUBRECEIVER_RATIONAL_STRICTNESS_PROVED'] is False,'rational strictness falsely promoted in V27')
    req(s['cycle_ledger']['counts']=={'live':1,'untested':3,'blocked':6,'dominated':1},'audited cycle counts moved')
    req(s['current']['unit']=='36-09H' and s['current']['36_09H_entry_allowed'] is True,'36-09H not unlocked')
    req(s['current']['next_exact_leaf']=='36-09H_COMMON_JMINUS_FACTOR_SQUARECLASS_DESCENT_PREFLIGHT','36-09H next leaf moved')
    req(s['promotion_gates']['common_jminus_subreceiver_rational_strictness_proved'] is False and s['promotion_gates']['S34_W01_finite_squareclass_branch_family_proved'] is False,'promotion gate leaked')
    req(s['promotion_gates']['R29_CAMP2_closed'] is False and all(v is False for v in s['claims'].values()),'higher Stage36 credit leaked')
    av=s['audit_verifier']; req(av['path']=='stages/stage36/verify_stage36_36_09G_audited.py' and av['blob_sha']==blob(ROOT/av['path']),'audit verifier self-lock moved')

    print('PASS STAGE36_36_09G_HOSTILE_AUDITED_PROMOTION')
    print(f'audit_review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}; CI={CI_RUN}/{CI_JOB}')
    print('original blind chronology rechecked by git objects; squash merge content exact; freshness gap Stage35-EX only')
    print('math unchanged: common J-minus rank2/kernel1; B10 LIVE; S34-W01 preflight only; 36-09H unlocked')

if __name__=='__main__': main()
