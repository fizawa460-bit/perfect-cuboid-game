#!/usr/bin/env python3
"""R3-07 row350 exact standard-Python replay.
Proves four-real-place unit signature surjectivity, Cl^+(K)=Cl(K),
explicit real fake Kummer local line and bound dim <=31+c_S.
No class group computation, full S-unit calculation, true Selmer, MW upper or source veto.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json, subprocess, sys, math
P=Path(__file__).resolve().parent
C=json.loads((P/'row350_certificate.json').read_text())
for name,digest in C['parent_SHA256'].items():
    assert sha256((P/name).read_bytes()).hexdigest()==digest, (name,'parent hash mismatch')
if '--skip-parent-exact-replay' not in sys.argv:
    old=subprocess.run([sys.executable,str(P/'verify_index13_theta4_stdlib.py')],cwd=P,capture_output=True,text=True,timeout=180)
    assert old.returncode==0,(old.stdout[-1500:],old.stderr[-1500:])
    assert 'PASS index-13 superlattice' in old.stdout
    print('PASS fixed old row349 unit-index13 and row347 12-unit independence, SHA-locked exact replay')
U=json.loads((P/'unit12_certificate.json').read_text())
R=json.loads((P/'signed18_genus17_rank6_certificate.json').read_text())
L=json.loads((P/'signed18_c2_true_local_kummer_dimensions_certificate.json').read_text())
G=json.loads((P/'signed18_c2_global_sunits_preflight_certificate.json').read_text())
H=U['h2_coefficients_ascending']
assert H==R['h2_coefficients_ascending'] and H==C['h2_coefficients_ascending'] and len(H)==37 and H[0]==H[36]==1
assert G['signature']==[4,16] and G['S_unit_free_rank']==40 and G['finite_S_total']==21
assert G['fake_ambient_dim_expression']=='34+c_S' and G['fake_norm_square_ambient_dim_upper_expression']=='32+c_S'
assert L['archimedean_real_branchpoints']==4 and L['local_true_Kummer_J(Qv)/2_dimensions']['real']==1
# Explicit integer ZZ polynomial check inherited h=A^2-X B^2, so h(-t)>0 for t>0.
A=R['A_coefficients_ascending'];B=R['B_coefficients_ascending']
def mul(v,w):
    out=[0]*(len(v)+len(w)-1)
    for i,c in enumerate(v):
        for j,d in enumerate(w):out[i+j]+=c*d
    return out
AA=mul(A,A);BB=[0]+mul(B,B)
assert [AA[i]-(BB[i] if i<len(BB) else 0) for i in range(37)]==H

def qeval(v,x):
    a=Q(0)
    for c in reversed(v):a=a*x+c
    return a

def sign(v):
    return 1 if v>0 else (-1 if v<0 else 0)

def intpoly_range(v,l,r):
    """Rational interval Horner; safe overapproximation, signs rigorous."""
    lo=hi=Q(v[-1])
    for c in reversed(v[:-1]):
        choices=[lo*l,lo*r,hi*l,hi*r]
        lo=min(choices)+c;hi=max(choices)+c
    return lo,hi

def gf2rank(M):
    rows=[sum((int(v)&1)<<j for j,v in enumerate(row)) for row in M]
    r=0
    for col in range(len(M[0])):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>col)&1),None)
        if p is None:continue
        rows[p],rows[r]=rows[r],rows[p]
        for i in range(len(rows)):
            if i!=r and ((rows[i]>>col)&1):rows[i]^=rows[r]
        r+=1
    return r

assert len(H)==37
nonzero=[sign(c) for c in H[::-1] if c]
changes=sum(nonzero[i]!=nonzero[i+1] for i in range(len(nonzero)-1))
assert changes==4, changes
# 4 distinct positive real roots exist because h signs flip across four
# disjoint exact rational intervals, and Descartes bounds their number by four.
I=[(Q(*s[0]),Q(*s[1])) for s in C['rational_root_intervals']]
assert len(I)==4 and all(Q(0)<l<r for l,r in I) and all(I[i][1]<I[i+1][0] for i in range(3))
print('PASS Descartes sign variations exactly 4, plus 4 disjoint positive isolating intervals')
for i,(l,r) in enumerate(I):
    hs=[sign(qeval(H,l)),sign(qeval(H,r))]
    assert hs in ([1,-1],[-1,1]), (i,hs)
    assert hs==C['root_h_endpoint_signs'][i]
    print('  root',i+1,'interval',l,r,'h endpoint signs',hs)

p={'epsilon':[ -1,1 ],'rho':U['unit_definitions'][4]['q'], 'gamma8':U['unit_definitions'][7]['q']}
assert p['rho']==[-1,-4,1] and p['gamma8']==[1,16,76,80,-282,-656,-180,-80,1]
mat=[]
for l,r in I:
    signs={}
    for name,q in p.items():
        lo,hi=intpoly_range(q,l,r)
        if lo>0:bit=0
        elif hi<0:bit=1
        else:raise AssertionError((name,'interval inconclusive',l,r,lo,hi))
        signs[name]=bit
    mat.append([1,signs['epsilon'],signs['rho'],signs['gamma8']])
assert mat==C['unit_sign_matrix_root_rows']
assert gf2rank(mat)==4
print('PASS exact four real unit signatures [-1,epsilon,rho,gamma8] rank4 over F2')
print('  root-rows',mat)
assert C['narrow_and_ordinary_classgroup_canonically_isomorphic'] is True
# Classical exact sequence U -> signs -> Cl^+ -> Cl -> 0;
# signs onto -> narrow Cl^+ == usual Cl.
assert G['unit_free_rank']==19 and G['signature'][0]==4
assert 19+1-4==C['totally_positive_unit_mod_square_F2_dimension']==16
print('THEOREM: signature map O_K^* -> (±1)^4 surjective, Cl^+(K)=Cl(K), E^+/E^2 has dim16')
# Real fake Kummer image: old actual Q-rational Jacobian divisor D2 with
# theta-Kummer rho=G2(theta) up to square/rational scalar.
rho_bits=[row[2] for row in mat]
assert rho_bits==[1,1,0,0] and C['real_local_kummer_generator_bits']==rho_bits
# inherited exact real local true Kummer dimension=1
assert L['local_true_Kummer_J(Qv)/2_dimensions']['real']==1
# Kill scalar 1111 and D2 line 1100: lambda3=s1+s2 (also lambda4=s3+s4).
assert (rho_bits[0]+rho_bits[1])%2==0
assert (1+1)%2==0 # rational negative scalar all-one
# Norm-square necessary map on fake W_S: degree36 Norm(q)=q^36 square.
# Norm-sign function phi1 and odd-prime 2843 parity phi2; real phi3=s1+s2.
# Witnesses epsilon Norm-1 (phi1=1), h'(theta) Norm=2^1680 M (phi2=1),
# gamma8 Norm+1, sign (0,1,1,0) => (phi1,phi2,phi3)=(0,0,1).
unitnorm={z['name']:z['norm'] for z in U['unit_definitions']}
assert unitnorm['epsilon']==-1 and unitnorm['gamma8']==1
assert G['discriminant_S_unit']['norm_squareclass']=='M'
M=int(G['discriminant_S_unit']['M'])
assert M%2843==0 and (M//2843)%2843!=0
row_e=[1,0, (mat[0][1]+mat[1][1])%2]
# Derivative norm M positive, 2843-valuation odd. phi3 may be computed
# from derivative signs; h' signs alternate using endpoint crossing directions.
deriv_bits=[]
for l,r in I:
    # derivative sign at the unique root equals + if h crosses - to +;
    # because h is monic and has only 4 simple real roots, crossings alternate.
    deriv_bits.append(1 if qeval(H,l)>qeval(H,r) else 0)
row_d=[0,1,(deriv_bits[0]+deriv_bits[1])%2]
row_g=[0,0,(mat[0][3]+mat[1][3])%2]
W=[row_e,row_d,row_g]
assert W==C['independent_three_global_filters_witness_matrix']
assert gf2rank(W)==3
print('PASS independent fake norm/real necessary conditions: norm negative sign, norm odd p2843 valuation, real s1+s2')
print('  witnesses [epsilon, hprime(theta), gamma8] phi rows:', W)
# h'=Norm class M and epsilon norm sign independent old row346;
# gamma8 adds one independent REAL restriction to old norm candidate.
assert C['fake_real_and_square_norm_dimension_upper_expression']=='31+c_S'
assert C['global_true_selmer_bound_proved'] is False
print('NEW_SCOPED_THEOREM: dim(fake S-squareclass, necessary norm-square & real local Kummer) <=31+c_S, c_S UNKNOWN.')
print('NOT_PROVED: Cl_K[2] or Cl_S[2] numerical value, full ordinary/S-unit generation, true Sel2 <=16, MW rank upper, p163 Coleman, signed source exclusion.')
print('SHA256_CERT='+sha256((P/'row350_certificate.json').read_bytes()).hexdigest())
