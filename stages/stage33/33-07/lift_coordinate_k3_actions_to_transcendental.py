#!/usr/bin/env python3
"""Extend coordinate-K3 discriminant generators to the scaled pullback pieces.

Arithmetic firewall.
--------------------
The Picard action factors through Gal(Q(i,sqrt(2))/Q)=V4, but the deeper
2-primary transcendental action need not.  In particular, lifts of the two
field generators can commute only modulo the unscaled discriminant subgroup;
their commutator may be a nontrivial element of the deeper Galois kernel.
Therefore this leaf must NOT impose cc*ct=ct*cc on A_(2T).

For each K3 piece we enumerate all anti-isometries A_Pic -> A_T, then every
quadratic-form-preserving extension of the exact cc and ct actions from

    A_T = product Z/d_i  -->  A_(2T) = product Z/(2d_i),  x |-> 2x.

The groups have only 64 or 128 elements and each matrix entry has two possible
lifts, so all tests are exhaustive.  We retain all literal generator pairs and
record their commutators.  This is exactly the finite data needed to ask which
order-512 isotropic glues make the endpoint quotient action factor through the
audited V4 action.
"""
import hashlib,itertools,json,math
from pathlib import Path
HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'coordinate-k3-discriminant-v4-actions.json').read_text())

def rowact(x,M,mods): return tuple(sum(x[i]*M[i][j] for i in range(2))%mods[j] for j in range(2))
def elems(mods): return list(itertools.product(*[range(m) for m in mods]))
def order_elem(x,mods):
    o=1
    for a,m in zip(x,mods):
        if a%m: o=math.lcm(o,m//math.gcd(a,m))
    return o
def add(a,b,mods): return tuple((a[i]+b[i])%mods[i] for i in range(2))
def smul(n,a,mods): return tuple((n*a[i])%mods[i] for i in range(2))
def qnum(x,Q,den): return sum(x[i]*Q[i][j]*x[j] for i in range(2) for j in range(2))%(2*den)
def phi(x,ims,mods): return add(smul(x[0],ims[0],mods),smul(x[1],ims[1],mods),mods)
def compose(A,B,mods): return [[sum(A[i][k]*B[k][j] for k in range(2))%mods[j] for j in range(2)] for i in range(2)]
def I2(): return [[1,0],[0,1]]
def hom_well_defined(M,mods): return all((mods[i]*M[i][j])%mods[j]==0 for i in range(2) for j in range(2))
def bijective(M,mods): return len({rowact(x,M,mods) for x in elems(mods)})==math.prod(mods)
def preserves_q(M,mods,Q,den): return all(qnum(rowact(x,M,mods),Q,den)==qnum(x,Q,den) for x in elems(mods))
def involution(M,mods): return compose(M,M,mods)==I2()
def commutator_involutions(A,B,mods): return compose(compose(compose(A,B,mods),A,mods),B,mods)

def anti_isometries(mods,Qp,den):
    Qt=[[0,0],[0,0]]
    for i,m in enumerate(mods):
        if den%m: raise SystemExit('unscaled T denominator regression')
        Qt[i][i]=den//m
    E=elems(mods); choices=[[x for x in E if order_elem(x,mods)==mods[i]] for i in range(2)]
    out=[]
    for y0 in choices[0]:
      for y1 in choices[1]:
        seen=set(); ok=True
        for x in E:
            y=phi(x,(y0,y1),mods)
            if y in seen or (qnum(x,Qp,den)+qnum(y,Qt,den))%(2*den): ok=False; break
            seen.add(y)
        if ok and len(seen)==len(E): out.append((y0,y1))
    return out,Qt

def conjugate_action(Mp,ims,mods):
    E=elems(mods); f={x:phi(x,ims,mods) for x in E}; inv={y:x for x,y in f.items()}
    rows=[]
    for i in range(2):
        e=tuple(1 if j==i else 0 for j in range(2))
        rows.append(list(f[rowact(inv[e],Mp,mods)]))
    return rows

def scaled_extensions(Mold,oldmods,newmods,Qnew,dennew):
    out=[]
    for bits in itertools.product((0,1),repeat=4):
        M=[]; t=0
        for i in range(2):
            row=[]
            for j in range(2):
                row.append((int(Mold[i][j])+bits[t]*oldmods[j])%newmods[j]); t+=1
            M.append(row)
        if not hom_well_defined(M,newmods) or not bijective(M,newmods): continue
        if not preserves_q(M,newmods,Qnew,dennew): continue
        # All finite extensions found in these three pieces are involutions; we
        # certify this rather than assuming it from the absolute Galois lift.
        if not involution(M,newmods): continue
        for x in elems(oldmods):
            emb=tuple(2*x[i]%newmods[i] for i in range(2))
            y=rowact(x,Mold,oldmods); rhs=tuple(2*y[i]%newmods[i] for i in range(2))
            if rowact(emb,M,newmods)!=rhs: raise SystemExit('scaled restriction regression')
        out.append(M)
    return list({json.dumps(M):M for M in out}.values())

def derive_piece(mode):
    p=src['pieces'][mode]; oldmods=[int(x) for x in p['picard_discriminant_moduli']]
    den=int(p['discriminant_bilinear_numerator_denominator']); Qp=[[int(x) for x in r] for r in p['discriminant_bilinear_numerator_reduced']]
    anti,Qt=anti_isometries(oldmods,Qp,den)
    if not anti: raise SystemExit(f'{mode}: no Pic/T anti-isometry')
    newmods=[2*m for m in oldmods]; dennew=math.lcm(*newmods); Qnew=[[0,0],[0,0]]
    for i,m in enumerate(newmods): Qnew[i][i]=dennew//m
    records=[]
    for ims in anti:
        oldcc=conjugate_action(p['cc_action_mixed_moduli'],ims,oldmods)
        oldct=conjugate_action(p['ct_action_mixed_moduli'],ims,oldmods)
        for cc in scaled_extensions(oldcc,oldmods,newmods,Qnew,dennew):
          for ct in scaled_extensions(oldct,oldmods,newmods,Qnew,dennew):
            comm=commutator_involutions(cc,ct,newmods)
            records.append({'cc_scaled_action':cc,'ct_scaled_action':ct,'commutator_scaled_action':comm,
              'generators_commute_on_scaled_module':comm==I2(),
              'unscaled_cc_action_standard_T_coords':oldcc,'unscaled_ct_action_standard_T_coords':oldct,
              'anti_isometry_generator_images':[list(ims[0]),list(ims[1])]})
    if not records: raise SystemExit(f'{mode}: no scaled finite quadratic generator extension')
    uniq={json.dumps([r['cc_scaled_action'],r['ct_scaled_action']],sort_keys=True):r for r in records}; pairs=list(uniq.values())
    comms={json.dumps(r['commutator_scaled_action']):r['commutator_scaled_action'] for r in pairs}
    return {'unscaled_T_discriminant_moduli':oldmods,'unscaled_T_q_numerator_denominator':den,
      'unscaled_T_q_numerator_matrix':Qt,'picard_to_T_anti_isometry_count':len(anti),
      'scaled_pullback_discriminant_moduli':newmods,'scaled_pullback_q_numerator_denominator':dennew,
      'scaled_pullback_q_numerator_matrix':Qnew,'scaled_generator_pair_count':len(pairs),
      'scaled_generator_pairs':pairs,'distinct_commutator_count':len(comms),
      'distinct_commutators':list(comms.values()),
      'commutator_forced_independent_of_extension':len(comms)==1,
      'forced_commutator':next(iter(comms.values())) if len(comms)==1 else None,
      'forced_commutator_trivial':len(comms)==1 and next(iter(comms.values()))==I2()}

pieces={m:derive_piece(m) for m in ('kb','kc','ka')}
cert={'schema':'STAGE33_07_COORDINATE_K3_SCALED_DISCRIMINANT_GENERATOR_EXTENSIONS_V2',
 'source_locks':{'coordinate_k3_discriminant_actions_sha256':src['canonical_sha256']},'pieces':pieces,
 'arithmetic_galois_action_promoted_to_integral_betti_T_isometry':False,'semisimple_twist_used':False,
 'cc_ct_commutativity_imposed_above_unscaled_discriminant':False,'finite_quadratic_extension_exhaustive':True,
 'scaled_L0_generator_action_candidate_sets_complete_at_piece_level':True,
 'forced_deeper_commutator':{'kb':pieces['kb']['forced_commutator'],'kc':pieces['kc']['forced_commutator'],'ka':pieces['ka']['forced_commutator']},
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-CLASSIFY-ELEMENTARY-ORDER512-GLUE-KILLING-FORCED-COMMUTATOR-AND-MATCHING-TARGET-SNF-FORM-ACTION',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'coordinate-k3-integral-t-actions.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'scaled_generator_pair_counts':{k:v['scaled_generator_pair_count'] for k,v in pieces.items()},
 'forced_commutators':cert['forced_deeper_commutator'],'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
