#!/usr/bin/env python3
"""Derive q, cc, ct and seven retained signs in one exact Smith basis.

Only the sparse Gram matrix is sent to Magma for one Smith decomposition.
Magma emits the 14 relevant rows/columns of the Smith transform reduced modulo
eight and the reduced discriminant form.  The nine retained actions are
transported locally, so no coordinate-sign action is recomputed externally.
Reduction modulo eight is lossless because all target factors have order at
most eight.  Python then independently checks all finite q/action relations.
"""
import ast,hashlib,json,re
from pathlib import Path
from stoll_cuboid_source import run_magma

HERE=Path(__file__).resolve().parent
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
TGT_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
if TGT.get('canonical_sha256')!=TGT_LOCK:raise SystemExit('retained endpoint compact lock moved')
Psrc=json.loads((HERE/'picard-gram-rows.json').read_text())
ccsrc=json.loads((HERE/'picard-action-cc.json').read_text())
ctsrc=json.loads((HERE/'picard-action-ct.json').read_text())
NAMES=('a1','a2','a3','b1','b2','b3','c')
ssrc=[json.loads((HERE/f'picard-action-sign-{n}.json').read_text()) for n in NAMES]
blob=Psrc['upstream_git_blob_sha1']
if ccsrc['upstream_git_blob_sha1']!=blob or ctsrc['upstream_git_blob_sha1']!=blob or any(x['upstream_git_blob_sha1']!=blob for x in ssrc):raise SystemExit('split source blob mismatch')
if any(x.get('coordinate')!=n for x,n in zip(ssrc,NAMES)):raise SystemExit('coordinate sign row ordering regression')
P=Psrc['picard_gram_64x64'];Gs=[ccsrc['picard_action_64x64'],ctsrc['picard_action_64x64']]+[x['picard_action_64x64'] for x in ssrc]
if len(P)!=64 or any(len(r)!=64 for r in P) or any(len(G)!=64 or any(len(r)!=64 for r in G) for G in Gs):raise SystemExit('split matrix shape regression')
if Psrc.get('picard_rank')!=64:raise SystemExit('Picard Gram source-rank regression')

def sparse_literal(M):
    ts=[f'<{i},{j},{int(M[i-1][j-1])}>' for i in range(1,65) for j in range(1,65) if M[i-1][j-1]]
    return 'Matrix(SparseMatrix(Integers(),64,64,['+','.join(ts)+']))'

extra=r'''
D,_,V:=SmithForm(P); ds:=[Abs(Integers()!D[j,j]):j in [1..64]];
pos:=[j:j in [1..64]|ds[j] gt 1]; mods:=[ds[j]:j in pos];
assert mods eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
Vin:=V^-1; assert V*Vin eq IdentityMatrix(Integers(),64);
Pinv:=ChangeRing(P,Rationals())^-1; Vq:=ChangeRing(Vin,Rationals()); B8:=8*Vq*Pinv*Transpose(Vq);
printf "STAGE33_07_COMMON_SMITH_BEGIN\n"; printf "MODS=%o\n",mods;
for a in [1..14] do printf "R_%o=%o\n",a,[Integers()!Vin[pos[a],j] mod 8:j in [1..64]]; end for;
for j in [1..64] do printf "C_%o=%o\n",j,[Integers()!V[j,pos[b]] mod 8:b in [1..14]]; end for;
for a in [1..14] do printf "B8_%o=%o\n",a,[Integers()!B8[pos[a],pos[b]] mod (a eq b select 16 else 8):b in [1..14]]; end for;
printf "STAGE33_07_COMMON_SMITH_END\n";
'''
code='SetColumns(0);\nP:='+sparse_literal(P)+';\n'+extra
stdout,attempt=run_magma(code,180,'Stage33-07 retained-row common Smith transform')
if 'STAGE33_07_COMMON_SMITH_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
    print(stdout);raise SystemExit('common Smith transform failed')
def grab(name):
    m=re.search(rf'^{re.escape(name)}=(.+)$',stdout,re.M)
    if not m:raise SystemExit(f'missing common-Smith row {name}')
    return ast.literal_eval(m.group(1))
mods=[int(x) for x in grab('MODS')]
if mods!=[2]*4+[4]*6+[8]*4:raise SystemExit(f'endpoint Smith regression {mods}')
R=[[int(x)%8 for x in grab(f'R_{a}')] for a in range(1,15)]
C=[[int(x)%8 for x in grab(f'C_{j}')] for j in range(1,65)]
b8=[[int(x) for x in grab(f'B8_{a}')] for a in range(1,15)]
if any(len(r)!=64 for r in R) or any(len(r)!=14 for r in C+b8):raise SystemExit('common Smith compact row-length regression')
if [[sum(R[i][k]*C[k][j] for k in range(64))%8 for j in range(14)] for i in range(14)]!=[[int(i==j) for j in range(14)] for i in range(14)]:raise SystemExit('reduced Smith inverse regression')

def mm(A,B):
    out=[[0]*len(B[0]) for _ in range(len(A))];nz=[[j for j,x in enumerate(row) if x] for row in B]
    for i,row in enumerate(A):
        for k,a in enumerate(row):
            if a:
                for j in nz[k]:out[i][j]+=a*B[k][j]
    return out
