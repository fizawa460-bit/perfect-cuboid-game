#!/usr/bin/env python3
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/"stages/stage32-ex5/breadth-cycle-2/bc2_02_one_indexed_full178_terminal_to_picard64_completion.py"
RETAINED=ROOT/"stages/stage33/33-07/picard_base_rows_retained.py"
MARKING=ROOT/"stages/stage33/33-07/stage32_picard_marking_retained.py"
LOCKS={BASE:"6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633",RETAINED:"82e4d450a1d852e34f6615440fb88a029c6e54eb",MARKING:"5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"}
NORMAL=92; EXCEPTIONAL=48; RANK=64

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(p,n):
    s=importlib.util.spec_from_file_location(n,p); req(s and s.loader,"module "+n)
    m=importlib.util.module_from_spec(s); sys.modules[n]=m; s.loader.exec_module(m); return m
def row(v): return Matrix(1,RANK,[int(x) for x in v])

def main():
    for p,h in LOCKS.items(): req(p.is_file() and blob(p)==h,"source lock "+str(p))
    v1=load(BASE,"ex5_eff_affine02_base")
    bundle=v1.load_retained(RETAINED,"ex5_eff_affine02_bundle")
    marking=v1.load_retained(MARKING,"ex5_eff_affine02_marking")
    data=v1.reconstruct_translation_data(marking,bundle)
    P=Matrix(data["adapter"].pairing_matrix); bridge=data["bridge"]
    req(P.shape==(140,RANK),"pairing shape")
    drow=row(bridge.degree_functional); erow=row(bridge.exceptional_mass_functional)
    nsum=Matrix.zeros(1,RANK); esum=Matrix.zeros(1,RANK)
    for i in range(NORMAL): nsum += P.row(i)
    for i in range(NORMAL,NORMAL+EXCEPTIONAL): esum += P.row(i)
    req(esum==erow,"exceptional mass identity")
    req(nsum+5*esum==19*drow,"normal mass identity")
    req(P.rank()==RANK,"all140 pairing map not injective")

    # Recession theorem. On a fixed (d,e) slice, a recession direction r
    # preserving all140 nonnegativity has P_i r >= 0. The two exact mass
    # identities force sums over both blocks to zero, hence every P_i r=0.
    # Injectivity of P then forces r=0. Thus the all140 nonnegative fixed-(d,e)
    # Picard64 fiber is bounded; no extra per-coordinate bound is needed.
    out={
      "schema":"STAGE32EX5_EFF_AFFINE02_BOUNDED_COMPLEMENT_PREFLIGHT_V1",
      "status":"PASS_FIXED_DE_ALL140_FIBER_HAS_TRIVIAL_RECESSION_CONE",
      "source_locks":{"base":LOCKS[BASE],"retained":LOCKS[RETAINED],"marking":LOCKS[MARKING]},
      "exact_identities":{
        "exceptional_sum":"sum(E_48)=e",
        "normal_sum":"sum(N_92)=19*d-5*e",
        "all140_pairing_rank":int(P.rank()),
        "picard_rank":RANK,
      },
      "bounded_complement":{
        "for_all140_nonnegative_fixed_d_e":True,
        "exceptional_coordinate_bounds":"0 <= E_i <= e",
        "normal_coordinate_bounds":"0 <= N_i <= 19*d-5*e",
        "recession_cone":"{0}",
        "proof":"For a recession direction r, fixed d,e give sum exceptional(P r)=0 and sum normal(P r)=0. Since every component P_i r is nonnegative, all 140 vanish. rank(P)=64 implies r=0.",
      },
      "research_consequence":{
        "repairs_gap":"The prior producer-gap statement that a bounded complement was not source-locked is too strong once all140 nonnegativity and the exact mass identities are imposed together.",
        "next_exact_unit":"Construct a source-locked rowwise upper bound U(d,e,prefix) for N=-y^2 over this bounded polytope and compare directly with the quantized RR cutoff T(d)+2m^2.",
        "scope":"population-level producer architecture, not per-key FP58 enumeration"
      },
      "credit":{"effectivity":False,"main":False,"theorem":False,"endpoint":False,"merge":False}
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
