#!/usr/bin/env python3
from __future__ import annotations
import hashlib,importlib.util,json,sys
from pathlib import Path
from sympy import Matrix
ROOT=Path(__file__).resolve().parents[3]; RES=ROOT/"stages/stage32/residual-32-01-production"
sys.path.insert(0,str(RES))
from hperp_integral_adapter import HperpIntegralPairingAdapter
from direct_picard_slice_bridge import DirectPicardSliceBridge
RET=ROOT/"stages/stage33/33-07/picard_base_rows_retained.py"; MARK=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
LOCK={RES/"hperp_integral_adapter.py":"fb1eb380ca786e42a6b00c5ef454b0e79fdba771",RES/"direct_picard_slice_bridge.py":"be48bd94304d0217727c5c3368761d347cb22eaa",RET:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARK:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
def req(v,m):
 if not v: raise SystemExit("FAIL: "+m)
def blob(p):
 b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);req(s and s.loader,n);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.load()
def main():
 for p,h in LOCK.items():req(blob(p)==h,"lock "+str(p))
 bundle=load(RET,"eff02ret");mark=load(MARK,"eff02mark")
 a=HperpIntegralPairingAdapter.from_retained(mark,bundle); b=DirectPicardSliceBridge.from_retained(mark,bundle)
 P=Matrix(a.pairing_matrix); d=Matrix(1,64,b.degree_functional); e=Matrix(1,64,b.exceptional_mass_functional)
 normal=sum((P.row(i) for i in range(92)),Matrix.zeros(1,64)); exc=sum((P.row(i) for i in range(92,140)),Matrix.zeros(1,64))
 req(exc==e,"exceptional mass identity");req(normal+5*exc==19*d,"normal mass identity")
 req(a.certificate["selected64_change_of_basis_unimodular"] is True,"pairing injectivity certificate")
 out={"schema":"STAGE32EX5_EFF_AFFINE02_BOUNDED_COMPLEMENT_PREFLIGHT_V1","status":"PASS_FIXED_DE_ALL140_FIBER_HAS_TRIVIAL_RECESSION_CONE",
 "exact_identities":{"exceptional_sum":"sum(E_48)=e","normal_sum":"sum(N_92)=19*d-5*e","all140_pairing_map_injective":True},
 "bounded_complement":{"for_all140_nonnegative_fixed_d_e":True,"exceptional_coordinate_bounds":"0<=E_i<=e","normal_coordinate_bounds":"0<=N_i<=19*d-5*e","recession_cone":"{0}","proof":"fixed d,e plus nonnegative recession pairings force both block sums to zero; hence all140 pairings vanish; the certified unimodular selected64 basis makes the pairing map injective, so r=0"},
 "research_consequence":{"repairs_gap":"all140 nonnegativity plus exact mass identities supplies a source-locked bounded complement","next_exact_unit":"derive a population-level H-perp norm upper envelope from the bounded pairing polytope","scope":"population-level, not per-key FP58"},
 "credit":{"effectivity":False,"main":False,"theorem":False,"endpoint":False,"merge":False}}
 print("EFF_AFFINE02_BOUNDED_COMPLEMENT="+json.dumps(out,sort_keys=True,separators=(",",":")))
if __name__=="__main__":main()
