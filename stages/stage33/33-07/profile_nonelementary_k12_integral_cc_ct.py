#!/usr/bin/env python3
"""Scout exact integral cc/ct affine loci for the compressed k=1,2 skeleton orbits.

This is a planning leaf only.  It rebuilds the certified Q[2]/2Q support and
cc-mod2 skeleton orbit universes, then generalizes the exact k=3 lift-section
and integral-action equations to k=1,2.  For every skeleton-orbit
representative it checks all 1,024 raw retained cc choices and all 128 raw ct
choices after deduplicating only by exact normalized 14x14 matrices.

The scout records whether all cc choices induce one common affine stability
locus, whether ct changes the predecessor fibre, and the exact weighted H
counts if a common locus exists.  It does not grant integral-action, Q[4],
finite-q, actual-glue, HS, endpoint or theorem credit.
"""
import itertools,json,runpy,hashlib
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ACTION_LOCK='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20'
# Rebuild predecessor certificates and expose orbit representatives.
k1ns=runpy.run_path(str(HERE/'certify_nonelementary_k1_q2_2q_cc_orbits.py'))
k2ns=runpy.run_path(str(HERE/'certify_nonelementary_k2_q2_2q_skeleton_orbits.py'))
k1=json.loads((HERE/'nonelementary-k1-q2-2q-cc-orbits.json').read_text())
k2=json.loads((HERE/'nonelementary-k2-q2-2q-skeleton-orbits.json').read_text())
actions=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
if actions.get('canonical_sha256')!=ACTION_LOCK: raise SystemExit('action lock moved')
if k1['exact_skeleton_orbit_count']!=4595 or k2['exact_skeleton_orbit_count']!=427: raise SystemExit('orbit predecessor moved')

MODS=(4,)*14
PIECES=((0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13))
NAMES=('kb','kb','kb','kc','ka','ka','ka')
SCALES=(2,)*10+(4,)*4
X_MASK=(1<<10)-1

def canon(rows):
    piv={}
    for v in rows:
        x=int(v)
        for p in sorted(piv,reverse=True):
            if (x>>p)&1:x^=piv[p]
        if not x:continue
        p=x.bit_length()-1
        for q in list(piv):
            if (piv[q]>>p)&1:piv[q]^=x
        piv[p]=x
    return tuple(piv[p] for p in sorted(piv,reverse=True))
def rank(rows): return len(canon(rows))
def complement(base,whole):
    cur=list(canon(base));out=[]
    for v in canon(whole):
        if rank(cur+[v])>len(cur):cur.append(v);out.append(v)
    return tuple(out)
def span_coordinate_map(basis):
    c={0:0}
    for i,v in enumerate(basis):
        add={x^v:m|(1<<i) for x,m in c.items()}
        if any(x in c for x in add):raise SystemExit('dependent coordinate basis')
        c.update(add)
    return c
def dot(a,b): return (int(a)&int(b)).bit_count()&1

