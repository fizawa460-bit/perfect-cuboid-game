#!/usr/bin/env python3
"""Replay all norm certificates and exact 27 conic conditions for row386."""
from pathlib import Path
from hashlib import sha256
import json
from conic_arithmetic import *

HERE=Path(__file__).resolve().parent
INPUT_SHA256={
    'curve_C29.json': '04542e2e37a75ce382ca7921d51aae9e3bcc690b6a03d514dcbc0a511205bd74',
    'units381_exact.json': '78136c1f3c1fed53c429d26fc754af33edb0106d6c119fc738f7ea9f24373bd2',
    'row375_results.json': '28794c519ca99152599ccd1ef7a818f0106e2113f8a5b959daa35b6f79985d01',
    'four_lift_target384.json': '0eba8c6e2610e463f4252f566c12cdfc0bd153addc393ad6847b41aa6fa0dce0',
}


def read(name):
    raw=(HERE/name).read_bytes()
    if name in INPUT_SHA256:
        assert sha256(raw).hexdigest()==INPUT_SHA256[name],name
    return json.loads(raw)


def qmul(u,v,beta,gamma):
    a,b=u;c,d=v
    return a*c-gamma*b*d, a*d+b*c-beta*b*d


def qpow(w,n,beta,gamma):
    z=(beta.ring.one,beta.ring.zero)
    for _ in range(n):z=qmul(z,w,beta,gamma)
    return z


