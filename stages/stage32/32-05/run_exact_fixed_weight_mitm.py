#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, hashlib, itertools, json, math, pathlib, time
import sympy
import z3
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

SELECTED_ROWS=list(range(92,140))+[0,1,2,3,4,8,9,12,16,17,24,32,44,48,52,68]
DET=274877906944
DEN=8
SCHEMA='STAGE32_EXACT_FIXED_WEIGHT_MITM_V1'

def canon(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def build(core):
    rows=Matrix(core['raw_cross_pairings_with_basis']); gram=Matrix(core['basis_gram'])
    S=Matrix([core['raw_cross_pairings_with_basis'][i] for i in SELECTED_ROWS])
    assert abs(int(S.det()))==DET
    inv=S.inv(); den=1
    for x in inv: den=math.lcm(den,int(sympy.denom(x)))
    assert den==DEN
    N=inv*den; assert all(sympy.denom(x)==1 for x in N)
    N=Matrix([[int(N[i,j]) for j in range(64)] for i in range(64)])
    P=rows*N; P=Matrix([[int(P[i,j]) for j in range(64)] for i in range(140)])
    G=N.T*gram*N; G=Matrix([[int(G[i,j]) for j in range(64)] for i in range(64)])
    H=Matrix(core['hyperplane']).T*gram*N; h=[int(H[0,j]) for j in range(64)]
    # L = 8 Z^64 + span(quaternary residue columns).  Exceptional residues
    # are compatible with some quaternary residue iff they are zero in Z^64/L.
    q=Matrix([[int(N[i,j])%8 for j in range(48,64)] for i in range(64)])
    B=hermite_normal_form(Matrix.hstack(8*Matrix.eye(64),q))
    assert B.shape==(64,64)
    Binv=B.inv()
    sigcols=[]
    used=set()
    for j in range(48):
        v=Binv*Matrix([int(N[i,j])%8 for i in range(64)])
        bits=0
        for i,x in enumerate(v):
            f=x-sympy.floor(x)
            assert sympy.denom(f) in (1,2)
            if f==sympy.Rational(1,2): bits|=1<<i; used.add(i)
            else: assert f==0
        sigcols.append(bits)
    # Quotient seen by exceptional columns must be elementary 2-group rank 23.
    basis=[]
    for x in sigcols:
        y=x
        for p,b in basis:
            if (y>>p)&1: y^=b
        if y:
            p=y.bit_length()-1
            basis.append((p,y)); basis.sort(reverse=True)
    assert len(basis)==23, len(basis)
    return N,P,G,h,sigcols,{
      'selected_matrix_determinant':int(S.det()),'inverse_denominator':den,
      'exceptional_mod_quaternary_quotient_rank_f2':23,
      'selected_matrix_sha256':canon([[int(S[i,j]) for j in range(64)] for i in range(64)]),
      'inverse_integer_matrix_sha256':canon([[int(N[i,j]) for j in range(64)] for i in range(64)])}

def half_states(cols, offset, maxw):
    out=[collections.defaultdict(list) for _ in range(maxw+1)]
    out[0][0].append(0)
    for k in range(1,maxw+1):
        d=out[k]
        for comb in itertools.combinations(range(24),k):
            s=0; mask=0
            for i in comb: s^=cols[offset+i]; mask|=1<<i
            d[s].append(mask)
    return out

def lin(coeff,vs):
    return z3.Sum([int(c)*v for c,v in zip(coeff,vs) if c]) if any(coeff) else z3.IntVal(0)

def solve_candidate(core,N,P,G,h,emask,degree,genus,e,a,proof_dir,idx,timeout_ms):
    q=[z3.Int(f'q{idx}_{j}') for j in range(16)]
    vals=[z3.IntVal((emask>>j)&1) for j in range(48)]+q
    s=z3.SolverFor('QF_NIA'); s.set(random_seed=0,threads=1)
    if timeout_ms: s.set(timeout=timeout_ms)
    for v in q: s.add(v>=0,v<=degree//2)
    for i in range(64): s.add(lin([int(N[i,j]) for j in range(64)],vals)%8==0)
    nums=[]
    for i in range(140):
        x=lin([int(P[i,j]) for j in range(64)],vals); nums.append(x)
        cap=degree//2 if i<92 else degree//4
        s.add(x>=0,x<=8*cap)
    s.add(lin(h,vals)==8*degree)
    s.add(z3.Sum(nums[92:])==8*e)
    s.add(z3.Sum(nums[:46])==8*a)
    s.add(z3.Sum(nums[:92])+5*z3.Sum(nums[92:])==8*19*degree)
    quad=[]
    for i in range(64):
      for j in range(64):
        if G[i,j]: quad.append(int(G[i,j])*vals[i]*vals[j])
    s.add(z3.Sum(quad)>=64*(-degree-2+2*genus))
    r=s.check()
    rec={'candidate_index':idx,'exceptional_mask':emask,'result':str(r)}
    if r==z3.sat:
        m=s.model(); selected=[(emask>>j)&1 for j in range(48)]+[m.eval(v,model_completion=True).as_long() for v in q]
        pic=N*Matrix(selected)
        assert all(int(x)%8==0 for x in pic)
        vec=[int(x)//8 for x in pic]
        pair=[sum(int(core['raw_cross_pairings_with_basis'][i][j])*vec[j] for j in range(64)) for i in range(140)]
        assert all(0<=x<=degree//2 for x in pair[:92]); assert all(0<=x<=degree//4 for x in pair[92:])
        rec['selected_intersections']=selected; rec['picard_coordinates']=vec; rec['pairing_sha256']=canon(pair)
    elif r==z3.unknown:
        rec['unknown_reason']=s.reason_unknown()
    return rec

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--core',type=pathlib.Path,required=True); ap.add_argument('--output',type=pathlib.Path,required=True)
    ap.add_argument('--degree',type=int,default=6); ap.add_argument('--genus',type=int,default=1); ap.add_argument('--exceptional-mass',type=int,required=True); ap.add_argument('--curve-group-mass',type=int,required=True); ap.add_argument('--candidate-timeout-ms',type=int,default=120000)
    args=ap.parse_args(); t=time.perf_counter(); core=json.loads(args.core.read_text()); N,P,G,h,sigcols,cert=build(core); e=args.exceptional_mass
    left=half_states(sigcols,0,e); right=half_states(sigcols,24,e)
    candidates=[]; join_counts=[]
    for lw in range(e+1):
        rw=e-lw
        if lw>24 or rw>24: continue
        count=0
        for sig,lmasks in left[lw].items():
            rmasks=right[rw].get(sig,()) # XOR sum zero in quotient
            if not rmasks: continue
            count+=len(lmasks)*len(rmasks)
            for lm in lmasks:
                for rm in rmasks: candidates.append(lm | (rm<<24))
        join_counts.append({'left_weight':lw,'right_weight':rw,'compatible_exceptional_patterns':count})
    # deterministic unique set; exact quotient join is exhaustive necessary filter.
    candidates=sorted(set(candidates))
    results=[]
    for i,m in enumerate(candidates): results.append(solve_candidate(core,N,P,G,h,m,args.degree,args.genus,e,args.curve_group_mass,args.output.parent,i,args.candidate_timeout_ms))
    sat=[r for r in results if r['result']=='sat']; unk=[r for r in results if r['result']=='unknown']; unsat=sum(r['result']=='unsat' for r in results)
    report={'schema':SCHEMA,'degree':args.degree,'genus':args.genus,'exceptional_mass':e,'curve_group_mass':args.curve_group_mass,
      'transform_certificate':cert,'join_counts':join_counts,'exact_join_candidate_count':len(candidates),'candidate_result_counts':{'unsat':unsat,'sat':len(sat),'unknown':len(unk)},
      'all_candidates_exactly_resolved':len(unk)==0,'exact_parent_unsat':len(candidates)>=0 and len(unk)==0 and len(sat)==0,
      'survivors':sat,'unknowns':unk,'elapsed_seconds':time.perf_counter()-t,
      'theorem_credit':False,'receiver_credit':False,'low_degree_prefix_complete':False,'full_d176_d192_numerical_orbit_census':False,
      'G10_LOWGENUS_PICARD':'AMBER'}
    report['canonical_sha256_without_this_field']=canon(report); args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'e':e,'a':args.curve_group_mass,'candidates':len(candidates),'unsat':unsat,'sat':len(sat),'unknown':len(unk),'elapsed':report['elapsed_seconds']},sort_keys=True))
    if unk: raise SystemExit(2)

if __name__=='__main__': main()
