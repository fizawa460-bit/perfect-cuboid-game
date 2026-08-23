#!/usr/bin/env python3
"""Exact bounded intersection-coordinate solver for Stage32 residual parents."""
from __future__ import annotations
import argparse, hashlib, json, math, pathlib, time
from typing import Any
import sympy, z3
from sympy import Matrix
from cap_certificate import canonical_sha256, load_and_verify

SCHEMA="STAGE32_INTERSECTION_COORD_BUDGET_V1"
ALGORITHM_ID="INTERSECTION_COORD_DENOM8_QF_NIA_CAP140_V1"
SELECTED_ROWS=list(range(92,140))+[0,1,2,3,4,8,9,12,16,17,24,32,44,48,52,68]
EXPECTED_SELECTED_DETERMINANT=274877906944
EXPECTED_INVERSE_DENOMINATOR=8

def matrix_list(m): return [[int(m[i,j]) for j in range(m.cols)] for i in range(m.rows)]
def matrix_sha256(m): return canonical_sha256(matrix_list(m))
def linear(cs,vs):
    terms=[c*vs[j] for j,c in enumerate(cs) if c]
    return z3.Sum(terms) if terms else z3.IntVal(0)

def build_transform(core:dict[str,Any])->dict[str,Any]:
    rows=Matrix(core['raw_cross_pairings_with_basis']); gram=Matrix(core['basis_gram'])
    selected=Matrix([core['raw_cross_pairings_with_basis'][i] for i in SELECTED_ROWS])
    det=int(selected.det()); assert abs(det)==EXPECTED_SELECTED_DETERMINANT
    inv=selected.inv(); den=1
    for value in inv: den=math.lcm(den,int(sympy.denom(value)))
    assert den==EXPECTED_INVERSE_DENOMINATOR
    m=inv*den; assert all(sympy.denom(v)==1 for v in m)
    m=Matrix([[int(m[i,j]) for j in range(64)] for i in range(64)])
    assert selected*m==den*Matrix.eye(64)
    t=rows*m; assert all(sympy.denom(v)==1 for v in t)
    t=Matrix([[int(t[i,j]) for j in range(64)] for i in range(140)])
    h=Matrix(core['hyperplane']).T*gram*m
    assert all(sympy.denom(v)==1 for v in h)
    hrow=[int(h[0,j]) for j in range(64)]
    b=m.T*gram*m; assert all(sympy.denom(v)==1 for v in b)
    b=Matrix([[int(b[i,j]) for j in range(64)] for i in range(64)])
    cert={'algorithm_id':ALGORITHM_ID,'selected_rows_1based':[i+1 for i in SELECTED_ROWS],
          'selected_matrix_determinant':det,'inverse_denominator':den,
          'selected_matrix_sha256':matrix_sha256(selected),'inverse_integer_matrix_sha256':matrix_sha256(m),
          'transformed_pairing_matrix_sha256':matrix_sha256(t),'transformed_gram_sha256':matrix_sha256(b),
          'transformed_hform_sha256':canonical_sha256(hrow)}
    return {'denominator':den,'inverse_integer':m,'pairings':t,'hform':hrow,'gram':b,'certificate':cert}

