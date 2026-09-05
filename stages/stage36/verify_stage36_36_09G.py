#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json'
BLIND=ROOT/'stages/stage36/36-09G/blind-rediscovery-only.json'
F=ROOT/'stages/stage36/36-09F/paired-legendre-receiver-intersection-preflight.json'
E=ROOT/'stages/stage36/36-09E/character-elliptic-quotient-arithmetic-preflight.json'
PHYS=ROOT/'stages/stage36/36-03/physical-open-boundary.json'
SIGN=ROOT/'stages/stage29/29-02ha/exact-sign-cover-model.md'
CYCLE=ROOT/'docs/research-os/policies/cycle-exploration-safety-protocol.md'
W01=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
W02=ROOT/'docs/arsenal/cards/formal/S34-W02.md'
W03=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
BASE='9309801b9caffa857adc5599ad5dd686d84d47d8'
BLIND_COMMIT='30c37a19053638cdf806e88fa726f8d099146306'
BLIND_BLOB='3f00245edc26394d43a16a699d99634eed831909'
COMPARISON_COMMIT='0ea755a7c48b472fdb377b6a044596135de58b66'
CERT_BLOB='bae34622d8ab7f94fafab4a290e770a3830e47fc'
LOCKS={
 F:'0615844de212eb3644f15cd3f5577b37ccc3855a',
 E:'081b704fecaa3bd39e6a523ee7beaefe706683f4',
 PHYS:'fc1947b2de08f7d8a104bdc91902b20e88635349',
 SIGN:'fc2d5284a259750f45d2d756a952002671e3bccc',
 CYCLE:'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',
 W01:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
 W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b',
 W03:'1d5275321f42768a6414d4610ac912c63be43f96',
}

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def blob_bytes(b:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def blob(p:Path)->str:
    return blob_bytes(p.read_bytes())
def git(*args:str,check=True,text=True):
    return subprocess.run(['git',*args],cwd=ROOT,check=check,capture_output=True,text=text)
def git_out(*args:str)->str:
    return git(*args).stdout.strip()
def git_show_bytes(spec:str)->bytes:
    return subprocess.check_output(['git','show',spec],cwd=ROOT)
def rank_f2(rows):
    a=[list(map(int,r)) for r in rows]; m=len(a); n=len(a[0]); rank=0
    for col in range(n):
        p=next((i for i in range(rank,m) if a[i][col]),None)
        if p is None: continue
        a[rank],a[p]=a[p],a[rank]
        for i in range(m):
            if i!=rank and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank,a

def walk(obj):
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield str(k)
            yield from walk(v)
    elif isinstance(obj,list):
        for v in obj: yield from walk(v)
    elif isinstance(obj,str):
        yield obj

def main()->None:
    # Immutable chronology: blind artifact is one exact parent-before-comparison commit.
    req(git_out('show','-s','--format=%P',BLIND_COMMIT)==BASE,'blind snapshot parent is not exact current base')
    req(git_out('show','-s','--format=%P',COMPARISON_COMMIT)==BLIND_COMMIT,'comparison commit is not direct child of blind snapshot')
    req(git('merge-base','--is-ancestor',COMPARISON_COMMIT,'HEAD',check=False).returncode==0,'comparison commit not ancestor of HEAD')
    blind_bytes=git_show_bytes(f'{BLIND_COMMIT}:stages/stage36/36-09G/blind-rediscovery-only.json')
    req(blob_bytes(blind_bytes)==BLIND_BLOB,'immutable blind snapshot blob drift')
    req(git('cat-file','-e',f'{BLIND_COMMIT}:stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json',check=False).returncode!=0,'comparison certificate already existed at blind snapshot commit')
    comparison_bytes=git_show_bytes(f'{COMPARISON_COMMIT}:stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json')
    req(blob_bytes(comparison_bytes)==CERT_BLOB,'comparison certificate blob at comparison commit drift')
    req(blob(BLIND)==BLIND_BLOB,'working blind snapshot drift')
    req(blob(CERT)==CERT_BLOB,'working 36-09G certificate drift')

    b=json.loads(blind_bytes.decode())
    req(b['schema']=='STAGE36_36_09G_BLIND_REDISCOVERY_ONLY_V1','blind schema moved')
    req(b['base_main_sha']==BASE,'blind base moved')
    cc=b['chronology_contract']
    req(cc['contains_route_ledger_mapping'] is False and cc['contains_reusable_method_comparison'] is False and cc['contains_selected_route'] is False,'blind chronology flags moved')
    tokens=list(walk(b))
    forbidden_exact={'mapped_ledger','selected_route','refreshed_candidate_ledger','arsenal_comparison_after_blind_snapshot','route_ledger_mapping_after_blind_snapshot'}
    req(not any(x in forbidden_exact for x in tokens),'blind snapshot contains ledger/comparison key')
    req(not any('S34-W' in x or re.match(r'^B(?:[1-9]|1[01])_',x) for x in tokens),'blind snapshot contains Arsenal or historical route identifier')
    ids=[x['id'] for x in b['blind_generated_views']]
    req(ids==['COMMON_TWO_JMINUS','SINGLE_REP_THREE_CHARACTER','FULL_FOUR_CHARACTER','CONIC_CHAIN','STANDARD_CAMPEDELLI_TRANSFER','MULTIPLACE_RECIPROCITY','MOVING_FAMILY_MW_CONGRUENCE','ASYMPTOTIC_SIEVE'],'blind candidate inventory moved')
    bj=next(x for x in b['blind_generated_views'] if x['id']=='COMMON_TWO_JMINUS')
    req(bj['squareclass_matrix_BCD']==[[1,1,1],[1,1,0]] and bj['rank_F2']==2 and bj['kernel_dimension']==1 and bj['kernel_generator']==[1,1,0],'blind common Jminus algebra moved')
    br,_=rank_f2(bj['squareclass_matrix_BCD']); req(br==2,'blind common Jminus matrix rank wrong')
    sr=next(x for x in b['blind_generated_views'] if x['id']=='SINGLE_REP_THREE_CHARACTER')
    rows=sr['row_dictionary_BCD_after_A_square']
    for names in sr['representative_row_sets'].values():
        rr,_=rank_f2([rows[n] for n in names]); req(rr==3,'blind single-representative rank is not 3')

    for p,sha in LOCKS.items(): req(blob(p)==sha,f'locked source drift: {p}')
    c=json.loads(CERT.read_text())
    req(c['schema']=='STAGE36_36_09G_ENDPOINT_EQUIVALENCE_BREADTH_REFRESH_V2','36-09G schema moved')
    req(c['base_main_sha']==BASE,'36-09G base moved')
    bp=c['blind_provenance']
    req(bp['snapshot_commit']==BLIND_COMMIT and bp['snapshot_blob_sha']==BLIND_BLOB and bp['snapshot_expected_parent']==BASE,'blind provenance identity moved')
    req(bp['full_comparison_certificate_absent_at_snapshot_commit'] is True,'blind chronology firewall moved')

    e=json.loads(E.read_text()); f=json.loads(F.read_text())
    req(e['four_family_collapse']['common_J_MINUS_pair_each_representative']==['E_t_PLUS','E_t_MINUS'],'common Jminus source moved')
    ps=e['physical_squareclass_restriction']['chart_ratio_consequences']
    req(ps=={'t=x/y':'square','s=z/y':'square','t+1=(x+y)/y':'square'},'physical squareclass source moved')
    rhs={k:v['rhs'] for k,v in f['four_paired_legendre_equations'].items()}
    req(rhs['E_t_PLUS']=='B*C*D' and rhs['E_t_MINUS']=='A*B*C','common Jminus RHS source moved')

    r=c['common_jminus_exact_reduction']
    req(r['common_pair_matrix_F2']==[[1,1,1],[1,1,0]],'common pair matrix moved')
    rr,_=rank_f2(r['common_pair_matrix_F2']); req(rr==2 and r['rank_F2']==2 and r['kernel_dimension']==1,'common pair rank/kernel moved')
    kg=r['kernel_generator']; req(kg==[1,1,0] and all(sum(a*b for a,b in zip(row,kg))%2==0 for row in r['common_pair_matrix_F2']),'common pair kernel invalid')
    req(r['reduced_receiver']==['D=s+t+1 is a rational square','B*C=(s+1)*(s+t) is a rational square'],'reduced receiver moved')
    req(r['endpoint_pushes_to_common_subreceiver'] is True and r['strict_rational_properness_witness_obtained'] is False,'properness firewall moved')

    rows2=c['single_representative_full_character_check']['row_dictionary_in_BCD_after_A_square']
    reps=c['single_representative_full_character_check']['representatives']
    for name,data in reps.items():
        q,_=rank_f2([rows2[x] for x in data['rows']]); req(q==3 and data['rank_F2']==3,f'{name}: full-character rank moved')

    mapping=c['route_ledger_mapping_after_blind_snapshot']
    req(mapping['COMMON_TWO_JMINUS']=={'mapped_ledger':'B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER','status':'LIVE'},'post-blind B10 mapping moved')
    req(mapping['CONIC_CHAIN']['mapped_ledger']=='B3_FINITE_CURVE_OR_COVER_DECOMPOSITION','post-blind B3 mapping moved')
    ar=c['arsenal_comparison_after_blind_snapshot']
    req(ar['S34_W01']['status']=='APPLICABILITY_CANDIDATE_PREFLIGHT_REQUIRED','S34-W01 boundary moved')
    req(ar['S34_W02']['status']=='NOT_TRIGGERED' and ar['S34_W03']['status']=='NOT_EXECUTED_ON_NEW_SUBRECEIVER','Arsenal firewalls moved')
    req('SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT' in W01.read_text(),'S34-W01 identity moved')
    req('GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION' in W02.read_text(),'S34-W02 identity moved')
    req('RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION' in W03.read_text(),'S34-W03 identity moved')

    ledger=c['refreshed_candidate_ledger']
    req(ledger['B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER']=='LIVE_COMMON_TWO_JMINUS_SUBRECEIVER','B10 live route moved')
    req(ledger['B6_FIBRATION_TO_CURVE_BASE']=='BLOCKED_BY_EXACT_ENDPOINT_EQUIVALENCE_NO_PROPER_RECEIVER_GAIN','B6 block moved')
    req(ledger['B3_FINITE_CURVE_OR_COVER_DECOMPOSITION']=='UNTESTED' and ledger['B7_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER']=='UNTESTED' and ledger['B11_DIRECT_MULTIPLACE_ADELIC_RECIPROCITY']=='UNTESTED','untested candidates not preserved')
    req(ledger['counts']=={'live':1,'untested':3,'blocked':6,'dominated':1},'ledger counts moved')
    route=c['route_selection']
    req(route['selected_route']=='B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER' and route['selected_receiver']=='PHYSICAL_COMMON_TWO_JMINUS_SUBRECEIVER','selected route moved')
    req(route['S34_W01_TRIGGERED'] is False and route['S34_W01_PREFLIGHT_REQUIRED'] is True,'S34-W01 trigger firewall moved')
    req(route['next_route_after_hostile_audit']=='36-09H_COMMON_JMINUS_FACTOR_SQUARECLASS_DESCENT_PREFLIGHT','36-09H routing moved')
    cu=c['cycle_update']
    req(cu['fresh_EXHAUSTIVE_VIEW_AUDIT_after_36_09F'] is True and cu['fresh_BLIND_REDISCOVERY_after_36_09F'] is True,'fresh breadth not complete')
    req(cu['blind_snapshot_precedes_ledger_and_arsenal_commit'] is True,'chronology claim moved')
    req(all(v is False for v in c['claims'].values()),'36-09G higher credit leaked')

    print('PASS STAGE36_36_09G_ENDPOINT_EQUIVALENCE_BREADTH_REFRESH_V2')
    print(f'blind_commit={BLIND_COMMIT}; blind_blob={BLIND_BLOB}; comparison_commit={COMPARISON_COMMIT}; cert_blob={CERT_BLOB}')
    print('chronology fail-closed: blind-only parent commit -> ledger/Arsenal comparison child commit -> current audited boundary')
    print('math unchanged: common two J_MINUS rank2/kernel1; single-representative three-character rank3; B10 live; next 36-09H locked pending hostile audit')

if __name__=='__main__': main()
