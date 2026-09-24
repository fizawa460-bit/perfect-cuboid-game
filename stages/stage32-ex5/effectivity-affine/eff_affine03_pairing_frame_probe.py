#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,sys
from fractions import Fraction
from pathlib import Path
from sympy import Matrix,Rational

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/"stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_to_picard64_completion.py"
RET=ROOT/"stages/stage33/33-07/picard_base_rows_retained.py"
MARK=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
LOCK={BASE:"6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633",RET:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARK:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
def req(v,m):
 if not v: raise SystemExit("FAIL: "+m)
def blob(p):
 b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);req(s and s.loader,n);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
def solve_span(S,G,H):
 # Solve S = a G + b H^T H from two independent entries, then verify exactly.
 Q=H.T*H
 pairs=[]
 for i in range(64):
  for j in range(i,64):
   pairs.append((i,j,G[i,j],Q[i,j],S[i,j]))
 for u in range(len(pairs)):
  i,j,g1,q1,s1=pairs[u]
  for v in range(u+1,len(pairs)):
   k,l,g2,q2,s2=pairs[v]
   det=g1*q2-g2*q1
   if det:
    a=Rational(s1*q2-s2*q1,det);b=Rational(g1*s2-g2*s1,det)
    R=S-a*G-b*Q
    return a,b,R
 return None,None,S
def stats(R):
 nz=[R[i,j] for i in range(64) for j in range(64) if R[i,j]!=0]
 return {"zero":not nz,"rank":int(R.rank()),"nonzero_entries":len(nz),"max_abs_num":max([abs(int(x.p)) for x in nz],default=0),"max_den":max([int(x.q) for x in nz],default=1)}
def main():
 # Population-level exact frame probe; no effectivity credit is granted here.
 for p,h in LOCK.items():req(blob(p)==h,"lock "+str(p))
 v=load(BASE,"eff03base");bundle=v.load_retained(RET,"eff03ret");mark=v.load_retained(MARK,"eff03mark")
 data=v.reconstruct_translation_data(mark,bundle);P=Matrix(data["adapter"].pairing_matrix);G=Matrix(bundle["picard_gram_64x64"]);H=Matrix(1,64,[int(x) for x in data["bridge"].degree_functional])
 req(P.shape==(140,64) and G.shape==(64,64),"shape")
 blocks={"all140":P,"normal92":P[:92,:],"exceptional48":P[92:140,:]}
 out={}
 for name,A in blocks.items():
  S=A.T*A;a,b,R=solve_span(S,G,H)
  out[name]={"a_G":str(a),"b_HH":str(b),"residual":stats(R)}
 # Also ask whether the exact all140 frame identity directly reconstructs H-perp norm.
 allid=out["all140"]; exact=allid["residual"]["zero"]
 consequence=None
 if exact:
  a=Rational(allid["a_G"]);b=Rational(allid["b_HH"])
  consequence={"identity":"sum_i (C.E_i)^2 = a*C^2 + b*d^2","a":str(a),"b":str(b),
   "population_level":True,
   "rr_norm_reconstruction":"If a!=0, C^2=(sum_pairing_squares-b*d^2)/a, hence N follows exactly from the 140 pairing squares."}
 print("EFF_AFFINE03_FRAME_PROBE="+json.dumps({"exact_frame_identity":exact,"blocks":out,"consequence":consequence},sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