def verify_norms(r,fixture):
    assert fixture['field_modulus']==hex(bitmask(r.h))
    assert fixture['precision']==lr.PRECISION==24
    H=[int(s,16) for s in fixture['matrix']]
    basis=unit_basis(r);n=len(basis)
    assert n==85 and len(H)==n and len(fixture['witnesses'])==n-1
    ranks=[]
    for i,record in enumerate(fixture['witnesses']):
        assert record['basis_index']==i
        d=(i//r.degree)*2+1;k=(d-1)//2
        assert record['defect']==d
        beta=r.pi_powers[3-k]
        gamma=divide_pi(1-basis[i],2*k)
        assert gamma.valuation()==1
        powers={j:qpow((r.zero,r.one),j,beta,gamma) for j in range(1,12,2)}
        norm_codes=[]
        for j,h,s in record['norm_generators']:
            assert 1<=j<=11 and j%2==1 and 0<=h<28
            a,b=powers[j];x=r.lift(1<<h)
            a=1+x*a;b=x*b
            # Direct product (a+b*w)(a+b*(-beta-w)).
            conjugate=(a-beta*b,-b)
            norm,coefficient=qmul((a,b),conjugate,beta,gamma)
            assert coefficient==0 and norm.valuation()==0
            code=r.coordinate(norm)
            assert code==int(s,16)
            norm_codes.append(code)
        rank=len(span(norm_codes));assert rank==record['norm_unit_rank']==84
        assert H[i]==int(record['functional'],16) and H[i]
        assert all(not parity(v&H[i]) for v in norm_codes)
        ranks.append(rank)
    assert H[-1]==0 and len(span(H))==84
    assert all(((H[i]>>j)&1)==((H[j]>>i)&1) for i in range(n) for j in range(n))
    minus=r.coordinate(-r.one)
    assert all(parity(H[i]&minus)==((H[i]>>i)&1) for i in range(n))
    # Independent simple-field controls: symbols restricted from Q2, degree84 even.
    for a in [-1,3,5,7]:
        for b in [-1,3,5,7]:
            assert pairing(H,r.coordinate(r.constant(a)),r.coordinate(r.constant(b)))==0
    for v in range(2,18):
        a=r.lift(v)
        assert pairing(H,r.coordinate(a),r.coordinate(1-a))==0
    return H,basis,ranks


def run():
    data=read('units381_exact.json');target=read('four_lift_target384.json')
    curve=read('curve_C29.json');known=read('row375_results.json')
    assert data['unit_Selmer_dimension']==9
    full_codes=[int(x,16) for x in data['kernel_basis_local_codes']]
    masks=[int(x,16) for x in data['kernel_basis_as_unit_bitmasks']]
    r=LocalRing(sum(1<<i for i in lr.R28))
    H,basis,ranks=verify_norms(r,read('hilbert_norm_witnesses386.json'))
    codes=[c>>22 for c in full_codes]
    assert len(span(codes))==9
    reps=[decode(r,c,basis) for c in codes]
    f,_=lr.source_data(HERE)
    order=(2**28-1)//3
    assert r.fpow(2,order)==1
    residual=r.fpow(2,2*pow(3,-1,order))
    w=r.hensel(r.scaled_polynomial(f,210),r.zero,residual)
    frob=r.conjugates();one=r.one
    roots=[twist_root(w,z,one,0) for z in frob]
    residues=[a.digit(0) for a in roots]
    assert len(set(residues))==28
    assert all(evaluate(r.scaled_polynomial(f,210),a)==0 for a in roots)
    ds=[[r.coordinate(transform(v,z,one,0)) for v in reps] for z in frob]
    equations=[equation(r,H,roots[0],roots[k],ds[0],ds[k],[0,k]) for k in range(1,28)]
    # Direct identities for the two actual point controls.
    controls={0xa1:1,0x49:-1}
    for m,x in controls.items():
        for k,root in enumerate(roots):
            image=0
            for j,c in enumerate(ds[k]):
                if m>>j&1:image^=c
            direct=(r.pi-root) if x==1 else -root
            assert image==r.coordinate(direct)
        assert sum(int(c) for c in curve['F_ascending'][::2])+x*sum(int(c) for c in curve['F_ascending'][1::2])==2**70
    assert r.coordinate(1-r.pi_powers[2]*roots[0])==0 # x=0.
    pairs=[(i,j) for i in range(9) for j in range(i+1,9)]
    polynomial_vectors=[]
    for e in equations:
        polynomial_vectors.append(int(e['linear'],16)^sum(1<<(9+pairs.index(tuple(p))) for p in e['cross']))
    good=[];complement=[];distribution={}
    for m in range(512):
        fail=[k+1 for k,e in enumerate(equations) if test_eq(e,m)]
        if not fail:good.append(m)
        if m&0x100:
            complement.append({'coordinates':hex(m),'failed_frobenius_indices':fail})
            distribution[len(fail)]=distribution.get(len(fail),0)+1
    assert good==[0,0x49,0xa1]
    assert len(complement)==256 and min(len(v['failed_frobenius_indices']) for v in complement)==6
    assert len(span(polynomial_vectors))==13
    cover=[10,6,11,13,4,1,2]
    remaining=set(range(256,512));cover_sizes=[]
    for k in cover:
        remaining={m for m in remaining if not test_eq(equations[k-1],m)}
        cover_sizes.append(len(remaining))
    assert not remaining
    delta_mask=int(target['unit_basis_mask'],16);coord=0x10c
    mask=0;code=0
    for i in range(9):
        if coord>>i&1:mask^=masks[i];code^=full_codes[i]
    assert mask==delta_mask==0x4125e122ae5103
    assert code==int(target['independent_local_code'],16)
    known_coords=[0xcf,0xa1,0x49,0xe,0xa8,0x6b,0xf6,0x51]
    assert len(span(known_coords))==8
    assert all(not c&0x100 for c in known_coords)
    assert len(known_coords)==len(known['unit_squareclasses_at_2'])
    for coord,c in zip(known_coords,known['unit_squareclasses_at_2']):
        v=0
        for i in range(9):
            if coord>>i&1:v^=full_codes[i]
        assert v==int(c,16)
    result={
      'root_degree':105,'genus':52,'dyadic_field_degree':84,
      'dyadic_ramification_index':3,'dyadic_residue_degree':28,
      'precision_in_pi':24,'unit_squareclass_dimension':85,
      'quadratic_norm_unit_ranks':ranks,'hilbert_unit_rank':84,
      'unit_Selmer_dimension':9,'unit_Selmer_projection_to_degree84_rank':9,
      'frobenius_pair_conics':27,'quadratic_polynomial_span_rank':13,
      'tested_unit_Selmer_classes':512,'admissible_coordinates':list(map(hex,good)),
      'witness_x_for_each_admissible_class':['infinity or 0','-1','1'],
      'delta_plus_known8_coset_size':256,'admissible_in_delta_coset':0,
      'delta_coset_minimum_failed_conics':6,
      'delta_coset_failure_count_distribution':{str(k):v for k,v in sorted(distribution.items())},
      'seven_conic_cover_frobenius_indices':cover,'remaining_after_each_conic':cover_sizes,
      'delta_star_coordinates':'0x10c',
      'delta_star_failed_frobenius_indices':[k+1 for k,e in enumerate(equations) if test_eq(e,0x10c)],
      'conic_equations':equations,
      'class_group_obstruction_qstar_value':'UNDETERMINED',
      'delta_star_true_Sel4_membership':'UNDETERMINED',
      'new_unconditional_signed_exclusions':0
    }
    print(json.dumps(result,indent=2))


if __name__=='__main__':run()
