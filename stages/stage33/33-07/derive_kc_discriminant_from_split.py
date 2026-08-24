#!/usr/bin/env python3
"""Combine split endpoint-Galois and K_c geometry shards into a 2-generator discriminant certificate."""
import hashlib,json
from pathlib import Path
import sympy as sp
HERE=Path(__file__).resolve().parent
k=json.loads((HERE/'kc-picard-maps.json').read_text())
cc=json.loads((HERE/'picard-action-cc.json').read_text())
ct=json.loads((HERE/'picard-action-ct.json').read_text())
P=sp.Matrix(k['picard_gram_20x20']); KS=sp.Matrix(k['MatKtoS_20x64']); SK=sp.Matrix(k['MatStoK_64x20'])
V=sp.Matrix(k['smith_right_transform_V_20x20']); GScc=sp.Matrix(cc['picard_action_64x64']); GSct=sp.Matrix(ct['picard_action_64x64'])
if P.shape!=(20,20) or KS.shape!=(20,64) or SK.shape!=(64,20): raise SystemExit('Kc split shape regression')
if KS*SK!=2*sp.eye(20): raise SystemExit('Kc pull-push regression')
if KS*sp.Matrix(json.loads((HERE/'picard-gram-rows.json').read_text())['picard_gram_64x64'])*KS.T != 2*P:
 raise SystemExit('Kc pairing pullback regression')

def induced_k(GS):
 T=KS*GS*SK
 if any(int(x)%2 for x in T): raise SystemExit('Kc induced action lost divisibility by 2')
 G=sp.Matrix([[int(T[i,j])//2 for j in range(20)] for i in range(20)])
 if G*P*G.T!=P or G*G!=sp.eye(20): raise SystemExit('Kc induced action regression')
 if G*KS!=KS*GS: raise SystemExit('Kc equivariant pullback regression')
 return G
Gcc=induced_k(GScc); Gct=induced_k(GSct)
if Gcc*Gct!=Gct*Gcc: raise SystemExit('Kc V4 commuting regression')
Vin=V.inv()
if any(sp.denom(x)!=1 for x in Vin): raise SystemExit('Kc Smith V not unimodular')
# Same row-quotient convention as endpoint compact certificate.
def disc_action(G):
 B=Vin*G.T*V  # G is involutive, so G^{-T}=G^T
 if any(sp.denom(x)!=1 for x in B): raise SystemExit('Kc discriminant action nonintegral')
 pos=[18,19]; mods=[4,8]
 return [[int(B[pos[i],pos[j]])%mods[j] for j in range(2)] for i in range(2)]
Mcc=disc_action(Gcc); Mct=disc_action(Gct); mods=[4,8]
Pinv=P.inv(); Bd=Vin*Pinv*Vin.T; B8=8*Bd; pos=[18,19]
if any(sp.denom(B8[i,j])!=1 for i in pos for j in pos): raise SystemExit('Kc B8 nonintegral')
b8=[]
for a,i in enumerate(pos):
 row=[]
 for b,j in enumerate(pos): row.append(int(B8[i,j])%(16 if a==b else 8))
 b8.append(row)
def mul(A,B): return [[sum(A[i][r]*B[r][j] for r in range(2))%mods[j] for j in range(2)] for i in range(2)]
I=[[1,0],[0,1]]
if mul(Mcc,Mcc)!=I or mul(Mct,Mct)!=I or mul(Mcc,Mct)!=mul(Mct,Mcc): raise SystemExit('Kc mixed action V4 regression')
cert={
 'schema':'STAGE33_07_KC_DISCRIMINANT_SPLIT_V1',
 'source_locks':{'kc_picard_maps_sha256':k['canonical_sha256'],'endpoint_cc_action_sha256':cc['canonical_sha256'],'endpoint_ct_action_sha256':ct['canonical_sha256'],
  'upstream_git_blob_sha1':k['upstream_git_blob_sha1'],'stage33_05_hostile_audit':'stages/stage33/33-05/audit.md'},
 'picard_rank':20,'picard_determinant':int(P.det()),'discriminant_moduli':mods,'picard_discriminant_group':'Z/4 direct_sum Z/8',
 'cc_action_mixed_moduli':Mcc,'ct_action_mixed_moduli':Mct,'discriminant_bilinear_numerator_over_8_reduced':b8,
 'audited_Kc_Br2_invariant_dimension_f2':2,'audited_Kc_HS_d2_kernel_dimension_f2':1,
 'audited_Kc_HS_d2_kernel_basis':['J2'],'audited_Kc_HS_d2_nonzero_class':'q1',
 'proposed_endpoint_secondary_bockstein_validated':False,'role':'HS_D2_REGRESSION_INPUT_ONLY','theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'kc-discriminant-compact.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'cc':Mcc,'ct':Mct,'b8':b8,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
