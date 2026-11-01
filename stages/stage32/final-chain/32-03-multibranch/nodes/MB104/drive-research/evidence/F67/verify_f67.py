#!/usr/bin/env python3
"""Bounded exact evidence for F67 collision Artin algebras and norm jets.

No MB104 candidate, finite window, or branch partition is computed by this
script. The all-m geometric argument is in the accompanying proof note.
"""
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
from fractions import Fraction
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
PRIOR_SHA='4093984e78d817e8dd32724a0054e814f116cf7782f5a81923c559f2e940c218'
EXPECTED_FILES={'verify_f67.py','negative_tests.py','MB104-F66-20261029.zip'}
def require(v,m='verification condition failed'):
    if not v:raise ValueError(m)
def add(*ps):return [sum(p[j] if j<len(p) else 0 for p in ps) for j in range(max(map(len,ps)))]
def scale(p,c):return [c*x for x in p]
def at(p,m):return sum(x*m**j for j,x in enumerate(p))
def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    while len(r)>1 and r[-1]==0:r.pop()
    return r
def pa(*ps):
    r={}
    for p in ps:
        for e,c in p.items():r[e]=r.get(e,0)+c
    return {e:c for e,c in r.items() if c}
def pm(p,q):
    r={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(x+y for x,y in zip(e,f));r[k]=r.get(k,0)+a*b
    return {e:c for e,c in r.items() if c}
def ps(p,a):return {e:c*a for e,c in p.items() if c*a}
def canon(p):return [[*e,c] for e,c in sorted(p.items())]
def rank(a):
    a=[[Fraction(x) for x in row] for row in a];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k];v=a[r][j];a[r]=[x/v for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[r])]
        r+=1
        if r==len(a):break
    return r
def hilbert(a,b):
    h=[d+1-max(0,d-a+1)-max(0,d-b+1)+max(0,d-a-b+1) for d in range(a+b-1)]
    numerator=[1]+[0]*(a+b)
    numerator[a]-=1;numerator[b]-=1;numerator[a+b]+=1
    require(mul(h,[1,-2,1])==numerator)
    require(sum(h)==a*b and h[-1]==1 and all(x>0 for x in h))
    return {'a':a,'b':b,'r':a+b,'hilbert_function':h,'length':sum(h),
        'jets_sufficient':a+b-2,'loewy_length':a+b-1}
def local_triple():
    # Variables (x,y,e). The ordinary triple is y*x*(y-x), split 1+2.
    one={(0,0,0):1};x={(1,0,0):1};y={(0,1,0):1};e={(0,0,1):1}
    f=y;g=pm(x,pa(y,ps(x,-1)));base=pm(f,g)
    df=ps(one,-1);dg=x
    h1=pa(pm(g,df),pm(f,dg));h2=pm(df,dg)
    require(h1=={(2,0,0):1} and h2=={(1,0,0):-1})
    moving=pm(pa(f,pm(e,df)),pa(g,pm(e,dg)))
    require(moving==pa(base,pm(e,h1),pm(pm(e,e),h2)))
    # Q=C[[x,y]]/(y,x^2). Values discard the nonzero nilpotent x.
    def residue(p):return {k:v for k,v in p.items() if k[1]==0 and k[0]<2}
    require(residue(x)==x and residue(h1)=={} and residue(ps(h2,-1))==x)
    require(pm(x,x)=={(2,0,0):1} and residue(pm(x,x))=={})
    require(residue(pa(h2,ps(h2,-1)))=={})
    slopes=[(0,1),(1,0),(-1,1)]
    det=[slopes[i][0]*slopes[j][1]-slopes[i][1]*slopes[j][0] for i in range(3) for j in range(i+1,3)]
    require(all(det))
    return {'scope':'LOCAL_TOY_NOT_AN_MB104_CANDIDATE','branches':'y, x, y-x',
        'sheet_partition':[1,2],'pairwise_tangent_determinants':det,
        'collision_ideal':['y','x^2'],'collision_algebra_basis':['1','x'],
        'collision_length':2,'reduced_support_length':1,
        'value_only_false_pass':canon(x),'first_order_coefficient':canon(h1),
        'required_second_order_coefficient':canon(h2),
        'straight_line_second_order_obstruction':canon(ps(h2,-1)),
        'exact_factorized_family':canon(moving),'all_candidate_exclusions':0}
def norm_recurrence():
    # P1xP1 toy from F66; tau(x,y)=(-x,-y). All polynomials are exact.
    s={(0,0):1,(1,0):1,(0,1):2,(1,1):1}
    ts=lambda p:{k:v*((-1)**sum(k)) for k,v in p.items()}
    base=pm(s,ts(s));monomials=[{(0,0):1},{(1,0):1},{(0,1):1},{(1,1):1}]
    target=[(0,0),(2,0),(1,1),(0,2),(2,2)]
    L=lambda t:pa(pm(ts(s),t),pm(s,ts(t)))
    mat=[[L(p).get(k,0) for p in monomials] for k in target]
    require(rank(mat)==4)
    coeffs=[s,{(0,0):1,(1,0):2},{(0,1):-1,(1,1):1},{(0,0):3},{(1,0):1},{}]
    b=[];rows=[]
    for n in range(len(coeffs)):
        b.append(pa(*(pm(coeffs[i],ts(coeffs[n-i])) for i in range(n+1))))
    for n in range(1,len(coeffs)):
        lower=pa(*(pm(coeffs[i],ts(coeffs[n-i])) for i in range(1,n))) if n>1 else {}
        residual=pa(b[n],ps(lower,-1))
        require(residual==L(coeffs[n]))
        row={'order':n,'full_coefficient':canon(b[n]),'lower_quadratic_sum':canon(lower),
            'residual_equals_unique_linear_lift':True}
        rows.append(row)
    # An independent point pair x^2=2, xy=-1, y^2=1/2 has E=1+xy=0.
    # t=1 gives t*tau(t)=1, so a tangent straight line has second-order obstruction -1.
    require(L(monomials[0])=={(0,0):2,(1,1):2})
    require(pm(monomials[0],ts(monomials[0]))=={(0,0):1})
    return {'scope':'GLOBAL_TOY_NOT_AN_MB104_CANDIDATE','linear_rank':4,
        'orders_checked':len(rows),'recurrence_checks':rows,
        'first_order_PASS_does_not_imply_second_order_PASS':True}
