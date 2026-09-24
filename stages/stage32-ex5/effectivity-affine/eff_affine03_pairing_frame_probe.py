#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,sys,json
from pathlib import Path
from sympy import Matrix,Rational
ROOT=Path(__file__).resolve().parents[3];RES=ROOT/"stages/stage32/residual-32-01-production";sys.path.insert(0,str(RES))
from hperp_integral_adapter import HperpIntegralPairingAdapter
from direct_picard_slice_bridge import DirectPicardSliceBridge
RET=ROOT/"stages/stage33/33-07/picard_base_rows_retained.py";MARK=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
LOCK={RES/"hperp_integral_adapter.py":"fb1eb380ca786e42a6b00c5ef454b0e79fdba771",RES/"direct_picard_slice_bridge.py":"be48bd94304d0217727c5c3368761d347cb22eaa",RET:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARK:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
def req(v,m):
 if not v:raise SystemExit("FAIL: "+m)
def blob(p):
 b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);req(s and s.loader,n);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.load()
def solve(S,G,H):
 Q=H.T*H
 for i in range(64):
  for j in range(i,64):
   for k in range(i,64):
    for l in range(k,64):
     det=G[i,j]*Q[k,l]-G[k,l]*Q[i,j]
     if det:
      a=Rational(S[i,j]*Q[k,l]-S[k,l]*Q[i,j],det);b=Rational(G[i,j]*S[k,l]-G[k,l]*S[i,j],det)
      R=S-a*G-b*Q;return a,b,R
 return None,None,S
def st(R):
 nz=[R[i,j] for i in range(64) for j in range(64) if R[i,j]]
 return {"zero":not nz,"rank":int(R.rank()) if nz else 0,"nonzero_entries":len(nz)}
def main():
 for p,h in LOCK.items():req(blob(p)==h,"lock "+str(p))
 bundle=load(RET,"eff03ret");mark=load(MARK,"eff03mark");a=HperpIntegralPairingAdapter.from_retained(mark,bundle);b=DirectPicardSliceBridge.from_retained(mark,bundle)
 P=Matrix(a.pairing_matrix);G=Matrix(bundle["picard_gram_64x64"]);H=Matrix(1,64,b.degree_functional)
 out={}
 for name,A in {"all140":P,"normal92":P[:92,:],"exceptional48":P[92:140,:]}.items():
  aa,bb,R=solve(A.T*A,G,H);out[name]={"a_G":str(aa),"b_HH":str(bb),"residual":st(R)}
 exact=out["all140"]["residual"]["zero"]
 print("EFF_AFFINE03_FRAME_PROBE="+json.dumps({"exact_frame_identity":exact,"blocks":out,"next":"If exact, reconstruct H-perp norm from pairing squares. If not exact, decompose the residual under the slice stabilizer and seek a certified PSD domination inequality rather than returning to per-key FP58."},sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
