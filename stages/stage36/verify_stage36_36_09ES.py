#!/usr/bin/env python3
import hashlib,itertools,json,math,runpy,subprocess
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EP='stages/stage36/36-09EP/rho-sel2-support-rank-criterion-preflight.json'
EP_VERIFY='stages/stage36/verify_stage36_36_09EP.py'
EQ='stages/stage36/36-09EQ/rho-legendre-graph-leaf-pivot-preflight.json'
ER='stages/stage36/36-09ER/rho-legendre-core-parity-preflight.json'
RECEIPT='stages/stage36/36-09ER/intermediate-hostile-audit-pass-consumption.json'
SOURCE='stages/stage36/36-09ES/rho-legendre-pattern-classification-source-lock.md'
CERT='stages/stage36/36-09ES/rho-legendre-pattern-classification-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EP:'4e3f103a3711220f1d5f6475f1fcff345b31ae7a',
 EP_VERIFY:'ea98901ddf3d6a9a579ea9db63ef5a44d7346e32',
 EQ:'ff4f8215b5e607c278b01f65aa858a5f038e0b35',
 ER:'2994b87f098fad43d79cec17468889f72724b24b',
 RECEIPT:'06240ead7dc71d973896120183b4011342553a68',
 SOURCE:'933ae803454f906e4ea38151158e5b53536ff917',
 CERT:'1a464aaffb328dc5068cda2e6f3a5073bc9d7f69',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
c=load(CERT);ep=load(EP);eq=load(EQ);er=load(ER);receipt=load(RECEIPT)
assert receipt['hostile_audit_review_id']==5154394408 and receipt['hostile_audit_result']=='PASS'
assert receipt['consumption_result']['36_09ES_entry_allowed'] is True
assert ep['support_matrix']['criterion_necessary_and_sufficient'] is True
assert eq['leaf_pivot_criterion']['sufficient_for_Sel2_dimension_2'] is True
assert er['eo_graph_certificate_closure']['all_exact_EO_max_rank_rows_have_graph_certificates'] is True

# Reuse the exact-green EP construction only after immutable hash-locking it.
ns=runpy.run_path(str(ROOT/EP_VERIFY))
matrix_support=ns['matrix_support'];rank=ns['rank'];nullspace=ns['nullspace'];legbit=ns['legbit']
REAL=ns['REAL'];W2S=ns['W2S'];W2D=ns['W2D'];ODD=ns['ODD']

def raw_pattern(a,b):
    M,G,labels,eps=matrix_support(a,b)
    odd=G[2:]
    verts=[(q,labels[q],q%8) for q in odd]
    leg={(q,r):legbit(r,q) for q in odd for r in odd if q!=r}
    return M,G,verts,leg,eps

def canonical_object(a,b):
    M,G,verts,leg,eps=raw_pattern(a,b)
    best=None
    for swap in (False,True):
        lm={'P':'Q','Q':'P','D':'D'} if swap else {'P':'P','Q':'Q','D':'D'}
        groups=defaultdict(list)
        for q,label,m8 in verts:groups[(lm[label],m8)].append(q)
        keys=sorted(groups)
        permlists=[list(itertools.permutations(groups[k])) for k in keys]
        for choice in itertools.product(*permlists):
            order=[];attrs=[]
            for k,ch in zip(keys,choice):
                for q in ch:order.append(q);attrs.append(k)
            mat=[[0 if i==j else leg[(order[i],order[j])] for j in range(len(order))] for i in range(len(order))]
            obj={'eps':eps,'vertices':[[x,y] for x,y in attrs],'legendre_bits':mat}
            enc=json.dumps(obj,separators=(',',':'),sort_keys=True)
            key=(enc,obj)
            if best is None or enc<best[0]:best=key
    return best[1]

def phash(obj):
    return hashlib.sha256(json.dumps(obj,separators=(',',':'),sort_keys=True).encode()).hexdigest()

def matrix_from_pattern(obj):
    attrs=[tuple(x) for x in obj['vertices']]; L=obj['legendre_bits']; eps=obj['eps']; m=len(attrs)
    G=[-1,2]+list(range(m)); rows=[]
    def add_place(W,dl,loc):
        for z in nullspace(W,2*dl):
            z1=z[:dl];z2=z[dl:];row=[0]*(2*len(G))
            for j,bits in enumerate(loc):
                row[j]=sum(x*y for x,y in zip(z1,bits))&1
                row[len(G)+j]=sum(x*y for x,y in zip(z2,bits))&1
            rows.append(tuple(row))
    add_place(REAL,1,[(1,),(0,)]+[(0,)]*m)
    q2=[(0,1,0),(1,0,0)]+[{1:(0,0,0),3:(0,1,1),5:(0,0,1),7:(0,1,0)}[m8] for _,m8 in attrs]
    add_place(W2S if eps=='shallow' else W2D,3,q2)
    for i,(label,m8) in enumerate(attrs):
        key=(label,m8) if label in ('P','Q') else ('D',None)
        loc=[(0,1 if m8 in (3,7) else 0),(0,1 if m8 in (3,5) else 0)]
        loc += [(1,0) if i==j else (0,L[i][j]) for j in range(m)]
        add_place(ODD[key],2,loc)
    return tuple(rows),len(G)

