#!/usr/bin/env python3
import json,runpy,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EP='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'
EQV='stages/stage36/verify_stage36_36_09EQ.py'
ER='stages/stage36/36-09ER/rho-legendre-core-parity-preflight.json'
EX='stages/stage36/36-09EX/rho-t6-controlled-radical-relaxation-preflight.json'
EXV='stages/stage36/verify_stage36_36_09EX.py'
SOURCE='stages/stage36/36-09EY/rho-radical-refinement-rank-compression-source-lock.md'
CERT='stages/stage36/36-09EY/rho-radical-refinement-rank-compression-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EP:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a',
 EQV:'bcae53e30d7cc22832365eaae3fd3d205b730b75',
 ER:'2994b87f098fad43d79cec17468889f72724b24b',
 EX:'75663e2fbde9189a9c570a2075b76490151cd0b6',
 EXV:'3adbd3fe00b2e4c85261862f8e949a5c8af09c03',
 SOURCE:'fbc813e48f60e4651e01fcb826626ec561645d43',
 CERT:'dbad704b6e05eb0a08ff33b1794436cab7f94fc6',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)

ep=load(EP);er=load(ER);ex=load(EX);c=load(CERT)
assert ep['support_matrix']['sel2_dimension_formula']=='dim_F2 Sel^2(E_rho,p/Q)=2n-rank_F2 M_R(R(a,b))'
assert ep['support_matrix']['criterion_necessary_and_sufficient'] is True
assert er['odd_matching_parity_criterion']['sufficient_for_rank_2n_minus_2'] is True
assert ex['controlled_radical_result']['expanded_exact_sufficient_template_count']==17
assert c['schema']=='STAGE36_36_09EY_RHO_T6_RADICAL_REFINEMENT_RANK_COMPRESSION_PREFLIGHT_V1R1'
assert c['repair']=='T17_canonical_pattern_peel_row_replaces_raw_arithmetic_peel_row_only'
assert c['entry_authority']['v282_exact_head']=='fce8877acde317f1215c1804a9d93033209c8df0'
assert c['entry_authority']['v282_exact_head_ci']=='34412114871/102668682937'
rep=c['template_replay_representation']
assert rep['T10_through_T17']=='canonical 36-09ES abstract pattern matrices promoted by 36-09EX'
assert rep['T17_v283_raw_row']=={'leaf_pivots':17,'residual_size':15,'residual_rank':13,'residual_nullity':2}
assert rep['T17_v283r1_canonical_row']=={'leaf_pivots':18,'residual_size':14,'residual_rank':12,'residual_nullity':2}
assert rep['repair_changes_nullity_or_sel2'] is False

# Load the exact-green EQ and EX constructions after immutable blob locks.
eqns=runpy.run_path(str(ROOT/EQV))
rank=eqns['rank'];matrix_support=eqns['matrix_support']
exns=runpy.run_path(str(ROOT/EXV))
FACT=exns['FACT'];canonical_from_support=exns['canonical_from_support'];matrix_from_pattern=exns['matrix_from_pattern']

# A legal leaf deletion is an exact rank-one split. Verify the identity at every
# deterministic peel step rather than trusting only the final rank.
def replay_leaf_rank_identity(M):
    A=[list(r) for r in M];k=0
    while A and A[0]:
        nr=len(A);nc=len(A[0]);chosen=None
        for i in range(nr):
            js=[j for j in range(nc) if A[i][j]]
            if len(js)==1:chosen=(i,js[0]);break
        if chosen is None:
            for j in range(nc):
                ii=[i for i in range(nr) if A[i][j]]
                if len(ii)==1:chosen=(ii[0],j);break
        if chosen is None:break
        i,j=chosen
        B=[[A[r][q] for q in range(nc) if q!=j] for r in range(nr) if r!=i]
        assert rank(A)==1+rank(B)
        A=B;k+=1
    return k,A

expected={x['id']:x for x in c['template_replay']}
small={
'T1':(2,1),'T2':(1,5),'T3':(2,7),'T4':(2,9),'T5':(6,43),
'T6':(3,47),'T7':(1,277),'T8':(1,333),'T9':(134,863),
}
seen=set()
for tid,(a,b) in small.items():
    M,G=matrix_support(a,b);n=len(G)
    k,H=replay_leaf_rank_identity(M);m=len(H);rh=rank(H)
    row=expected[tid]
    assert (n,k,m,rh,m-rh)==(row['n'],row['leaf_pivots'],row['residual_size'],row['residual_rank'],row['residual_nullity'])
    assert rank(M)==k+rh
    assert 2*n-rank(M)==m-rh==2
    seen.add(tid)

for t in ex['templates']:
    tid=t['id'];u=t['u'];f=FACT[u]
    SD=sorted({3}|set(f['u'])|set(f['b'])|set(f['q']))
    SP=sorted({7}|set(f['s']))
    SQ=sorted({41}|set(f['t']))
    obj=canonical_from_support(SD,SP,SQ)
    M,n=matrix_from_pattern(obj)
    k,H=replay_leaf_rank_identity(M);m=len(H);rh=rank(H)
    row=expected[tid]
    assert (n,k,m,rh,m-rh)==(row['n'],row['leaf_pivots'],row['residual_size'],row['residual_rank'],row['residual_nullity'])
    assert rank(M)==k+rh
    assert 2*n-rank(M)==m-rh==2
    seen.add(tid)

assert seen==set(expected)=={f'T{i}' for i in range(1,18)}
summary=c['replay_summary']
assert summary['template_count']==17
assert summary['all_residual_nullity_two'] is True
assert summary['leaf_only_template_count']==10
assert summary['genuine_residual_core_template_count']==7

th=c['leaf_core_theorem']
assert th['rank_identity']=='rank_F2(M)=k+rank_F2(H)'
assert th['sel2_identity']=='dim_F2 Sel^2(E_rho,p/Q)=nullity_F2(H)'
assert th['sel2_dimension_2_iff']=='nullity_F2(H)=2'
assert th['criterion_exact_not_only_sufficient'] is True
inv=c['leaf_extension_invariance']
assert inv['arbitrary_factor_split_preserves_sel2'] is False
assert inv['residual_core_change_must_be_checked'] is True
assert c['route_result']['next_leaf']=='36-09EZ_RHO_CORE_NULLITY_CONTROLLED_RADICAL_SEARCH_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for key,val in c['scope_firewalls'].items():assert val is False,(key,val)
print('36-09EY V1R1 verified: leaf-core rank identity is exact; T17 canonical replay is k=18/core14/rank12/nullity2, and all T1..T17 retain residual nullity two. No new fixed-p/infinitude/parent receiver/endpoint credit.')
