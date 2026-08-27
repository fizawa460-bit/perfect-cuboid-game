#!/usr/bin/env python3
"""Reduce the remaining 12 quartic-norm carrier hyperplanes to six exact
biquadratic Kummer connectedness tests on normalizations of six plane quartics.

For a carrier
    x + lambda*y + mu*c = 0
with x,y two of b1,b2,b3 and c the space diagonal, put
    x^2=Sx, y^2=Sy, c^2=S4,
    T=mu^2*S4-Sx-lambda^2*Sy.
Then T=2*lambda*x*y, hence the base image in P2_[a1:a2:a3] is
    T^2=4*lambda^2*Sx*Sy.
The omitted b-coordinate contributes an independent square root Su.  Thus the
hyperplane function algebra over the base-quartic function field K is
    K(sqrt(Sx),sqrt(Su)).

The 12 carriers pair into six common base quartics.  On every normalization:
* Su has a simple smooth zero, so [Su] is ramified and nontrivial;
* Sx has even valuation everywhere.  Smooth intersections are certified by
  even line-intersection multiplicities.  At every node lying on Sx=0, the
  local quadratic tangent cone is a unit multiple of Sx and the quartic term
  is nonzero on both tangent directions, giving valuation exactly 4 on each
  normalization branch.

Therefore [Sx] cannot equal [Su].  Each of the 12 hyperplane sections has one
prime component iff [Sx] is nontrivial, and two prime components iff [Sx] is a
square.  The remaining problem is exactly six unramified Kummer square-
triviality tests (Pic[2] image plus a possible constant squareclass).
"""
import hashlib
import itertools
import json
from math import gcd
from functools import reduce
from pathlib import Path

import sympy as sp

HERE=Path(__file__).resolve().parent
SPLIT=HERE/'ambient-linear-carrier-boundary-offboundary-split.json'
BJ=HERE/'bj-offboundary-genus1-components.json'
OUT=HERE/'quartic-norm-biquadratic-cover-reduction.json'
EXPECTED_SPLIT_SHA='13140597dd2196a0593038534a789a75b2f92cf389df34b2f61462835a9b6abb'
EXPECTED_BJ_SHA='d3543d8eed2b4ba79d384a7491b22f6c3d968542cc16752dd9c025acb6b71ee6'

I=sp.I
a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
A=(a1,a2,a3); B=(b1,b2,b3); COORDS=(a1,a2,a3,b1,b2,b3,c)
S1=a2*a2+a3*a3
S2=a1*a1+a3*a3
S3=a1*a1+a2*a2
S4=a1*a1+a2*a2+a3*a3
SQUARES={b1:S1,b2:S2,b3:S3,c:S4}


