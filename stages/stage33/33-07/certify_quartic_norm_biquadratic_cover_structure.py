#!/usr/bin/env python3
"""Reduce the 12 quartic-norm off-boundary carrier sections to six exact
biquadratic-cover / Pic[2] decisions.

Every quartic carrier linear form uses exactly two of b1,b2,b3 together with c,
omitting the third b-variable.  Its full sign norm is Q^4 for an irreducible
plane quartic Q(a1,a2,a3).  The projective sign stabilizer of the hyperplane is
V4: flip the omitted radical, and flip all three radicals occurring in L.

Writing L = alpha*r + beta*s + gamma*c, squaring L=0 and using the surface
relations gives

    r*s = M := (gamma^2*q_c - alpha^2*q_r - beta^2*q_s)/(2*alpha*beta),
    q_r*q_s = M^2  on Q.

Thus the two occurring b-radicands have the same squareclass on K(Q).  Exact
Groebner checks show they have no common zero on Q, so their zero divisors on
the normalization of Q are even.  They define one unramified class tau_Q in
Pic(Qtilde)[2], possibly trivial.  The omitted b-radicand has an explicitly odd
intersection divisor and is therefore a genuinely ramified, non-square class.

Hence each carrier normalization is controlled by one definite ramified
quadratic extension plus the single binary decision tau_Q != 0.  If tau_Q is
nontrivial the carrier is a connected V4 cover; if tau_Q is trivial it splits
into two conjugate copies of the ramified quadratic cover.  No global Gersten
lift or off-boundary residue vanishing is inferred here.
"""
import hashlib, itertools, json
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
IN=HERE/'ambient-linear-carrier-boundary-offboundary-split.json'
OUT=HERE/'quartic-norm-biquadratic-cover-structure.json'
EXPECTED_SPLIT_SHA='13140597dd2196a0593038534a789a75b2f92cf389df34b2f61462835a9b6abb'

a1,a2,a3,b1,b2,b3,c=sp.symbols('a1 a2 a3 b1 b2 b3 c')
BASE=(a1,a2,a3); BRADS=(b1,b2,b3); RADS=(b1,b2,b3,c)
COORDS=(a1,a2,a3,b1,b2,b3,c); I=sp.I
Q_SQ={
 b1:a2*a2+a3*a3,
 b2:a1*a1+a3*a3,
 b3:a1*a1+a2*a2,
 c:a1*a1+a2*a2+a3*a3,
}