I64=[[int(i==j) for j in range(64)] for i in range(64)]
for name,G in [('cc',Gs[0]),('ct',Gs[1])]+list(zip(NAMES,Gs[2:])):
    if mm(G,G)!=I64 or mm(mm(G,P),list(map(list,zip(*G))))!=P:raise SystemExit(f'Picard action regression {name}')
def induced(G):
    # B=V^-1*G^(-T)*V; every retained G was rechecked above as an involution.
    return [[x%mods[j] for j,x in enumerate(row)] for row in mm(mm(R,list(map(list,zip(*G)))),C)]
AA=[induced(G) for G in Gs];cc,ct=AA[:2];signs=AA[2:]
def well(M):return all((mods[i]*M[i][j])%mods[j]==0 for i in range(14) for j in range(14))
def comp(A,B):return [[sum(A[i][k]*B[k][j] for k in range(14))%mods[j] for j in range(14)] for i in range(14)]
I=[[int(i==j)%mods[j] for j in range(14)] for i in range(14)]
def transform_form(M):return [[sum(M[i][a]*b8[a][b]*M[j][b] for a in range(14) for b in range(14)) for j in range(14)] for i in range(14)]
def preserves_q(M):
    B=transform_form(M);return all((B[i][j]-b8[i][j])%(16 if i==j else 8)==0 for i in range(14) for j in range(14))
for name,M in [('cc',cc),('ct',ct)]+list(zip(NAMES,signs)):
    if not well(M) or comp(M,M)!=I or not preserves_q(M):raise SystemExit(f'finite q/action regression {name}')
if comp(cc,ct)!=comp(ct,cc):raise SystemExit('finite cc/ct failed commute')
if any(comp(M,cc)!=comp(cc,M) or comp(M,ct)!=comp(ct,M) for M in signs):raise SystemExit('finite coordinate sign/Galois commutation failed')
if any(comp(signs[i],signs[j])!=comp(signs[j],signs[i]) for i in range(7) for j in range(7)):raise SystemExit('finite coordinate signs failed commute')
prod=I
for M in signs:prod=comp(prod,M)
if prod!=I:raise SystemExit('finite seven-sign product relation failed')
if any((b8[i][j]-b8[j][i])%(16 if i==j else 8) for i in range(14) for j in range(14)):raise SystemExit('split discriminant form symmetry regression')

def fixed_log2(M,power):
    lim=[min(m,2**power) for m in mods];gens=[]
    for i,(m,l) in enumerate(zip(mods,lim)):
        v=[0]*14;v[i]=m//l;gens.append(v)
    dif=[]
    for v in gens:
        y=[sum(v[i]*M[i][j] for i in range(14))%mods[j] for j in range(14)];dif.append([(y[j]-v[j])%mods[j] for j in range(14)])
    image={(0,)*14}
    for v,l in zip(dif,lim):
        old=list(image);nxt=set(image);cur=(0,)*14
        for _ in range(1,l):
            cur=tuple((cur[j]+v[j])%mods[j] for j in range(14))
            for x in old:nxt.add(tuple((x[j]+cur[j])%mods[j] for j in range(14)))
        image=nxt
    domain=1
    for l in lim:domain*=l
    return (domain//len(image)).bit_length()-1
if fixed_log2(cc,1)!=10 or fixed_log2(ct,1)!=13:raise SystemExit('split endpoint fixed-Q2 regression against retained package')

cert={'schema':'STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_SPLIT_V2','source_locks':{
 'testa_stoll_git_blob_sha1':blob,'retained_endpoint_compact_sha256':TGT_LOCK,'picard_gram_rows_sha256':Psrc['canonical_sha256'],
 'picard_cc_rows_sha256':ccsrc['canonical_sha256'],'picard_ct_rows_sha256':ctsrc['canonical_sha256'],
 'picard_sign_rows_sha256':{n:x['canonical_sha256'] for n,x in zip(NAMES,ssrc)},
 'common_smith_submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest()},
 'common_smith_backend':'Magma exact SmithForm on retained sparse Gram only; retained actions transported locally',
 'common_smith_request_attempt':attempt,'smith_transform_reduced_modulo':8,'coordinate_order':list(NAMES),'discriminant_moduli':mods,
 'picard_determinant':int(TGT['picard_determinant']),'discriminant_bilinear_numerator_over_8_reduced':b8,
 'quadratic_value_convention':'q_Pic(x)=x*B8*x^T/8 mod 2Z; use -B8 for T, which has the same isometry group/action matrices',
 'cc_action_mixed_moduli':cc,'ct_action_mixed_moduli':ct,'sign_actions_mixed_moduli':signs,
 'all_actions_well_defined_involutions_and_q_isometries':True,'seven_sign_involutions_commute':True,'seven_sign_product_identity':True,
 'signs_commute_with_cc_ct':True,'split_smith_basis_literal_match_to_retained_compact_not_assumed':True,
 'split_cc_fixed_Q2_log2':10,'split_ct_fixed_Q2_log2':13,
 'picard_to_transcendental_rule':'same finite action matrices under anti-isometry; T quadratic form is negative Picard form',
 'actual_index512_glue_identified':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'endpoint-coordinate-sign-discriminant-actions-split.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'coordinate_sign_count':7,'mods':mods,'cc_fix2':10,'ct_fix2':13,'canonical_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