def canonical_sha256(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load_locked(path,expected):
    x=json.load(open(path)); claimed=x.pop('canonical_sha256')
    if claimed!=expected or canonical_sha256(x)!=expected:
        raise SystemExit(f'source lock moved: {path.name}')
    return x

def dec(z):
    return sp.Rational(int(z[0]),int(z[1]))+I*sp.Rational(int(z[2]),int(z[3]))

def enc_qi(x):
    x=sp.cancel(sp.expand(x)); xc=sp.cancel(sp.conjugate(x))
    re=sp.cancel((x+xc)/2); im=sp.cancel((x-xc)/(2*I))
    if re.is_Rational is not True or im.is_Rational is not True:
        raise SystemExit(f'coefficient escaped Q(i): {x}')
    return [int(sp.numer(re)),int(sp.denom(re)),int(sp.numer(im)),int(sp.denom(im))]

def ambient_expr(row):
    d={x['coordinate']:dec(x['coefficient_Qi']) for x in row['ambient_linear_form']}
    return sp.expand(sum(d.get(str(v),0)*v for v in COORDS))

def factor_record_expr(fr):
    out=0
    for term in fr['normalized_terms']:
        q=dec(term['coefficient_Qi'])
        mon=sp.Integer(1)
        for v,e in zip(A,term['monomial_exponents']): mon*=v**int(e)
        out += q*mon
    return sp.expand(out)

def canonical_integral_quartic(expr):
    p=sp.Poly(sp.expand(expr),*A,extension=I)
    coeff=[]
    for mon,q in p.terms():
        q=sp.cancel(q)
        if sp.im(q)!=0: raise SystemExit(f'base quartic is not rational: {expr}')
        coeff.append(sp.Rational(sp.re(q)))
    lcm=sp.ilcm(*[int(sp.denom(q)) for q in coeff])
    ints=[int(q*lcm) for q in coeff]
    g=reduce(gcd,[abs(x) for x in ints if x])
    scale=sp.Rational(lcm,g)
    out=sp.Poly(sp.expand(expr*scale),*A,domain=sp.QQ)
    first=out.terms()[0][1]
    if first<0: out=-out
    # Make primitive exactly.
    vals=[int(q) for _,q in out.terms()]
    gg=reduce(gcd,[abs(x) for x in vals if x])
    if gg>1: out=sp.Poly(out.as_expr()/gg,*A,domain=sp.QQ)
    return sp.expand(out.as_expr())

def quartic_key(expr):
    p=sp.Poly(canonical_integral_quartic(expr),*A,domain=sp.QQ)
    return tuple((tuple(mon),int(q)) for mon,q in p.terms())

def poly_terms(expr):
    p=sp.Poly(sp.expand(expr),*A,extension=I)
    return [{'monomial_exponents':list(mon),'coefficient_Qi':enc_qi(q)} for mon,q in p.terms()]

def scalar_associate(f,g):
    pf=sp.Poly(sp.expand(f),*A,extension=I); pg=sp.Poly(sp.expand(g),*A,extension=I)
    if pf.total_degree()!=pg.total_degree(): return None
    tf=pf.terms(); tg=pg.terms()
    if [m for m,_ in tf] != [m for m,_ in tg]: return None
    ratio=sp.cancel(tf[0][1]/tg[0][1])
    if all(sp.cancel(q-ratio*r)==0 for (_,q),(_,r) in zip(tf,tg)): return ratio
    return None

def quadratic_square_matrix(F):
    p=sp.Poly(F,*A,domain=sp.QQ); M=sp.zeros(3)
    for i,v in enumerate(A): M[i,i]=p.coeff_monomial(v**4)
    for i in range(3):
        for j in range(i+1,3):
            q=p.coeff_monomial(A[i]**2*A[j]**2)
            M[i,j]=M[j,i]=sp.Rational(q,2)
    # No odd monomials are allowed in this exact reduction.
    rebuilt=sp.expand(sum(M[i,j]*A[i]**2*A[j]**2 for i in range(3) for j in range(3)))
    if sp.expand(rebuilt-F)!=0: raise SystemExit(f'quartic escaped biquadratic form: {F}')
    return M

def singular_node_certificate(F):
    M=quadratic_square_matrix(F)
    principal={}
    for r in (2,3):
        for S in itertools.combinations(range(3),r):
            d=sp.factor(M.extract(S,S).det())
            if d==0: raise SystemExit(f'non-coordinate singular support possible for {F}, subset {S}')
            principal[''.join(str(i+1) for i in S)]=str(d)
    nodes=[]
    for i in range(3):
        if M[i,i]!=0: continue
        P=[0,0,0]; P[i]=1
        chart=A[i]; locals_=[A[j] for j in range(3) if j!=i]
        f=sp.expand(F.subs(chart,1))
        H=sp.hessian(f,locals_).subs({v:0 for v in locals_})
        det=sp.factor(H.det())
        if det==0: raise SystemExit(f'coordinate singularity not an ordinary node: F={F}, P={P}')
        nodes.append({'projective_point':P,'affine_hessian':[[str(H[r,s]) for s in range(2)] for r in range(2)],'hessian_det':str(det)})
    genus=3-len(nodes)
    if genus not in (1,2): raise SystemExit(f'unexpected normalization genus {genus}')
    fac=sp.factor_list(F,*A,extension=I)[1]
    if len(fac)!=1 or fac[0][1]!=1 or sp.Poly(fac[0][0],*A).total_degree()!=4:
        raise SystemExit(f'base quartic reducible over Q(i): {F} -> {fac}')
    return M,principal,nodes,genus

def line_factors(S):
    fs=sp.factor_list(S,*A,extension=I)[1]
    lines=[]
    for f,e in fs:
        if e!=1 or sp.Poly(f,*A).total_degree()!=1: raise SystemExit(f'nonlinear square radicand factor: {S}')
        lines.append(sp.expand(f))
    if len(lines)!=2: raise SystemExit(f'radicand did not split into two lines: {S}')
    return lines

def line_substitution(line):
    p=sp.Poly(line,*A,extension=I)
    for pivot in A:
        coef=p.coeff_monomial(pivot)
        if coef!=0:
            rhs=-sp.expand(line-coef*pivot)/coef
            return pivot,sp.expand(rhs),[v for v in A if v!=pivot]
    raise SystemExit('zero line')

def restriction_factor_exponents(F,line):
    pivot,rhs,free=line_substitution(line)
    R=sp.expand(F.subs(pivot,rhs))
    if R==0: raise SystemExit(f'line is a component of quartic: {line}')
    fac=sp.factor_list(R,*free,extension=I)[1]
    return R,[{'degree':int(sp.Poly(f,*free).total_degree()),'exponent':int(e),'factor_terms':poly_terms(f)} for f,e in fac]

def eval_point(expr,P):
    return sp.cancel(expr.subs({v:sp.Integer(x) for v,x in zip(A,P)}))

def sx_node_branch_check(F,Sx,nodes):
    records=[]
    for node in nodes:
        P=node['projective_point']
        if eval_point(Sx,P)!=0: continue
        i=P.index(1); chart=A[i]; locals_=[A[j] for j in range(3) if j!=i]
        f=sp.expand(F.subs(chart,1)); sx=sp.expand(Sx.subs(chart,1))
        poly=sp.Poly(f,*locals_)
        q2=sum(coef*sp.prod(v**e for v,e in zip(locals_,mon)) for mon,coef in poly.terms() if sum(mon)==2)
        q4=sp.expand(f-q2)
        ratio=scalar_associate(q2,sx)
        if ratio is None: raise SystemExit(f'node tangent cone not Sx: F={F}, P={P}, q2={q2}, Sx={sx}')
        tangents=sp.factor_list(sx,*locals_,extension=I)[1]
        if len(tangents)!=2 or any(e!=1 or sp.Poly(t,*locals_).total_degree()!=1 for t,e in tangents):
            raise SystemExit(f'Sx tangent cone did not split simply at node {P}')
        tangent_rows=[]
        for tangent,_ in tangents:
            pivot,rhs,free=line_substitution(tangent)
            # line_substitution uses global A; do local solve explicitly instead.
            lp=sp.Poly(tangent,*locals_,extension=I)
            piv=next(v for v in locals_ if lp.coeff_monomial(v)!=0)
            co=lp.coeff_monomial(piv); rr=-sp.expand(tangent-co*piv)/co
            rest=sp.expand(q4.subs(piv,rr))
            if rest==0 or sp.Poly(rest,*[v for v in locals_ if v!=piv]).total_degree()!=4:
                raise SystemExit(f'quartic correction vanishes on tangent at node {P}')
            tangent_rows.append({'tangent_line':str(sp.expand(tangent)),'quartic_term_on_tangent':str(sp.factor(rest)),'normalization_branch_valuation_of_Sx':4})
        records.append({'projective_node':P,'quadratic_tangent_cone':str(sp.factor(q2)),'tangent_cone_over_Sx_unit':str(ratio),'branches':tangent_rows})
    return records

def squareclass_divisor_certificate(F,Sx,Su,nodes):
    sx_lines=line_factors(Sx); su_lines=line_factors(Su)
    sx_restr=[]
    for line in sx_lines:
        R,fac=restriction_factor_exponents(F,line)
        if any(r['exponent']%2 for r in fac):
            raise SystemExit(f'Sx has odd smooth plane intersection multiplicity: F={F}, line={line}, factors={fac}')
        sx_restr.append({'line':str(line),'restricted_quartic':str(sp.factor(R)),'factorization':fac,'all_plane_intersection_multiplicities_even':True})
    node_records=sx_node_branch_check(F,Sx,nodes)
    # Every singular point on Sx must be handled by the branch check above.
    singular_on_sx=[n['projective_point'] for n in nodes if eval_point(Sx,n['projective_point'])==0]
    if sorted(singular_on_sx)!=sorted(r['projective_node'] for r in node_records): raise SystemExit('Sx node inventory mismatch')

    common=[P for P in ([1,0,0],[0,1,0],[0,0,1]) if all(eval_point(line,P)==0 for line in su_lines)]
    if len(common)!=1 or eval_point(F,common[0])==0:
        raise SystemExit(f'Su line intersection lies on base quartic: Su={Su}, common={common}')
    su_restr=[]; odd_found=False
    for line in su_lines:
        if any(eval_point(line,n['projective_point'])==0 for n in nodes):
            raise SystemExit(f'Su ramification line meets a singular node: F={F}, line={line}')
        R,fac=restriction_factor_exponents(F,line)
        odd=any(r['exponent']%2 for r in fac)
        odd_found |= odd
        su_restr.append({'line':str(line),'restricted_quartic':str(sp.factor(R)),'factorization':fac,'has_odd_smooth_intersection_multiplicity':odd})
    if not odd_found: raise SystemExit(f'Su unexpectedly unramified: F={F}, Su={Su}')
    return {
      'Sx_unramified_certificate':{
        'radicand':str(Sx),'line_restrictions':sx_restr,'node_branch_checks':node_records,
        'poles_even_reason':'Sx has homogeneous degree 2, so after dividing by any affine-chart coordinate square all poles are even',
        'conclusion':'all valuations on the normalization are even',
      },
      'Su_ramified_certificate':{
        'radicand':str(Su),'line_restrictions':su_restr,'two_radical_lines_common_point':common[0],
        'common_point_not_on_curve':True,
        'singular_nodes_avoided_by_both_radical_lines':True,
        'conclusion':'Su has an odd valuation at a smooth normalization point and is a nontrivial squareclass',
      },
    }

def coefficients_in_ambient(expr):
    p=sp.Poly(expr,*COORDS,extension=I)
    return {v:p.coeff_monomial(v) for v in COORDS}

split=load_locked(SPLIT,EXPECTED_SPLIT_SHA)
bj=load_locked(BJ,EXPECTED_BJ_SHA)
if bj['constructive_progress']['split_linear_offboundary_hyperplanes_decomposed']!=3:
    raise SystemExit('b_j decomposition prefix moved')
quartic_rows=[r for r in split['carrier_records'] if r['classification']=='OFF_BOUNDARY_IRREDUCIBLE_QUARTIC_BASE_NORM']
if len(quartic_rows)!=12: raise SystemExit('quartic carrier count moved')

groups={}
for row in quartic_rows:
    non=[fr for fr in row['norm_factorization_over_Qi'] if fr['coordinate_factor'] is None]
    if len(non)!=1 or non[0]['degree']!=4 or non[0]['exponent_in_norm']!=4:
        raise SystemExit(f'quartic norm shape moved for carrier {row["carrier_index_1based"]}')
    F=canonical_integral_quartic(factor_record_expr(non[0]))
    groups.setdefault(quartic_key(F),{'F':F,'rows':[]})['rows'].append(row)
if len(groups)!=6 or any(len(g['rows'])!=2 for g in groups.values()):
    raise SystemExit(f'12 carriers did not pair into six quartics: {[len(g["rows"]) for g in groups.values()]}')

records=[]
for gid,g in enumerate(sorted(groups.values(),key=lambda z:quartic_key(z['F'])),1):
    F=g['F']; M,principal,nodes,genus=singular_node_certificate(F)
    member_records=[]; common_radicand_pair=None
    for row in sorted(g['rows'],key=lambda r:r['carrier_index_1based']):
        L=ambient_expr(row); coeff=coefficients_in_ambient(L)
        bvars=[v for v in B if coeff[v]!=0]
        if len(bvars)!=2 or coeff[c]==0: raise SystemExit(f'quartic carrier is not two-b-plus-c: {L}')
        x,y=bvars[0],bvars[1]
        ax=coeff[x]; lam=sp.cancel(coeff[y]/ax); mu=sp.cancel(coeff[c]/ax)
        if lam==0 or mu==0: raise SystemExit('zero lambda/mu')
        Sx=SQUARES[x]; Sy=SQUARES[y]
        unused=next(v for v in B if v not in bvars); Su=SQUARES[unused]
        T=sp.expand(mu*mu*S4-Sx-lam*lam*Sy)
        baseeq=sp.expand(T*T-4*lam*lam*Sx*Sy)
        ratio=scalar_associate(baseeq,F)
        if ratio is None: raise SystemExit(f'elimination quartic mismatch: L={L}, baseeq={baseeq}, F={F}')
        pair=(str(Sx),str(Su))
        if common_radicand_pair is None: common_radicand_pair=(Sx,Su,x,unused)
        elif (str(common_radicand_pair[0]),str(common_radicand_pair[1]))!=pair:
            raise SystemExit(f'paired carriers have different Kummer radicands: {pair} vs {common_radicand_pair[:2]}')
        member_records.append({
          'carrier_index_1based':int(row['carrier_index_1based']),
          'ambient_linear_equation':str(L),
          'chosen_x_radical':str(x),'chosen_y_radical':str(y),'unused_radical':str(unused),
          'lambda':str(lam),'mu':str(mu),'T':str(T),
          'elimination_equation':'T^2=4*lambda^2*Sx*Sy',
          'elimination_polynomial_over_base_quartic_unit':str(ratio),
        })
    Sx,Su,xvar,uvar=common_radicand_pair
    divcert=squareclass_divisor_certificate(F,Sx,Su,nodes)
    records.append({
      'group_id':f'QG{gid:02d}',
      'base_quartic_integral':str(F),
      'base_quartic_terms':poly_terms(F),
      'carrier_members':member_records,
      'normalization':{
        'irreducible_over_Qi':True,
        'biquadratic_square_matrix':[[str(M[i,j]) for j in range(3)] for i in range(3)],
        'nonzero_principal_minors_for_support_size_at_least_2':principal,
        'singularities_are_exactly_coordinate_nodes':nodes,
        'ordinary_node_count':len(nodes),'geometric_genus':genus,
      },
      'Kummer_cover_algebra':{
        'base_function_field':'K=Q(i)(normalization of base quartic)',
        'first_radical':str(xvar),'Sx':str(Sx),
        'second_radical':str(uvar),'Su':str(Su),
        'generic_algebra':'K[sqrt(Sx),sqrt(Su)]',
        'generic_total_rank_before_squareclass_collapse':4,
      },
      'squareclass_divisor_analysis':divcert,
      'connectedness_decision':{
        'Su_nontrivial_ramified':True,
        'Sx_unramified':True,
        'Sx_cannot_equal_Su_squareclass':True,
        'if_Sx_is_square':'each carrier has exactly 2 prime components',
        'if_Sx_is_nonsquare':'each carrier is one prime component of degree 4 over the base normalization',
        'remaining_test':'is the unramified Kummer class [Sx] trivial in K*/K*2? Its Pic[2] image is the first test; if that image vanishes, a residual constant squareclass must also be checked.',
      },
    })

hist={}
for r in records: hist[str(r['normalization']['geometric_genus'])]=hist.get(str(r['normalization']['geometric_genus']),0)+1
if hist!={'1':3,'2':3}: raise SystemExit(f'normalization genus histogram moved: {hist}')
if sum(len(r['carrier_members']) for r in records)!=12: raise SystemExit('carrier pairing count regression')

cert={
 'schema':'STAGE33_07_QUARTIC_NORM_BIQUADRATIC_COVER_REDUCTION_V1',
 'source_locks':{
   'carrier_boundary_offboundary_split_sha256':EXPECTED_SPLIT_SHA,
   'bj_genus1_decomposition_sha256':EXPECTED_BJ_SHA,
 },
 'field':'Q(i), with downstream arithmetic field L=Q(i,sqrt(2))',
 'reduction_summary':{
   'quartic_norm_hyperplanes':12,
   'paired_base_quartics':6,
   'base_quartic_normalization_genus_histogram':hist,
   'each_hyperplane_generic_cover_rank':4,
   'ramified_nontrivial_squareclasses_certified':6,
   'unramified_Kummer_squareclasses_remaining':6,
   'possible_prime_component_count_per_quartic_hyperplane':[1,2],
   'four_component_case_excluded':True,
 },
 'quartic_group_records':records,
 'exact_checks':{
   'twelve_hyperplanes_pair_into_six_identical_base_quartics':True,
   'every_base_quartic_is_irreducible_over_Qi':True,
   'all_projective_singularities_exhausted_by_biquadratic_support_matrix_minors':True,
   'every_base_quartic_singularity_is_an_ordinary_node':True,
   'normalization_genera_are_exactly_three_genus1_and_three_genus2':True,
   'every_hyperplane_elimination_reproduces_its_base_quartic':True,
   'every_pair_has_identical_Sx_and_Su_Kummer_radicands':True,
   'every_Sx_has_even_valuation_on_the_base_normalization':True,
   'every_Su_has_a_simple_smooth_zero_and_is_nonsquare':True,
   'Su_ramification_excludes_Sx_equals_Su_in_squareclasses':True,
   'each_quartic_hyperplane_has_at_most_two_prime_components':True,
 },
 'constructive_progress':{
   'boundary_vs_offboundary_carrier_split_closed':True,
   'split_linear_offboundary_hyperplanes_decomposed':3,
   'quartic_norm_hyperplanes_reduced_to_Kummer_tests':12,
   'quartic_base_normalizations_materialized':6,
   'unramified_Kummer_square_triviality_tests_remaining':6,
   'off_boundary_prime_divisor_decomposition_fully_closed':False,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-6-UNRAMIFIED-KUMMER-SQUARECLASS-TRIVIALITY-ON-3-GENUS1-PLUS-3-GENUS2-NORMALIZATIONS',
 'next_exact_leaf':'L33-07-COMPUTE-6-UNRAMIFIED-KUMMER-CLASSES-IN-PIC2-PLUS-CONSTANT-SQUARECLASSES',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=canonical_sha256(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,'quartic_hyperplanes':'12/12','base_quartics':6,
 'normalization_genus_histogram':hist,
 'ramified_Su_classes':'6/6','unramified_Sx_tests_remaining':6,
 'prime_components_per_quartic_hyperplane':'1 or 2; never 4',
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
