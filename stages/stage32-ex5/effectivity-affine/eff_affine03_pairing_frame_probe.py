#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,sys,json
from pathlib import Path
from sympy import Matrix,Rational
ROOT=Path(__file__).resolve().parents[3];RES=ROOT/"stages/stage32/residual-32-01-production";sys.path.insert(0,str(RES))
from hperp_integral_adapter import HperpIntegralPairingAdapter
from direct_picard_slice_bridge import DirectPicardSliceBridge
from pairing_prefix_engine import close_permutation_group
RET=ROOT/"stages/stage33/33-07/picard_base_rows_retained.py";MARK=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
LOCK={RES/"hperp_integral_adapter.py":"fb1eb380ca786e42a6b00c5ef454b0e79fdba771",RES/"direct_picard_slice_bridge.py":"be48bd94304d0217727c5c3368761d347cb22eaa",RET:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARK:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
def req(v,m):
 if not v:raise SystemExit("FAIL: "+m)
def blob(p):
 b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);req(s and s.loader,n);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.load()
def upper(m):
 return Matrix([m[i,j] for i in range(64) for j in range(i,64)])
def span_solution(forms,target):
 A=Matrix.hstack(*[upper(x) for x in forms]); b=upper(target)
 try:
  x,params=Matrix(A).gauss_jordan_solve(b)
 except ValueError:
  return None
 return None if params.rows else [x[i,0] for i in range(x.rows)]
def main():
 for p,h in LOCK.items():req(blob(p)==h,"lock "+str(p))
 bundle=load(RET,"eff03ret");mark=load(MARK,"eff03mark")
 a=HperpIntegralPairingAdapter.from_retained(mark,bundle);b=DirectPicardSliceBridge.from_retained(mark,bundle)
 P=Matrix(a.pairing_matrix);G=Matrix(bundle["picard_gram_64x64"]);H=Matrix(1,64,b.degree_functional);HH=H.T*H
 group=close_permutation_group(mark["aut_action"]["permutations_1based"])
 unseen=set(range(140));orbits=[]
 while unseen:
  s=min(unseen);o=tuple(sorted({g[s] for g in group}));orbits.append(o);unseen.difference_update(o)
 orbit_forms=[]
 orbit_meta=[]
 coords=Matrix(a.class_coordinates_in_retained_basis)
 for o in orbits:
  A=P[list(o),:];orbit_forms.append(A.T*A)
  degs=sorted({int((H*coords[i,:].T)[0]) for i in o})
  selfsq=sorted({int((coords[i,:]*G*coords[i,:].T)[0]) for i in o})
  orbit_meta.append({"size":len(o),"degrees":degs,"self_squares":selfsq,"first_index":min(o)})
 # Strongest cheap possibility: exact Aut(S)-orbit frame decomposition of the
 # H-perp positive form Q=d^2/16-C^2.  If it exists, N is controlled directly
 # by four orbitwise sums of pairing squares, eliminating the 58D search.
 Q=Rational(1,16)*HH-G
 qsol=span_solution(orbit_forms+[HH],Q)
 gsol=span_solution(orbit_forms+[HH],G)
 out={"aut_group_order":len(group),"orbit_count":len(orbits),"orbits":orbit_meta,
      "hperp_Q_in_orbit_frame_span":qsol is not None,
      "hperp_Q_coefficients":None if qsol is None else [str(x) for x in qsol],
      "intersection_G_in_orbit_frame_span":gsol is not None,
      "intersection_G_coefficients":None if gsol is None else [str(x) for x in gsol],
      "interpretation":("EXACT_ORBIT_FRAME_RECONSTRUCTION_AVAILABLE" if qsol is not None else "NO_EXACT_ORBIT_FRAME_IDENTITY__NEXT_SEEK_CERTIFIED_PSD_DOMINATION_WITH_ORBIT_WEIGHTS"),
      "credit":{"effectivity":False,"main":False}}
 print("EFF_AFFINE03_ORBIT_FRAME="+json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
