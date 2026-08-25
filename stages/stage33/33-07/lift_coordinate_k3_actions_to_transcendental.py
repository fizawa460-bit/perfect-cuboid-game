#!/usr/bin/env python3
"""Extend each coordinate-K3 discriminant action to the scaled pullback piece.

Important arithmetic firewall.
------------------------------
The arithmetic G_Q action on the 2-adic transcendental realization need not be
an integral Z-isometry of the positive Betti lattice T(Kx).  The K_c hostile
regression already exhibits this: its exact ct action on A_T=Z/4+Z/8 is not
induced by any integral isometry of diag(4,8).  Therefore this leaf does NOT
ask for an integral T-action.

What the index-512 glue calculation actually needs is only the finite quadratic
module action on the degree-two pullback lattice.  If T has Gram D, the pullback
piece has Gram 2D and

    A_T       = product Z/d_i,
    A_(2T)    = product Z/(2d_i),
    A_T -> A_(2T),  x |-> 2x.

For each exact Picard-discriminant action, we first enumerate all anti-isometries
A_Pic -> A_T.  We then enumerate every matrix lift of cc and ct from the even
subgroup 2*A_(2T) to the full finite quadratic module A_(2T), retaining exactly
the quadratic-form-preserving commuting involutions.  The groups have only 64
or 128 elements, so all checks are exhaustive.

This gives a conservative finite set of scaled discriminant V4 actions.  It
does not claim that every finite extension comes from the full 2-adic Galois
representation; keeping extra possibilities is safe for the subsequent glue
classification.
"""
import hashlib,itertools,json,math
from pathlib import Path
HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'coordinate-k3-discriminant-v4-actions.json').read_text())


def rowact(x,M,mods):
    return tuple(sum(x[i]*M[i][j] for i in range(2))%mods[j] for j in range(2))
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
def compose(A,B,mods):
    # row action: x -> x A -> (x A) B
    return [[sum(A[i][k]*B[k][j] for k in range(2))%mods[j] for j in range(2)] for i in range(2)]
def identity_matrix(): return [[1,0],[0,1]]

def hom_well_defined(M,mods):
    return all((mods[i]*M[i][j])%mods[j]==0 for i in range(2) for j in range(2))
def bijective(M,mods):
    E=elems(mods)
    return len({rowact(x,M,mods) for x in E})==len(E)
def preserves_q(M,mods,Q,den):
    return all(qnum(rowact(x,M,mods),Q,den)==qnum(x,Q,den) for x in elems(mods))
def involution(M,mods): return compose(M,M,mods)==identity_matrix()
def commute(A,B,mods): return compose(A,B,mods)==compose(B,A,mods)

def anti_isometries(mods,Qp,den):
    # T(Kb)=diag(4,4); T(Kc)=T(Ka)=diag(4,8), so in the standard
    # discriminant coordinates q_T has numerator diag(den/d_i).
    Qt=[[0,0],[0,0]]
    for i,m in enumerate(mods):
        if den%m: raise SystemExit('unscaled T denominator regression')
        Qt[i][i]=den//m
    E=elems(mods)
    choices=[[x for x in E if order_elem(x,mods)==mods[i]] for i in range(2)]
    out=[]
    for y0 in choices[0]:
      for y1 in choices[1]:
        seen=set(); ok=True
        for x in E:
            y=phi(x,(y0,y1),mods)
            if y in seen or (qnum(x,Qp,den)+qnum(y,Qt,den))%(2*den):
                ok=False; break
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
    # Restriction under A_T -> A_(2T), x -> 2x, says each entry is fixed
    # modulo oldmods[j].  Each target column therefore has exactly two lifts.
    out=[]
    for bits in itertools.product((0,1), repeat=4):
        M=[]; t=0
        for i in range(2):
            row=[]
            for j in range(2):
                row.append((int(Mold[i][j])+bits[t]*oldmods[j])%newmods[j]); t+=1
            M.append(row)
        if not hom_well_defined(M,newmods): continue
        if not bijective(M,newmods): continue
        if not preserves_q(M,newmods,Qnew,dennew): continue
        if not involution(M,newmods): continue
        # Explicit restriction check on the whole embedded old group.
        good=True
        for x in elems(oldmods):
            emb=tuple((2*x[i])%newmods[i] for i in range(2))
            lhs=rowact(emb,M,newmods)
            y=rowact(x,Mold,oldmods)
            rhs=tuple((2*y[i])%newmods[i] for i in range(2))
            if lhs!=rhs: good=False; break
        if good: out.append(M)
    # literal dedup
    return list({json.dumps(M):M for M in out}.values())

