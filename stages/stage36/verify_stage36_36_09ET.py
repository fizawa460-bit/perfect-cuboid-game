#!/usr/bin/env python3
import hashlib,itertools,json,math,runpy,subprocess
from array import array
from collections import Counter,defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EO='stages/stage36/36-09EO/rho-point-search-free-sel2-evaluator-preflight.json'
EP='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'
EPV='stages/stage36/verify_stage36_36_09EP.py'
ES='stages/stage36/36-09ES/rho-legendre-pattern-classification-preflight.json'
ESV='stages/stage36/verify_stage36_36_09ES.py'
EH='stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json'
EI='stages/stage36/36-09EI/bounded-rho-no4-no3-screen-preflight.json'
EK='stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json'
SOURCE='stages/stage36/36-09ET/rho-template-realization-nearmiss-expansion-source-lock.md'
CERT='stages/stage36/36-09ET/rho-template-realization-nearmiss-expansion-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EO:'bb76c05c7549ebb243a193376691138d8e01a7fb',
 EP:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a',
 EPV:'ea98901ddf3d6a9a579ea9db63ef5a44d7346e32',
 ES:'1a464aaffb328dc5068cda2e6f3a5073bc9d7f69',
 ESV:'e32e84f5fa0957f9b08904928d563f3815e64264',
 EH:'d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37',
 EI:'979a2d58384d751a98c74555abf9581d95b30d37',
 EK:'f6af11a0f7fd8a303531b2a587b7446c382a84c5',
 SOURCE:'8028ff70fbf0f615e8726fd7254518f5f7fb23a0',
 CERT:'6130e12a668c66fa181b1e9a6be17c9219257002',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
eo=load(EO);ep=load(EP);es=load(ES);eh=load(EH);ei=load(EI);ek=load(EK);c=load(CERT)
assert c['entry_authority']['v272_exact_head']=='b017efc62d7c9a362da52fe0c1b351315ef8c95f'
assert c['entry_authority']['v272_promotion_ci']=='34360323530/102495334858'
assert c['entry_authority']['36_09ET_entry_allowed'] is True
assert ep['support_matrix']['criterion_necessary_and_sufficient'] is True
assert es['abstract_matrix_theorem']['template_matching_sufficient_for_sel2_dimension_2_when_template_rank_is_2n_minus_2'] is True
assert eh['rank_and_torsion_criterion']['sel2_dimension_condition']==2
assert ek['literal_orbit_theorem']['positive_literal_orbit_complete'] is True

# Load exact-green ES machinery only after immutable hash-locking it.
ns=runpy.run_path(str(ROOT/ESV))
canonical_object=ns['canonical_object'];phash=ns['phash'];matrix_from_pattern=ns['matrix_from_pattern']
matrix_support=ns['matrix_support'];rank=ns['rank']

# Fast radical-support factorization for the 1..2000 targeted realization scan.
B=2000
LIMIT=2*B*B
spf=array('I',range(LIMIT+1))
if LIMIT>=1:spf[1]=1
for i in range(2,math.isqrt(LIMIT)+1):
    if spf[i]==i:
        for j in range(i*i,LIMIT+1,i):
            if spf[j]==j:spf[j]=i

def pf(n):
    n=abs(n);out=[]
    while n>1:
        p=int(spf[n]);out.append(p)
        while n%p==0:n//=p
    return out

def v2(n):
    n=abs(n);z=0
    while n%2==0:z+=1;n//=2
    return z

def fast_datum(a,b):
    N=a*a-b*b;d=a*b;P=N+2*d;Q=N-2*d
    assert abs(P)<=LIMIT and abs(Q)<=LIMIT
    SP=sorted(q for q in pf(P) if q!=2);SQ=sorted(q for q in pf(Q) if q!=2)
    dpr=set()
    for x in (a,b,a-b,a+b):
        for q in pf(x):
            if q!=2:dpr.add(q)
    SD=sorted(q for q in dpr if P%q and Q%q)
    assert not(set(SP)&set(SQ) or set(SP)&set(SD) or set(SQ)&set(SD))
    odd=sorted(SP+SQ+SD)
    labels={q:('P' if q in SP else ('Q' if q in SQ else 'D')) for q in odd}
    g=math.gcd(abs(P),abs(Q));r=0 if g==1 else 1;A=P//(2**r);BB=Q//(2**r)
    eps='shallow' if v2(A*A-BB*BB)==4 else 'deep'
    return odd,labels,eps

