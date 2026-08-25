#!/usr/bin/env python3
"""Lift each coordinate-K3 Picard discriminant V4 action to integral T(Kx).

For Kb the certified transcendental lattice is diag(4,4); for Kc and Ka it is
diag(4,8).  Their discriminant groups have only 16 or 32 elements.  We therefore
avoid any semisimple/twist inference: enumerate the full integral isometry group
of the rank-two positive lattice, enumerate all anti-isometries from the Picard
discriminant form to A_T, and retain exactly the commuting involution pairs that
intertwine both cc and ct.

This determines the integral rank-two Galois action up to the exact ambiguity
visible to the discriminant form.  If more than one integral lift remains, the
certificate records all of them and does not choose one silently.
"""
import hashlib,itertools,json,math
from pathlib import Path
HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'coordinate-k3-discriminant-v4-actions.json').read_text())


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def eye(): return [[1,0],[0,1]]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def rowact(x,M,mods):
    return tuple(sum(x[i]*M[i][j] for i in range(2))%mods[j] for j in range(2))
def order_elem(x,mods):
    o=1
    for a,m in zip(x,mods):
        if a%m:
            o=math.lcm(o,m//math.gcd(a,m))
    return o
def elems(mods): return list(itertools.product(*[range(m) for m in mods]))
def qnum(x,Q,den):
    return sum(x[i]*Q[i][j]*x[j] for i in range(2) for j in range(2))%(2*den)
def add(a,b,mods): return tuple((a[i]+b[i])%mods[i] for i in range(2))
def smul(n,a,mods): return tuple((n*a[i])%mods[i] for i in range(2))

def integral_isometries(D):
    # Positive rank two; coefficient bounds follow from column/row norms.  [-3,3]
    # is safely beyond what diag(4,4) and diag(4,8) permit.
    out=[]
    for a,b,c,d in itertools.product(range(-3,4), repeat=4):
        G=[[a,b],[c,d]]
        if abs(det(G))!=1: continue
        GD=matmul(G,D); GDGT=matmul(GD,[[a,c],[b,d]])
        if GDGT==D: out.append(G)
    return out

def discr_action_from_integral(G,D,mods):
    # row dual coefficients y represent y*D^{-1}; after r -> rG,
    # y -> y*D^{-1}*G*D.
    out=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            num=G[i][j]*D[j][j]
            den=D[i][i]
            if num%den: raise SystemExit('dual action integrality regression')
            out[i][j]=(num//den)%mods[j]
    return out

def anti_isometries(mods,Qp,den,D):
    E=elems(mods); src_orders=mods
    Qt=[[0,0],[0,0]]
    for i,m in enumerate(mods):
        # den * q_T(e_i^*/T) = den / m for diagonal T Gram m.
        if den%m: raise SystemExit('T denominator regression')
        Qt[i][i]=den//m
    choices=[[x for x in E if order_elem(x,mods)==src_orders[i]] for i in range(2)]
    out=[]
    for y0 in choices[0]:
      for y1 in choices[1]:
        images=[]; seen=set(); ok=True
        for x in E:
            y=add(smul(x[0],y0,mods),smul(x[1],y1,mods),mods)
            if y in seen: ok=False; break
            seen.add(y); images.append(y)
            if (qnum(x,Qp,den)+qnum(y,Qt,den))%(2*den): ok=False; break
        if ok and len(seen)==len(E):
            out.append((y0,y1))
    return out,Qt

def phi(x,ims,mods): return add(smul(x[0],ims[0],mods),smul(x[1],ims[1],mods),mods)

def derive_piece(mode):
    p=src['pieces'][mode]
    mods=[int(x) for x in p['picard_discriminant_moduli']]
    Mpcc=[[int(x) for x in r] for r in p['cc_action_mixed_moduli']]
    Mpct=[[int(x) for x in r] for r in p['ct_action_mixed_moduli']]
    den=int(p['discriminant_bilinear_numerator_denominator'])
    Qp=[[int(x) for x in r] for r in p['discriminant_bilinear_numerator_reduced']]
    D=[[4,0],[0,4 if mode=='kb' else 8]]
    if mods!=[D[0][0],D[1][1]]: raise SystemExit(f'{mode} T/Pic group type mismatch')
    O=integral_isometries(D)
    anti,Qt=anti_isometries(mods,Qp,den,D)
    if not anti: raise SystemExit(f'{mode} no Pic-to-T anti-isometry: form regression')
    invol=[G for G in O if matmul(G,G)==eye()]
    candidates=[]; E=elems(mods)
    for Gcc in invol:
      Mtcc=discr_action_from_integral(Gcc,D,mods)
      for Gct in invol:
        if matmul(Gct,Gcc)!=matmul(Gcc,Gct): continue
        Mtct=discr_action_from_integral(Gct,D,mods)
        witnesses=[]
        for ims in anti:
            good=True
            for x in E:
                if phi(rowact(x,Mpcc,mods),ims,mods)!=rowact(phi(x,ims,mods),Mtcc,mods): good=False; break
                if phi(rowact(x,Mpct,mods),ims,mods)!=rowact(phi(x,ims,mods),Mtct,mods): good=False; break
            if good: witnesses.append([list(ims[0]),list(ims[1])])
        if witnesses:
            candidates.append({'cc_integral_T_action':Gcc,'ct_integral_T_action':Gct,
              'cc_discriminant_action':Mtcc,'ct_discriminant_action':Mtct,
              'anti_isometry_witness_count':len(witnesses),'first_anti_isometry_generator_images':witnesses[0]})
    if not candidates: raise SystemExit(f'{mode} no integral T-action lift')
    # Deduplicate literal action pairs; different anti-isometries are witnesses only.
    uniq={json.dumps([c['cc_integral_T_action'],c['ct_integral_T_action']],sort_keys=True):c for c in candidates}
    candidates=list(uniq.values())
    return {'T_gram':D,'T_discriminant_moduli':mods,'T_discriminant_q_numerator_denominator':den,
      'T_discriminant_q_numerator_matrix':Qt,'integral_isometry_group_order':len(O),
      'picard_to_T_anti_isometry_count':len(anti),'integral_v4_lift_count':len(candidates),
      'integral_v4_lifts':candidates,'unique_integral_v4_lift':len(candidates)==1}

pieces={m:derive_piece(m) for m in ('kb','kc','ka')}
cert={'schema':'STAGE33_07_COORDINATE_K3_INTEGRAL_T_ACTION_LIFTS_V1',
 'source_locks':{'coordinate_k3_discriminant_actions_sha256':src['canonical_sha256']},
 'pieces':pieces,
 'semisimple_twist_used':False,
 'all_piece_lifts_exist':True,
 'all_piece_lifts_unique':all(x['unique_integral_v4_lift'] for x in pieces.values()),
 'scaled_L0_action_constructible_without_twist':all(x['unique_integral_v4_lift'] for x in pieces.values()),
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-CONSTRUCT-EXACT-L0-V4-ACTION-AND-CLASSIFY-STABLE-ORDER512-ISOTROPIC-GLUE',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'coordinate-k3-integral-t-actions.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'lift_counts':{k:v['integral_v4_lift_count'] for k,v in pieces.items()},
 'anti_isometry_counts':{k:v['picard_to_T_anti_isometry_count'] for k,v in pieces.items()},
 'all_unique':cert['all_piece_lifts_unique'],'next':cert['next_exact_leaf'],
 'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
