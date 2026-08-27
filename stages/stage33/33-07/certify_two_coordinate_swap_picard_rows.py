#!/usr/bin/env python3
"""Recover the two coordinate-swap Picard actions without Smith reduction.

Only the pinned Testa--Stoll Picard construction and automorphism block are run
remotely.  The output is two small 64x64 integer matrices for
(a1 a2)(b1 b2) and (a1 a3)(b1 b3).  No discriminant Smith form, Gersten map,
or localization connecting class is computed here.
"""
import ast, hashlib, json, re
from pathlib import Path
from stoll_cuboid_source import load_pinned_source, run_magma
from picard_base_rows_retained import load as load_base

HERE=Path(__file__).resolve().parent
OUT=HERE/'picard-two-coordinate-swap-actions.json'

def canonical_sha256(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def mm(A,B):
    return [[sum(int(A[i][k])*int(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):return [list(r) for r in zip(*A)]

def grab(stdout,name):
    m=re.search(rf'^{re.escape(name)}=(.+)$',stdout,re.M)
    if not m: raise SystemExit(f'missing Magma output {name}')
    return ast.literal_eval(m.group(1))

full,core,blob,source_attempt=load_pinned_source()
a=full.index('// The automorphism group (see Proposition 4)')
b=full.index('// Automorphisms + Galois on Pic/2*Pic',a)
block='\n'.join(line for line in full[a:b].splitlines()
                if not line.startswith('AutS :=') and not line.startswith('printf "#Aut(S) ='))+'\n'
tail=r'''
selected := [1,2];
for z in [1..2] do
  G := action[selected[z]];
  assert G^2 eq IdentityMatrix(Integers(),64);
  assert G*pmPic*Transpose(G) eq pmPic;
  for r in [1..64] do
    printf "SWAP_%o_ROW_%o=%o\n",z,r,Eltseq(G[r]);
  end for;
end for;
printf "STAGE33_TWO_SWAP_ROWS_DONE\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+block+'\n'+tail
stdout,magma_attempt=run_magma(code,420,'Stage33 two coordinate-swap Picard rows',user_agent='perfect-cuboid-stage33/4.0')
if 'STAGE33_TWO_SWAP_ROWS_DONE' not in stdout:
    print(stdout);raise SystemExit('two-swap Magma run did not finish')
actions=[]
for z in (1,2):
    M=[]
    for r in range(1,65):
        row=[int(x) for x in grab(stdout,f'SWAP_{z}_ROW_{r}')]
        if len(row)!=64:raise SystemExit('swap row width regression')
        M.append(row)
    actions.append(M)
base=load_base(); gram=base['picard_gram_64x64'];I=[[1 if i==j else 0 for j in range(64)] for i in range(64)]
for z,M in enumerate(actions,1):
    if mm(M,M)!=I:raise SystemExit(f'swap {z} is not involutive')
    if mm(mm(M,gram),transpose(M))!=gram:raise SystemExit(f'swap {z} does not preserve retained Gram')
cert={
 'schema':'STAGE33_07_TWO_COORDINATE_SWAP_PICARD_ROWS_V1',
 'source_locks':{
   'testa_stoll_cuboids_magma_blob_sha1':blob,
   'retained_picard_base_bundle_sha256':base['canonical_sha256'],
   'submitted_magma_code_sha256':hashlib.sha256(code.encode()).hexdigest(),
 },
 'coordinate_swaps':['swap_a1_a2_b1_b2','swap_a1_a3_b1_b3'],
 'picard_actions_64x64':actions,
 'exact_checks':{
   'both_actions_involutions':True,
   'both_actions_preserve_retained_picard_gram':True,
   'smith_form_used':False,
 },
 'execution':{'source_fetch_attempt':source_attempt,'magma_request_attempt':magma_attempt,'remote_cas_used':True},
 'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,
}
cert['canonical_sha256']=canonical_sha256(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'swap_count':2,'smith_form_used':False,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