def orbit(a,b):
    x=abs(a-b);y=a+b;g=math.gcd(x,y);x//=g;y//=g
    return sorted({(a,b),(b,a),(x,y),(y,x)})

# The EK identities imply this is a genuine four-point partition. Replay the
# defining P,Q transformations on every representative actually used.
def PQ(a,b):
    return a*a+2*a*b-b*b, a*a-2*a*b-b*b

def check_orbit_identities(a,b):
    P,Q=PQ(a,b);Pi,Qi=PQ(b,a)
    assert (Pi,Qi)==(-Q,-P)
    Pc,Qc=PQ(a+b,a-b)
    assert (Pc,Qc)==(2*P,-2*Q)

# Coarse ES profile targets, allowing the global P/Q swap.
def parse_vertex(s):return (s[0],int(s[1:]))
targets={t['id']:Counter(parse_vertex(v) for v in t['vertices']) for t in es['templates']}
def coarse_targets(odd,labels,eps):
    if eps!='shallow':return []
    a=Counter((labels[q],q%8) for q in odd)
    lm={'P':'Q','Q':'P','D':'D'}
    z=Counter((lm[labels[q]],q%8) for q in odd)
    return [tid for tid,v in targets.items() if a==v or z==v]

rows=0;reps=0;candidates=[]
for a in range(1,B+1):
    for b in range(1,B+1):
        if a==b or math.gcd(a,b)!=1:continue
        rows+=1
        inside=[x for x in orbit(a,b) if x[0]<=B and x[1]<=B]
        if (a,b)!=min(inside):continue
        reps+=1;check_orbit_identities(a,b)
        odd,labels,eps=fast_datum(a,b)
        tids=coarse_targets(odd,labels,eps)
        if not tids:continue
        h=phash(canonical_object(a,b))
        candidates.append(((a,b),inside,tids,h))
assert rows==2433174
assert reps==811155
assert len(candidates)==11
assert sum(len(x[1]) for x in candidates)==44

old_hash_to_id={t['sha256']:t['id'] for t in es['templates']}
old_reps={(1,2),(1,5),(2,7),(2,9),(3,47),(6,43)}
matched=[x for x in candidates if x[3] in old_hash_to_id]
near=[x for x in candidates if x[3] not in old_hash_to_id]
assert {x[0] for x in matched}==old_reps
assert sum(len(x[1]) for x in matched)==24
assert len(near)==5 and sum(len(x[1]) for x in near)==20
assert {x[0] for x in near}=={(1,277),(1,333),(1,1323),(81,317),(134,863)}
assert all(x[2]==['T6'] for x in near)

# Only the five targeted near misses receive a Selmer-rank replay.
near_results={}
for rep,inside,tids,h in near:
    M,G,labels,eps=matrix_support(*rep);n=len(G);r=rank(M);dim=2*n-r
    near_results[rep]=(h,n,r,dim)
expected_near={
 (1,277):('de74adf6b206d460c3863a55f9ea306aac136fc36bc9d86bb20cbedb73ff36c7',10,18,2),
 (1,333):('f22028ff420881c6bf0379bf2aa4d9f6d0c91bec911f9348c18827b1e4d09921',10,18,2),
 (1,1323):('fa0099a7c51111569b06af3a6f74a678e4001ea590b4a88c8007bc73f21232ce',10,16,4),
 (81,317):('878b70e2136f234d743f7b79ad9bedcf49994dd0d4c6ebd3368567d4c504ecd1',10,16,4),
 (134,863):('1d016b4933622e66e1d3a4d83cb7fd349366d53abe67f72feccf77d86bad481b',10,18,2),
}
assert near_results==expected_near

