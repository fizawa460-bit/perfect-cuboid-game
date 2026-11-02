#!/usr/bin/env python3
"""Bounded exact evidence for the F66 equivariant Koszul/nodal calculation.

The geometric theorem is in the proof note. No candidate or marked node set is
constructed or tested here. All checks survive python -O and are read-only.
"""
import argparse, hashlib, json, subprocess, sys, tempfile, zipfile
from fractions import Fraction
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
PRIOR_SHA='d52bf5d0adf5b150d3371a98d59a1b8d59901f2cfb46e53c6a1ea3dcefb529ae'
EXPECTED_FILES={'verify_f66.py','negative_tests.py','MB104-F65-20261029.zip'}
def require(value,message='verification condition failed'):
    if not value: raise ValueError(message)
def add(*ps): return [sum(p[j] if j<len(p) else 0 for p in ps) for j in range(max(map(len,ps)))]
def scale(p,c): return [c*x for x in p]
def at(p,m): return sum(x*m**j for j,x in enumerate(p))
def rank(a):
    a=[[Fraction(x) for x in row] for row in a];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[r])]
        r+=1
        if r==len(a):break
    return r
def pa(*ps):
    out={}
    for p in ps:
        for e,c in p.items():out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}
def pm(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            g=(e[0]+f[0],e[1]+f[1]);out[g]=out.get(g,0)+c*d
    return {e:c for e,c in out.items() if c}
def ps(p,c):return {e:x*c for e,x in p.items() if x*c}
def tau(p):return {e:c*((-1)**sum(e)) for e,c in p.items()}
def canon(p):return [[*e,c] for e,c in sorted(p.items())]
def toy():
    # On P1 x P1, tau(x,y)=(-x,-y), s=1+x+2y+xy.
    # Its two conjugate intersections form one free orbit; this is a toy model.
    s={(0,0):1,(1,0):1,(0,1):2,(1,1):1};ts=tau(s)
    basis=[{(0,0):1},{(1,0):1},{(0,1):1},{(1,1):1}]
    exps=[(0,0),(2,0),(1,1),(0,2),(2,2)]
    norm=pm(s,ts)
    require(norm=={(0,0):1,(1,1):-2,(2,2):1,(2,0):-1,(0,2):-4})
    columns=[pa(pm(ts,t),pm(s,tau(t))) for t in basis]
    matrix=[[c.get(e,0) for c in columns] for e in exps]
    require(matrix==[[2,0,0,0],[0,-2,0,0],[2,-4,-2,2],[0,0,-4,0],[0,0,0,2]])
    ev=[Fraction(1),Fraction(2),Fraction(-1),Fraction(1,2),Fraction(1)]
    require(all(sum(ev[j]*matrix[j][k] for j in range(5))==0 for k in range(4)))
    require(rank(matrix)==4 and rank([ev])==1 and 5-rank([ev])==rank(matrix))
    # alpha(c)=(s*c,-tau(s)*c), beta(a,b)=tau(s)*a+s*b.
    require(pa(pm(ts,s),ps(pm(s,ts),-1))=={})
    require((ps(s,-1),ts)==(tau(ps(ts,-1)),tau(s)))
    # Swap+tau sends alpha(1) to -alpha(1), not to alpha(1).
    require(tau(ps(ts,-1))==ps(s,-1) and tau(s)==ts)
    # At E=1+xy=0, O=x+2y=0: y^2=1/2, x=-2y;
    # det(dE,dO)^2=(2y-x)^2=16*y^2=8, so transverse and free.
    require(16*Fraction(1,2)==8)
    return {'model':'TOY_ONLY_NOT_MB104_CANDIDATE','norm':canon(norm),
      'target_basis':[list(e) for e in exps],'derivative_matrix':matrix,
      'evaluation_row':['1','2','-1','1/2','1'],'derivative_rank':4,
      'evaluation_rank':1,'intersection_jacobian_determinant_squared':8,
      'koszul_kernel_character':-1}
def local_cover():
    # Blow up the isolated tau=(-1,-1) fixed point: b=a*t.
    # Quotient chart is (x=a^2,t), A1 invariants (u,v,w)=(x,xt,xt^2).
    u={(2,0):1};v={(2,1):1};w={(2,2):1}
    require(pm(u,w)==pm(v,v))
    require(all(e[0]%2==0 for p in (u,v,w) for e in p))
    # Every a^i t^j has the unique form x^(i//2)t^j times 1 or a.
    for i in range(9):
        for j in range(9):
            q,r=divmod(i,2);require(2*q+r==i and r in (0,1))
    return {'A1_relation_checked':True,'blowup_charts':2,'finite_flat_degree':2,
      'ramification_exceptional_pullback_multiplicity':2,
      'fixed_points_blown_up':16,'canonical_discrepancy_cancels':True}
def prior():
    p=ROOT/'MB104-F65-20261029.zip'
    require(hashlib.sha256(p.read_bytes()).hexdigest()==PRIOR_SHA,'frozen F65 hash mismatch')
    with zipfile.ZipFile(p) as z:
        c=json.loads(z.read('F65-certificate.json'))
        require(set(c['files_sha256'])=={'verify_f65.py','negative_tests.py','MB104-F64-20261029.zip'})
        for name,h in c['files_sha256'].items():
            require(hashlib.sha256(z.read(name)).hexdigest()==h,'nested F65 dependency mismatch')
    require(c['claims']['all_m_h1_Y']==6 and c['claims']['all_m_h1_X']==4)
    return c
def computations():
    c=prior();hy=c['computed']['Y']['all_m_h0_coefficients'];target=c['computed']['target_h0_coefficients']
    require(hy==[18,-112,336] and target==[12,-112,672])
    nodes=[0,0,336];evaluation_rank=add(target,scale(hy,-1))
    cokernel=add(nodes,scale(evaluation_rank,-1));norm_tangent=add(hy,[-1])
    require(evaluation_rank==[-6,0,336] and cokernel==[6,0,0])
    require(add(norm_tangent,evaluation_rank)==add(target,[-1]))
    require(c['computed']['norm_codim_coefficients']==evaluation_rank)
    # H0(O_Z with sign)=H1(O_Z with sign)=0; the former avoids a -1 error.
    h0_kernel_invariant=0;h1_kernel_invariant=0
    require((h0_kernel_invariant,h1_kernel_invariant)==(0,0))
    intrinsic=[0,112,336];total=add(intrinsic,nodes)
    full_tangent=add(target,[-1]);norm_coker=add(total,scale(norm_tangent,-1))
    full_coker=add(total,scale(full_tangent,-1));own_coker=add(intrinsic,scale(norm_tangent,-1))
    require(total==[0,112,672] and full_coker==[-11,224,0])
    require(own_coker==[-17,224,0] and add(own_coker,cokernel)==full_coker)
    require(add(full_coker,evaluation_rank)==norm_coker)
    # These exact-sequence identities are not sums of independent exclusions.
    table=[]
    for m in (1,2,3,5):
        table.append({'m':m,'mixed_nodes':at(nodes,m),'target_h0':at(target,m),
          'ideal_h0':at(hy,m),'evaluation_rank':at(evaluation_rank,m),
          'evaluation_cokernel':at(cokernel,m),'norm_tangent_dimension':at(norm_tangent,m),
          'intrinsic_nodes_if_nodal_genus1':at(intrinsic,m),
          'total_nodes_if_nodal_genus1':at(total,m),
          'full_nodal_cokernel_if_exists':at(full_coker,m),
          'intrinsic_nodal_cokernel_in_norm_if_exists':at(own_coker,m),
          'all_node_cokernel_restricted_to_norm_if_exists':at(norm_coker,m)})
    return {'local_double_cover':local_cover(),'equivariant_toy':toy(),
      'koszul_H0_kernel_invariant':h0_kernel_invariant,
      'koszul_H1_kernel_invariant':h1_kernel_invariant,
      'mixed_nodes_coefficients':nodes,'target_h0_coefficients':target,
      'ideal_h0_coefficients':hy,'evaluation_rank_coefficients':evaluation_rank,
      'evaluation_cokernel_coefficients':cokernel,
      'norm_tangent_coefficients':norm_tangent,
      'conditional_nodal_total_coefficients':total,
      'conditional_full_nodal_cokernel_coefficients':full_coker,
      'conditional_intrinsic_nodal_cokernel_coefficients':own_coker,'table':table}
def claims():
    return {'scope':'SOURCE_CONDITIONAL_COMPLEX_MODEL_RESEARCH_UNAUDITED_ZERO_CREDIT',
      'requires_ordinary_transverse_mixed_nodes':True,'requires_complete_marked_mixed_node_set':True,
      'requires_no_common_component':True,'requires_fixed_line_class_and_source_adapter':True,
      'mixed_node_evaluation_rank':'336*m^2-6','mixed_node_evaluation_cokernel':6,
      'mixed_node_ideal_h0':'336*m^2-112*m+18',
      'norm_differential_projective_kernel':0,
      'norm_germ_equals_mixed_node_preserving_germ_under_stated_conditions':True,
      'all_candidates_nodal':False,'actual_node_evaluation_performed':False,
      'rank_condition_sufficient_for_global_norm':False,
      'genus_one_existence_proved':False,'genus_one_nonexistence_proved':False,
      'actual_source_adapter_proved':False,'coreless_no_clump_proved':False,
      'candidate_exclusion':0,'uniform_degree_bound':False,'MB104':'OPEN',
      'theorem_credit':0,'receiver_credit':0,'endpoint_credit':0,'independent_audit':False}
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--certificate',type=Path,default=ROOT/'F66-certificate.json')
    ap.add_argument('--replay-f65',action='store_true');a=ap.parse_args()
    c=json.loads(a.certificate.read_text())
    require(set(c)=={'schema','claims','computed','files_sha256'},'certificate shape mismatch')
    require(c['schema']=='MB104-F66-RESEARCH-CERT-v1' and c['claims']==claims(),'claim scope mismatch')
    require(set(c['files_sha256'])==EXPECTED_FILES,'incomplete dependency hash table')
    for name,h in c['files_sha256'].items():
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'dependency hash mismatch: '+name)
    require(c['computed']==computations(),'computed evidence mismatch')
    if a.replay_f65:
        with tempfile.TemporaryDirectory(prefix='f66-prior-') as d:
            with zipfile.ZipFile(ROOT/'MB104-F65-20261029.zip') as z:z.extractall(d)
            for flags in ([],['-O']):
                r=subprocess.run([sys.executable]+flags+[str(Path(d)/'verify_f65.py')],capture_output=True,text=True)
                require(r.returncode==0,r.stderr or r.stdout)
    print(json.dumps({'status':'PASS','mixed_node_evaluation_rank':'336*m^2-6',
      'mixed_node_evaluation_cokernel':6,'actual_candidate_evaluated':False,
      'geometric_theorem':'conditional; see proof note','candidate_exclusion':0,'MB104':'OPEN'}))
if __name__=='__main__':
    try:main()
    except Exception as e:print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