# Six templates: canonical hashes and abstract ranks independent of integer seeds.
templates={x['id']:x for x in c['templates']}
seeds={'T1':(2,1),'T2':(1,5),'T3':(2,7),'T4':(2,9),'T5':(6,43),'T6':(3,47)}
expected_hashes={
'T1':'ee1d27ad67abd6f37ebf6d71794a53b03f229d7aa0c7148396bc64133f48cb75',
'T2':'7c342b8cb3df57cb259c7f959602d83d3b8b8832d5a9c3d6846b661518905073',
'T3':'f3a8734144e03d36a04f57e51506873bbc632d9807f9b77ba22bb94e060a04e9',
'T4':'6b6299864b83e8e21938f14c7054415fbf47553de5ece93241a9c8515d4b56c3',
'T5':'4e26e5ba1e9269376a3f4a62899c3e68e43c64694d0a31acfd0d91b2a25236d2',
'T6':'4b2b444bf1d8af43e1b9b7a49b8dd19befebd0d2cb6da1887637ec4f0150fa7a'}
template_objects={}
for tid,(a,b) in seeds.items():
    obj=canonical_object(a,b);h=phash(obj);t=templates[tid]
    assert h==expected_hashes[tid]==t['sha256']
    assert obj['eps']=='shallow'
    MT,n=matrix_from_pattern(obj)
    assert n==t['n'] and rank(MT)==t['rank']==2*n-2
    template_objects[tid]=obj

# Cheap exact template matcher: enumerate only bijections inside equal labelled/mod-8 groups.
def matches_template(a,b,tobj):
    M,G,verts,leg,eps=raw_pattern(a,b)
    if eps!=tobj['eps'] or len(verts)!=len(tobj['vertices']):return False
    target=[tuple(x) for x in tobj['vertices']]
    for swap in (False,True):
        lm={'P':'Q','Q':'P','D':'D'} if swap else {'P':'P','Q':'Q','D':'D'}
        ag=defaultdict(list)
        for q,label,m8 in verts:ag[(lm[label],m8)].append(q)
        tg=defaultdict(list)
        for i,attr in enumerate(target):tg[attr].append(i)
        if {k:len(v) for k,v in ag.items()}!={k:len(v) for k,v in tg.items()}:continue
        keys=sorted(tg)
        choices=[list(itertools.permutations(ag[k])) for k in keys]
        for parts in itertools.product(*choices):
            order=[None]*len(target)
            for k,part in zip(keys,parts):
                for idx,q in zip(tg[k],part):order[idx]=q
            ok=True
            L=tobj['legendre_bits']
            for i in range(len(order)):
                for j in range(len(order)):
                    bit=0 if i==j else leg[(order[i],order[j])]
                    if bit!=L[i][j]:ok=False;break
                if not ok:break
            if ok:return True
    return False

# Exact EO replay: template matching iff exact Sel2 dimension two, and exactly six four-row classes.
classes=defaultdict(list);dim2=[];matches=[];count=0
for a in range(1,51):
    for b in range(1,51):
        if a==b or math.gcd(a,b)!=1:continue
        M,G,labels,eps=matrix_support(a,b);d=2*len(G)-rank(M)
        tids=[tid for tid,obj in template_objects.items() if matches_template(a,b,obj)]
        assert len(tids)<=1,(a,b,tids)
        tid=tids[0] if tids else None
        if d==2:dim2.append((a,b))
        if tid:
            matches.append((a,b));classes[tid].append((a,b))
            MT,n=matrix_from_pattern(template_objects[tid])
            assert rank(MT)==2*n-2 and d==2
        count+=1
assert count==1546 and len(dim2)==24 and set(matches)==set(dim2)
assert len(classes)==6 and all(len(v)==4 for v in classes.values())
expected_classes={
'T1':[(1,2),(1,3),(2,1),(3,1)],
'T2':[(1,5),(2,3),(3,2),(5,1)],
'T3':[(2,7),(5,9),(7,2),(9,5)],
'T4':[(2,9),(7,11),(9,2),(11,7)],
'T5':[(6,43),(37,49),(43,6),(49,37)],
'T6':[(3,47),(22,25),(25,22),(47,3)]}
for tid,v in expected_classes.items():assert sorted(classes[tid])==sorted(v)
# Recheck canonical hashes on all 24 known rows to lock the P/Q-swap convention.
for tid,rows in expected_classes.items():
    for a,b in rows:assert phash(canonical_object(a,b))==expected_hashes[tid]
xc=c['EO_exact_classification']
assert xc['row_count']==1546 and xc['template_match_row_count']==24 and xc['exact_sel2_dimension_2_row_count']==24
assert xc['template_match_iff_sel2_dimension_2_on_domain'] is True
assert xc['pattern_class_count']==6 and xc['each_pattern_class_size']==4
th=c['abstract_matrix_theorem']
assert th['matrix_constructed_from_pattern_alone'] is True
assert th['actual_matrix_permutation_equivalent_to_pattern_matrix'] is True
assert th['template_matching_sufficient_for_sel2_dimension_2_when_template_rank_is_2n_minus_2'] is True
assert th['global_in_parameter_not_box_restricted'] is True
assert c['route_result']['next_leaf']=='36-09ET_RHO_TEMPLATE_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for k,v in c['scope_firewalls'].items():assert v is False,(k,v)
print('36-09ES verified: corrected P/Q-swap canonicalization yields six abstract labelled-Legendre templates of rank 2n-2; exact template matching on all 1546 EO rows occurs iff Sel2_dim=2, giving six four-row classes. No exhaustive/full receiver/endpoint credit.')
