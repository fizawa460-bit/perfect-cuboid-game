#!/usr/bin/env python3
from fractions import Fraction
import hashlib,json,math
from sympy import Matrix

def digest(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def produce(row_id,d,terminal_identity,selected_pairings,Psel,gram,source_locks):
    d=int(d); P=Matrix(Psel); G=Matrix(gram); y=Matrix([int(v) for v in selected_pairings])
    if P.shape!=(64,64) or G.shape!=(64,64) or y.shape!=(64,1): raise ValueError("require exact selected64/Gram64")
    if P.det()==0: raise ValueError("selected64 pairing matrix singular")
    c=P.inv()*y
    if any(v.q!=1 for v in c): raise ValueError("pairings do not reconstruct an integral Picard64 class")
    ci=[int(v) for v in c]; C2=int((c.T*G*c)[0])
    m=16//math.gcd(d,16); Nq=Fraction(m*m*d*d,16)-m*m*C2
    if Nq.denominator!=1 or Nq<0: raise ValueError("invalid Hperp norm reconstruction")
    N=int(Nq)
    return {"schema":"STAGE32_32_02_SCALAR_PRODUCER_V1","row_id":row_id,"terminal_identity":terminal_identity,"d":d,"m":m,"picard64_coordinates":ci,"picard64_coordinates_sha256":digest(ci),"negative_hperp_square_N":N,"C2":C2,"selected_pairing_matrix_sha256":digest(Psel),"gram64_sha256":digest(gram),"witness_source_locks":source_locks,"credit":{"main":False,"pruning":False,"effectivity_final":False,"irreducible_member":False,"merge":False}}