def derive_piece(mode):
    p=src['pieces'][mode]
    oldmods=[int(x) for x in p['picard_discriminant_moduli']]
    Qp=[[int(x) for x in r] for r in p['discriminant_bilinear_numerator_reduced']]
    den=int(p['discriminant_bilinear_numerator_denominator'])
    anti,Qt=anti_isometries(oldmods,Qp,den)
    if not anti: raise SystemExit(f'{mode}: no Pic/T anti-isometry')
    newmods=[2*m for m in oldmods]
    dennew=math.lcm(*newmods)
    Qnew=[[0,0],[0,0]]
    for i,m in enumerate(newmods): Qnew[i][i]=dennew//m
    pair_records=[]
    for ims in anti:
        oldcc=conjugate_action(p['cc_action_mixed_moduli'],ims,oldmods)
        oldct=conjugate_action(p['ct_action_mixed_moduli'],ims,oldmods)
        ecc=scaled_extensions(oldcc,oldmods,newmods,Qnew,dennew)
        ect=scaled_extensions(oldct,oldmods,newmods,Qnew,dennew)
        for cc in ecc:
          for ct in ect:
            if commute(cc,ct,newmods):
                pair_records.append({'cc_scaled_action':cc,'ct_scaled_action':ct,
                  'unscaled_cc_action_standard_T_coords':oldcc,
                  'unscaled_ct_action_standard_T_coords':oldct,
                  'anti_isometry_generator_images':[list(ims[0]),list(ims[1])]})
    if not pair_records: raise SystemExit(f'{mode}: no scaled finite quadratic V4 extension')
    # Different anti-isometries may give the same scaled action pair.  Keep one
    # witness for each literal pair; no quotient by automorphism is silently used.
    uniq={json.dumps([r['cc_scaled_action'],r['ct_scaled_action']],sort_keys=True):r for r in pair_records}
    pairs=list(uniq.values())
    return {
      'unscaled_T_discriminant_moduli':oldmods,
      'unscaled_T_q_numerator_denominator':den,
      'unscaled_T_q_numerator_matrix':Qt,
      'picard_to_T_anti_isometry_count':len(anti),
      'scaled_pullback_discriminant_moduli':newmods,
      'scaled_pullback_q_numerator_denominator':dennew,
      'scaled_pullback_q_numerator_matrix':Qnew,
      'scaled_v4_action_pair_count':len(pairs),
      'scaled_v4_action_pairs':pairs,
      'unique_scaled_v4_action_pair':len(pairs)==1,
    }

pieces={m:derive_piece(m) for m in ('kb','kc','ka')}
cert={
 'schema':'STAGE33_07_COORDINATE_K3_SCALED_DISCRIMINANT_V4_EXTENSIONS_V1',
 'source_locks':{'coordinate_k3_discriminant_actions_sha256':src['canonical_sha256']},
 'pieces':pieces,
 'arithmetic_galois_action_promoted_to_integral_betti_T_isometry':False,
 'semisimple_twist_used':False,
 'finite_quadratic_extension_exhaustive':True,
 'scaled_L0_discriminant_action_candidate_sets_complete':True,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-CLASSIFY-V4-STABLE-ORDER512-ISOTROPIC-GLUE-ACROSS-ALL-SCALED-ACTION-EXTENSIONS',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'coordinate-k3-integral-t-actions.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,
 'scaled_action_pair_counts':{k:v['scaled_v4_action_pair_count'] for k,v in pieces.items()},
 'anti_isometry_counts':{k:v['picard_to_T_anti_isometry_count'] for k,v in pieces.items()},
 'all_unique':all(v['unique_scaled_v4_action_pair'] for v in pieces.values()),
 'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