def prior():
    p=ROOT/'MB104-F66-20261029.zip'
    require(hashlib.sha256(p.read_bytes()).hexdigest()==PRIOR_SHA,'frozen F66 hash mismatch')
    with zipfile.ZipFile(p) as z:
        c=json.loads(z.read('F66-certificate.json'))
        require(set(c['files_sha256'])=={'verify_f66.py','negative_tests.py','MB104-F65-20261029.zip'})
        for n,h in c['files_sha256'].items():require(hashlib.sha256(z.read(n)).hexdigest()==h,'nested F66 dependency mismatch')
    return c
def computations():
    c=prior();hy=c['computed']['ideal_h0_coefficients'];target=c['computed']['target_h0_coefficients']
    length=[0,0,336];linear_rank=add(target,scale(hy,-1));coker=add(length,scale(linear_rank,-1))
    require(hy==[18,-112,336] and target==[12,-112,672])
    require(linear_rank==[-6,0,336] and coker==[6,0,0])
    examples=[hilbert(a,b) for a,b in ((1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(3,4))]
    for a in range(1,9):
        for b in range(1,9):hilbert(a,b)
    table=[{'m':m,'collision_scheme_length':at(length,m),'jet_evaluation_rank':at(linear_rank,m),
        'jet_evaluation_cokernel':at(coker,m),'linear_lift_dimension':at(hy,m),
        'norm_germ_dimension':at(hy,m)-1} for m in (1,2,3,5)]
    return {'scheme_length_coefficients':length,'jet_rank_coefficients':linear_rank,
        'jet_cokernel_coefficients':coker,'linear_lift_dimension_coefficients':hy,
        'ordinary_partition_hilbert_examples':examples,'ordinary_partition_bounded_checks':64,
        'local_ordinary_triple':local_triple(),'norm_recurrence':norm_recurrence(),'table':table}
def claims():
    return {'scope':'SOURCE_CONDITIONAL_COMPLEX_MODEL_RESEARCH_UNAUDITED_ZERO_CREDIT',
        'MB104_goal':'POPULATION_WIDE_FINITE_DEGREE_INTERSECTION_WINDOW',
        'requires_ordinary_nodes_only':False,'allows_ordinary_multibranch_points':True,
        'requires_full_marked_collision_scheme_not_just_support':True,
        'requires_no_common_component_and_fixed_line_class':True,
        'requires_cover_etale_on_collision_scheme':True,
        'collision_scheme_length':'336*m^2','jet_evaluation_rank':'336*m^2-6',
        'jet_evaluation_cokernel':6,'norm_immersion_at_integral_split_locus':True,
        'ordinary_partition_local_length':'a*b','ordinary_partition_jet_order':'a+b-2',
        'formal_norm_lift_at_each_finite_order':'IFF_RECURSIVE_RESIDUES_VANISH_WITH_FIXED_INITIAL_s',
        'first_order_test_sufficient_for_full_norm':False,
        'arbitrary_finite_jet_PASS_proves_global_norm':False,
        'failure_of_chosen_deformation_excludes_base_candidate':False,
        'actual_candidate_or_collision_scheme_evaluated':False,
        'genus_one_existence_or_nonexistence_proved':False,
        'actual_source_adapter_proved':False,'coreless_no_clump_proved':False,
        'uniform_degree_bound':False,'population_wide_finite_window_proved':False,
        'finite_picard_enumeration_released':False,'candidate_exclusion':0,'MB104':'OPEN',
        'theorem_credit':0,'receiver_credit':0,'endpoint_credit':0,'independent_audit':False}
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--certificate',type=Path,default=ROOT/'F67-certificate.json')
    ap.add_argument('--replay-f66',action='store_true');a=ap.parse_args()
    c=json.loads(a.certificate.read_text())
    require(set(c)=={'schema','claims','computed','files_sha256'},'certificate shape mismatch')
    require(c['schema']=='MB104-F67-RESEARCH-CERT-v1' and c['claims']==claims(),'claim scope mismatch')
    require(set(c['files_sha256'])==EXPECTED_FILES,'incomplete dependency hash table')
    for n,h in c['files_sha256'].items():require(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h,'dependency hash mismatch: '+n)
    require(c['computed']==computations(),'computed evidence mismatch')
    if a.replay_f66:
        with tempfile.TemporaryDirectory(prefix='f67-prior-') as d:
            with zipfile.ZipFile(ROOT/'MB104-F66-20261029.zip') as z:z.extractall(d)
            for flags in ([],['-O']):
                run=subprocess.run([sys.executable]+flags+[str(Path(d)/'verify_f66.py')],capture_output=True,text=True)
                require(run.returncode==0,run.stderr or run.stdout)
    print(json.dumps({'status':'PASS','jet_evaluation_rank':'336*m^2-6','jet_cokernel':6,
      'actual_candidate_evaluated':False,'finite_window_proved':False,'candidate_exclusion':0,'MB104':'OPEN'}))
if __name__=='__main__':
    try:main()
    except Exception as e:print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