# Reconstruct T7..T9 as abstract patterns and verify maximal rank independently
# of the parameter-specific matrix.
newmap={'T7':(1,277),'T8':(1,333),'T9':(134,863)}
for t in c['new_templates']:
    rep=newmap[t['id']];obj=canonical_object(*rep);h=phash(obj);MT,n=matrix_from_pattern(obj)
    assert h==t['sha256']==expected_near[rep][0]
    assert n==t['n']==10 and rank(MT)==t['rank']==18==2*n-2
    assert t['sel2_dimension']==2 and t['global_sufficient_template'] is True
assert c['template_library_impact']['expanded_exact_template_count']==9
assert c['template_library_impact']['matching_any_T1_through_T9_is_sufficient_for_sel2_dimension_2'] is True
assert c['template_library_impact']['T1_through_T9_exhaust_all_max_rank_patterns'] is False

# Deterministic representative digest.
records=[]
for rep,inside,tids,h in candidates:
    if h in old_hash_to_id:dim=2;status=old_hash_to_id[h]
    else:
        dim=near_results[rep][3];status='NEW_MAX' if dim==2 else 'DEF4'
    records.append((rep[0],rep[1],h,dim,status))
records.sort()
txt=''.join(f'{a},{b},{h},{dim},{status}\n' for a,b,h,dim,status in records)
digest=hashlib.sha256(txt.encode()).hexdigest()
assert digest=='a3b974818373c1d22601061f77d2f0c8ef494234849d517b484c624fa999429c'
ts=c['targeted_scan']
assert ts['ordered_row_count']==rows
assert ts['coarse_profile_match_row_count']==44 and ts['coarse_profile_literal_orbit_count']==11
assert ts['exact_old_template_match_row_count']==24 and ts['new_exact_realizations_of_T1_through_T6']==0
assert ts['near_miss_row_count']==20 and ts['near_miss_literal_orbit_count']==5
assert ts['candidate_rep_digest_sha256']==digest

# Exact EH no-4/no-3 checks for the three new orbit seeds.
def is_square(n):
    if n<0:return False
    r=math.isqrt(n);return r*r==n
def psi3_coeffs(a,b):
    N=a*a-b*b;M=a*a+b*b;d=a*b
    return [-64*N*N*d*d*(M**4+4*N*N*d*d),-192*N*N*d*d*M*M,-96*N*N*d*d,4*M*M,3]
def vals_mod(cs,q):
    out=[]
    for x in range(q):
        y=0
        for z in reversed(cs):y=(y*x+z)%q
        out.append(y)
    return out
checks={
 (1,277):-170029248,
 (1,333):-295405632,
 (134,863):-672400871568,
}
for rep,eightNd in checks.items():
    a,b=rep;N=a*a-b*b;d=a*b
    assert 8*N*d==eightNd
    assert not is_square(eightNd) and not is_square(-eightNd)
    cs=psi3_coeffs(a,b)
    assert [x%5 for x in cs]==[4,0,4,0,3]
    assert vals_mod(cs,5)==[4,1,3,3,1]

# Literal orbits and registry expansion.
new_orbits=[
 ['1/277','138/139','139/138','277'],
 ['1/333','166/167','167/166','333'],
 ['134/863','729/997','863/134','997/729'],
]
assert c['new_fixed_parameter_exclusions']['orbits']==new_orbits
newset=set(sum(new_orbits,[]));oldset=set(eo['criterion_consumption']['expanded_fixed_parameter_registry'])
assert len(newset)==12 and newset.isdisjoint(oldset)
assert len(oldset)==24
impact=c['new_fixed_parameter_exclusions']
assert impact['new_parameter_count']==12 and impact['previous_registry_count']==24 and impact['expanded_registry_count']==36
assert impact['each_new_fixed_parameter_receiver_sector_empty'] is True
assert c['route_result']['next_leaf']=='36-09EU_RHO_T6_PROFILE_LEGENDRE_RIGIDITY_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09ET verified: targeted 1..2000 six-template realization scan has no new T1..T6 matches; five T6-profile near-miss orbits yield three new rank-18 templates T7..T9, all satisfying EH no4/no3, adding 12 exact fixed-p exclusions (registry 24->36).')