def section_equations(p_basis,quotient_basis):
    k=len(p_basis);q=len(quotient_basis);rows=[]
    for i in range(k):
        for j in range(i):
            mask=0
            for a,v in enumerate(quotient_basis):
                if dot(v&X_MASK,p_basis[j]&X_MASK):mask^=1<<(q*i+a)
                if dot(v&X_MASK,p_basis[i]&X_MASK):mask^=1<<(q*j+a)
            c=((p_basis[i]&p_basis[j]&X_MASK).bit_count()+2*(p_basis[i]&p_basis[j]&~X_MASK).bit_count())
            if c&1:raise SystemExit('half-pairing parity regression')
            rows.append((mask,(c//2)&1))
    return rows

def affine_rref(rows,nvar):
    maskall=(1<<nvar)-1;piv={}
    for mask,rhs in rows:
        value=int(mask)|((int(rhs)&1)<<nvar);coef=value&maskall
        while coef:
            p=coef.bit_length()-1
            if p in piv:value^=piv[p];coef=value&maskall
            else:
                for old in list(piv):
                    if (piv[old]>>p)&1:piv[old]^=value
                piv[p]=value;break
        if not coef and ((value>>nvar)&1):return None
    return tuple(piv[p] for p in sorted(piv,reverse=True))

def normalized_global_action(choice,kind):
    M=[[int(i==j) for j in range(14)] for i in range(14)]
    for (a,b),name,idx in zip(PIECES,NAMES,choice):
        local=actions['pieces'][name][kind+'_actions'][idx]
        for ii,old in enumerate((a,b)):
            for jj,new in enumerate((a,b)):
                num=SCALES[old]*int(local[ii][jj])
                if num%SCALES[new]:raise SystemExit('scaled action descent regression')
                M[old][new]=(num//SCALES[new])%4
    return tuple(tuple(r) for r in M)
def all_actions(kind):
    ranges=[range(len(actions['pieces'][name][kind+'_actions'])) for name in NAMES]
    raw=tuple(normalized_global_action(c,kind) for c in itertools.product(*ranges))
    return raw
ccraw=all_actions('cc');ctraw=all_actions('ct')
if len(ccraw)!=1024 or len(ctraw)!=128:raise SystemExit('raw action count regression')
cc=tuple(sorted(set(ccraw)));ct=tuple(sorted(set(ctraw)))
if len(cc)!=8 or len(ct)!=1:raise SystemExit('normalized action count regression')
if set(Counter(ccraw).values())!={128} or set(Counter(ctraw).values())!={128}:raise SystemExit('action multiplicity regression')

def action_mod4_bits(v,M):
    return tuple(sum(((int(v)>>i)&1)*M[i][j] for i in range(14))%4 for j in range(14))
def bits2(c): return sum((int(x)&1)<<j for j,x in enumerate(c))

def stability_equations(p_basis,w_basis,quotient_basis,M):
    k=len(p_basis);wdim=len(w_basis);q=len(quotient_basis);nvar=k*q
    coords=span_coordinate_map(w_basis+quotient_basis);pcoords=span_coordinate_map(p_basis)
    tq=[bits2(action_mod4_bits(v,M)) for v in quotient_basis]
    rows=[]
    for ig,p in enumerate(p_basis):
        tp4=action_mod4_bits(p,M);tp2=bits2(tp4);comb=pcoords.get(tp2)
        if comb is None:return None
        selected=[j for j in range(k) if (comb>>j)&1]
        carry=0
        for c in range(14):
            s=sum((p_basis[j]>>c)&1 for j in selected);d=(tp4[c]-s)%4
            if d&1:raise SystemExit('integral carry parity regression')
            if d==2:carry|=1<<c
        carryq=coords[carry]>>wdim
        for ob in range(q):
            mask=0
            for ib,t in enumerate(tq):
                if (coords[t]>>(wdim+ob))&1:mask^=1<<(q*ig+ib)
            for j in selected:
                mask^=1<<(q*j+ob)
            rows.append((mask,(carryq>>ob)&1))
    return rows

def process(label,source):
    reps=source['orbit_representatives'];hist=Counter();weighted=0;rawweighted=0
    common_all=True;ct_neutral_all=True;inconsistent=0;cc_locus_count_hist=Counter();records=[]
    for idx,r in enumerate(reps):
        p=tuple(map(int,r['P_basis_bits']));w=tuple(map(int,r['W_basis_bits']));orbit=int(r['orbit_size'])
        k=len(p);wdim=len(w);q=14-wdim;nvar=k*q
        qb=complement(w,canon(1<<j for j in range(14)))
        if len(qb)!=q:raise SystemExit('quotient dimension regression')
        base=section_equations(p,qb);br=affine_rref(base,nvar)
        if br is None:raise SystemExit('base fibre inconsistent')
        base_dim=nvar-len(br);rawweighted+=orbit*(1<<base_dim)
        loci=set();bad=False
        for M in cc:
            ex=stability_equations(p,w,qb,M)
            if ex is None:bad=True;continue
            rr=affine_rref(base+ex,nvar)
            if rr is None:bad=True;continue
            loci.add(rr)
        if bad or not loci:
            inconsistent+=1;common_all=False;continue
        cc_locus_count_hist[len(loci)]+=1
        if len(loci)!=1:common_all=False
        # Planning count only when every cc choice has one identical locus.
        rr=min(loci);dim=nvar-len(rr);hist[dim]+=1
        if len(loci)==1:weighted+=orbit*(1<<dim)
        for M in ct:
            ex=stability_equations(p,w,qb,M)
            if ex is None or affine_rref(base+ex,nvar)!=br:ct_neutral_all=False
        records.append({'orbit':idx,'k':k,'orbit_size':orbit,'base_dim':base_dim,'cc_locus_count':len(loci),'chosen_cc_dim':dim})
    return {'skeleton_orbits':len(reps),'raw_structural_H_reconstructed':rawweighted,'all_cc_choices_common_locus':common_all,'cc_locus_count_histogram':{str(k):v for k,v in sorted(cc_locus_count_hist.items())},'ct_neutral_on_base_fibre_every_orbit':ct_neutral_all,'orbits_with_missing_or_inconsistent_cc':inconsistent,'common_cc_dimension_histogram':{str(k):v for k,v in sorted(hist.items())},'weighted_H_after_common_cc_locus_if_applicable':weighted,'records':records}

out1=process('k1',k1);out2=process('k2',k2)
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_INTEGRAL_CC_CT_SCOUT_V1','source_k1_sha256':k1['canonical_sha256'],'source_k2_sha256':k2['canonical_sha256'],'source_actions_sha256':ACTION_LOCK,'raw_cc_choices':1024,'distinct_normalized_cc_actions':8,'raw_ct_choices':128,'distinct_normalized_ct_actions':1,'k1':out1,'k2':out2,'planning_only':True,'integral_cc_ct_certified':False,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();(HERE/'nonelementary-k12-integral-cc-ct-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'k1':{x:y for x,y in out1.items() if x!='records'},'k2':{x:y for x,y in out2.items() if x!='records'},'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