def verify_model(core,transform,ys,degree,genus,e,a):
    den=transform['denominator']; m=transform['inverse_integer']; nums=m*Matrix(ys)
    assert all(int(v)%den==0 for v in nums); x=[int(v)//den for v in nums]
    rows=core['raw_cross_pairings_with_basis']; ps=[sum(int(r[j])*x[j] for j in range(64)) for r in rows]
    cc,ec=degree//2,degree//4
    assert all(0<=v<=cc for v in ps[:92]) and all(0<=v<=ec for v in ps[92:])
    assert sum(ps[92:])==e and sum(ps[:46])==a and sum(ps[:92])+5*sum(ps[92:])==19*degree
    g=core['basis_gram']; square=sum(x[i]*int(g[i][j])*x[j] for i in range(64) for j in range(64))
    assert square>=-degree-2+2*genus
    hp=core['hyperplane']; hx=sum(int(hp[i])*int(g[i][j])*x[j] for i in range(64) for j in range(64))
    assert hx==degree and [ps[i] for i in SELECTED_ROWS]==ys
    return {'picard_coordinates':x,'selected_intersections':ys,'self_intersection':square,
            'intersection_vector_sha256':canonical_sha256(ps)}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--core',type=pathlib.Path,required=True); p.add_argument('--cap-certificate',type=pathlib.Path,required=True)
    p.add_argument('--output-dir',type=pathlib.Path,required=True); p.add_argument('--degree',type=int,required=True); p.add_argument('--genus',type=int,choices=(0,1),required=True)
    p.add_argument('--exceptional-mass',type=int,required=True); p.add_argument('--curve-group-mass',type=int,required=True); p.add_argument('--timeout',type=float,default=180.0); p.add_argument('--proof',action='store_true')
    args=p.parse_args(); assert args.degree>0 and args.degree%2==0
    core,_,cap_summary=load_and_verify(args.core,args.cap_certificate); tr=build_transform(core); den=tr['denominator']; t=tr['pairings']; m=tr['inverse_integer']; b=tr['gram']
    cc,ec=args.degree//2,args.degree//4
    if args.proof: z3.set_param(proof=True)
    y=[z3.Int(f'intersection_coord_{j+1}') for j in range(64)]; s=z3.SolverFor('QF_NIA'); s.set(random_seed=0,threads=1)
    if args.timeout: s.set(timeout=int(args.timeout*1000))
    for j in range(48): s.add(y[j]>=0,y[j]<=ec)
    for j in range(48,64): s.add(y[j]>=0,y[j]<=cc)
    for i in range(64): s.add(linear([int(m[i,j]) for j in range(64)],y)%den==0)
    pn=[]
    for i in range(140):
        num=linear([int(t[i,j]) for j in range(64)],y); pn.append(num); cap=cc if i<92 else ec; s.add(num>=0,num<=den*cap)
    s.add(linear(tr['hform'],y)==den*args.degree); s.add(z3.Sum(pn[92:])==den*args.exceptional_mass); s.add(z3.Sum(pn[:46])==den*args.curve_group_mass)
    s.add(z3.Sum(pn[:92])+5*z3.Sum(pn[92:])==den*19*args.degree)
    q=[int(b[i,j])*y[i]*y[j] for i in range(64) for j in range(64) if b[i,j]]; lower=-args.degree-2+2*args.genus; s.add(z3.Sum(q)>=den*den*lower)
    label=f'd{args.degree}-g{args.genus}-e{args.exceptional_mass}-a{args.curve_group_mass}'; shard=args.output_dir/f'coord-{label}'; shard.mkdir(parents=True,exist_ok=True)
    smt=s.to_smt2(); (shard/'problem.smt2').write_text(smt,encoding='utf-8',newline='\n'); smt_sha=hashlib.sha256(smt.encode()).hexdigest()
    survivors=[]; started=time.perf_counter(); result=s.check()
    while result==z3.sat:
        model=s.model(); vals=[model.eval(v,model_completion=True).as_long() for v in y]; survivors.append(verify_model(core,tr,vals,args.degree,args.genus,args.exceptional_mass,args.curve_group_mass)); s.add(z3.Or([v!=q for v,q in zip(y,vals)])); result=s.check()
    elapsed=time.perf_counter()-started; proof_sha=None; proof_name=None
    if result==z3.unsat and args.proof:
        text=s.proof().sexpr()+'\n'; proof_name='proof.sexpr'; (shard/proof_name).write_text(text,encoding='utf-8',newline='\n'); proof_sha=hashlib.sha256(text.encode()).hexdigest()
    complete=result==z3.unsat
    deterministic={'schema':SCHEMA,'algorithm_id':ALGORITHM_ID,'degree':args.degree,'genus':args.genus,'exceptional_mass':args.exceptional_mass,'curve_group_mass':args.curve_group_mass,
      'core_canonical_sha256':core['canonical_sha256_without_this_field'],'cap_certificate_canonical_sha256':cap_summary['certificate_canonical_sha256'],'transform_certificate':tr['certificate'],
      'solver_result':str(result),'complete':complete,'exact_survivor_count':len(survivors) if complete else None,'survivors':survivors if complete else [],'smt2_sha256':smt_sha,'proof_sha256':proof_sha,'random_seed':0,'threads':1}
    payload={**deterministic,'unknown_reason':s.reason_unknown() if result==z3.unknown else None,'elapsed_seconds':round(elapsed,6),'files':{'problem':'problem.smt2','proof':proof_name},
      'deterministic_result_sha256':canonical_sha256(deterministic),'floating_point_feasibility_credit':False,'receiver_credit':False}
    unsigned=dict(payload); payload['checkpoint_sha256_without_this_field']=canonical_sha256(unsigned); (shard/'checkpoint.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(payload,sort_keys=True));
    if not complete: raise SystemExit('intersection-coordinate exact enumeration did not close this parent')
if __name__=='__main__': main()
