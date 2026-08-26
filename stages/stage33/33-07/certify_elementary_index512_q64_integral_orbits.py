#!/usr/bin/env python3
"""Classify the 64 simultaneous-V4 elementary H under integral Aut(L0).

L0=<8>^10 direct_sum <16>^4. Every integral isometry of this diagonal lattice
is a signed permutation within the ten <8> coordinates and within the four
<16> coordinates. Signs act trivially on A0[2], so equivalence of elementary
H is coordinate permutation equivalence preserving X/Y blocks.

A 288-element geometric subgroup explicitly connects every reported orbit.
Distinct orbits are separated by the split code weight enumerator (wt_X,wt_Y),
invariant under full Aut(L0). The same enumerator also gives an abstract-lattice
fingerprint: for a codeword h, the minimum norm in its glue coset is
2*wt_X(h)+4*wt_Y(h); hence norm-4 vectors are counted exactly from weights
(2,0) and (0,1).
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
from elementary_index512_q256_retained import load as load_q256
Q=load_q256()
V4=json.loads((HERE/'elementary-index512-q256-simultaneous-v4-census-retained.json').read_text())
V4_LOCK='a35211b2f18d2a7be3a91724fd7e13750a09d712201b56387fd3fad8adc5a252'
if V4['canonical_sha256']!=V4_LOCK: raise SystemExit('simultaneous V4 retained lock moved')
SURV=[int(x) for x in V4['survivor_indices']]
if SURV!=list(range(64,128)): raise SystemExit('q64 survivor index regression')

def canon(rows):
    piv={}
    for z in rows:
        x=int(z)
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:
                piv[p]=x
                for q in list(piv):
                    if q!=p and ((piv[q]>>p)&1):piv[q]^=x
                break
    return tuple(piv[p] for p in sorted(piv,reverse=True))
H={int(r['index']):canon(r['H_basis_bits']) for r in Q['records']}
lookup={v:k for k,v in H.items()}
if len(lookup)!=256: raise SystemExit('q256 duplicate H regression')

def apply_perm(B,p):
    out=[]
    for x in B:
        y=0
        for i in range(14):
            if (x>>i)&1:y|=1<<p[i]
        out.append(y)
    return canon(out)

def geometric_perms():
    out=[]
    for pk in itertools.permutations(range(3)):
      for swaps in itertools.product((0,1),repeat=3):
       for pa in itertools.permutations(range(3)):
        p=list(range(14))
        for k in range(3):
            old=(2*k,2*k+1);new=(2*pk[k],2*pk[k]+1)
            if swaps[k]:new=(new[1],new[0])
            p[old[0]],p[old[1]]=new
        p[6]=6;p[10]=10
        for k in range(3):p[7+k]=7+pa[k];p[11+k]=11+pa[k]
        out.append(tuple(p))
    if len(set(out))!=288:raise SystemExit('geometric group cardinality regression')
    return out
GP=geometric_perms()

def split_weight_enumerator(B):
    c=Counter();B=list(B)
    for m in range(1<<len(B)):
        x=0
        for i,b in enumerate(B):
            if (m>>i)&1:x^=b
        c[((x&1023).bit_count(),((x>>10)&15).bit_count())]+=1
    if sum(c.values())!=512:raise SystemExit('weight enumerator mass regression')
    return {'%d,%d'%k:int(v) for k,v in sorted(c.items())}

def norm4_count(we):
    # A nonzero glue coset represented by h has minimal norm
    # 2*wt_X(h)+4*wt_Y(h). For norm 4, (2,0) gives 2^2 sign choices and
    # (0,1) gives 2 sign choices. L0 itself has minimum norm 8.
    return 4*int(we.get('2,0',0))+2*int(we.get('0,1',0))

unseen=set(SURV);orbits=[]
while unseen:
    rep=min(unseen);members=set();witness={}
    for p in GP:
        j=lookup.get(apply_perm(H[rep],p))
        if j in SURV and j not in members:
            members.add(j);witness[str(j)]=list(p)
    if rep not in members:raise SystemExit('identity orbit regression')
    we=split_weight_enumerator(H[rep])
    orbits.append({'representative':rep,'members':sorted(members),'size':len(members),'split_weight_enumerator':we,'norm4_vector_count':norm4_count(we),'explicit_geometric_permutation_to_each_member':witness})
    unseen-=members
if [o['representative'] for o in orbits]!=[64,68,88] or [o['size'] for o in orbits]!=[4,36,24]:
    raise SystemExit('q64 integral orbit census regression')
if [o['norm4_vector_count'] for o in orbits]!=[24,8,0]:raise SystemExit('q64 norm4 fingerprint regression')
if sum(o['size'] for o in orbits)!=64 or sorted(sum((o['members'] for o in orbits),[]))!=SURV:
    raise SystemExit('q64 orbit coverage regression')
keys=[json.dumps(o['split_weight_enumerator'],sort_keys=True) for o in orbits]
if len(set(keys))!=3:raise SystemExit('full Aut(L0) separation invariant collapsed')
cert={'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q64_INTEGRAL_AUT_L0_ORBITS_V2','source_q256_sha256':Q['canonical_sha256'],'source_simultaneous_v4_sha256':V4_LOCK,'survivor_count_before':64,'integral_Aut_L0_orbit_count':3,'orbit_sizes':[4,36,24],'orbit_representatives':[64,68,88],'norm4_vector_counts':[24,8,0],'orbits':orbits,'full_Aut_L0_separation_proved_by_split_weight_enumerator':True,'within_orbit_equivalence_proved_by_explicit_geometric_permutations':True,'three_abstract_integral_lattices_pairwise_nonisometric_by_norm4_count':True,'actual_index512_glue_identified':False,'next_exact_leaf':'L33-07-DISTINGUISH-3-INTEGRAL-ELEMENTARY-GLUE-ORBITS-USING-COORDINATE-SIGNS-OR-ENDPOINT-THETA','new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-3-INTEGRAL-ORBITS-PLUS-NONELEMENTARY-SIGN-STABLE-TYPES','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q64-integral-orbits.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':64,'integral_Aut_L0_orbits':3,'orbit_sizes':[4,36,24],'representatives':[64,68,88],'norm4_vector_counts':[24,8,0],'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
