#!/usr/bin/env python3
"""Extract only the K_c Picard Gram, pull/push maps, and Smith right transform.

No endpoint Galois action is computed in this Magma request; those are extracted
in separate <60s shards and combined later in Python.
"""
import ast, hashlib, json, pathlib, re
from stoll_cuboid_source import load_pinned_source, run_magma
HERE=pathlib.Path(__file__).resolve().parent
text,core,blob,source_attempt=load_pinned_source()
START='// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6.'
END='// action of sign change of c'
i0=text.index(START); i1=text.index(END,i0); kcore=text[i0:i1]
extra=r'''
D,U,V:=SmithForm(pmPicK);
diag:=[Abs(Integers()!D[j,j]):j in [1..20]]; assert diag[19..20] eq [4,8];
printf "STAGE33_07_KC_MAPS_BEGIN\n";
printf "DET=%o\n",Determinant(pmPicK); printf "DIAG=%o\n",diag;
for r in [1..20] do printf "P_ROW_%o=%o\n",r,[pmPicK[r,c]:c in [1..20]]; end for;
for r in [1..20] do printf "KS_ROW_%o=%o\n",r,[MatKtoS[r,c]:c in [1..64]]; end for;
for r in [1..64] do printf "SK_ROW_%o=%o\n",r,[MatStoK[r,c]:c in [1..20]]; end for;
for r in [1..20] do printf "V_ROW_%o=%o\n",r,[V[r,c]:c in [1..20]]; end for;
printf "STAGE33_07_KC_MAPS_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+kcore+'\n'+extra
stdout,attempt=run_magma(code,300,'Stage33-07 Kc Picard maps Magma')
(HERE/'kc-picard-maps-magma-stdout.txt').write_text(stdout,encoding='utf-8')
if 'STAGE33_07_KC_MAPS_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','Assertion failed')):
 print(stdout); raise SystemExit('Kc Picard maps extraction failed')
def grab(name):
 m=re.search(rf'^{name}=(.+)$',stdout,re.M)
 if not m: raise SystemExit(f'missing {name}')
 return ast.literal_eval(m.group(1))
def rows(prefix,n,m):
 out=[]
 for r in range(1,n+1):
  x=[int(v) for v in grab(f'{prefix}_ROW_{r}')]
  if len(x)!=m: raise SystemExit(f'{prefix} row length regression')
  out.append(x)
 return out
diag=[int(x) for x in grab('DIAG')]; det=int(re.search(r'^DET=(-?\d+)$',stdout,re.M).group(1))
if diag[-2:]!=[4,8] or abs(det)!=32: raise SystemExit('Kc Smith regression')
out={'schema':'STAGE33_07_KC_PICARD_MAPS_V1','upstream_git_blob_sha1':blob,'source_fetch_attempt':source_attempt,
 'submitted_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'magma_request_attempt':attempt,
 'picard_determinant':det,'picard_smith_diagonal':diag,
 'picard_gram_20x20':rows('P',20,20),'MatKtoS_20x64':rows('KS',20,64),'MatStoK_64x20':rows('SK',64,20),
 'smith_right_transform_V_20x20':rows('V',20,20)}
can=json.dumps(out,sort_keys=True,separators=(',',':')).encode(); out['canonical_sha256']=hashlib.sha256(can).hexdigest()
(HERE/'kc-picard-maps.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'determinant':det,'nontrivial_smith':diag[-2:],'certificate_sha256':out['canonical_sha256']},indent=2,sort_keys=True))