def sha(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def dec(z): return sp.Rational(int(z[0]),int(z[1]))+I*sp.Rational(int(z[2]),int(z[3]))
def enc_qi(x):
    x=sp.cancel(sp.expand(x)); xc=sp.cancel(sp.conjugate(x))
    re=sp.cancel((x+xc)/2); im=sp.cancel((x-xc)/(2*I))
    if re.is_Rational is not True or im.is_Rational is not True: raise SystemExit(f'escaped Q(i): {x}')
    return [int(sp.numer(re)),int(sp.denom(re)),int(sp.numer(im)),int(sp.denom(im))]
def form_expr(row):
    d={x['coordinate']:dec(x['coefficient_Qi']) for x in row['ambient_linear_form']}
    return sp.expand(sum(d.get(str(v),0)*v for v in COORDS))
def quartic_expr(frec):
    out=0
    for t in frec['normalized_terms']:
        q=dec(t['coefficient_Qi']); m=t['monomial_exponents']
        out += q*a1**m[0]*a2**m[1]*a3**m[2]
    return sp.expand(out)
def projective_empty(polys):
    for v in BASE:
        G=sp.groebner([*polys,v-1],*BASE,extension=I,order='lex')
        if not G.contains(sp.Integer(1)): return False
    return True
def canonical_coeff_tuple(expr):
    p=sp.Poly(sp.expand(expr),*RADS,extension=I)
    vals=[sp.cancel(p.coeff_monomial(v)) for v in RADS]
    pivot=next((q for q in vals if q!=0),None)
    if pivot is None: raise SystemExit('zero radical form')
    return tuple(sp.cancel(q/pivot) for q in vals)
def sign_transform(expr,signs):
    return sp.expand(expr.subs({v:s*v for v,s in zip(RADS,signs)}))
def normalized_terms_key(frec): return json.dumps(frec['normalized_terms'],sort_keys=True,separators=(',',':'))
def poly_proportional(p,q):
    P=sp.Poly(sp.expand(p),*BASE,extension=I); Q=sp.Poly(sp.expand(q),*BASE,extension=I)
    pd={m:c for m,c in P.terms()}; qd={m:c for m,c in Q.terms()}
    common=next((m for m in pd if pd[m]!=0 and qd.get(m,0)!=0),None)
    if common is None: return None
    lam=sp.cancel(pd[common]/qd[common])
    return lam if sp.expand(p-lam*q)==0 else None

def singular_points(Q):
    eq=[Q,*[sp.diff(Q,v) for v in BASE]]
    pts=set()
    for chart_i,chart in enumerate(BASE):
        sol=sp.solve([*eq,chart-1],BASE,dict=True)
        for s in sol:
            vals=[sp.simplify(s.get(v,v)) for v in BASE]
            if any(v.free_symbols for v in vals): raise SystemExit(f'positive-dimensional singular solve for {Q}')
            pivot=next(x for x in vals if x!=0)
            vals=tuple(sp.cancel(x/pivot) for x in vals)
            pts.add(vals)
    return sorted(pts,key=str)
def ordinary_node_check(Q,P):
    k=next(i for i,x in enumerate(P) if x!=0)
    chart=BASE[k]; others=[v for i,v in enumerate(BASE) if i!=k]
    subs={chart:1}
    for i,v in enumerate(BASE):
        if i!=k: subs[v]=v+P[i]/P[k]
    local=sp.expand(Q.subs(subs))
    t=sp.symbols('_t')
    scaled=sp.expand(local.subs({v:t*v for v in others}))
    quad=sp.expand(sp.Poly(scaled,t).coeff_monomial(t**2))
    H=sp.hessian(quad,others)
    return quad,sp.cancel(H.det())
def base_factor_record(Q):
    p=sp.Poly(Q,*BASE,extension=I); lead=p.terms()[0][1]; p=sp.Poly(sp.expand(Q/lead),*BASE,extension=I)
    return [{'monomial_exponents':list(m),'coefficient_Qi':enc_qi(q)} for m,q in p.terms()]
def branch_line_data(rad,Q,singular):
    if rad==b1:
        specs=[('+',{a2:I*a3},(a1,a3)),('-',{a2:-I*a3},(a1,a3))]
        meet=(sp.Integer(1),sp.Integer(0),sp.Integer(0))
    elif rad==b2:
        specs=[('+',{a1:I*a3},(a2,a3)),('-',{a1:-I*a3},(a2,a3))]
        meet=(sp.Integer(0),sp.Integer(1),sp.Integer(0))
    elif rad==b3:
        specs=[('+',{a1:I*a2},(a2,a3)),('-',{a1:-I*a2},(a2,a3))]
        meet=(sp.Integer(0),sp.Integer(0),sp.Integer(1))
    else: raise SystemExit('branch-line helper only supports b_j radicands')
    if sp.expand(Q.subs(dict(zip(BASE,meet))))==0:
        raise SystemExit(f'two branch lines meet on Q for {rad}: {meet}')
    rows=[]; total_odd=0
    for sign,sub,uv in specs:
        f=sp.expand(Q.subs(sub))
        unit,facs=sp.factor_list(f,*uv,extension=I)
        odd=[]; odddeg=0
        for fac,e in facs:
            deg=int(sp.Poly(fac,*uv,extension=I).total_degree())
            if e%2:
                odd.append({'degree':deg,'exponent':int(e),'factor':str(sp.expand(fac))})
                odddeg+=deg
        if odddeg==0: raise SystemExit(f'expected ramified odd divisor but got square restriction {rad} {sign}')
        # Any odd root used as a branch witness must avoid the singular locus.
        for P in singular:
            if sp.expand(Q.subs(dict(zip(BASE,P))))!=0: raise SystemExit('bad singular inventory')
            # check whether P lies on this branch line, then test the odd part at its line coordinates
            lies=all(sp.expand(v.subs(dict(zip(BASE,P))))==0 for v in [])
            if rad==b1: on=(sp.expand(P[1]-(I if sign=='+' else -I)*P[2])==0); vals=(P[0],P[2])
            elif rad==b2: on=(sp.expand(P[0]-(I if sign=='+' else -I)*P[2])==0); vals=(P[1],P[2])
            else: on=(sp.expand(P[0]-(I if sign=='+' else -I)*P[1])==0); vals=(P[1],P[2])
            if on:
                for o in odd:
                    fac=sp.sympify(o['factor'],locals={str(v):v for v in BASE}|{'I':I})
                    if sp.expand(fac.subs(dict(zip(uv,vals))))==0:
                        raise SystemExit(f'odd branch witness hits singular point: {rad} {sign} {P}')
        rows.append({'line_sign':sign,'restricted_quartic':str(f),'odd_squarefree_geometric_degree':odddeg,'odd_factors':odd})
        total_odd+=odddeg
    return rows,total_odd

src=json.load(open(IN)); claimed=src.pop('canonical_sha256')
if claimed!=EXPECTED_SPLIT_SHA or sha(src)!=EXPECTED_SPLIT_SHA: raise SystemExit('carrier split source lock moved')
quartic_rows=[r for r in src['carrier_records'] if r['classification']=='OFF_BOUNDARY_IRREDUCIBLE_QUARTIC_BASE_NORM']
if len(quartic_rows)!=12: raise SystemExit('quartic carrier count moved')

groups={}
for row in quartic_rows:
    non=[f for f in row['norm_factorization_over_Qi'] if f['coordinate_factor'] is None]
    if len(non)!=1 or non[0]['degree']!=4 or non[0]['exponent_in_norm']!=4: raise SystemExit('quartic factor type moved')
    groups.setdefault(normalized_terms_key(non[0]),[]).append((row,non[0]))
if len(groups)!=6 or sorted(len(v) for v in groups.values())!=[2]*6: raise SystemExit('12 carriers did not pair into six quartics')

records=[]; genus_hist={}; branch_hist={}; all_observed=[]
for gid,(gkey,pairs) in enumerate(sorted(groups.items(),key=lambda kv:min(x[0]['carrier_index_1based'] for x in kv[1])),1):
    Q=quartic_expr(pairs[0][1])
    unit,factors=sp.factor_list(Q,*BASE,extension=I)
    if len(factors)!=1 or factors[0][1]!=1 or int(sp.Poly(factors[0][0],*BASE,extension=I).total_degree())!=4:
        raise SystemExit(f'base quartic {gid} lost irreducibility over Q(i)')
    singular=singular_points(Q)
    if len(singular) not in (1,2): raise SystemExit(f'unexpected singular count on quartic {gid}: {singular}')
    nodes=[]
    for P in singular:
        quad,det=ordinary_node_check(Q,P)
        if det==0: raise SystemExit(f'nonordinary singularity on quartic {gid}: {P}')
        nodes.append({'projective_point':[str(x) for x in P],'tangent_cone_quadratic':str(quad),'hessian_det':str(det)})
    gbase=3-len(singular)
    genus_hist[str(gbase)]=genus_hist.get(str(gbase),0)+1

    carrier_records=[]; orbit_reference=None; omitted_ref=None; present_bs_ref=None; tau_rad_ref=None; branch_rad_ref=None; M_ref=None
    for row,_ in pairs:
        L=form_expr(row)
        coeff={v:sp.Poly(L,*COORDS,extension=I).coeff_monomial(v) for v in RADS}
        present=[v for v in RADS if coeff[v]!=0]
        if c not in present or len(present)!=3 or sum(v in BRADS for v in present)!=2:
            raise SystemExit(f'quartic carrier support not two b plus c: {row["carrier_index_1based"]} {present}')
        omitted=next(v for v in BRADS if v not in present)
        pbs=[v for v in BRADS if v in present]
        r,s=sorted(pbs,key=lambda v:str(v)); alpha,beta,gamma=coeff[r],coeff[s],coeff[c]
        M=sp.cancel((gamma**2*Q_SQ[c]-alpha**2*Q_SQ[r]-beta**2*Q_SQ[s])/(2*alpha*beta))
        relation=sp.expand(Q_SQ[r]*Q_SQ[s]-M**2)
        lam=poly_proportional(relation,Q)
        if lam is None: raise SystemExit(f'quartic relation mismatch carrier {row["carrier_index_1based"]}')
        if not projective_empty([Q,Q_SQ[r],Q_SQ[s]]):
            raise SystemExit(f'present radicands meet on base quartic carrier {row["carrier_index_1based"]}')
        if not projective_empty([Q,Q_SQ[omitted],Q_SQ[r]]):
            raise SystemExit(f'ramified and tau radicands meet on base quartic carrier {row["carrier_index_1based"]}')
        basecanon=canonical_coeff_tuple(L)
        orbit={}; stabilizer=[]
        for signs in itertools.product((-1,1),repeat=4):
            tr=canonical_coeff_tuple(sign_transform(L,signs))
            orbit.setdefault(tuple(str(x) for x in tr),0); orbit[tuple(str(x) for x in tr)]+=1
            if tr==basecanon: stabilizer.append(signs)
        if len(orbit)!=4 or sorted(orbit.values())!=[4,4,4,4] or len(stabilizer)!=4:
            raise SystemExit(f'V4 projective sign orbit moved carrier {row["carrier_index_1based"]}')
        expected=set()
        for signs in itertools.product((-1,1),repeat=4):
            d=dict(zip(RADS,signs))
            if (d[omitted]==1 and all(d[v]==1 for v in present)) or (d[omitted]==-1 and all(d[v]==1 for v in present)) or (d[omitted]==1 and all(d[v]==-1 for v in present)) or (d[omitted]==-1 and all(d[v]==-1 for v in present)):
                expected.add(signs)
        if set(stabilizer)!=expected: raise SystemExit(f'projective stabilizer generators moved carrier {row["carrier_index_1based"]}')
        if orbit_reference is None:
            orbit_reference=set(orbit); omitted_ref=omitted; present_bs_ref=pbs; tau_rad_ref=r; branch_rad_ref=omitted; M_ref=M
        else:
            if set(orbit)!=orbit_reference or omitted!=omitted_ref or set(pbs)!=set(present_bs_ref):
                raise SystemExit(f'paired carriers do not belong to one sign orbit quartic {gid}')
        carrier_records.append({
          'carrier_index_1based':row['carrier_index_1based'],'occurrences':row['occurrences'],
          'linear_form':str(L),'present_b_radicals':[str(x) for x in pbs],'omitted_b_radical':str(omitted),
          'projective_sign_orbit_size':4,'projective_sign_stabilizer_size':4,
          'projective_sign_stabilizer':[[int(x) for x in sgn] for sgn in sorted(stabilizer)],
          'product_relation_M':str(M),'quartic_relation_scalar':str(lam),
        })
        all_observed.append(row['carrier_index_1based'])

    # The omitted b-radicand is definitely ramified.  Count only odd smooth
    # intersection roots on its two Q(i)-linear branch components.
    branch_rows,branch_count=branch_line_data(branch_rad_ref,Q,singular)
    if branch_count not in (4,8): raise SystemExit(f'unexpected branch count quartic {gid}: {branch_count}')
    branch_hist[str(branch_count)]=branch_hist.get(str(branch_count),0)+1
    if (gbase,branch_count) not in ((1,8),(2,4)):
        raise SystemExit(f'genus/branch pairing moved quartic {gid}: {(gbase,branch_count)}')
    quadratic_cover_genus=2*gbase-1+branch_count//2
    if quadratic_cover_genus!=5: raise SystemExit(f'ramified quadratic cover genus moved quartic {gid}')

    records.append({
      'base_quartic_id':f'Q4_{gid:02d}',
      'base_quartic_normalized_terms':base_factor_record(Q),
      'observed_carrier_indices_1based':sorted(x['carrier_index_1based'] for x,_ in pairs),
      'observed_carriers_are_in_same_four_element_projective_sign_orbit':True,
      'base_quartic_irreducible_over_Qi':True,
      'ordinary_node_count':len(singular),'ordinary_nodes':nodes,
      'normalization_genus':gbase,
      'projective_sign_stabilizer':{
        'group':'V4','order':4,
        'generator_description':f'flip omitted {omitted_ref}; flip all three present radicals',
      },
      'function_field_reduction':{
        'present_b_radicals':[str(x) for x in present_bs_ref],
        'omitted_b_radical':str(omitted_ref),
        'relation':f'{present_bs_ref[0]}*{present_bs_ref[1]} = {sp.cancel(M_ref)}',
        'present_b_squareclasses_equal':True,
        'present_b_zero_divisors_even_on_base_normalization':True,
        'unramified_pic2_candidate_tau_radical':str(tau_rad_ref),
        'unramified_pic2_candidate_tau_status':'UNRESOLVED_TRIVIAL_OR_NONTRIVIAL',
        'definitely_ramified_radical':str(branch_rad_ref),
        'definitely_ramified_radical_independent_from_nontrivial_tau_if_tau_nonzero':True,
      },
      'ramified_radical_branch_certificate':{
        'branch_lines_over_Qi':branch_rows,'geometric_odd_branch_point_count':branch_count,
        'all_counted_odd_branch_points_are_smooth_on_base_quartic':True,
        'two_branch_line_intersection_is_not_on_base_quartic':True,
      },
      'ramified_quadratic_cover':{
        'degree':2,'connected':True,'genus':quadratic_cover_genus,
      },
      'conditional_full_carrier_normalization':{
        'if_tau_nontrivial':{'connected':True,'degree_over_base_quartic':4,'galois_group':'V4','genus':2*quadratic_cover_genus-1},
        'if_tau_trivial':{'connected':False,'component_count':2,'degree_per_component_over_base_quartic':2,'genus_per_component':quadratic_cover_genus},
      },
      'carrier_records':carrier_records,
    })

if sorted(all_observed)!=sorted(r['carrier_index_1based'] for r in quartic_rows): raise SystemExit('carrier grouping lost rows')
if genus_hist!={'1':3,'2':3}: raise SystemExit(f'base normalization genus histogram moved: {genus_hist}')
if branch_hist!={'4':3,'8':3}: raise SystemExit(f'branch histogram moved: {branch_hist}')

cert={
 'schema':'STAGE33_07_QUARTIC_NORM_BIQUADRATIC_COVER_STRUCTURE_V1',
 'source_lock':{'carrier_boundary_offboundary_split_sha256':EXPECTED_SPLIT_SHA},
 'field':'Q(i) (all statements remain valid after extension to L=Q(i,sqrt(2)))',
 'reduction_summary':{
   'quartic_norm_carrier_hyperplanes':12,
   'distinct_irreducible_base_quartics':6,
   'observed_carriers_per_base_quartic':2,
   'full_projective_sign_orbit_size_per_base_quartic':4,
   'projective_stabilizer_per_carrier':'V4 order 4',
   'base_normalization_genus_histogram':genus_hist,
   'definitely_ramified_branch_count_histogram':branch_hist,
   'ramified_quadratic_intermediate_genus':5,
   'remaining_binary_pic2_triviality_tests':6,
 },
 'base_quartic_records':records,
 'exact_checks':{
   '12_quartic_carriers_pair_into_exactly_6_base_quartics':True,
   'all_6_base_quartics_irreducible_over_Qi':True,
   'all_base_quartic_singularities_are_exactly_ordinary_nodes':True,
   'base_normalization_genus_histogram_is_3_genus1_plus_3_genus2':True,
   'each_carrier_uses_exactly_two_b_radicals_plus_c':True,
   'each_carrier_has_four_element_projective_sign_orbit_and_V4_stabilizer':True,
   'paired_observed_carriers_lie_in_same_projective_sign_orbit':True,
   'each_quartic_relation_qr_qs_equals_M_squared_is_exact':True,
   'present_b_radicands_have_no_common_zero_on_base_quartic':True,
   'present_b_squareclass_is_unramified_on_base_normalization':True,
   'omitted_b_radical_has_explicit_odd_smooth_branch_divisor':True,
   'ramified_and_unramified_candidate_radicands_have_no_common_zero':True,
   'all_6_ramified_quadratic_intermediate_covers_have_genus5':True,
   'no_tau_nontriviality_credit_is_taken_without_pic2_proof':True,
 },
 'constructive_progress':{
   'split_linear_offboundary_hyperplanes_decomposed':3,
   'split_linear_offboundary_prime_divisors_materialized':12,
   'quartic_norm_hyperplanes_structurally_reduced':12,
   'quartic_norm_base_quartics_materialized':6,
   'quartic_norm_remaining_pic2_triviality_tests':6,
   'quartic_norm_prime_divisor_decomposition_closed':False,
   'global_geometric_Gersten_lifts_materialized_count':0,
   'off_boundary_codimension1_residue_certificates_materialized_count':0,
   'project_14x26_L_squareclass_tensor_materialized':False,
   'absolute_delta_loc_computed':False,'arithmetic_HS_closed':False,
 },
 'new_smallest_exact_kernel':'R33-BR2A-6-QUARTIC-BASE-UNRAMIFIED-PIC2-TRIVIALITY-DECISIONS',
 'next_exact_leaf':'L33-07-DECIDE-SIX-TAU-Q-UNRAMIFIED-PIC2-CLASSES-ON-NORMALIZED-BASE-QUARTICS',
 'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,
}
cert['canonical_sha256']=sha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({
 'success':True,'quartic_carriers':'12/12','base_quartics':6,
 'base_genus_histogram':genus_hist,'ramified_branch_histogram':branch_hist,
 'ramified_intermediate_genus':5,'remaining_pic2_tests':6,
 'certificate_sha256':cert['canonical_sha256'],'next_exact_leaf':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
